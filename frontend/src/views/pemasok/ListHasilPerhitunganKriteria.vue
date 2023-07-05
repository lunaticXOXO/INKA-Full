<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Kriteria Pemasok</h1>
      <br>
      <v-card
        class="mx-auto text-center"
        max-width="1000">

          <v-data-table
            :headers = "headers"
            :items = "hasilkriteria"
            :items-row-page = 5>            
        </v-data-table>
      </v-card>
    </v-card>
  </template>
  
  <script>
    import axios from 'axios'
    export default {
      data: () => ({
        valid: true,
        headers:[
          {text : 'ID Kriteria',                value : 'IDKriteria'},
          {text : 'Nilai',                      value : 'Nilai'},
          {text : 'ID Kriteria 2',              value : 'IDKriteria02'},
          {text : 'Nilai 02',                      value : 'Nilai02'},

        ],
        hasilkriteria :[],
        
        editedIndex : -1,
        editedItem : {
          id : '',
          nama : '',
          customerid : ''
        },
  
        defaultItem : {
          id : 'New ID',
          nama : 'New Nama',
          customerid : 'New Customer'
         },
         'id' : '',
         'nama' : '',
         'customerid' : ''
      }),
  
      mounted(){
          this.fetchData()
        
      },
  
      methods: {
        async fetchData(){
          try{
            const res = await axios.get(`/supplier/get_hasil_perhitungan_kriteria`);
            if(res.data == null){
                alert("Proyek Kosong")
            }else{
                this.hasilkriteria = res.data;
                console.log(res,this.hasilkriteria)
            }
          } 
          catch(error){
              alert("Error")
              console.log(error)
          }
        },
  
       
  
      
  
        close(){
          setTimeout(()=>{
            this.editedItem = Object.assign({},this.defaultItem)
            this.editedIndex = -1;
  
          },300)
        },
  
        updateProyek(proyek){
          console.log(proyek.id)
          this.editedIndex = this.proyek.indexOf(proyek)
          this.editedItem = Object.assign({},proyek)
        },
  
        deleteProyek(proyek){
          console.log(proyek.id)
        }
      }
    }
  </script>