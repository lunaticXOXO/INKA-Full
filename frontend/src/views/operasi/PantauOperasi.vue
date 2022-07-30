<template>
    <v-app>
        <div class="d-flex">
            <h1 class="ma-4">Pantau Operasi</h1>
            <v-card
            class="text-center ml-4 pa-2"
            max-width="500"
            flat
            >
                <v-form
                    ref="form"
                    @submit.prevent="submitHandler"
                    v-model="valid"
                    lazy-validation
                >
                    <div class="d-flex">
                        <v-text-field
                            v-model="idProduk"
                            class="mr-4 text-center"
                            label="Input ID Produk"
                            type="text"
                            >
                        </v-text-field>
                        <v-btn
                            color="blue"
                            class="mr-4 mt-4"
                            type="submit"
                            @click="submitHandler()"
                            >
                            Submit
                        </v-btn>
                    </div>
                </v-form>
            </v-card>
        </div>
        <v-flex d-flex>
            <v-layout wrap>
                <v-flex md4 v-for="item in items" :key="item.idOperasi">
                    <v-card class="card-container mx-8 my-8">
                        <div class="ma-4">
                            <br>
                            <h3>{{ item.namaProses }}</h3>
                            <p>{{ item.idOperasi }}</p>
                            <div class="d-flex">
                                <v-btn
                                    color="success"
                                    class="mr-1"
                                    type="submit"
                                    @click="startOperation(item)">
                                    Mulai Operasi
                                </v-btn>
                                <v-btn
                                    color="red"
                                    type="submit"
                                    @click="stopOperation(item)">
                                    Stop Operasi
                                </v-btn>
                            </div>
                            <br>
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
    </v-app>
</template>

<script>
export default {
    data: () => ({
      valid: true,
      items:[],
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      idProduk: undefined
    }),

    mounted(){
        //this.fetchData()
    },

    methods: {
        async fetchData(idProduk){
            try{
                const axios = require('axios');
                const res = await axios.get(`/operasi/pantau_operasi/` + idProduk);
                if(res.data == null || res.data == []){
                    alert("Tidak ada Operasi!")
                }else{
                    this.items = res.data;
                    console.log(res,this.items)
                }
            } 
            catch(error){
                alert("Error" + error)
                console.log(error)
            }
        },

        async startOperation(item){
            console.log(item.idOperasi)
            try{
                const axios = require('axios');
                const response = await axios.post('/operasi/start_operasi/' + item.idOperasi);
                console.log(response,this.data)
                if(response.data.status == "berhasil"){
                    this.snackbar = {
                    message : "Mulai Operasi Success",
                    color : 'green',
                    show : true
                }}
                else if(response.data.status == "gagal"){
                    this.snackbar = {
                    message : "Mulai Operasi Failed",
                    color : 'red',
                    show : true
                }}
            }
            catch(error){
                this.snackbar = {
                    message : "Mulai Operasi Error",
                    color : 'error',
                    show : true
                }
                console.log(error)
            }
        },

        async stopOperation(item){
            console.log(item.idOperasi)
            try{
                const axios = require('axios');
                const response = await axios.post('/operasi/end_operasi/' + item.idOperasi);
                console.log(response,this.data)
                if(response.data.status == "berhasil"){
                    this.snackbar = {
                    message : "Stop Operasi Success",
                    color : 'green',
                    show : true
                }}
                else if(response.data.status == "gagal"){
                    this.snackbar = {
                    message : "Stop Operasi Failed",
                    color : 'red',
                    show : true
                }}
            }
            catch(error){
                this.snackbar = {
                    message : "Stop Operasi Error",
                    color : 'error',
                    show : true
                }
                console.log(error)
            }
        },

        submitHandler() {
            console.log(this.idProduk)
            this.fetchData(this.idProduk)
        },
    }
}
</script>
