<style scoped>
.input-group {
  background: #ededed;
  border-radius: 4px;
  width: max-content;
  margin: auto;
}
input {
  padding: 6px 10px;
  background: #ededed;
  border-radius: 4px;
  padding-left: 15px;
}
input:focus {
  border: none;
  outline: none;
}
small {
  padding: 5px 10px;
  border-radius: 10px;
  background: #ededed;
  margin-right: 6px;
  cursor: pointer;
}
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
      <h1 class="mb-4 font-bold">Buscar</h1>
      <p>Busca por terminos en ingles</p>
      <div class="mt-4">
        <form @submit.prevent="search">
          <div class="input-group">
            <span class="material-icons ml-2">search</span>
            <input type="text" placeholder="Busca un termino" v-model="query" />
          </div>
          <button type="submit" class="mt-2">Buscar</button>
        </form>
        <div>
          <p class="mt-2 text-sm mb-2">Podrías probar una de las siguientes</p>
          <div>
            <small
              v-for="(tag, key) in tags"
              :key="key"
              @click="searchTag(tag)"
              class="inline-block mb-2"
              >{{ tag }}</small
            >
          </div>
        </div>
      </div>
      <div v-if="searching" class="pt-8">
        Buscando...
      </div>
      <div v-if="images.length" class="px-14 pt-8">
        <p>{{ images.length }} imagenes encontradas</p>
        <masonry-wall :items="images" :ssr-columns="1" :padding="16">
          <template #default="{ item, index }">
            <div style="" :key="index" class="img-wrapper">
              <img :src="item" alt="" />
            </div>
          </template>
        </masonry-wall>
      </div>
      <div v-if="noResults" class="pt-8">
        No obtuvimos resultados
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// @ is an alias to /src

export default {
  name: 'Search',
  data() {
    return {
      query: '',
      images: [],
      noResults: false,
      searching: false,
      tags: [],
    };
  },
  components: {},
  mounted() {
    this.getTags();
  },
  methods: {
    search() {
      this.noResults = false;
      this.searching = true;
      console.log('search');
      const url = `http://34.135.14.66/search?q=${this.query}`;
      axios
        .get(url)
        .then((response) => {
          if (!response.data.results.length) this.noResults = true;
          this.images = response.data.results;
          this.searching = false;
        })
        .catch((err) => {
          console.error(err);
          this.searching = false;
        });
    },
    getTags() {
      axios
        .get('http://34.135.14.66/tags')
        // .get('http://localhost:5000/tags')
        .then((response) => {
          this.tags = response.data.results;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    searchTag(tag) {
      this.query = tag;
      this.search();
    },
  },
};
</script>
