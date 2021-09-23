<template>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
              rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;400;500;700;900&display=swap" rel="stylesheet">

  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/gallery">Gallery</router-link> |
    <router-link to="/upload">Upload</router-link> |
    <router-link to="/search">Search</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view />
</template>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
