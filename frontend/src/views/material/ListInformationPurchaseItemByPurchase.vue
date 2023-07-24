<template>
    <v-app>

    <v-card
        class="mt-10"
        max-width = "1000">
        <br>
        <h2>Detail Purchase Material</h2>
        <br>
        <v-data-table 
            :headers="column"
            :items="information1">
          </v-data-table>
      </v-card>

      <v-card 
          class="mt-10"
          max-width = "1500">
          <br>
          <h1>List Purchase Item Order</h1>
          <br>
         
          <v-data-table 
            :headers = "column2"
            :items = "information_detail"
            :items-per-page="3"
            >
          </v-data-table>
      </v-card>

      <v-card 
          class="mt-5"
          max-width = "700">
          <br>
          <h1>Total Harga</h1>
          <br>
         
          <v-data-table 
            :headers = "column3"
            :items = "sum"
            :items-per-page="3"
            >
          </v-data-table>
      </v-card>
      
    </v-app>
  </template>
   
  <script>
      export default {
        data(){
          return {
            valid : true,
            column : [
                {text : 'Nama',                         value : 'namaPurchase'},
                {text : 'Tanggal Pesan',                value : 'purchaseDate'},
                {text : 'Schedulled Arrival',           value : 'schedulledArrival'},
                {text : 'Supplier',                     value : 'supplierCode'},
              
            ],
            
            column2 : [
              {text : 'Code Material',              value : 'materialTypeCode'},
              {text : 'Nama Material',              value : 'namaMaterial'},
              {text : 'Pesan',                      value : 'quantity'},
              {text : 'Harga',                      value : 'Harga'},
              {text : 'Lead Time',                  value : 'LeadTime'},
              {text : 'Minimal Order',              value : 'MinimalOrder'}              


            ],

            column3 : [
             
              {text : 'Total Harga',           value : 'Total'}
          ],
            
          information1 : [],
        information_detail : [],
          sum : [],
            dueDate: undefined
          }
        },
    
        mounted(){
          this.fetchInformation1(),
          this.fetchInformation2(),
          this.fetchSum()
        },
    
        methods: {
          
    
          async fetchInformation1(){
            try{
              const axios = require('axios');
              const res = await axios.get('/material/get_information_purchaseitem/' + this.$route.params.id);
              if (res.data == null){
                alert('Purchase Item Kosong')
              }else{
                this.information1 = res.data
                console.log(res,this.information1)
              }
            }
            catch(error){
              alert("Error")
              console.log(error)
            }
          },
  
          async fetchInformation2(){
            try{
              const axios = require('axios');
              const res = await axios.get('/material/get_information_purchaseitem_detail/' + this.$route.params.id);
              if (res.data == null){
                alert('Purchase Item Kosong')
              }else{
                this.information_detail = res.data
                console.log(res,this.information_detail)
              }
            }
            catch(error){
              alert("Error")
              console.log(error)
            }
          },
          
          async fetchSum(){
            try{
             
              const axios = require('axios');
              const res = await axios.get('/material/get_sum_purchaseitem/' + this.$route.params.id);
              if (res.data == null){
                alert('Data Kosong')
              }else{
                this.sum = res.data
                console.log(res,this.sum)
              }
            }
            catch(error){
              alert("Error")
              console.log(error)
            }
          }
        }
      }
    </script>
  