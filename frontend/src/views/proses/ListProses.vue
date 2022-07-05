<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Proses</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
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
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            column : [
                {text : 'ID Proses', value : 'id'},
                {text : 'Proses Sesudahnya', value : 'prosesSesudahnya'},
                {text : 'Nama', value : 'nama'},
                {text : 'Durasi', value : 'durasi'},
                {text : 'Satuan Durasi', value : 'satuanDurasi'},
                {text : 'Jenis Proses', value : 'jenisProses'},
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Action', value : 'aksi'}
            ],
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
        this.fetchProses(),
        this.fetchJenisProses(),
        this.fetchNodal()
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

        async fetchProses(){
              try{
                    const axios = require('axios')
                    const res = await axios.get('/proses/get_listprocess')
                    if (res.data == null){
                        alert("Proses Kosong")
                    }else{
                        this.proses = res.data
                        //this.prosesData = res.data
                        console.log(res,this.proses)
                    }
                }
                catch(error){
                    alert(error)
                    console.log(error)
                }
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

        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.proses[this.editedIndex],this.editedItem)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const res = await axios.post('/proses/update_proses/'+ this.editedItem.id,{
                    id : this.editedItem.id,
                    prosesSesudahnya : this.editedItem.prosesSesudahnya,
                    nama : this.editedItem.nama,
                    durasi : this.editedItem.durasi,
                    satuanDurasi : this.editedItem.satuanDurasi,
                    jenisProses : this.editedItem.jenisProses,
                    nodalOutput : this.editedItem.idNodal
            })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        },

        selectProcesstoWorkStation(proses){
            console.log(proses.id)
            //open(`/listStasiunKerjabyProcess/${proses.id}`)
        }
    }
}

</script>