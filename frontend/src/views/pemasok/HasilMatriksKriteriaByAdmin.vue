<template>
    <v-app>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Kriteria Bobot </h1>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "kriteriabobot"
            :items-per-page="3"
            >
          </v-data-table>
      </v-card>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Matriks Kriteria</h1>
          <br>
         
          <v-data-table 
            :headers = "column2"
            :items = "matrikskriteria"
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
              {text : 'ID Kriteria',                   value : 'IDKriteria'},
              {text : 'Bobot',                         value : 'Bobot'},
              {text : 'Rangking',                      value : 'rangking'},
              {text : 'ID Penghitung',                  value : 'idPenghitung'}
           
          ],

         column2 : [
            {text : 'ID Kriteria 01', value : 'IDKriteria'},
            {text : 'ID Kriteria 02', value : 'IDKriteria02'},
            {text : 'Nilai', value : 'Nilai'},
            {text : 'Nilai02', value : 'Nilai02'},
            {text : 'ID Penghitung', value : 'idPenghitung'}
         ],

          matrikskriteria : [],
          kriteriabobot : [],
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
            const res = await axios.get('/ahp/hasil_matriksbobot/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.kriteriabobot = res.data
              console.log(res,this.kriteriabobot)
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
            const res = await axios.get('/ahp/hasil_matrikskriteria/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.matrikskriteria = res.data
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