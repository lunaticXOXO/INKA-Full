<template>
  <v-app class="grey lighten-4">
    <div v-if="idRole == 'Guest'">
      <SidebarGuest />
    </div>
    <div v-if="idRole == 1">
      <SidebarAdmin />
    </div>
    <!--
    <div v-else-if="idRole == 1">
      <OwnerNavbar />
    </div>
    <div v-else-if="idRole == 2">
      <InventoryNavbar />
    </div>
    -->
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import SidebarGuest from './components/SidebarGuest.vue'
import SidebarAdmin from './components/SidebarAdmin.vue'
import Login from "./services/Login.js"

export default {
  name: 'App',
  components: { 
    SidebarGuest, 
    SidebarAdmin 
  },

  mounted() {
    this.fetchData();
  },

  data: () => {
    const data = [];
      return {
          idRole: null,
          loginService: new Login(),
          data,
      };
  },

  methods: {
    async fetchData() {
        this.idRole = this.loginService.getCurrentUserType();
        console.log(this.idRole)
    },
  },
};
</script>
