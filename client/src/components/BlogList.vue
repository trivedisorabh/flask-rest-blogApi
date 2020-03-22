
<template>
<div id="bloglistWrapper">
  <!-- Shared navbar component -->
  <div id="sidebar">
    <sidebar/>
  </div>

  <div id="header">
    <h2> Posts </h2>

  </div>

  <mdb-tbl btn responsive striped class="table">
    <mdb-tbl-head>
      <tr>
        <th>Id</th>
        <th>Title</th>
        <th>Author id</th>
        <th>Actions</th>
      </tr>
    </mdb-tbl-head>
    <mdb-tbl-body>
       <tr v-for="post in dataRes" :key="post.id">

        <td> {{post.id}}</td>
        <td> {{post.name}} </td>
        <td> {{post.author_id}} </td>
        <td> <button type="button" class="btn btn-indigo btn-sm m-0">Edit</button> </td>
        <td> <button type="button" class="btn btn-red btn-sm m-0">Delete</button> </td>

      </tr>

    </mdb-tbl-body>
  </mdb-tbl>


</div>
</template>

<script>
import AdminNav from './AdminNav'
import axios from 'axios';
import {mdbTbl, mdbTblHead, mdbTblBody} from 'mdbvue';

export default {
  name: 'bloglist',
  components: {
    'sidebar': AdminNav,
    mdbTbl,
    mdbTblHead,
    mdbTblBody
  },
  data() {
    return {
      dataRes: [],
      msg: ''
    }
  },
  mounted() {
    const blogpostData = 'http://localhost:5000/blogpost'
    axios.get(blogpostData)
    .then(respons => {
      this.dataRes = respons.data.blogposts

      // eslint-disable-next-line
      console.log(this.dataRes);
    })
    .catch(error => {
      // eslint-disable-next-line
      console.log(error)
    })
  },
  methods: {

  }

}
</script>

<style>

td {

}
#header {
  margin-left: 50%;
}

#bloglistWrapper {
  display: table-cell;;

}

.table {
  padding-left: 400px;
}


</style>
