<template>
  <div id="app">
    <img src="./assets/logo.png" />
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      message: '',
    }
  },
  mounted: function () {
    axios.get('http://localhost:5000/api/hello').then((response) => {
      this.message = response.data.message
    })
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
