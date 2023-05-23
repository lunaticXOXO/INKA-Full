<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Peringkat Supplier</h1>
      <br>
      <v-card
        class="mx-auto text-center"
        max-width="1000">
          <v-data-table
            :headers = "headers"
            :items = "supplier"> 
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
          {text : 'ID Supplier',               value : 'code'},
          {text : 'Nama Supplier',             value : 'nama'},
          {text : 'Adress',                    value : 'adress1'},
          {text : 'Phone',                     value : 'phone'},
          {text : 'Action',                    value : 'aksi'}        
        ],
        supplier :[],
        
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
  
        
        selectProyek(proyek){ 
          console.log(proyek.id)
          //open(`/listRProyekbyProyek/${proyek.id}`)
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