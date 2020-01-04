<template>
  <div id="admin-wrapper">
    <!-- shared navbar for admin view -->
    <div id="sidebar">
      <sidebar/>
    </div>

  <!-- welcomebox main page. -->
    <div class="welcome">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <div class="content">
              <!-- rember to implement user -->
              <h2>Velcome to Admin panel </h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor</p>
            </div>
          </div>
        </div>
      </div>
    </div>
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

#admin-wrapper {

}

.welcome{
  color: #CCC;
  width: 30%%;
  position: absolute;
  padding: 15px;
  top: 100px;
  margin-left: 250px;
}

.welcome .content {
  background-color: #393E46;
}

.content {
  padding: 15px;
}

</style>
