<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Struktur Jenis Produk</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
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
                        <v-btn class="mx-1" x-small color="blue" @click="selectSJProduct(item)">
                            <v-icon small dark>mdi-check</v-icon>
                        </v-btn>
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
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            headers : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'ID Induk Nodal', value : 'indukNodal'},
                {text : 'Nama', value : 'nama'},
                {text : 'Jumlah', value : 'jumlah'},
                {text : 'Satuan',value : 'satuan'},
                {text : 'Jenis Produk', value : 'jnsProduk'},
                {text : 'Action', value : 'aksi'}
            ],
            sjproduk : [],
            jenisproduk: [],
            indukNodal: [],
            editedIndex: -1,
            editedItem: {
                idNodal: '',
                indukNodal: '',
                nama: '',
                jumlah: '',
                satuan: '',
                jnsProduk: '',
            },
            defaultItem: {
                idNodal: '',
                indukNodal: '',
                nama: '',
                jumlah: '',
                satuan: '',
                jnsProduk: '',
            }
        }
    },
    
    mounted(){
        this.fetchSJProduk(),
        this.fetchJnsProduk()
    },

    methods: {
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

        async fetchSJProduk(){
            try{
                const res = await axios.get('/sjproduct/get_sjproduct')
                if(res.data == null){
                    alert("Data Kosong")
                }else{
                    this.sjproduk = res.data
                    this.indukNodal = res.data
                    console.log(res,this.sjproduk)
                }
            }catch(error){
                console.log(error)
            }
        },

        async fetchJnsProduk(){
            try{
                const res = await axios.get('/jproduct/get_jproduct')
                if(res.data == null){
                    alert("Data Kosong")
                }else{
                    this.jenisproduk = res.data
                    console.log(res,this.jenisproduk)
                }
            }
            catch(error){
                console.log(error)
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
                  jnsproduk: this.editedItem.jnsproduk 
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        },

        selectSJProduct(sjproduk){
            open(`/listProcessbySJProduk/${sjproduk.idNodal}`)
        }
    }
}
</script>
