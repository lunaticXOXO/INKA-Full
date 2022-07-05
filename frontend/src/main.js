import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Axios from 'axios';
import VueAxios from 'vue-axios';

Vue.config.productionTip = false

Vue.use(VueAxios, Axios);

Vue.prototype.$axios = Axios;
Vue.axios.defaults.baseURL = `http://localhost:8181`;

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
