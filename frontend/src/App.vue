<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import Logo from './components/parts/Logo'
export default {
  name: 'App',
  components: {
    Logo
  }
}
</script>

<style>
@import "./assets/css/style.css";
#app {
  width: 100%;
  height: 100%;
}
</style>
