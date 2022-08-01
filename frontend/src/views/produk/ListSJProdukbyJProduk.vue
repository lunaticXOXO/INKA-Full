<template>
    <v-app>
        <div class="d-flex">
            <v-card class="mx-auto text-center mt-10" width="300">
                <h3>Jenis Produk {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "column2"
                    :items = "jproduk">
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-10">
                <v-data-table
                    :headers = "column3"
                    :items = "produk"
                >
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-10">
                 <v-data-table
                    :headers = "column4"
                    :items = "rproyek"
                >
                </v-data-table>
            </v-card>

            <v-card class="mx-auto text-center mt-10">
                <v-data-table
                    :headers = "column5"
                    :items = "proyek"
                >
                </v-data-table>
            </v-card>

              <v-card class="mx-auto text-center mt-10">
                <v-data-table
                    :headers = "column6"
                    :items = "customer"
                >
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" width="1000">
            <br>
            <h1>List Struktur Jenis Produk by Jenis Produk</h1><h1>{{this.$route.params.id}}</h1>
            <br>
            <router-link :to="{name : 'Tambah Struktur Jenis Produk by Jenis Produk',params : {id : `${this.$route.params.id}`}}">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Sturktur Jenis Produk by Jenis Produk
                </v-btn>
            </router-link>
            <v-card
            class="mx-auto text-center"
            max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "sjproduk">
                    <template v-slot:[`item.idNodal`]="{ item }">
                    <div v-if="item.idNodal == editedItem.idNodal">
                        <v-text-field disabled v-model="editedItem.idNodal" :hide-details="true" dense single-line :autofocus="true" v-if="item.idNodal == editedItem.idNodal"></v-text-field>
                        <span v-else>{{item.idNodal}}</span>
                    </div>
                    <div v-else>
                        <v-text-field v-model="editedItem.idNodal" :hide-details="true" dense single-line :autofocus="true" v-if="item.idNodal == editedItem.idNodal"></v-text-field>
                        <span v-else>{{item.idNodal}}</span>
                    </div>
                    </template>
                    <template v-slot:[`item.indukNodal`]="{ item }">
                        <v-select v-model="editedItem.indukNodal" item-text="idNodal" item-value="idNodal" :items="indukNodal" v-if="item.idNodal == editedItem.idNodal"></v-select>
                        <span v-else>{{item.indukNodal}}</span>
                    </template>
                    <template v-slot:[`item.nama`]="{ item }">
                        <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.idNodal == editedItem.idNodal" ></v-text-field>
                        <span v-else>{{item.nama}}</span>
                    </template>
                    <template v-slot:[`item.jumlah`]="{ item }">
                        <v-text-field v-model="editedItem.jumlah" :hide-details="true" dense single-line v-if="item.idNodal == editedItem.idNodal" ></v-text-field>
                        <span v-else>{{item.jumlah}}</span>
                    </template>
                    <template v-slot:[`item.satuan`]="{ item }">
                        <v-text-field v-model="editedItem.satuan" :hide-details="true" dense single-line v-if="item.idNodal == editedItem.idNodal" ></v-text-field>
                        <span v-else>{{item.satuan}}</span>
                    </template>
                    <template v-slot:[`item.jnsProduk`]="{ item }">
                        <v-select v-model="editedItem.jnsProduk" item-text="id" item-value="id" :items="jenisproduk" v-if="item.idNodal == editedItem.idNodal"></v-select>
                        <span v-else>{{item.jnsProduk}}</span>
                    </template>
                    <template v-slot:[`item.aksi`]="{ item }">
                        <div v-if="item.idNodal == editedItem.idNodal">
                            <v-icon color="red" class="mr-3" @click="close">
                            mdi-window-close
                            </v-icon>
                            <v-icon color="green"  @click="updateData()">
                            mdi-content-save
                            </v-icon>
                        </div>
                        <div v-else>
                            <router-link :to="{name : 'List Process by Struktur Jenis Produk',params:{ id : `${item.idNodal}`}}">
                            <v-btn class="mx-1" x-small color="blue" @click="selectSJProduct(item)">
                                <v-icon small dark>mdi-check</v-icon>
                            </v-btn>
                            </router-link>

                            <v-btn class="mx-1" x-small color="green" @click="editSJProduct(item)">
                                <v-icon small dark>mdi-pencil</v-icon>
                            </v-btn>
                            <v-btn class="mx-1" x-small color="red" @click="deleteSJProduct(item)">
                                <v-icon small dark>mdi-trash-can-outline</v-icon>
                            </v-btn>
                        </div>
                    </template>
                </v-data-table>
            </v-card>
        </v-card>
    </v-app>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            column : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Induk Nodal',value : 'indukNodal'},
                {text : 'Nama', value : 'nama'},
                {text : 'Jumlah', value : 'jumlah'},
                {text : 'Satuan', value : 'satuan'},
                {text : 'ID Jenis Produk', value : 'id'},
                {text : 'Action', value : 'aksi'}
            ],
            column2 : [
                {text : 'ID Jenis Produk',value : 'IdJenisProduk'},
                {text : 'Nama Jenis Produk',value : 'NamaJenisProduk'},
            ],

            column3 : [
                {text : 'ID Produk',value : 'IdProduk'},
                {text : 'Due Date Produk',value : 'dueDateProduk'},
            ],
            column4 : [
                {text : 'ID Rincian Proyek',value : 'IdRincian'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date Rincian',value : 'dueDateRincian'},
            ],
            column5 : [
                {text : 'ID Proyek', value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'namaProyek'},
            ],
            column6 : [
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'namaCustomer'}
            ],

            jproduk : [],
            produk : [],
            rproyek : [],
            proyek : [],
            customer : [],
            sjproduk : [],
            indukNodal: [],
            editedIndex: -1,
            editedItem: {
                idNodal: '',
                indukNodal: '',
                nama: '',
                jumlah: '',
                satuan: '',
                jnsProduk: ''
            },
            defaultItem: {
                idNodal: '',
                indukNodal: '',
                nama: '',
                jumlah: '',
                satuan: '',
                jnsProduk: ''
            }
        }
    },

    mounted(){
        this.fetchSJProductbyJProduk()
        this.fetchJProductInSJProduk()
    },

    methods: {
        async fetchSJProductbyJProduk(){
            const res = await axios.get('/sjproduct/get_sjproduct_by_jproduct/' + this.$route.params.id)
            if(res.data == null){
                alert("Data Kosong")
            }else{
                this.sjproduk = res.data
                this.indukNodal = res.data
                console.log(res,this.sjproduk)
            }
        },
        
           async fetchJProductInSJProduk(){
            const res = await axios.get('/sjproduct/get_jproduct_insjproduct/' + this.$route.params.id)
            if(res.data == null){
                console.log("Data Kosong")
            }else{
               this.jproduk = res.data
               this.produk = res.data
               this.rproyek = res.data
               this.proyek = res.data
               this.customer = res.data
               console.log(res,this.jproduk)
            }
        },
        async updateData(){
            if (this.editedIndex > -1) {
                Object.assign(this.sjproduk[this.editedIndex], this.editedItem)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/sjproduct/update_sjproduct/'+ this.editedItem.idNodal,
                { idNodal : this.editedItem.idNodal,
                  indukNodal : this.editedItem.indukNodal,
                  nama : this.editedItem.nama,
                  jumlah: this.editedItem.jumlah,
                  satuan: this.editedItem.satuan,
                  jnsproduk: this.$route.params.id 
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        },

        close () {
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        editSJProduct(sjProd){
            console.log('ID Nodal : ' + sjProd.idNodal)
            this.editedIndex = this.sjproduk.indexOf(sjProd);
            this.editedItem = Object.assign({}, sjProd);
        },
        
        selectSJProduct(sjproduk){
            console.log(sjproduk.id)
            //open(`/listProcessbySJProduk/${sjproduk.idNodal}`)
        }
    }  
}
</script>
