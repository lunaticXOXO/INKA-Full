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
            <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
            </template>    
            
            <template v-slot:[`item.rencanaMulai`]="{ item }">
                <span>{{item.rencanaMulai}}</span>
            </template>
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
        <h2> KEBUTUHAN PENDISTRIBUSIAN PERKAKAS {{this.$route.params.id}} </h2>
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

        </v-data-table>

        </v-card>

        <v-btn 
                class="mx-auto text-center mb-5 mt-3" 
                color="green"
                v-bind="attrs"
                v-on="on"
                @click="validate()"
                >
                Pengemasan Perkakas
            </v-btn>

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
                {text : 'kurangPengemasan', value : 'kurangPengemasan'}
            

            ],
            operation : [],
            operation_complement : [],
            toolneed : [],
            rencanaMulai : '',
            datetime : '',
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
            location.replace('/listKetersediaanPerkakasByWorkstation/' + this.$route.params.id + '?rencanaMulai=' + this.$route.query.rencanaMulai)

        },

        async fetchData(){
            try{
                const axios = require('axios')
                // const res_complement = await axios.get('/operasi/get_operasi_byws/' + this.$route.params.id)
                // this.operation_complement = res_complement.data
                //this.rencanaMulai = this.operation_complement[0].rencanaMulai

                //const res = await axios.get('/operasi/get_operasi_bywsrenmul/' + this.$route.params.id + '?rencanaMulai=' + this.rencanaMulai)

             
                const res = await axios.get('/operasi/get_operasi_bywsrenmul/' + this.$route.params.id,{
                    params : {
                        rencanaMulai : this.$route.query.rencanaMulai
                    }
                })
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
                const res = await axios.get('/tools/get_request_kebutuhantool_byws/' + this.$route.params.id,{
                    params : {
                        rencanaMulai : this.$route.query.rencanaMulai
                    }

                })
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
