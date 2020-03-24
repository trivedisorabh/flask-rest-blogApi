<template>
  <div id="home-wrapper">
    <div id="navbar">
    <navbar/>
    </div>
  </div>

</template>

<script>

import Nav from './Nav.vue'

export default {
  name: 'home',
  components: {
    'navbar': Nav
  }
}
</script>

<style>
</style>
