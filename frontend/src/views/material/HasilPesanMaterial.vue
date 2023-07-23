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
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()">
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
                      @click="deleteMaterial(item)"
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

          snackbar : {
            show : false,
            color : null,
            message : null,
          },
         
        }
      },
    
      mounted(){
          this.fetchData(),
          this.fetchData2(),
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
                  location.replace('/listPurchaseItemByPurchaseMaterialNew/' + this.$route.params.id)

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

           
        }   
        
      }
    }
  </script>