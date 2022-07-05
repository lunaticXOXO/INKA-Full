<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Rincian Proyek</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "rincian">
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

                <template v-slot:[`item.jumlah`]="{ item }">
                    <v-text-field v-model="editedItem.jumlah" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.jumlah}}</span>
                </template>

                 <template v-slot:[`item.dueDate`]="{ item }">
                    <div v-if="item.id === editedItem.id">
                        <v-text-field disabled v-model="editedItem.dueDate" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.dueDate}}</span>
                    </div>
                    <div v-else>
                        <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.dueDate}}</span>
                    </div>
                </template>

                <template v-slot:[`item.proyek`]="{ item }">
                    <v-select v-model="editedItem.proyek" item-text="id" item-value="id" :items="proyek" v-if="item.id == editedItem.id"></v-select>
                <span v-else>{{item.proyek}}</span> 
                </template>

                <template v-slot:[`item.jenisProduk`]="{ item }">
                     <v-select v-model="editedItem.jenisProduk" item-text="id" item-value="id" :items="jenisProduk" v-if="item.id == editedItem.id"></v-select>
                <span v-else>{{item.jenisProduk}}</span> 
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
                        <router-link :to="{name:'List Produk by Rincian Proyek',params:{'id': `${item.id}`}}">
                        <v-btn class="mx-1" x-small color="blue" @click="selectRinciantoProduct(item)">
                            <v-icon small dark>mdi-check</v-icon>
                        </v-btn>
                        </router-link>

                        <router-link :to="{name : 'List Jenis Produk by RProyek',params:{'id':`${item.id}`}}">
                        <v-btn class="mx-1" x-small color="brown" @click="selectRinciantoJProduct(item)">
                            <v-icon small dark>mdi-check</v-icon>
                        </v-btn>
                        </router-link>

                        <v-btn class="mx-1" x-small color="green" @click="editRincian(item)">
                            <v-icon small dark>mdi-pencil</v-icon>
                        </v-btn>
                        <v-btn class="mx-1" x-small color="red" @click="deleteRincian(item)">
                            <v-icon small dark>mdi-trash-can-outline</v-icon>
                        </v-btn>
                    </div>
                </template>
            </v-data-table>
            <v-row justify="space-around">
            <router-link to="/">
            <v-btn color="primary">
                Add Rincian Proyek
            </v-btn>
            </router-link>
            </v-row>
        </v-card>
    </v-card>
</template>

<script>
    export default {
        data(){
            return{
                column : [
                    {text : 'ID Rincian Proyek',value : 'id'},
                    {text : 'Jumlah',value : 'jumlah'},
                    {text : 'Due Date', value : 'dueDate'},
                    {text : 'Proyek',value : 'proyek'},
                    {text : 'Jenis Produk',value : 'jenisProduk'},
                    {text : 'Action',value : 'aksi'}
                ],
                rincian : [],
                jenisProduk : [],
                proyek : [],
                editedIndex : -1,
                editedItem : {
                    id : '',
                    jumlah : '',
                    dueDate : '',
                    proyek : '',
                    jenisProduk : ''
                },
                defaultItem : {
                    id : 'New ID',
                    jumlah : 'New Jumlah',
                    dueDate : 'New Due Date',
                    proyek : 'New Proyek',
                    jenisProduk : 'New Jenis Produk'
                },
            }
        },
        
        mounted(){
            this.fetchRincianProyek()
            this.fetchProyek()
            this.fetchJenisProduk()
        },

        methods: {
            editRincian(rincian){
                console.log('ID : ' + rincian.id)
                this.editedIndex = this.rincian.indexOf(rincian)
                this.editedItem = Object.assign({},rincian)
            },

            close(){
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                }, 300)
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
            
            async fetchProyek(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/proyek/get_allproyek')
                    if(res.data == null){
                        //alert("Data kosong")
                        console.log("Data proyek kosong")
                    }else{
                        this.proyek = res.data
                        console.log(res,this.proyek)
                    }

                }catch(error){
                    console.log(error)
                }
            },
            async fetchJenisProduk(){
                try{

                    const axios = require('axios')
                    const res = await axios.get('/jproduct/get_jproduct')
                    if(res.data == null){
                        alert("Data jproduct kosong")
                    }else{
                        this.jenisProduk = res.data
                        console.log(res,this.jenisProduk)
                    }
                }catch(error){
                    console.log(error)
                }
            },
            async updateData(){
                if(this.editedIndex > -1){
                    Object.assign(this.rincian[this.editedIndex],this.editedItem)
                }
                this.close()
                try{
                    const axios = require('axios')
                    const res = await axios.post('/rproyek/update_rproyek/' + this.editedItem.id,{ 
                        id : this.editedItem.id,
                        jumlah : this.editedItem.jumlah,
                        dueDate : this.editedItem.dueDate,
                        proyek : this.editedItem.proyek,
                        jenisProduk : this.editedItem.jenisProduk
                    })
                    console.log(res)                    
                }catch(error){
                    console.log(error)
                }
            },

            selectRinciantoProduct(rincian){
                console.log(rincian.id)
                //open(`/listProdukbyRProyek/${rincian.id}`)
            },

            selectRinciantoJProduct(rincian){
                console.log(rincian.id)
                //open(`/listJenisProdukbyRProyek/${rincian.id}`)
            },

            deleteRincian(rincian){
                console.log('ID : ' + rincian.id)
                try{
                    const axios = require('axios');
                    axios.delete(`/rincianProyek/deleteRincianProyek/${rincian.id}`);
                    alert("Delete Rincian Proyek Success!")
                    this.fetchData()
                }
                catch(error){
                    console.log(error)
                }
            }
        }
    }
</script>
