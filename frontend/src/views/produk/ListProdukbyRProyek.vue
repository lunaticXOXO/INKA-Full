<template>
    <v-app>
        <div class="d-flex">
        <v-card class="mx-auto text-center mt-6" width="500">
            <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
              RINCIAN PROYEK {{this.$route.params.id}}
            </v-card-title>
          </v-card>

                <v-data-table
                    :headers= "column2"
                    :items= "rproyek">
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-6" width="350">

                <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
              PROYEK {{this.idproyek}}
            </v-card-title>
          </v-card>
                <v-data-table
                    :headers="column3"
                    :items = "proyek"
                >
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-6" width="350">
                <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
              PELANGGAN {{this.idcustomer}}
            </v-card-title>
          </v-card>

                <v-data-table
                    :headers="column4"
                    :items="customer"
                >
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" width="1500">
        
            <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="400"
            >
            <v-card-title class="text-h4">
              DAFTAR PRODUK RINCIAN PROYEK {{this.$route.params.id}}
            </v-card-title>
            </v-card>
            <br><br>
            <v-data-table 
                :headers="column"
                :items="produk"
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
                        <router-link :to="{name:'List Operasi By Produk Tabel',params:{'id': `${item.id}`}}">
                            <v-tooltip top>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn 
                                    class="mx-1" 
                                    x-small
                                    color="blue"
                                    @click="selectOperasitoProduct(item)"
                                    v-bind="attrs"
                                    v-on="on">
                                    <v-icon small dark>mdi-check</v-icon>
                                    </v-btn>
                                </template>
                                <span>List Operasi By Produk</span>
                                </v-tooltip>
                        </router-link>
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
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            column : [
                {text : 'ID Product',value : 'id'},
                {text : 'Rincian Proyek',value : 'rincianProyek'},
                {text : 'Action',value : 'aksi'}
            ],
            column2 : [
                {text : 'ID Rincian Proyek', value : 'IdRincian'},
                {text : 'Jumlah', value : 'jumlah'},
                {text : 'Due Date',value : 'dueDate'},
               
            ],
            column3 : [
                {text : 'ID Proyek',value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'NamaProyek'},
            ],
            
            column4 : [
                {text : 'ID Customer', value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'}
            ],
            rproyek : [],
            proyek : [],
            customer : [],
            produk  : [],
            rincian : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                rincianProyek  : ''
            },
            defaultItem : {
                id : '',
                rincianProyek  : ''
            },
            idproyek : '',
            idcustomer : ''
        }
    },

    mounted(){
        this.fetchProductbyRProyek(),
        this.fetchRincianProyek(),
        this.fetchRincianInProduk()
    },

    methods : {
        async fetchProductbyRProyek(){
            const axios = require('axios')
            const res = await axios.get('/product/get_product_by_rproyek/' + this.$route.params.id)
            try{
                if (res.data == null){
                    alert("Rincian Proyek Kosong")
             } else{  
                    this.produk = res.data
                    console.log(res)    
                }
            }catch(error){
                console.log(error)
            }
        },

        async fetchRincianProyek(){
            try{
                const axios = require('axios')
                const res = await axios.get('/rproyek/show_rproyek')
                if (res.data == null){
                    alert("Proyek Kosong")
                }else{
                    this.rincian = res.data
                    console.log(res,this.rincian)
                }
            }catch(error){
                alert(error)
                console.log(error)
            }
        },

        async fetchRincianInProduk(){
            try{
                
                const axios = require('axios')
                const res = await axios.get('/product/get_rproyek_inproduct/' + this.$route.params.id)
                if(res.data == null){
                    console.log("Data kosong")
                }else{
                    this.rproyek = res.data
                    this.proyek = res.data
                    this.customer = res.data
                    console.log(res)

                    this.idcustomer = this.customer[0].IdCustomer
                    this.idproyek = this.proyek[0].IdProyek
                    
                }

            }catch(error){
                alert("Error")
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

        selectOperasitoProduct(item){
            console.log(item.id)
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