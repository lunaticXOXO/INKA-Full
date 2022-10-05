<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Supplier</h1>
        <br>
        <router-link to="/tambahPemasok">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Supplier
            </v-btn>
        </router-link>

        <v-data-table 
            :headers = "column"
            :items = "supplier">
            <template v-slot:[`item.code`]="{ item }">
              <div v-if="item.code === editedItem.code">
                  <v-text-field disabled v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
            </template>
            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>
            <template v-slot:[`item.email`]="{ item }">
                <v-text-field v-model="editedItem.email" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.email}}</span>
            </template>
            <template v-slot:[`item.adress1`]="{ item }">
                <v-text-field v-model="editedItem.adress1" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.adress1}}</span>
            </template>

            <template v-slot:[`item.city`]="{ item }">
              <v-select v-model="editedItem.city" item-text="nama" item-value="code" :items="cities" v-if="item.code == editedItem.code"></v-select>
              <span v-else>{{item.city}}</span>
          </template>

            <template v-slot:[`item.phone`]="{ item }">
                <v-text-field v-model="editedItem.phone" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.phone}}</span>
            </template>
            <template v-slot:[`item.postalcode`]="{ item }">
                <v-text-field v-model="editedItem.postalcode" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.postalcode}}</span>
            </template>
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.code == editedItem.code">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <router-link :to="{name : 'List Material Type By Supplier',params:{id : `${item.code}`}}">
                  <v-btn class="mx-1" x-small color="blue">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                </router-link>
                <v-btn class="mx-1" x-small color="green" @click="editSupplier(item)">
                    <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="mx-1" x-small color="red" @click="deleteSupplier(item)">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>
              </div>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'Code',         value : 'code'},
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
        supplier : [],
        cities : [],
        editedIndex: -1,
        editedItem: {
          code: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
        defaultItem: {
          code: '',
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
        this.fetchSupplier(),
        this.fetchCity()
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editSupplier(supplier){
        console.log('ID : ' + supplier.code)
        this.editedIndex = this.supplier.indexOf(supplier);
        this.editedItem = Object.assign({},supplier);
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

      async fetchSupplier(){
        try{
          const axios = require('axios');
          const res = await axios.get('/supplier/get_supplier');
          if (res.data == null){
            alert('Supplier Kosong')
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

      deleteSupplier(supplier){
          console.log('ID : ' + supplier.code)
          try{
              const axios = require('axios');
              axios.delete(`/customer/deleteCustomer/${supplier.code}`);
              alert("Delete Customer Success!")
              this.fetchSupplier()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.supplier[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/supplier/update_supplier/'+ this.editedItem.code,
            { code: this.editedItem.code,
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