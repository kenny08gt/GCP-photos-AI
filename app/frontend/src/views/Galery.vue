<style scoped>
/* img {
  max-height: 250px;
  width: auto;
} */
.img-wrapper {
  height: auto;
  width: auto;
  transition: transform 0.2s;

}
.img-wrapper:hover {
  transform: scale(1.01);
}
.img-wrapper img {
    box-shadow: 0 3px 4px 0 rgb(0 0 0 / 20%), 0 3px 3px -2px rgb(0 0 0 / 14%),
    0 1px 8px 0 rgb(0 0 0 / 12%);
    border-radius: 4px;
}
</style>
<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 font-bold">Galeria</h1>
      <div class="mt-4 px-14">
        <masonry-wall :items="images" :ssr-columns="1" :padding="16">
          <template #default="{ item, index }">
            <div style="" :key="index" class="img-wrapper">
              <img :src="item" alt="" />
            </div>
          </template>
        </masonry-wall>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// @ is an alias to /src

export default {
  name: 'Gallery',
  components: {},
  data() {
    return {
      images: [],
    };
  },
  mounted() {
    axios
      .get('http://34.135.14.66/images')
      .then((response) => {
        console.info(response.data);
        this.images = response.data.images;
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>
