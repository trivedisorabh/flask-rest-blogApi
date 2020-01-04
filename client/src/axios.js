import axios from 'axios'


/* Using vue-axios to connect to the api and handle the token */

const instance = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Authorization': {
      toString(){
        return `Bearer ${localStorage.getItem('userToken')}`
      }
    }
  }
});

export default instance
