<template>
    <v-app>
            <v-card
            class="mx-auto text-center mt-15"
            max-width="1200">
            <br>
            <h2> Kebutuhan Total Perkakas dan Ketersediaan Perkakas  </h2>
            <br>
            <v-card
                class="mx-auto text-center"
                width="1200">
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

            <template v-slot:[`item.kelompok`]="{ item }">
                <span>{{item.kelompok}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
            <div v-if="item.kelompok === 'box'">
                <router-link :to="{name : 'Choose Tool Stock Pengemasan', params:{id : `${item.toolTypeCode}`}}">
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
        <div v-else-if="item.kelompok === 'workstation'">
            <router-link :to="{name : 'Choose Tool Stock Pengemasan Non Box', params:{id : `${item.toolTypeCode}`}}">
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
                {text : 'Kekurangan Pengemasan', value : 'kekuranganPendistribusian'},
                {text : 'Kelompok', value : 'kelompok'},
                {text : 'Action', value : 'aksi'}
            

            ],

            toolneed : [],
            rencanaMulai : '',
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
        this.fetchData2()
    },

    methods : {
       

        async fetchData2(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/get_request_kebutuhantool_byws/' + this.$route.params.id,{
                    params : {
                        rencanaMulai : this.$route.query.rencanaMulai
                    }
                })
                if(res.data.length == 0){
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
