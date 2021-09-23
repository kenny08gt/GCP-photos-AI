<style scoped>
.dropzone {
  max-width: 770px;
  width: 90vw;
  height: 442px;
  background: #f8f8f8;
  border-radius: 8px;
  margin: auto;
  border: 2px dashed var(--blue);
  display: flex;
  justify-content: center;
  align-items: center;
}

.uploading {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: center;
  align-items: center;
  align-content: center;
  flex-flow: column;
}
</style>
<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 font-bold">Sube una imagen</h1>
      <div class="mt-4">
        <div v-bind="getRootProps()" class="dropzone">
          <input v-bind="getInputProps()" />
          <p v-if="isDragging">Suelta la imagen aqui ...</p>
          <p v-else>Drag 'n' drop tu imagen aqui o haz click aqui</p>
          <div v-show="isUploading" class="uploading">
            Se esta subiendo...
            <loader />
          </div>
        </div>
        <div v-if="lastUploadedImage">
          <img :src="lastUploadedImage" alt=""
          style="height: 150px; width: auto; border-radius: 4px;"
          class="mt-8 mx-auto">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { useDropzone } from 'vue3-dropzone';
import axios from 'axios';
import { ref } from 'vue';
import Loader from '../components/Loader.vue';

export default {
  name: 'Upload',
  components: { Loader },
  setup() {
    const isDragging = ref(false);
    const isUploading = ref(false);
    const lastUploadedImage = ref('');

    function uploadFile(files) {
      console.log(files);
      const formData = new FormData();
      formData.append('image', files[0]);
      isUploading.value = true;
      axios
        // .post('http://34.135.14.66/upload', formData, {
        .post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Accept: 'application/json',
          },
        })
        .then((response) => {
          console.info(response.data);
          isUploading.value = false;
          lastUploadedImage.value = response.data.url;
          alert('Se subió con éxito!');
        })
        .catch((err) => {
          console.error(err);
          isUploading.value = false;
        });
    }

    function onDrop(acceptFiles, rejectReasons) {
      console.log('onDrop');
      isDragging.value = false;
      if (acceptFiles.length > 0) uploadFile(acceptFiles);
      if (rejectReasons.length > 0) {
        alert('something went wrong');
        console.log(rejectReasons);
      }
    }

    function onDragEnter() {
      isDragging.value = true;
      console.log('drag enter');
    }

    function onDragLeave() {
      isDragging.value = false;
      console.log('drag leave');
    }

    const options = {
      onDrop,
      onDragEnter,
      onDragLeave,
      maxFiles: 1,
      multiple: false,
      accept: 'image/jpg,image/png,image/jpeg',
    };

    const { getRootProps, getInputProps, ...rest } = useDropzone(options);

    return {
      getRootProps,
      getInputProps,
      isDragging,
      isUploading,
      lastUploadedImage,
      ...rest,
    };
  },
};
</script>
