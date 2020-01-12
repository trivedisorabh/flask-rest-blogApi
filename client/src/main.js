import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from './axios'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'


Vue.use(BootstrapVue, axios)
Vue.component('vue-simplemde', VueSimplemde)
Vue.config.productionTip = false
axios.defaults.headers.common['Authorization'] = "Bearer" + localStorage.getItem('userToken')


// should thos code maybe be structured somewhere els?
// beforeEach is checking if the token i valid, and protects the routes.
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    // eslint-disable-next-line
    console.log(to.matched.some(record => record.meta.requiresAuth))
    if (localStorage.getItem('userToken') == null){
      next({
        path: '/login',
        params: {nextUrl: to.fullPath}
      })
    }
    else{
      next()
    }
  }
  else{
    if(localStorage.getItem('userToken') != null){
      next({
        path: '/admin',
        param: {nextUrl: '/admin'}
      })
    }
    else{
      next()
    }
  }
});

new Vue({
  router,
  axios,
  render: h => h(App),
}).$mount('#app')
