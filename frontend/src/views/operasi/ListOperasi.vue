<template>
    <v-app>
        <h1 class="ma-4">List Operasi</h1>
        <v-flex d-flex>    
            <br><br>
            <v-layout wrap>
                <v-flex md4 v-for="item in items" :key="item.id">
                    <v-card class="card-container mx-8 my-8 pa-4">
                        <h3>ID Proses</h3>
                        {{ item.proses }}
                    </v-card>
                </v-flex>
            </v-layout>
        </v-flex>
    </v-app>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      items:[],
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
        async fetchData(){
            try{
                const axios = require('axios');
                const res = await axios.get(`/operasi/get_operasi_byproduk/PR_02`);
                if(res.data == null){
                    alert("Operasi Kosong")
                }else{
                    this.items = res.data;
                    console.log(res,this.items)
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