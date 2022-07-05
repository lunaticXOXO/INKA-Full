<template>
    <v-flex d-flex>
        <h1>List Operasi</h1>
        <v-layout wrap>
            <v-flex md4 v-for="item in this.$store.getters.getItems" :key="item.id">
                <v-card class="card-container">
                    {{ item.title }}
                </v-card>
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      items:[],
    }),

    mounted(){
        //this.fetchData()
    },

    methods: {
        async fetchData(){
            try{
                const axios = require('axios');
                const res = await axios.get(`/operasi/get_alloperasi`);
                if(res.data == null){
                    alert("Operasi Kosong")
                }else{
                    this.operasi = res.data;
                    console.log(res,this.data)
                }
            } 
            catch(error){
                alert("Error" + error)
                console.log(error)
            }
        },
    }
  }
</script>