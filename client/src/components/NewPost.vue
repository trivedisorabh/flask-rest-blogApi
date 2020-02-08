<template>
<div id="article-wrapper">

  <!-- shared navbar for admin view -->
  <div id="sidebar">
    <sidebar/>
  </div>

  <div id="form-data">
    <b-form>
      <b-form-group id="input-gr-1" label="Title">
          <b-form-input id="input-1" type="text" placeholder="Enter blog title">
          </b-form-input>
      </b-form-group>
    </b-form>
  </div>

  <!-- editor that produces markdown. be sure to test out a rich editor aswell -->
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

#form-data {
  margin-left: 400px;
  margin-top: 50px;
  width: 60%
}

#input-gr-1{
  padding-top: 20px;
}



@import '~simplemde/dist/simplemde.min.css';

</style>
