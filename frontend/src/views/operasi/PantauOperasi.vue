<template>
    <v-app>
        <v-card class="mx-auto text-center mt-6 mb-6" max-width="1000" elevation="0">
            <h1>Pantau Operasi</h1>
        </v-card>
        <v-card class="mx-auto text-center" width="600">
            <v-data-table
                :headers = "headers"
                :items = "items2">
                <template v-slot:[`item.id`]="{ item }">
                    <span>{{item.id}}</span>
                </template>
                <template v-slot:[`item.aksi`]="{ item }">
                    <v-btn class="mx-1" x-small color="blue" @click="submitHandler(item)">
                        <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                </template>
            </v-data-table>
        </v-card>
        <v-flex d-flex>
            <v-layout wrap>
                <v-flex md4 v-for="item in items" :key="item.idOperasi">
                    <v-card class="card-container mx-8 my-8">
                        <div class="ma-4">
                            <br>
                            <h3>{{ item.namaProses }}</h3>
                            <p>{{ item.idOperasi }}</p>
                            <div v-if="(item.mulai == null && item.selesai == null)">
                                <v-chip color="yellow" dark>
                                    <p class="mt-4 black--text" >Tidak Ada Operasi</p>
                                </v-chip>
                            </div>
                            <div v-else-if="(item.mulai != null && item.selesai == null)">
                                <v-chip color="blue light">
                                    <p class="mt-4 black--text">Sedang Ada Operasi</p>
                                </v-chip>
                            </div>
                            <div v-else-if="(item.mulai != null && item.selesai != null)">
                                <v-chip color="green">
                                    <p class="mt-4 black--text">Operasi Selesai</p>
                                </v-chip>
                            </div>
                            <br>
                            <h3>Operator</h3>
                            <p>{{item.namaOperator}}</p>
                            <h3>Stasiun Kerja</h3>
                            <p>{{item.stasiunKerja}}</p>
                            <h3>Rencana Mulai</h3>
                            <p>{{ item.rencanaMulai }}</p>
                            <h3>Rencana Selesai</h3>
                            <p>{{ item.rencanaSelesai }}</p>
                            <br>
                        </div>
                        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
                            {{snackbar.message}}
                        </v-snackbar>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-flex>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-app>
</template>

<script>
export default {
    data: () => ({
        headers : [
            {text : 'ID Produk',value : 'id'},
            {text : 'ID Rincian Proyek',value : 'IdRincian'},
            {text : 'Nama Proyek',value : 'NamaProyek'},
            {text : 'Nama Customer',value : 'NamaCustomer'},
            {text : 'Action', value: 'aksi'}
        ],
        valid: true,
        items:[],
        items2: [],
        idProduk: undefined,
        snackbar: {
            show: false,
            message: null,
            color: null
        },
        index : 0
    }),

    mounted(){
        this.fetchData2()
    },

    methods: {
        async fetchData(idProduk){
            try{
                const axios = require('axios');
                const res = await axios.get(`/operasi/get_operasi_byproduk/` + idProduk);
                if(res.data.length == 0 ){
                    this.snackbar = {
                        message : "Tidak Ada Operasi",
                        color : 'red',
                        show : true
                    }
                }else{
                    this.items = res.data;
                    this.snackbar = {
                        message : "Operasi Ditampilkan",
                        color : 'green',
                        show : true
                    }
                   

                    console.log(res,this.items)
                }

                
            } 
            catch(error){
                alert("Error" + error)
                console.log(error)
            }
        },

        async fetchData2(){
            try{
                const axios = require('axios');
                const res = await axios.get(`/operasi/show_product_inpantauoperasi`);
                if(res.data == null || res.data == []){
                    alert("Tidak ada Operasi!")
                }else{
                    this.items2 = res.data;
                    console.log(res,this.items2)
                }
            } 
            catch(error){
                alert("Error" + error)
                console.log(error)
            }
        },

        submitHandler(item) {
            console.log(item.id)
            this.fetchData(item.id)
        },
    }
}
</script>
