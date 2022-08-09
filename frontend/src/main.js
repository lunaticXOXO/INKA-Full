import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Axios from 'axios';
import VueAxios from 'vue-axios';
import DatetimePicker from 'vuetify-datetime-picker';

Vue.config.productionTip = false

Vue.use(VueAxios, Axios, DatetimePicker);

Vue.prototype.$axios = Axios;
Vue.axios.defaults.baseURL = `https://backend-inka-deploy.herokuapp.com/`;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
