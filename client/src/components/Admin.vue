<template>
  <div id="sidebar">
    <sidebar/>
  </div>

</template>

<script>

import AdminNav from './AdminNav.vue';

export default {
  name: 'admin',
  components: {
    'sidebar': AdminNav
  }
}

</script>

<style>

</style>
