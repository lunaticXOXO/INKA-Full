<template>
    <v-app>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1>Supplier</h1>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "supplier"
            :items-per-page="3"
            >
          </v-data-table>
      </v-card>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Pemesanan Material</h1>
          <br>
         
          <v-data-table 
            :headers = "column2"
            :items = "hasilpesan"
            :items-per-page="5"
            >

            <template v-slot:[`item.id`]="{ item }">
              <div v-if="item.id === editedItem.id">
                  <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                  <span v-else>{{item.id}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                  <span v-else>{{item.id}}</span>
              </div>
            </template>
          

            <template v-slot:[`item.jumlah`]="{ item }">
                <v-text-field v-model="editedItem.jumlah" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.jumlah}}</span>
            </template>
              
            <template v-slot:[`item.Harga`]="{ item }">
                <v-text-field v-model="editedItem.Harga" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.Harga}}</span>
            </template>

            <template v-slot:[`item.LeadTime`]="{ item }">
                <v-text-field v-model="editedItem.LeadTime" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.LeadTime}}</span>
            </template>

            <template v-slot:[`item.MinimalOrder`]="{ item }">
                <v-text-field v-model="editedItem.MinimalOrder" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.MinimalOrder}}</span>
            </template>


            <template v-slot:[`item.unit`]="{ item }">
              <v-select v-model="editedItem.unit" item-text="nama" item-value="id" :items="units" v-if="item.id == editedItem.id"></v-select>
              <span v-else>{{item.unit}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.id == editedItem.id">
                  <v-icon color="red" class="mr-3" @click="close" >
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()" :loading="loading">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editPesanan(item)"
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
                      @click="deletePesanan(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-trash-can-outline</v-icon>
                    </v-btn>
                  </template>
                  <span>Delete</span>
                </v-tooltip>
              </div>
            </template>

          </v-data-table>

          <v-btn 
          color="primary" 
          class="mt-5 mb-3"
          v-bind="attrs"
          @click = "addOrdersToPurchaseItem()"
          v-on="on"
   >    
        Order
    </v-btn> 

    
    <v-dialog
          v-model="dialog"
          width="500">
          <v-card class="pa-6">
            <v-card-title class="text-h5 grey lighten-2">
              Updating...
            </v-card-title>
            <br>
            <div class="mx-auto text-center">
              <v-progress-circular
                :size="70"
                :width="7"
                indeterminate
                color="grey darken-2"
              ></v-progress-circular>
              <br>
        
            </div>
          </v-card>
        </v-dialog>

    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
    </v-snackbar>

   

      </v-card>

    </v-app>
  </template>
  
  <script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'ID Supplier',            value : 'code'},
              {text : 'Nama',                   value : 'nama'},
              {text : 'Email',                  value : 'email'},
              {text : 'Alamat',                 value : 'adress1'},
              {text : 'Kota',                   value : 'city'},
              {text : 'Phone',                  value : 'phone'}
           
          ],

         column2 : [
            {text : 'Code Material',        value : 'code'},
            {text : 'Nama Material',        value : 'nama'},
            {text : 'Pesan',                value : 'jumlah'},
            {text : 'Harga',                value : 'Harga'},
            {text : 'Lead Time',            value : 'LeadTime'},
            {text : 'Minimal',              value : 'MinimalOrder'},
            {text : 'Rencana Kedatangan',   value : 'RencanaKedatangan'},
            {text : 'Unit',                 value : 'unit'},
            {text : 'Action',               value : 'aksi'}
         ],

           supplier : [],
           hasilpesan : [],
           units : [],
          editedIndex: -1,
          dialog : false,
          loading : false,

          editedItem: {
           
            jumlah: '',
            Harga: '',
            LeadTime : '',
            MinimalOrder : '',
            unit : ''

          },
          defaultItem: {
           
            jumlah: '',
            Harga: '',
            LeadTime : '',
            MinimalOrder : '',
            unit : ''
          },

          snackbar : {
            show : false,
            color : null,
            message : null,
          },
         
        }
      },
    

      watch: {
      dialog (val) {
        if (!val) return

        if(this.snackbar.color == "green"){
          this.dialog = false
        }else{
          this.dialog = true
        }
      },
    },

      mounted(){
          this.fetchData(),

           window.setInterval(() => {
            this.fetchData2()
           }, 7000)
         
          this.fetchUnit()
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

        editPesanan(hasilpesan){
     
            console.log('ID : ' + hasilpesan.id)
            this.editedIndex = this.hasilpesan.indexOf(hasilpesan);
            this.editedItem = Object.assign({},hasilpesan);
            console.log("id index : ", this.editedItem.id)
     
        },

        deletePesanan(hasilpesan){
          try{

            const axios = require('axios')
            const res = axios.delete('/material/delete_pemesanan_material/' + hasilpesan.id)
            if(res.data.status == 'berhasil'){
              alert("Delete Success")
              this.snackbar = {
                  show : true,
                  message : "Delete Success",
                  color : "green" 
                }
            }else if(res.data.status == 'gagal'){
              this.snackbar = {
                  show : true,
                  message : "Delete Failed",
                  color : "green" 
                }

            }

          }
          catch(error){

            console.log(error)
          }

        },
  
        async fetchData(){
          try{
            const axios = require('axios');
            const res = await axios.get('/supplier/get_supplier_inharuspesan');
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.supplier = res.data
              console.log(res,this.supplier)
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
            const res = await axios.get('/material/hasil_pemesanan/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.hasilpesan = res.data
              console.log(res,this.hasilpesan)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },

        async fetchUnit(){
        try{
            const axios = require('axios')
            const res = await axios.get('/unit/get_unit')
            if (res.data == null){
                alert("Material Unit Kosong")
            }else{
                this.units = res.data
                console.log(res,this.units)
            }
        }catch(error){
            alert(error)
            console.log(error)
        } 
      },
        
        async addOrdersToPurchaseItem(){
          try{

             const axios = require('axios')
             const res = await axios.post('/material/add_order_to_purchaseitem/' + this.$route.params.id)
             if(res.data.status == 'berhasil'){
              console.log("success")
              this.snackbar = {
                  show : true,
                  message : "Order Success",
                  color : "green" 
                }
                setTimeout(() => { 
                  location.replace('/informationPurchaseItem/' + this.$route.params.id)

                }, 1000)
          }
          else if(res.data.status == 'gagal'){
            this.snackbar = {
                  show : true,
                  message : "Order Failed",
                  color : "red" 
                }
          }
          }catch(error){
            console.log(error)
          }
        },

      async  updateData(){
          if(this.editedIndex > -1){
             Object.assign(this.hasilpesan[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
          }
          this.close()        
         
          try{
           
              const axios = require('axios')
              const res =  await axios.post('/material/update_pemesanan_material/'+ this.editedItem.id,{
                  jumlah        : this.editedItem.jumlah,
                  Harga         : this.editedItem.Harga,
                  LeadTime      : this.editedItem.LeadTime,
                  MinimalOrder  : this.editedItem.MinimalOrder,
                  unit          : this.editedItem.unit
              })
              this.loading = true
              this.dialog = true
              if(res.data.status == 'berhasil'){
                  
                  console.log("berhasil")
                  // setTimeout(() => { 
                  this.snackbar = {
                    show : true,
                    message : "Update Success",
                    color : "green" 
                  }
                // }, 1000)
                  this.dialog = false
                  this.loading = false
              }
             
              else if(res.data.status == 'gagal'){
                this.snackbar = {
                    show : true,
                    message : "Update Failed",
                    color : "red" 
                  }

                  this.loading = false
              }
      
        }
          catch(error){
            this.snackbar = {
                    show : true,
                    message : "Update Error",
                    color : "red" 
                  }
            console.log(error)
          }
      
        },

        

        
      }
    }
  </script>