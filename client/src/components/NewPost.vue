<template>
<div id="article-wrapper">

  <!-- shared navbar for admin view -->
  <div id="sidebar">
    <sidebar/>
  </div>

<div id="main-content">
  <div id="form-data">
    <b-form>
      <b-form-group v-model="name" id="input-gr-1" label="Title">
          <b-form-input  id="input-1" type="text" placeholder="Enter blog title">
          </b-form-input>
      </b-form-group>
    </b-form>
  </div>

  <!-- editor that produces markdown. be sure to test out a rich editor aswell -->
  <div id="markdown-editor">
    <vue-simplemde v-model="content"  ref="markdownEditor" />
    <b-button variant="dark" v-on:click= "onSubmit"> Publish </b-button>
  </div>

</div>

</div>

</template>


<script>

import AdminNav from './AdminNav';
import VueSimplemde from 'vue-simplemde';
import axios from 'axios';

export default {
  name: 'admin',
  components: {
    'sidebar': AdminNav,
    VueSimplemde
  },
  data() {
    return {
      content: '',
      msg: '',
      id: 0,
      name: ''
    }
  },
  methods: {
    onSubmit: function() {
      let userId = JSON.parse(localStorage.getItem('userId'))
      this.id = userId

      // Prints just for validating and testing. 

      // eslint-disable-next-line
      console.log(localStorage.getItem('userToken'))
      // eslint-disable-next-line
      console.log(userId)
      axios.get('http://localhost:5000/user/' + userId, {
        headers: {
          "x-access-token" : localStorage.getItem('userToken')
        }
      })
      .then(res => {
        // eslint-disable-next-line
        console.log(res.data)
      })
      .catch(error => {
        this.msg = error.res.data.message
        // eslint-disable-next-line
        console.log(msg)
      })
      const postData = {
        "name" : this.name,
        "content" : this.content,
        "author_id" : this.id
      }
      axios.post('http://localhost:5000/blogpost', postData)
      .then(res => {
        // eslint-disable-next-line
        console.log(res.data.message);
      })
    }
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
  width: 60%;
}


#main-content {
  margin-top: 100px;
  display: table-cell;
}



@import '~simplemde/dist/simplemde.min.css';

</style>
