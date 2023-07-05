<template>
    <v-app>
            <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h2> Kebutuhan Total Perkakas dan Ketersediaan Perkakas  </h2>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "toolneed"
                    :items-per-page="5"
                >
                <template v-slot:[`item.toolTypeCode`]="{ item }">
                <span>{{item.toolTypeCode}}</span>
            </template>

            <template v-slot:[`item.namaTool`]="{ item }">
                <span>{{item.namaTool}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
            <div>
                <router-link :to="{name : 'Tambah Tool Stock By Box', params:{id : `${item.id}`}}">
                    <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn 
                            class="mx-1" 
                            x-small
                            color="green"
                            v-bind="attrs"
                            v-on="on">
                            <v-icon small dark>mdi-check</v-icon>
                            </v-btn>
                        </template>
                        <span>Choose Tool Type</span>
                    </v-tooltip>
                </router-link>
        </div>
        </template>           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
       
        <v-card
                class="mx-auto text-center"
                max-width="1250">
        <v-data-table
                :headers = "column2"
                :items = "operation"
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
                {text : 'Tool Type Code', value : 'toolTypeCode'},
                {text : 'Nama Tool', value : 'namaTool'},
                {text : 'Jumlah Kebutuhan',value : 'butuh'},
                {text : 'Kekurangan Pendistribusian', value : 'kekuranganPendistribusian'},
                {text : 'Action', value : 'aksi'}
            

            ],

            column2: [
              
              {text : 'ID Opeerasi', value : 'id'},
              {text : 'Rencana Mulai', value : 'rencanaMulai'},
              {text : 'Rencana Selesai', value : 'rencanaSelesai'},
            
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
