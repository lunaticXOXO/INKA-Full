<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1800">

      <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="300"
        >
        <v-card-title class="text-h4">
              DAFTAR PRODUK
            </v-card-title>
        </v-card>
        <br><br>

    <v-data-table
        :headers = "headers"
        :items = "produk">
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
      <template v-slot:[`item.rincianProyek`]="{ item }">
          <v-select v-model="editedItem.rincianProyek" item-text="id" item-value="id" :items="rincian" v-if="item.id == editedItem.id"></v-select>
          <span v-else>{{item.rincianProyek}}</span>
      </template>
      <template v-slot:[`item.aksi`]="{ item }">
        <div v-if="item.id == editedItem.id">
          <v-icon color="red" class="mr-3" @click="close()">
            mdi-window-close
          </v-icon>
          <v-icon color="green" @click="updateProduk()">
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
              @click="editProduct(item)"
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
              @click="deleteProduct(item)"
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
    <br>
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
    data: () => ({
      valid: true,
      headers:[
        {text : 'ID Produk', value : 'id'},
        {text : 'Rincian Proyek', value : 'rincianProyek'},
        {text : 'Action', value : 'aksi'}      
      ],
      produk:[],
      rincian:[],
      editedIndex : -1,
      editedItem : {
        id : '',
        rincianProyek  : ''
      },
      defaultItem : {
        id : '',
        rincianProyek  : ''
      },
    }),

    mounted(){
        this.fetchDataProduk(),
        this.fetchRincianProyek()
    },

    methods: {
      async fetchDataProduk(){
        try{
          const axios = require('axios');
          const res = await axios.get('/product/get_product');
          if(res.data == null){
              alert("List Produk Kosong")
          }else{
              this.produk = res.data;
              console.log(res,this.produk)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async fetchRincianProyek(){
        try{
            const axios = require('axios')
            const res = await axios.get('/rproyek/show_rproyek')
            if (res.data == null){
                alert("Rincian Proyek Kosong")
            }else{
                this.rincian = res.data
                console.log(res,this.rincian)
            }
        }
        catch(error){
            alert(error)
            console.log(error)
        }
      },

      async updateProduk(){
        if (this.editedIndex > -1) {
            Object.assign(this.produk[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/jproduct/update_jproduct/' + this.editedItem.id,
            { id : this.editedItem.id,
              rincianProyek : this.editedItem.rincianProyek
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      },

      close(){
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem);
          this.editedIndex = -1;
        }, 300)
      },
      
      editProduct(product){
        console.log('ID : ' + product.id)
        this.editedIndex = this.produk.indexOf(product)
        this.editedItem = Object.assign({},product)
      },
      
      deleteProduct(product){
        console.log(product.id)
      }
    }
  }
</script>