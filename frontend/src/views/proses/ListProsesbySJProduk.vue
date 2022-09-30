<template>
    <v-app>
        <div class="d-flex">
            <v-card class="ml-6 text-center mt-6" width="700">
                <v-data-table
                    :headers="column2"
                    :items = "sjproduk">
                </v-data-table>
            </v-card>
            <v-card class="ml-12 text-center mt-6" width="700">
                <v-data-table
                    :headers="column3"
                    :items = "sjproduk">
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" max-width="1000">
            <br>
            <h1>List Proses by Sturktur Jenis Produk</h1><h1>{{this.$route.params.id}}</h1>
            <br>
            <router-link :to="{name : 'Tambah Proses by Struktur Jenis Produk', params:{id : `${this.$route.params.id}`}}">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Process by Struktur Jenis Produk
                </v-btn>
            </router-link>
            <v-card class="mx-auto text-center" max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "proses">
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
                    <template v-slot:[`item.prosesSesudahnya`]="{ item }">
                        <v-select v-model="editedItem.prosesSesudahnya" item-text="id" item-value="id" :items="prosesData" v-if="item.id == editedItem.id"></v-select>
                        <span v-else>{{item.prosesSesudahnya}}</span>
                    </template>
                    <template v-slot:[`item.nama`]="{ item }">
                        <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.nama}}</span>
                    </template>
                    <template v-slot:[`item.durasi`]="{ item }">
                        <v-text-field v-model="editedItem.durasi" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.durasi}}</span>
                    </template>
                    <template v-slot:[`item.satuanDurasi`]="{ item }">
                        <v-select v-model="editedItem.satuanDurasi" :items="satuan_durasi" v-if="item.id == editedItem.id"></v-select>
                        <span v-else>{{item.satuanDurasi}}</span>
                    </template>
                    <template v-slot:[`item.jenisProses`]="{ item }">
                        <v-select v-model="editedItem.jenisProses" item-text="namajenisproses" item-value="id" :items="jenis_proses" v-if="item.id == editedItem.id"></v-select>
                        <span v-else>{{item.jenisProses}}</span>
                    </template>
                    <template v-slot:[`item.idNodal`]="{ item }">
                        <v-select v-model="editedItem.idNodal" item-text="idNodal" item-value="idNodal" :items="nodal" v-if="item.id == editedItem.id"></v-select>
                        <span v-else>{{item.idNodal}}</span>
                    </template>
                    <template v-slot:[`item.aksi`]="{ item }">
                        <div v-if="item.id == editedItem.id">
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                        <v-icon color="green" @click="updateData()">
                            mdi-content-save
                        </v-icon>
                        </div>
                        <div v-else>
                            <router-link :to="{name : 'List Stasiun Kerja by Process',params : {id : `${item.id}`}}">
                            <v-btn class="mx-1" x-small color="blue" @click="selectProsestoWorkStation(item)">
                                <v-icon small dark>mdi-check</v-icon>
                            </v-btn>
                            </router-link>
                            <v-btn class="mx-1" x-small color="green" @click="editProses(item)">
                                <v-icon small dark>mdi-pencil</v-icon>
                            </v-btn>
                            <v-btn class="mx-1" x-small color="red" @click="deleteProses(item)">
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
        return {
            column : [
                {text : 'ID Proses', value : 'id'},
                {text : 'Proses Sesudahnya',value : 'prosesSesudahnya'},
                {text : 'Nama', value : 'nama'},
                {text : 'Durasi', value : 'durasi'},
                {text : 'Satuan Durasi', value : 'satuanDurasi'},
                {text : 'Jenis Proses', value : 'jenisProses'},
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Action', value : 'aksi'}
            ],
            column2 : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Nama', value : 'nama'},
                {text : 'Induk Nodal',value : 'indukNodal'},
                {text : 'ID Jenis Produk',value : 'IdJenisProduk'},
                {text : 'Nama Jenis Produk',value : 'NamaJenisProduk'},
                {text : 'ID Rincian Proyek',value : 'IdRincian'},
            ],
            column3 : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date Rincian',value : 'dueDateRincian'},
                {text : 'ID Produk',value : 'IdProduk'},
                {text : 'Nama Proyek',value : 'namaProyek'},
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'namaCustomer'}
            ],
            sjproduk : [],
            proses : [],
            prosesData : [],
            nodal: [],
            jenis_proses: [],
            satuan_durasi: [
                "Minutes",
            ],
            editedIndex : -1,
            editedItem : {
                id: '',
                prosesSesudahnya: '',
                nama: '',
                durasi: '',
                satuanDurasi: '',
                jenisProses: '',
                idNodal: ''
            },
            defaultItem : {
                id: '',
                prosesSesudahnya: '',
                nama: '',
                durasi: '',
                satuanDurasi: '',
                jenisProses: '',
                idNodal: ''
            },
        }
    },

    mounted(){
        this.fetchProsesbySJProduk(),
        this.fetchJenisProses(),
        this.fetchNodal(),
        this.fetchSJProdukInProses()
    },

    methods : {
        close(){
            setTimeout(()=>{
            this.editedItem = Object.assign({},this.defaultItem)
            this.editedIndex = -1;
            },300)
        },

        editProses(prosesItem){
            console.log(prosesItem.id)
            this.editedIndex = this.proses.indexOf(prosesItem)
            this.editedItem = Object.assign({},prosesItem)
        },

        async fetchJenisProses(){
            try{
                const res = await axios.get('/jenis_proses/get_jenisproses')
                if (res.data == null){
                    alert("Jenis Proses Kosong")
                }else{
                    this.jenis_proses = res.data
                    console.log(res,this.jenis_proses)
                }
            }
            catch(error){
                alert(error)
                console.log(error)
            }
        },

        async fetchNodal(){
            try{
                const res = await axios.get('/sjproduct/get_sjproduct')
                if (res.data == null){
                    alert("Struktur Jenis Produk Kosong")
                }else{
                    this.nodal = res.data
                    console.log(res,this.nodal)
                }
            }
            catch(error){
                alert(error)
                console.log(error)
            }
        },

        async fetchProsesbySJProduk(){
            try{
                const res = await axios.get('/proses/get_process_by_sjproduct/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Kosong")
                }else{
                    this.proses = res.data
                    this.prosesData = res.data
                    console.log(res,this.proses)
                }
                
            } catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async fetchSJProdukInProses(){
                try{
                const res = await axios.get('/proses/get_sjproduct_inprocess/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Kosong")
                }else{
                    this.sjproduk = res.data

                    console.log(res,this.sjproduk)
                }
            } catch(error){
                alert("Error")
                console.log(error)
            }
        },

        selectProsestoWorkStation(proses){
            console.log(proses.id)
        }
    }
}
</script>
