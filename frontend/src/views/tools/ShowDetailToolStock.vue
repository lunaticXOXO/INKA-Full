<template>
    <v-app>
            <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>Tool type</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "toolStock"
                    :items-per-page="5"
                >           
                </v-data-table>
            </v-card>
        </v-card>

        <v-card class="text-center mt-10 ml-3 mr-2"
        max-width="1250">
        <h2>List Detail Tool Stock {{this.$route.params.id}} </h2>
        <v-card
                class="mx-auto text-center"
                max-width="1250">
                <v-data-table
                    :headers = "column2"
                    :items = "toolDetailStock"
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
                  
                    {text : 'ID Tool Type', value : 'toolTypeCode'},
                    {text : 'Merk', value : 'merk'},
                    {text : 'Quantity', value : 'quantity'},
                    {text : 'Satuan', value : 'unit'},
                    {text : 'Action',value : 'aksi'}
                ],

                column2 : [
                    {text : 'ID Tool Stock', value : 'id'},
                    {text : 'Merk', value : 'merk'},
                    {text : 'Quantity',value : 'quantity'},
                    {text : 'Satuan', value : 'unit'},
                    {text : 'Arrival Date', value : 'arrivalDate'}
                ],
                toolStock : [],
                toolDetailStock : [],

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
                    const res = await axios.get('/tools/show_tooltype_detailstock/' + this.$route.params.id)
                    if(res.data == null){
                        alert("Data Tool Box kosong")
                    }else{
                        this.toolStock = res.data
                        console.log(res,this.toolStock)
                    }
                }
                catch(error){
                    console.log(error)
                }
            },


            async fetchData2(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/tools/detail_toolstock/' + this.$route.params.id)
                    if(res.data == null){
                        alert("Data Tool Box kosong")
                    }else{
                        this.toolDetailStock = res.data
                        console.log(res,this.toolDetailStock)
                    }
                }
                catch(error){
                    console.log(error)
                }

            },
            
            editToolBox(toolBox){
                console.log('ID : ' + toolBox.id)
                this.editedIndex = this.toolBox.indexOf(toolBox)
                this.editedItem = Object.assign({},toolBox)
            },
            
            close(){
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                }, 300)
            },
    
            async updateToolBox(){
                if (this.editedIndex > -1) {
                    Object.assign(this.toolBox[this.editedIndex], this.toolBox)
                    console.log(this.editedItem)
                }
                this.close()
                try{
                    const axios = require('axios')
                    const res = await axios.post('/box/update_toolbox/' + this.editedItem.id,
                    { id : this.editedItem.id,
                      nama : this.editedItem.nama
                    })
                    console.log(res)
                }catch(error){
                    console.log(error)
                }
            }
        }
    }
    </script>
    