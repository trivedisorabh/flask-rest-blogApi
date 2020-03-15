
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
      <th>Id</th>
      <th>Title</th>
      <th>Author<th>
      <th>Category </th>

    </mdb-tbl-head>
    <mdb-tbl-body>
      <tr>
        <th scope="row"> 1</th>
        <td>
          <button type="button" class="btn btn-indigo btn-sm m-0"> press </button>
        </td>
      </tr>
      <tr>
        <th scope="row"> 2</th>
        <td> blogpost </td>

      </tr>

    </mdb-tbl-body>
  </mdb-tbl>


</div>
</template>

<script>
import AdminNav from './AdminNav'
import {mdbTbl, mdbTblHead, mdbTblBody} from 'mdbvue';

export default {
  name: 'bloglist',
  components: {
    'sidebar': AdminNav,
    mdbTbl,
    mdbTblHead,
    mdbTblBody
  }
}
</script>

<style>
#header {
  margin-left: 50%;
}

#bloglistWrapper {
  display: table-cell;;

}

.table {
  padding-left: 260px;
}


</style>
