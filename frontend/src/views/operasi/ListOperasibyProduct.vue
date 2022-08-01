<template>
    <v-app>
        <div class="d-flex">
            <v-card class="mx-auto text-center mt-6" width="1250">
                <h3>Info Produk {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "headers"
                    :items = "items">
                </v-data-table>
            </v-card>
        </div>
        <br><br>
        <div class="d-flex">
            <v-card class="mx-auto text-center mt-6" width="1250">
                <h3>Info Operasi {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "headers2"
                    :items = "items2">
                </v-data-table>
            </v-card>
        </div>
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            headers : [
                {text : 'ID Operasi',value : 'id'},
                {text : 'Rencana Mulai',value : 'rencanaMulai'},
                {text : 'ID Produk',value : 'idProduk'},
                {text : 'Due Date Produk',value : 'dueDateProduk'},
                {text : 'ID Rincian Proyek',value : 'idRincian'},
                {text : 'Jumlah', value : 'jumlah'},
                {text : 'Due Date Rincian', value : 'dueDateRincian'},
                {text : 'ID Proyek', value : 'idProyek'},
                {text : 'Nama Proyek', value : 'namaProyek'},
                {text : 'ID Customer', value : 'idCustomer'},
                {text : 'Nama Customer', value : 'namaCustomer'}
            ],
            headers2 : [
                {text : 'ID Operasi', value : 'id'},
                {text : 'Nama Proses',value : 'nama'},
                {text : 'ID Proses', value : 'proses'},
                {text : 'Rencana Mulai', value : 'rencanaMulai'},
                {text : 'Rencana Selesai', value : 'rencanaSelesai'},
                {text : 'Stasiun Kerja', value : 'stasiunKerja'}
            ],
            items : [],
            items2 : [],
        }
    },

    mounted(){
        this.fetchInfoProduk(),
        this.fetchInfoOperasi()
    },

    methods : {
        async fetchInfoProduk(){
            try{
                const axios = require('axios')
                const res = await axios.get('/operasi/show_product_inoperasi/' + this.$route.params.id)
                if (res == null){
                    alert("Produk Kosong")  
                }
                else{
                    this.items = res.data
                    console.log(res,this.items)
                }
            }
            catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async fetchInfoOperasi(){
            try{
                
                const axios = require('axios')
                const res = await axios.get('/operasi/get_operasi_byproduk/' + this.$route.params.id)
                if(res == null){
                    console.log("Operasi kosong")
                }else{
                    this.items2 = res.data
                    console.log(res,this.items2)
                }

            }catch(error){
                alert("Error")
                console.log(error)
            }
        },
    }
}
</script>