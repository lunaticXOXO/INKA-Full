<template>
  <v-app class="grey lighten-4">
    <Sidebar />
    <v-main>
      <router-view/>
    </v-main>

  </v-app>
</template>

<script>
import Sidebar from '@/components/SidebarView'

export default {
  name: 'App',
  components: { Sidebar },
  data: () => ({
    
  }),
};
</script>
