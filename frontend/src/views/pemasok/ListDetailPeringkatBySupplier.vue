<template>
  <v-app>
    <v-card
    class="auto text-center ml-5 mr-5"
      max-width="1250">
      <br>
      <h1>Peringkat Supplier</h1>
      <br>

      <v-card
      
        max-width="1250">

          <v-data-table
            :headers = "headers"
            :items = "supplier"> 
        </v-data-table>
      </v-card>
    </v-card>

    <div class="d-flex">
    <v-card class=" mt-10 ml-5" max-width="1000" >
      <v-card
        class="mx-auto text-center"
        max-width="1000">
          <v-data-table
            :headers = "headers2"
            :items = "detailsupplier"
            :item-class = "itemRowBackground" > 
        </v-data-table>

      </v-card>

    </v-card>

  
        <v-card max-width="400"  class="mt-10  mb-4 ml-5">
          <template v-slot:title>
              This is a title
          </template>
  
          <template v-slot:subtitle>
            This is a subtitle
          </template>
  
          <template v-slot:text>
            This is content
          </template>

        <v-card-item>
        <v-card-title>Peringkat</v-card-title>
  
      <v-card-subtitle>Bobot</v-card-subtitle>
      </v-card-item>

      <v-card-text>
        This is content
      </v-card-text>
      </v-card>

    </div>


  </v-app>
  </template>
  
  <script>
    import axios from 'axios'
    export default {
      data: () => ({
        valid: true,
        headers:[
          {text : 'ID Supplier',               value : 'code'},
          {text : 'Nama Supplier',             value : 'nama'},
          {text : 'Adress',                    value : 'adress1'},
          {text : 'Phone',                     value : 'phone'},
          {text : 'Action',                    value : 'aksi'}        
        ],

        headers2 : [
            {text : 'Material', value : 'nama'},
            {text : 'Harga', value : 'Harga'},
            {text : 'Lead Time', value : 'LeadTime'},
            {text : 'Minimal Order', value : 'MinimalOrder'}
        ],

        supplier :[],
        detailsupplier : []
        
     
  
      
     
      }),
  
      mounted(){
          this.fetchData(),
          this.fetchData2()
        
      },
  
      methods: {
        async fetchData(){
          try{
            const res = await axios.get(`/supplier/get_supplier_byid/` + this.$route.params.id);
            if(res.data == null){
                alert("Proyek Kosong")
            }else{
                this.supplier = res.data;
                console.log(res,this.data)
            }
          } 
          catch(error){
              alert("Error")
              console.log(error)
          }
        },
  
        async fetchData2(){
          try{
            const res = await axios.get(`/supplier/detail_get_supplier_rank/` + this.$route.params.id);
            if(res.data == null){
                alert("Proyek Kosong")
            }else{
                this.detailsupplier = res.data;
                console.log(res,this.detailsupplier)
            }
          } 
          catch(error){
              alert("Error")
              console.log(error)
          }
           
        },
        itemRowBackground: function () {
            return  'style-1'
        },
        
        
      }
    }
  </script>