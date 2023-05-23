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
            :items = "supplierRank"> 
             
            <template v-slot:[`item.aksi`]="{ item }">
            
            <div>
              <router-link :to="{name : 'List Detail Peringkat By Supplier',params:{id : `${item.id}`}}">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="blue"
                      @click="selectProyek(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                  </template>
                  <span>Detail Supplier</span>
                </v-tooltip>
              </router-link>
<!--               
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    class="mx-1" 
                    x-small
                    color="green"
                    @click="editProyek(item)"
                    v-bind="attrs"
                    v-on="on">
                    <v-icon small dark>mdi-pencil</v-icon>
                  </v-btn>
                </template>
                <span>Edit</span>
              </v-tooltip>
  
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    class="mx-1" 
                    x-small
                    color="red"
                    @click="deleteProyek(item)"
                    v-bind="attrs"
                    v-on="on">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                  </v-btn>
                </template>
                <span>Delete</span>
              </v-tooltip> -->
            </div>
          </template>
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
          {text : 'ID Supplier',               value : 'IDSupplier'},
          {text : 'Nama Supplier',             value : 'namaSupplier'},
          {text : 'Peringkat',                 value : 'Rangking'},
          {text : 'Bobot',                     value : 'Bobot'},
          {text : 'Action',                    value : 'aksi'}        
        ],
        supplierRank :[],
        
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
            const res = await axios.get(`/supplier/get_supplier_rank`);
            if(res.data == null){
                alert("Proyek Kosong")
            }else{
                this.supplierRank = res.data;
                console.log(res,this.data)
            }
          } 
          catch(error){
              alert("Error")
              console.log(error)
          }
        },
  
        async fetchCustomer(){
          try{
            const res = await axios.get('/customers/get_customers');
            if (res.data == null){
              alert('Customer Kosong')
            }else{
              this.customer = res.data
              console.log(res,this.customer)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
        async updateData(){
          if(this.editedIndex > -1){
            Object.assign(this.proyek[this.editedIndex],this.editedItem)
            console.log(this.editedItem)
          }
          this.close()
          try{
            const axios = require('axios')
            const res = await axios.post('/proyek/update_proyek/'+ this.editedItem.id,{
              id : this.editedItem.id,
              nama : this.editedItem.nama,
              customerid : this.editedItem.customerid
            })
  
            console.log(res)
  
          }catch(error){
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