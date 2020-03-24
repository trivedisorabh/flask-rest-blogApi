import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Login from './components/Login.vue';
import Admin from './components/Admin.vue';
import NewPost from './components/NewPost.vue';
import BlogList from './components/BlogList.vue'
import Home from './components/Home.vue'

Vue.use(Router);


export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { requiresAuth: false}
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin,
      meta: {requiresAuth: true}
    },
    {
      path: '/newpost',
      name: 'NewPost',
      component: NewPost,
      meta: {requiresAuth: true}
    },
    {
      path: '/bloglist',
      name: 'BlogList',
      component: BlogList
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ],
});
