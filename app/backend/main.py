import logging
import os

from flask import Flask, render_template, request
import google.cloud.logging
from google.cloud import firestore
from google.cloud import storage
from flask_cors import CORS, cross_origin
from PredictImage import predict_image_classification_sample

# import os

# os.environ[
#     "GOOGLE_APPLICATION_CREDENTIALS"
# ] = "./past-time-machine-dev-live-ca8d0925e601.json"

client = google.cloud.logging.Client()
client.get_default_handler()
client.setup_logging()

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def root():
    return render_template("home.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    successful_upload = False
    url = ""
    predictedName = ""
    predictedConfidence = 0
    if request.method == "POST":
        uploaded_file = request.files.get("image")

        if uploaded_file:
            gcs = storage.Client()
            bucket = gcs.get_bucket(
                os.environ.get("BUCKET", "past-time-machine-dev-live-bucket-01")
            )
            blob = bucket.blob(uploaded_file.filename)

            blob.upload_from_string(
                uploaded_file.read(), content_type=uploaded_file.content_type
            )

            url = blob.public_url

            predictions = predict_image_classification_sample(
                project="824650660486",
                endpoint_id="5346599590432866304",
                location="us-central1",
                filename=url,
            )

            logging.info(blob.public_url)

            successful_upload = True

            for prediction in predictions:
                prediction = dict(prediction)
                print(prediction)
                predictedName = prediction["displayNames"]
                predictedConfidence = prediction["confidences"]
                print(" prediction:", predictedName[0], predictedConfidence[0])
                store_resutls(predictedName[0], url)

    return {
        "success": successful_upload,
        "url": url,
        "predictions": predictedConfidence[0],
        "predictionName": predictedName[0],
    }


@app.route("/images", methods=["GET"])
def images():
    if request.method == "GET":
        storage_client = storage.Client()

        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.list_blobs(
            os.environ.get("BUCKET", "past-time-machine-dev-live-bucket-01")
        )

        response = []
        for blob in blobs:
            print(blob.name)
            response.append(blob.public_url)

        return {"images": response}


@app.route("/search")
def search():
    query = request.args.get("q")
    results = []

    if query:
        db = firestore.Client()
        doc = db.collection(u"tags").document(query.lower()).get().to_dict()

        try:
            for url in doc["photo_urls"]:
                results.append(url)
        except TypeError as e:
            pass

    return {"results": results, "query": query}


@app.route("/tags")
def tags():
    results = []

    db = firestore.Client()
    docs = db.collection(u"tags").stream()

    try:
        for doc in docs:
            results.append(doc.id)
    except TypeError as e:
        pass

    return {"results": results}


@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return render_template("error.html"), 500


def store_resutls(tag, file_name):
    gcs = storage.Client()
    bucket = gcs.get_bucket(
        os.environ.get("BUCKET", "past-time-machine-dev-live-bucket-01")
    )
    db = firestore.Client()
    db.collection(u"tags").document(tag.lower()).set(
        {u"photo_urls": firestore.ArrayUnion([file_name])},
        merge=True,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
