<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Jenis Produk by Rincian Proyek</h1><h1>{{this.$route.params.id}}</h1>
        <br>
        <router-link :to="{name : '',params : {}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Jenis Produk
            </v-btn>
        </router-link>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "jenisproduk">
            
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
                <router-link :to="{name : 'List Struktur Jenis Produk by Jenis Produk',params:{id : `${item.id}`}}">
                <v-btn class="mx-1" x-small color="blue" @click="selectJProducttoSJProduct(item)">
                    <v-icon small dark>mdi-check</v-icon>
                </v-btn>
                </router-link>

                <v-btn class="mx-1" x-small color="green" @click="editJenisProduct(item)">
                    <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="mx-1" x-small color="red" @click="deleteJenisProduct(item)">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>
            </div>
                </template>
            </v-data-table>
        </v-card>
    </v-card>
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
            jenisproduk : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                nama : '',
                
            },
            defaultItem : {
                id : 'New ID',
                nama : 'New Nama'
            },
            'id' : '',
            'nama' : ''
        }
    },  

    mounted(){
        this.fetchJenisProdukbyRProyek()
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
           //open(`/listStrukturJenisProduk/${jenisproduk.id}`)
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