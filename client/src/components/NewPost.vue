<template>
<div id="article-wrapper">

  <!-- shared navbar for admin view -->
  <div id="sidebar">
    <sidebar/>
  </div>

  <div id="markdown-editor">
    <vue-simplemde ref="markdownEditor" />
  </div>

</div>

</template>


<script>

import AdminNav from './AdminNav';
import VueSimplemde from 'vue-simplemde'

export default {
  name: 'admin',
  components: {
    'sidebar': AdminNav,
    VueSimplemde
  }
}

</script>

<style>

</style>
