<template>
    <v-app>
    
    
        
    
    
    
        <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>List Tool Stock </h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "toolStock"
                    :items-per-page="5"
                >
                <template v-slot:[`item.id`]="{ item }">
                    <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.id}}</span>
                </template>
    
                <template v-slot:[`item.toolTypeCode`]="{ item }">
                    <v-text-field v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.toolTypeCode}}</span>
                </template>

            
                <template v-slot:[`item.merk`]="{ item }">
                    <v-text-field v-model="editedItem.merk" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.merk}}</span>
                </template>
    
                <template v-slot:[`item.quantity`]="{ item }">
                    <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.quantity}}</span>
                </template>
    
                <template v-slot:[`item.unit`]="{ item }">
                    <v-text-field v-model="editedItem.unit" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.unit}}</span>
                </template>
    
                
                <template v-slot:[`item.arrivalDate`]="{ item }">
                    <v-text-field v-model="editedItem.arrivalDate" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.arrivalDate}}</span>
                </template>
    
    
    
                <template v-slot:[`item.aksi`]="{ item }">
                <div v-if="item.id==editedItem.id">
                    <v-icon color="red" class="mr-3" @click="close()">
                        mdi-window-close
                    </v-icon>
                    <v-icon color="green" @click="updateToolBox()">
                        mdi-content-save
                    </v-icon>
                </div>
                <div v-else>
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
                            <span>Detail Tool Stock</span>
                        </v-tooltip>
                    </router-link>
    
                    <v-tooltip top>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                          class="mx-1" 
                          x-small
                          color="green"
                          @click="editToolBox(item)"
                          v-bind="attrs"
                          v-on="on">
                          <v-icon small dark>mdi-pencil</v-icon>
                        </v-btn>
                      </template>
                      <span>Edit</span>
                    </v-tooltip>
    
                    <v-tooltip top>
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                          class="mx-1" 
                          x-small
                          color="red"
                          @click="deleteToolBox(item)"
                          v-bind="attrs"
                          v-on="on">
                          <v-icon small dark>mdi-trash-can-outline</v-icon>
                        </v-btn>
                      </template>
                      <span>Delete</span>
                    </v-tooltip>
                </div>
                </template>
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
                    {text : 'ID Tool Stock', value : 'id'},
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
                    const res = await axios.get('/tools/get_toolstock')
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
    