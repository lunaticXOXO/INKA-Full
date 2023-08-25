<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1700">
         <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             DAFTAR JENIS PRODUK
            </v-card-title>
        </v-card>
        <br>
        <br>
        <v-card
            class="mx-auto text-center"
            max-width="1700">
            <v-data-table
                :headers = "column"
                :items = "jenisproduk"
                :items-per-page="2"
            >
            <template v-slot:[`item.id`]="{ item }">
                <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.id}}</span>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
            <div v-if="item.id==editedItem.id">
                <v-icon color="red" class="mr-3" @click="close()">
                    mdi-window-close
                </v-icon>
                <v-icon color="green" @click="updateJenisProduk()">
                    mdi-content-save
                </v-icon>
            </div>
            <div v-else>
                <router-link :to="{name : 'List Struktur Jenis Produk by Jenis Produk', params:{id : `${item.id}`}}">
                    <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn 
                            class="mx-1" 
                            x-small
                            color="blue"
                            @click="selectJProduktoSJProduk(item)"
                            v-bind="attrs"
                            v-on="on">
                            <v-icon small dark>mdi-check</v-icon>
                            </v-btn>
                        </template>
                        <span>List Struktur Jenis Produk by Jenis Produk</span>
                    </v-tooltip>
                </router-link>

                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editJenisProduk(item)"
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
                      @click="deleteJenisProduk(item)"
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
            
        <!--
        <div class="d-flex">
            <router-link to="/tambahJenisProduk">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Jenis Produk Eksternal
                </v-btn>
            </router-link>

            <router-link to="/tambahJenisProdukInternal">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Jenis Produk Internal
                </v-btn>
            </router-link>
        </div>
        -->
        <br>

        <v-card
        color="#6f6f6f"
        dark
        class="px-5 py-3"
        max-height ="50"
        >
        </v-card>
        </v-card>
     

    </v-card>
</template>

<script>
export default {
    data(){
        return {
            column : [
                {text : 'ID Jenis Produk', value : 'id'},
                {text : 'Nama Jenis Produk', value : 'nama'},
                {text : 'Tanggal Dibuat',value : 'tglDibuat'},
                {text : 'Action',value : 'aksi'}
            ],
            jenisproduk : [],
            editedIndex : -1,
            editedItem : {
              id : '',
              nama  : '',
            },
            defaultItem : {
                id : '',
                nama : '',
            },
        }
    },

    mounted(){
        this.fetchJenisProduk()
    },

    methods : {
        async fetchJenisProduk(){
            try{
                const axios = require('axios')
                const res = await axios.get('/jproduct/get_jproduct')
                if(res.data == null){
                    alert("Data jenis product kosong")
                }else{
                    this.jenisproduk = res.data
                    console.log(res,this.jenisproduk)
                }
            }
            catch(error){
                console.log(error)
            }
        },
        
        editJenisProduk(jenisproduk){
            console.log('ID : ' + jenisproduk.id)
            this.editedIndex = this.jenisproduk.indexOf(jenisproduk)
            this.editedItem = Object.assign({},jenisproduk)
        },
        
        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        selectJProduktoSJProduk(jenisproduk){
            console.log(jenisproduk.id)
        },

        async updateJenisProduk(){
            if (this.editedIndex > -1) {
                Object.assign(this.jenisproduk[this.editedIndex], this.editedItem)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/jproduct/update_jproduct/' + this.editedItem.id,
                { id : this.editedItem.id,
                  nama : this.editedItem.nama
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        }
    }
}
</script>
