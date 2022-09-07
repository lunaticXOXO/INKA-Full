<template>
    <v-app>
        <div class="d-flex">
            <v-card class="mx-auto text-center mt-6" width="500">
                <h3>Info Item Proyek {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers= "column2"
                    :items= "rproyek">
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-6" width="350">
                <h3>Info Proyek {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers="column3"
                    :items = "proyek">
                </v-data-table>
            </v-card>
            <v-card class="mx-auto text-center mt-6" width="350">
                <h3>Info Pelanggan {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers="column4"
                    :items="customer">
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" width="1000">
            <br>
            <h1>Produk</h1><h1>{{this.$route.params.id}}</h1>
            <br>
            <v-data-table 
                :headers="column"
                :items="produk">
                <template v-slot:[`item.percentage`]="{ item }">
                  <span>{{item.percentage}}%</span>
              </template>
            </v-data-table>
        </v-card>
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            column : [
                {text : 'SN',value : 'id'},
                {text : 'Tipe Produk',value : 'jenisProduk'},
                {text : 'Batas Pengerjaan',value : 'dueDate'},
                {text : 'Pengerjaan',value : 'percentage'},
            ],
            column2 : [
                {text : 'ID Item Proyek', value : 'IdRincian'},
                {text : 'Jumlah', value : 'jumlah'},
                {text : 'Batas Pembuatan',value : 'dueDate'},
            ],
            column3 : [
                {text : 'ID Proyek',value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'NamaProyek'},
            ],
            column4 : [
                {text : 'ID Pelanggan', value : 'IdCustomer'},
                {text : 'Nama Pelanggan',value : 'NamaCustomer'}
            ],
            rproyek : [],
            produk  : [],
            customer : [],
            proyek : [],
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
        this.fetchRincianInProduk()
    },

    methods : {
        async fetchProductbyRProyek(){
            const axios = require('axios')
            const res = await axios.get('/product/get_product_by_rproyekDSP/' + this.$route.params.id)
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
                    console.log(res,this.rincianinproduk)
                }

            }catch(error){
                alert("Error")
            }
        },
    }
}
</script>