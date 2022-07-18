<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Produk</h1>
        <br>
        <router-link to="/tambahProduk">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Produk
            </v-btn>
        </router-link>

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
            <v-btn class="mx-1" x-small color="green" @click="editProduct(item)">
                <v-icon small dark>mdi-pencil</v-icon>
            </v-btn>
            <v-btn class="mx-1" x-small color="red" @click="deleteProduct(item)">
                <v-icon small dark>mdi-trash-can-outline</v-icon>
            </v-btn>
          </div>
          </template>
        </v-data-table>
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