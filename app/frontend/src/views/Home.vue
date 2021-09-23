<style scoped>
p {
  max-width: 500px;
}
</style>
<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 mt-6 font-bold">Bienvenido</h1>

      <p class="text-left mx-auto">
        Esta es tu maquina para viajar al pasado. Recordar es volver a vivir
      </p>

      <div class="">
        <div class="text-left mx-auto mt-6">
          <img
            src="/para-mas-placer.jpeg"
            alt="Homer para mas placer meme"
            style="max-height: 150px; width: auto;"
            class="mx-auto"
          />
          <p style="" class="mx-auto mt-6 text-left">
            Este sistema utiliza ademas de la Vision api, un modelo entrenado que reconocera a
            traves de una imagen a que caricatura pertenece. Este modelo esta entrenada con images
            de los Simpsons, Rick and morty y Futurama. Así que si subes una imagen de estos dibujos
            animados, lo clasificara (hopefully) correctamente :)
          </p>
        </div>
        <div class="mt-8">
          <button @click="$router.push('/upload')">
            Subir imagen
            <span class="ml-2 material-icons blue">file_upload</span>
          </button>
          <button @click="$router.push('/gallery')">
            Galeria <span class="ml-2 material-icons blue">perm_media</span>
          </button>
          <button @click="$router.push('/search')">
            Buscar <span class="ml-2 material-icons blue">search</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {},
};
</script>
