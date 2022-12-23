import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import lock from "../assets/logo/lock.png";

Vue.use(Vuetify, {
    theme: {
        primary: '#9652ff'
    }
});

export default new Vuetify({
    icons: {
        values: {
          lock: { // name of our custom icon
            component: lock, // our custom component
          },
        },
      },
});
