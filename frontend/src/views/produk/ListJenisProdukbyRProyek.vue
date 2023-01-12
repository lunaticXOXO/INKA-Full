<template>
    <v-app>
        <div class="d-flex">
            <v-card class="mx-auto text-center mt-10" width="600">
                <h3>Rincian Proyek {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "column2"
                    :items = "rincianproyek">
                </v-data-table> 
            </v-card>
        </div>
        <div class="d-flex">
             <v-card class="mx-auto text-center mt-10" width="400">
                <v-data-table
                    :headers = "column3"
                    :items = "produk"
                >
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-10" width="400">
                <v-data-table
                    :headers = "column4"
                    :items = "proyek"
                >
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-10" width="400">
                    <v-data-table
                    :headers = "column5"
                    :items = "customer"
                >
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-10" width="1000">
            <br>
            <h2>List Jenis Produk by Rincian Proyek</h2><h2>{{this.$route.params.id}}</h2>
            <br>
            <v-card
            class="mx-auto text-center"
            max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "jenisproduk"
                    height = "200"
                    width = "300">
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

                    <template v-slot:[`item.nama`]="{item}">
                        <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.nama}}</span>
                    </template>

                    <template v-slot:[`item.aksi`]="{ item }">
                        <div v-if="item.id==editedItem.id">
                            <v-icon color="red" class="mr-3" @click="close()">
                                mdi-window-close
                            </v-icon>
                            <v-icon color="green" class="mr-3" @click="updateData()">
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
                                        @click="selectJProducttoSJProduct(item)"
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
                                    @click="editJenisProduct(item)"
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
                                    @click="deleteJenisProduct(item)"
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
            </v-card>
        </v-card>
    </v-app>
</template>

<script>

export default {
    data(){
        return{
            column : [
                {text : 'ID Jenis Produk',value : 'id'},
                {text : 'Nama',value : 'nama'},
                {text : 'Tanggal Dibuat', value : 'tglDibuat'},
                {text : 'Action',value : 'aksi'}
            ],

            column2 : [
                {text : 'ID Rincian Proyek',value : 'IdRincian'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date',value : 'dueDate'},
               
            ],
            column3 : [
                 {text : 'ID Produk',value : 'IdProduk'},
                {text : 'Due Date Produk',value : 'dueDateProduk'},
            ],
            column4 : [
                {text : 'ID Proyek',value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'NamaProyek'},
            ],
            column5 : [
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'}
            ],
            produk : [],
            jenisproduk : [],
            rincianproyek : [],
            customer : [],
            proyek : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                nama : '',
                
            },
            defaultItem : {
                id : '',
                nama : ''
            },
        }
    },  

    mounted(){
        this.fetchJenisProdukbyRProyek()
        this.fetchRProyekInJenisProduk()
    },

    methods : {
        async fetchJenisProdukbyRProyek(){
            try{
                const axios = require('axios')
                const res = await axios.get('/jproduct/get_jproduct_by_rproyek/' + this.$route.params.id)
                if (res.data == null){
                    alert("Data Jenis Product Kosong")
                }else{
                    this.jenisproduk = res.data
                    console.log(res,this.jenisproduk)
                }
            }catch(error){
                console.log(error)
            }
        },

        async fetchRProyekInJenisProduk(){
            try{
                
                const axios = require('axios')
                const res = await axios.get('/jproduct/get_rincian_injproduct/'+ this.$route.params.id)
                if(res.data == null){
                    console.log("Data kosong")
                }else{
                    this.rincianproyek = res.data
                    this.proyek = res.data
                    this.customer = res.data
                    this.produk = res.data
                    console.log(res,this.rincianproyek)
                }

            }catch(error){
                console.log(error)
            }
        },

        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.jenisproduk[this.editedIndex],this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/jproduct/update_jproduct/' + this.editedItem.id,{
                    id : this.editedItem.id,
                    nama : this.editedItem.nama
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        },

        selectJProducttoSJProduct(jenisproduk){
            console.log(jenisproduk.id)
        },

        editJenisProduct(jenisproduk){
           this.editedIndex = this.jenisproduk.indexOf(jenisproduk)
           this.editedItem = Object.assign({},jenisproduk)
        },

        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },
    }
}
</script>