<template>
    <v-card 
        class="mx-auto text-center mt-6"
        max-width = "1800"
        max-height = "1500"
        >
        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="400"
        >
        <v-card-title class="text-h4">
              DAFTAR PELANGGAN
            </v-card-title>

          
        </v-card>
        <br>
        <router-link to="/tambahPelanggan">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Tambah Data Pelanggan
            </v-btn>
        </router-link> 
       
          
        <v-data-table   
            :headers = "column"
            :items = "customers"  
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
            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>
            <template v-slot:[`item.email`]="{ item }">
                <v-text-field v-model="editedItem.email" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.email}}</span>
            </template>
            <template v-slot:[`item.adress1`]="{ item }">
                <v-text-field v-model="editedItem.adress1" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.adress1}}</span>
            </template>

          <template v-slot:[`item.city`]="{ item }">
              <v-select v-model="editedItem.city" item-text="nama" item-value="code" :items="cities" v-if="item.id == editedItem.id"></v-select>
              <span v-else>{{item.city}}</span>
          </template>

            <template v-slot:[`item.phone`]="{ item }">
                <v-text-field v-model="editedItem.phone" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.phone}}</span>
            </template>

            <template v-slot:[`item.postalcode`]="{ item }">
                <v-text-field v-model="editedItem.postalcode" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.postalcode}}</span>
            </template>
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.id == editedItem.id">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green"  @click="updateData()">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <router-link :to="{name : 'Proyek by Customer',params:{id : `${item.id}`}}">
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn 
                        class="mx-1" 
                        x-small
                        color="green"
                        @click="selectCustomer(item)"
                        v-bind="attrs"
                        v-on="on">
                        <v-icon small dark>mdi-check</v-icon>
                      </v-btn>
                    </template>
                    <span>List Proyek By Customer</span>
                  </v-tooltip>
                </router-link>
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editCustomer(item)"
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
                      @click="deleteCustomer(item)"
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
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="50"
        >
      
        </v-card>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'ID',           value : 'id'},
            {text : 'Nama',         value : 'nama'},
            {text : 'Email',        value : 'email'},
            {text : 'Alamat 1',     value : 'adress1'},
            //{text : 'Alamat 2',     value : 'adress2'},
            {text : 'Kota',         value : 'city'},
            //{text : 'Fax',          value : 'fax'},
            {text : 'Phone',        value : 'phone'},
            //{text : 'Pic',          value : 'pic'},
            {text : 'Kode Pos',     value : 'postalcode'},
            {text : 'Action',       value : 'aksi'}
            //{text : 'Sites',        value : 'situs'},
            //{text : 'Remark',     value : 'remark'}
        ],
        customers : [],
        cities : [],
        editedIndex: -1,
        editedItem: {
          id: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
        defaultItem: {
          id: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
      }
    },

    mounted(){
        this.fetchCustomer(),
        this.fetchCity()
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editCustomer(customers){
        console.log('ID : ' + customers.id)
        this.editedIndex = this.customers.indexOf(customers);
        this.editedItem = Object.assign({}, customers);
      },

      async fetchCustomer(){
        try{
          const axios = require('axios');
          const res = await axios.get('/customers/get_customers');
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.customers = res.data
            console.log(res,this.customers)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

       async fetchCity(){
          try{
              const axios = require('axios')
              const res = await axios.get('/city/get_allcities')
              if(res.data == null){
                 console.log("Data kota kosong")
              }else{
                  this.cities = res.data
                  console.log(res,this.cities)
              }
          }catch(error){
              console.log(error)
          }
      },
    
      selectCustomer(customers){
          console.log('ID : ' + customers.id)
          //open(`/proyekListbyCustomer/${customers.id}`)
      },

      deleteCustomer(customers){
          console.log('ID : ' + customers.id)
          try{
              const axios = require('axios');
              axios.delete(`/customer/deleteCustomer/${customers.id}`);
              alert("Delete Customer Success!")
              this.fetchCustomer()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.customers[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/customer/update_customer/'+ this.editedItem.id,
            { id: this.editedItem.id,
              nama: this.editedItem.nama,
              email: this.editedItem.email,
              adress1: this.editedItem.adress1,
              city: this.editedItem.city,
              phone: this.editedItem.phone,
              postalcode: this.editedItem.postalcode,
              
              //Data yang tidak ditampilkan
              adress2: this.editedItem.adress2,
              fax: this.editedItem.fax,
              pic: this.editedItem.pic,
              situs: this.editedItem.situs,
              remark: this.editedItem.remark,
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>






