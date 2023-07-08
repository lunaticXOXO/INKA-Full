<template>
    <v-app>
            <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>Tool Stock {{this.$route.params.id}}</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "stock"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
        <h2> Box yang tersedia </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1250">
                <v-data-table
                :headers = "column2"
                :items = "toolbox"
                :items-per-page="5"
            >
            <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <span>{{item.nama}}</span>
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
                            <v-icon small dark>mdi-plus</v-icon>
                            </v-btn>
                        </template>
                        <span>Add To Box</span>
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
              
                {text : 'ID Tool Stock', value : 'id'},
                {text : 'Nama Tools', value : 'nama'},
                {text : 'Merk', value : 'merk'},
                {text : 'Unit', value : 'unit'}
               
            ],

            column2 : [
                {text : 'ID', value : 'id'},
                {text : 'Nama Tool Box', value : 'nama'},
                {text : 'Action',value : 'aksi'}

            ],
            stock : [],
            toolbox : [],
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
        this.fetchToolBox()
    },

    methods : {
        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/get_toolstock_byid/' + this.$route.params.id)
                if(res.data == null){
                   console.log("data kosong")
                }else{
                    this.stock = res.data
                    console.log(res,this.operation)
                }
            }
            catch(error){
                console.log(error)
            }
        },


        async fetchToolBox(){
            try{
                const axios = require('axios')
                const res = await axios.get('/box/show_toolbox')
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.toolbox = res.data
                    console.log(res,this.toolbox)
                }
            }
            catch(error){
                console.log(error)
            }
        },
       
       
    }
}
</script>
