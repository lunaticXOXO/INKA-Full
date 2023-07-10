<template>
    <v-app>
            <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>Tool Box {{this.$route.params.id}}</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "box"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
        <h2> Isi Tool Box </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1250">
                <v-data-table
                :headers = "column2"
                :items = "boxitem"
                :items-per-page="5"
            >
            </v-data-table>
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
              
                {text : 'ID Tool Box', value : 'id'},
                {text : 'Nama', value : 'nama'}
               
               
            ],

            column2 : [
                {text : 'Id Tool Box', value : 'boxId'},
                {text : 'Id Tool Stock', value : 'toolStockId'},
                {text : 'Nama Tool', value : 'namaTool'}
              
            ],
            box : [],
            boxitem : [],
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
        this.fetchData(),
        this.fetchToolBox()
    },

    methods : {


        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/box/show_toolbox_byid/' + this.$route.params.id)
                if(res.data == null){
                   console.log("data kosong")
                }else{
                    this.box = res.data
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
                const res = await axios.get('/box/show_insertedtool_tobox/' + this.$route.params.id)
                
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.boxitem = res.data
                    console.log(res,this.toolbox)
                }
            }
            catch(error){
                console.log(error)
            }
        }
       
    }
}
</script>
