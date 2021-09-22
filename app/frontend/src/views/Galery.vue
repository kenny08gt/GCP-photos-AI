<style scoped>
/* img {
  max-height: 250px;
  width: auto;
} */
</style>
<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 font-bold">Galeria</h1>
      <div class="mt-4 px-14">
        <masonry-wall :items="images" :ssr-columns="1"  :padding="16">
          <template #default="{ item, index }" >
            <div style="height: auto; width:auto; overflow:hidden;" :key="index">
              <img :src="item" alt="">
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
  name: 'Galery',
  components: {},
  data() {
    return {
      images: [],
    };
  },
  mounted() {
    axios
      .get('http://localhost:5000/images')
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
