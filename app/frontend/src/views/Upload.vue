<style scoped>
.dropzone {
  width: 770px;
  height: 442px;
  background: #f8f8f8;
  border-radius: 8px;
  margin: auto;
  border: 2px dashed var(--blue);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 font-bold">Sube una imagen</h1>
      <div class="mt-4">
        <p v-if="isUploading">
          Is uploading ...
        </p>
        <div v-bind="getRootProps()" class="dropzone">
          <input v-bind="getInputProps()" />
          <p v-if="isDragging">Suelta la imagen aqui ...</p>
          <p v-else>Drag 'n' drop tu imagen aqui o haz click aqui</p>
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

export default {
  name: 'Upload',
  components: {},
  setup() {
    const isDragging = ref(false);
    const isUploading = ref(false);

    function uploadFile(files) {
      const formData = new FormData();
      formData.append('image', files[0]);
      isUploading.value = true;
      axios
        .post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Accept: 'application/json',
          },
        })
        .then((response) => {
          console.info(response.data);
          isUploading.value = false;
          alert('Success');
        })
        .catch((err) => {
          console.error(err);
          isUploading.value = false;
        });
    }

    function onDrop(acceptFiles, rejectReasons) {
      isDragging.value = false;
      if (acceptFiles.length > 0) uploadFile(acceptFiles);
      if (rejectReasons.length > 0) alert('something went wrong');
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
      accept: 'image/jpg,image/png',
    };

    const { getRootProps, getInputProps, ...rest } = useDropzone(options);

    return {
      getRootProps,
      getInputProps,
      isDragging,
      isUploading,
      ...rest,
    };
  },
};
</script>
