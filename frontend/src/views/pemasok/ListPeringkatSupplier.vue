<template>
  <v-card 
      class="mx-auto text-center mt-10"
      max-width = "1200">
      <br>
      <h1>List Supplier</h1>
      <br>
      <router-link to="/tambahPemasok">
          <v-btn color="primary" class="d-flex ml-4 mb-6">
              Add Supplier
          </v-btn>
      </router-link>
      
      <v-data-table 
          :headers = "headers"
          :items = "supplierRank">
          <template v-slot:[`item.IDSupplier`]="{ item }">
            <div v-if="item.IDSupplier === editedItem.IDSupplier">
                <v-text-field disabled v-model="editedItem.IDSupplier" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDSupplier == editedItem.IDSupplier"></v-text-field>
                <span v-else>{{item.IDSupplier}}</span>
            </div>
            <div v-else>
                <v-text-field v-model="editedItem.IDSupplier" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDSupplier == editedItem.IDSupplier"></v-text-field>
                <span v-else>{{item.IDSupplier}}</span>
            </div>
          </template>
          <!-- <template v-slot:[`item.namaSupplier`]="{ item }">
              <v-text-field v-model="editedItem.namaSupplier" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
              <span v-else>{{item.namaSupplier}}</span>
          </template>
          <template v-slot:[`item.Rangking`]="{ item }">
              <v-text-field v-model="editedItem.Rangking" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
              <span v-else>{{item.Rangking}}</span>
          </template>
          <template v-slot:[`item.Bobot`]="{ item }">
              <v-text-field v-model="editedItem.bobot" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
              <span v-else>{{item.Bobot}}</span>
          </template> -->

       

        
          <template v-slot:[`item.aksi`]="{ item }">
          
            <div>
              <router-link :to="{name : 'List Detail Peringkat By Supplier',params:{id : `${item.IDSupplier}`}}">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="blue"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                  </template>
                  <span>List Material Type By Supplier</span>
                </v-tooltip>
              </router-link>
             
             
            </div>
          </template>
      </v-data-table>
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

