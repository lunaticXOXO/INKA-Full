<template>
    <v-app>
    
    
        <v-card class="text-center mt-4 ml-3" max-width="1150">
    
            <v-form
              class="pa-6"
              ref="form"
              @submit.prevent="submitHandler"
              v-model="valid"
              lazy-validation>
            
              <v-autocomplete
                 item-text="nama"
                 item-value="id"
                 v-model="type"
                 :items="list_type"
                 label="Tool Type"
            ></v-autocomplete>

              <v-text-field
              v-model="merk"
              label="Merk"
              required
              ></v-text-field>
    
              <v-text-field
              v-model="quantity"
              label="Quantity"
              required
              ></v-text-field>
            
            <v-autocomplete
                 item-text="nama"
                 item-value="id"
                 v-model="unit"
                 :items="list_unit"
                 label="Unit"
            ></v-autocomplete>





    
              <div class="d-flex">
                <v-menu 
                  class="mt-6"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker full-width v-model="dueDate"></v-date-picker>
              </v-menu>
              
              <v-menu
                ref="menu"
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
               
              </v-menu>
    
    
    
            </div>
             
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                type="submit"
                @click="validate()"
              >
                Submit
                </v-btn>
    
                <v-btn
                  color="error"
                  class="mr-4"
                 @click="reset"
                  >
                  Reset
                </v-btn>
    
            </v-form>
    
        </v-card>
    
    
    
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
                    <router-link :to="{name : 'List Detail Tool Stock By Tool Stock', params:{id : `${item.toolTypeCode}`}}">
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
                toolStock : [],
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
            this.fetchData()
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
    