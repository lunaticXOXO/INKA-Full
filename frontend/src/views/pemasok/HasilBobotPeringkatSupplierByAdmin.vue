<template>
    <v-app>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Peringkat Supplier </h1>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "hasilperingkat"
            :items-per-page="3"
            >
          </v-data-table>
      </v-card>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Bobot Supplier</h1>
          <br>
         
          <v-data-table 
            :headers = "column2"
            :items = "hasilbobot"
            :items-per-page="5"
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
              {text : 'ID Supplier',                   value : 'IDSupplier'},
              {text : 'Bobot',                         value : 'Bobot'},
              {text : 'Rangking',                      value : 'Rangking'},
              {text : 'ID Penghitung',                  value : 'idPenghitung'}
           
          ],

         column2 : [
            {text : 'ID Kriteria', value : 'IDKriteria'},
            {text : 'ID Supplier', value : 'IDSupplier'},
            {text : 'Bobot', value : 'Bobot'},
            {text : 'Bobot Global', value : 'BobotGlobal'},
            {text : 'ID Penghitung', value : 'idPenghitung'}
         ],

          hasilperingkat : [],
          hasilbobot : [],
          editedIndex: -1,
          editedItem: {
            id: '',
            nama: '',
            purchaseDate: '',
            purchaserName: '',
          },
          defaultItem: {
            id: '',
            nama: '',
            purchaseDate: '',
            purchaserName: '',
          },
         
        }
      },
    
      mounted(){
          this.fetchData(),
          this.fetchData2()
      },


  
      methods: {
        close () {
          setTimeout(() => {
              this.editedItem = Object.assign({}, this.defaultItem);
              this.editedIndex = -1;
          }, 300)
        },
  
      validate(){

        location.replace('/')

      },

        editMaterial(types){
          console.log('ID : ' + types.id)
          this.editedIndex = this.types.indexOf(types);
          this.editedItem = Object.assign({},types);
        },
  
        async fetchData(){
          try{
            const axios = require('axios');
            const res = await axios.get('/ahp/hasil_rangking_supplier/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.hasilperingkat = res.data
              console.log(res,this.hasilperingkat)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },

        
        async fetchData2(){
          try{
            const axios = require('axios');
            const res = await axios.get('/ahp/hasil_bobot_supplier/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.hasilbobot = res.data
              console.log(res,this.hasilbobot)
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