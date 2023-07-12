<template>
    <v-app>
        <div class="d-flex">
            <v-card
            class="text-center mt-10 ml-3"
            max-width="800">
            <br>
            <h1>Tool Box {{this.$route.params.id}}</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="800">
                <v-data-table
                    :headers = "column"
                    :items = "box"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card
            class="text-center mt-10 ml-10"
            max-width="800">
            <br>
            <h1>Workstation</h1>
            <br>
            <v-card
                class="mx-auto text-center mt-2"
                max-width="800">
                <v-data-table
                    :headers = "column3"
                    :items = "workstation"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

    </div>

    <div class="d-flex">
        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1200">
        <h2> Isi Tool Box </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1200">
                <v-data-table
                :headers = "column2"
                :items = "boxitem"
                :items-per-page="5"
            >
            </v-data-table>
        </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1200">
        <h2> Tools Pada Workstation </h2>
        <v-card
                class="mx-auto text-center mt-7"
                max-width="1200">
                <v-data-table
                :headers = "column4"
                :items = "workstationtools"
                :items-per-page="5"
            >
            </v-data-table>
        </v-card>
        </v-card>
    
    </div>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
      </v-snackbar>
    
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

            column3 : [
                {text : 'ID Workstation', value : 'idWS'},
                {text : 'Nama Workstation', value : 'namaWS'}
            ],

            column4 : [
                {text : 'ID Workstation', value : 'id'},
                {text : 'Nama Workstation', value : 'nama'},
                {text : 'Tool Stock', value : 'toolStockId'}
            ],

            box : [],
            boxitem : [],
            workstation : [],
            workstationtools : [],
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
        this.fetchToolBox(),
        this.fetchWorkstation(),
        this.fetchWorkstationTools()
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
        },

        async fetchWorkstation(){
            try{
                const axios = require('axios')
                const res = await axios.get('/box/show_workstation_bybox/' + this.$route.params.id)
                if(res.data == null){
                    console.log("kosong")
                }   
                else{
                     this.workstation = res.data
                     console.log(res,this.workstation)
                }
            }
            catch(error){
                console.log(error)
            }
           
        },
        async fetchWorkstationTools(){
            try{
                const axios = require('axios')
                const res = await axios.get('/box/show_workstationtools_bybox/' + this.$route.params.id)
                if(res.data == null){
                    console.log("kosong")
                }   
                else{
                     this.workstationtools = res.data
                     console.log(res,this.workstationtools)
                }

            }catch(error){
                console.log(error)
            }
        }
       
    }
}
</script>
