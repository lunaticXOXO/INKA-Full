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
        <h2> PENGADAAN PERKAKAS {{this.$route.params.id}} </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1250">
        <v-data-table
                :headers = "column2"
                :items = "toolneed"
                :items-per-page="5"
        >
        <template v-slot:[`item.toolTypeCode`]="{ item }">
                <v-text-field v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                <span v-else>{{item.toolTypeCode}}</span>
            </template>

            <template v-slot:[`item.namaTool`]="{ item }">
                <v-text-field v-model="editedItem.namaTool" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                <span v-else>{{item.namaTool}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
           
            <div>
                <router-link :to="{name : 'Tambah Tool Stock By Box', params:{id : `${item.id}`}}">
                    <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn 
                            class="mx-1" 
                            x-small
                            color="blue"
                            v-bind="attrs"
                            v-on="on">
                            <v-icon small dark>mdi-check</v-icon>
                            </v-btn>
                        </template>
                        <span>Next</span>
                    </v-tooltip>
                </router-link>
            
              

              
            </div>
            </template>

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
                {text : 'Stock',value : 'stock'},
                {text : 'Jumlah Butuh', value : 'butuh'},
                {text : 'Pengadaan Tool', value : 'pengadaanTool'},
                {text : 'Action', value : 'aksi'}
            

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

        validate(){
            location.replace('/listKetersediaanPerkakasByWorkstation/' + this.$route.params.id)

        },

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
                const res = await axios.get('/tools/show_hasil_pengadaantools/' + this.$route.params.id)
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
