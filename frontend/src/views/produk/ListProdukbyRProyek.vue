<template>
<v-app>

    <div class="d-flex">
    <v-card class="ml-14">
         <h4>Rincian Proyek</h4><h4>{{this.$route.params.id}}</h4>
        <v-data-table
            :headers= "column2"
            :items= "rproyek"
        >
        </v-data-table>
    </v-card>
    </div>
    <div class="product">
    <v-card class="mt-10 text-center mx-10" max-width="1450">
        <br>
        <h1>Product List By Rincian Proyek</h1><h1>{{this.$route.params.id}}</h1>
        <br>

         <router-link :to="{name : 'Tambah Produk by RProyek',params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Produk
            </v-btn>
        </router-link>   
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
    </div>
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
                {text : 'ID Proyek',value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'NamaProyek'},
                {text : 'ID Customer', value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'}
            ],
            rproyek : [],
            produk : [],
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
                    console.log(res,this.product)    
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
                const res = await axios.get('/product/get_rpoyek_inproduct/' + this.$route.params.id)
                if(res.data == null){
                    console.log("Data kosong")
                }else{
                    this.rproyek = res.data
                    console.log(res,this.rincianinproduk)
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