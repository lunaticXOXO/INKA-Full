<template>
    <v-app>
            <v-card
            class="mx-auto text-center mt-15"
            max-width="1200">
            <br>
            <h2> Pilih Tool Stock Untuk Pengemasan By Box </h2>
            <br>
            <v-card
                class="mx-auto text-center"
                width="1200">
                <v-data-table
                    :headers = "column"
                    :items = "toolneed"
                    :items-per-page="5"
                >
                <template v-slot:[`item.idToolStock`]="{ item }">
                <span>{{item.idToolStock}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
            <div>
                <router-link :to="{name : 'Choose Box Item For Tool Stock', params:{id : `${item.idToolStock}`}}">
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
                        <span>Pengemasan Tool Stock</span>
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
                {text : 'ID Stock', value : 'idToolStock'},
                {text : 'Nama Tool', value : 'nama'},
                {text : 'Merk',value : 'merk'},
                {text : 'Quantity', value : 'quantity'},
                {text : 'Unit', value : 'unit'},
                {text : 'Action', value : 'aksi'}
            

            ],

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
        this.fetchData2()
    },

    methods : {
       

        async fetchData2(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/show_disttoolstock_bytype/' + this.$route.params.id)
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
