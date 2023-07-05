<template>
    <v-app>
            <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>Operasi di {{this.$route.params.id}}</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "operation"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
        <h2>Kebutuhan Perkakas di Stasiun Kerja {{this.$route.params.id}} </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1250">
                <v-data-table
                    :headers = "column2"
                    :items = "toolneed"
                    :items-per-page="5"
                >
        </v-data-table>
        </v-card>
        </v-card>
    
    </v-app>
</template>

 
<script>
export default {
    data(){
        return {
            column : [
              
                {text : 'ID Opeerasi', value : 'id'},
                {text : 'Rencana Mulai', value : 'rencanaMulai'},
                {text : 'Rencana Selesai', value : 'rencanaSelesai'},
                {text : 'Mulai', value : 'mulai'},
                {text : 'Selesai',value : 'selesai'}
            ],

            column2 : [
                {text : 'Tool Type Code', value : 'toolTypeCode'},
                {text : 'Nama Tool', value : 'namaTool'},
                {text : 'Jumlah Kebutuhan',value : 'butuh'},
                {text : 'Kekurangan Pendistribusian', value : 'kekuranganPendistribusian'},
                {text : 'Kelompok', value : 'kelompok'}
            

            ],
            operation : [],
            toolneed : [],

            editedIndex : -1,
            editedItem : {
                id : '',
                nama  : '',
            },
            defaultItem : {
                id : '',
                nama : '',
            },
        }
    },

    mounted(){
        this.fetchData(),
        this.fetchData2()
    },

    methods : {
        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/operasi/get_operasi_byws/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Operasi")
                }else{
                    this.operation = res.data
                    console.log(res,this.operation)
                }
            }
            catch(error){
                console.log(error)
            }
        },


        async fetchData2(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/get_request_kebutuhantool_byws/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data kosong")
                }else{
                    this.toolneed = res.data
                    console.log(res,this.toolneed)
                }
            }
            catch(error){
                console.log(error)
            }

        },
       
       
    }
}
</script>
