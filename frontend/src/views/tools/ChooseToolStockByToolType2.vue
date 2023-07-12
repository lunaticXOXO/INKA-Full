<template>
    <v-app>
            <v-card
            class="mx-auto text-center mt-15"
            max-width="1200">
            <br>
            <h2> Pilih Tool Stock Untuk Pengemasan By Workstation </h2>
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
                            color="blue"
                            v-bind="attrs"
                            v-on="on"
                            @click = addToolsNonBox()
                            >
                            <v-icon small dark>mdi-plus</v-icon>
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

        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
      </v-snackbar>

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

            snackbar: {
                show: false,
                message: null,
                color: null
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
                const res = await axios.get('/tools/show_disttoolstock_bytype_nobox/' + this.$route.params.id)
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

        async addToolsNonBox(){
            try{
                const axios = require('axios')
                const res = await axios.post('/box/add_toolstock_nonbox/' + this.$route.params.id)
                if(res.data.status == 'berhasil'){
                    this.snackbar = {
                        message : "Insert toolstock to workstation berhasil",
                        color : 'green',
                        show : true
                    }
                    //location.replace('/insertedToolInBox/' + this.$route.params.id)
                }
                else if(res.data.status == 'gagal'){
                    this.snackbar = {
                        message : "Insert toolstock to workstation gagal",
                        color : 'red',
                        show : true
                    }
                }
            }
            catch(error){
                console.log(error)
            }
        }
       
       
    }
}
</script>
