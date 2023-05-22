<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
        <br>
        <h1>Material Perlu Pesan</h1>
        <br>
        <!-- <router-link to="/jenisMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Material Type
            </v-btn>
        </router-link> -->

        <!-- <v-data-table 
            v-model="selected"
            :headers = "column"
            :items = "types"
            item-value = "code"
            show-select
            class="elevation-1">
           
        </v-data-table> -->

        <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="tanggalPurchase" v-bind="attrs" v-on="on" label="Purchase Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="500" v-model="tanggalPurchase"></v-date-picker>
          </v-menu>

        <v-data-table 
          id="mytable"
          show-select
          v-model="selected"
          :headers="headers"
          :items="types"
          :items-per-page="5"
          class="elevation-1"
          item-key="code"
    ></v-data-table>

    <v-btn color="primary" class="d-flex ml-15 mb-20">
        Purchase
    </v-btn>
    
    </v-card>
</template>

<script>
  export default {
   data(){
    return {
        selected: [],
        headers: [
        {
          text: 'Codes',
          align: 'left',
          sortable: false,
          value: 'code',
        },
       
        {text : 'Is Assy', value : 'isAssy'},
        {text : 'Is Available',value : 'isAvailable'},
        {text: 'Name' , value : 'nama'}
      ],
  
       types : []


   }    
},

mounted(){
  this.fetchMaterial()
},
  
  methods : {

    async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_type');
          if (res.data == null){
            alert('Material Kosong')
          }else{
            this.types = res.data
            console.log(res,this.types)
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