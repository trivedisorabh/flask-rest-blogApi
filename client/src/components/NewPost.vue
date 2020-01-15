<template>
<div id="article-wrapper">

  <!-- shared navbar for admin view -->
  <div id="sidebar">
    <sidebar/>
  </div>

  <div id="markdown-editor">
    <vue-simplemde preview-class="markdown-body" ref="markdownEditor" />
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

#markdown-editor {
  margin-left: 400px;
  margin-top: 50px;
  position: absolute;
  width: 60%;
}

.markdown-editor {

}

.markdown-body {
  margin-left: 500px;
}

@import '~simplemde/dist/simplemde.min.css';

</style>
