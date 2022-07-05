<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Pemasok</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "pemasok">
            </v-data-table>
        </v-card>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'Kode', value : 'code'},
        {text : 'Nama', value : 'nama'}      
      ],
      pemasok:[],
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
      async fetchData(){
        try{
          const axios = require('axios');
          const res = await axios.get(`/proyek/get_allsupplier`);
          if(res.data == null){
              alert("Pemasok Kosong")
          }else{
              this.pemasok = res.data;
              console.log(res,this.data)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },
    }
  }
</script>