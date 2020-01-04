<template>
  <div class="container-fluid h-100">
    <!-- bootstrap centering and higth regulation.. -->
    <div class="row justify-content-center align-items-center h-100">
      <div class="col col-sm6 col-md-6 col-lg-4 col-xl-3">
        <Form v-on:submit.prevent="onSubmit">
          <p class="h4 text-center mb-4"> Logg inn </p>
          <div class="grey-text">
            <!-- mdb need to be installed to use the UI-kit -->
            <mdb-input label="username" v-model="username" icon="user" type="text"/>
            <mdb-input label="password" v-model="password" icon="lock" type="password"/>
          </div>

          <div class="text-center">
            <mdb-btn type="submit"> Login </mdb-btn>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import {mdbInput, mdbBtn} from 'mdbvue';
  import axios from 'axios';
  import router from '../router'

  export default {
    name: 'Basic',
    components: {
      mdbInput,
      mdbBtn
    },
    data() {
      return {
        username: '',
        password: '',
      };

    },
    methods:{
      onSubmit() {
        const loginPath = 'http://localhost:5000/login';
        let loginData = {
          username: this.username,
          password: this.password
        }
        axios.post(loginPath, loginData)
        .then((res) => {
          localStorage.setItem('userToken',res.data)
          // eslint-disable-next-line
          console.log()
          router.push('/admin')
        })

      }
    }
  }
</script>

<style>


</style>
