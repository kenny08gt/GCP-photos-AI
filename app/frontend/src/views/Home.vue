<template>
  <div class="home">
    <div class="bg-gray">
      <h1 class="mb-4 mt-6 font-bold">Bienvenido</h1>
      <p>Esta es tu maquina para viajar al pasado. Recordar es volver a vivir</p>
      <div class="mt-4">
        <button @click="$router.push('/upload')">Subir imagen
          <span class="ml-2 material-icons blue">file_upload</span>
        </button>
        <button @click="$router.push('/galery')">Galeria
          <span class="ml-2 material-icons blue">perm_media</span></button>
        <button @click="$router.push('/search')">Buscar
          <span class="ml-2 material-icons blue">search</span></button>
      </div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  },
};
</script>
