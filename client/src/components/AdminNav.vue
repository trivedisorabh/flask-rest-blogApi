<template>
  <body>
    <div id="sidenav">
      <aside id="sidebar-wrapper">
        <div class="sidebar-brand">
          <h2>Admin</h2>
        </div>
        <ul class="sidebar-nav">
          <li class="active">
            <a href="#"><i class="fa fa-home"></i>Hjem</a>
          </li>
          <li>
            <a href="#"><i class="fas fa-blog"></i>Poster</a>
          </li>
          <li>
            <router-link to="/NewPost"><i class="fas fa-envelope"></i> Ny post</router-link>
          </li>
        </ul>
      </aside>
    </div>
  </body>
</template>


<script>


</script>

<style>
/* simple prototype css, need to be adjust for sevral views... */
#sidenav {

  /* must be a simpler way to have the navbar fill out the voids */
  padding-left: 0;
  transition: all 0.5s;
  position: relative;
  margin-top: -50px;
  margin-bottom: 50px;
  /* Testing this vs "inline block" in new post, and main window handling */
  display: table;
  

}

#sidebar-wrapper{
  background: #222;
  position: fixed;
  height: 100%;
  width: 250px;
  overflow-y: auto;
  overflow-x: hidden;
  z-index: 1000;
}

.sidebar-brand {
  position: absolute;
  width: 250px;
  text-align: center;
  padding: 20px 0;
}

.sidebar-brand h2 {
  margin: 0;
  font-weight: 600;
  font-size: 24px;
  color: #fff;
}

.sidebar-nav {
  position: absolute;
  top: 75px;
  width: 250px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.sidebar-nav > li a {
  display: block;
  text-decoration: none;
  color: #757575;
  font-weight: 600;
  font-size: 18px;
}

.sidebar-nav li {
  text-indent: 10px;
  line-height: 42px;
}

.sidebar-nav li a:hover {
  text-decoration: none;
  color: #fff;
  background: #F8BE12;
}

.sidebar-nav li a i.fa{
  font-size: 24px;
  width: 60px;
}

.sidebar-nav li a i.fas{
  font-size: 24px;
  width: 60px;
}


</style>
