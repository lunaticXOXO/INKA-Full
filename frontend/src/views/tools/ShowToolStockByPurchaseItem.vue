<template>
    <v-app>
    
    
        <v-card class="text-center mt-4 ml-3" max-width="1350">
    
            <v-form
              class="pa-6"
              ref="form"
              @submit.prevent="submitHandler"
              v-model="valid"
              lazy-validation>
    
           
              <v-text-field
                v-model="merk"
                label="Merk"
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
                  <v-text-field class="mx-10" :value="arrivalDate" v-bind="attrs" v-on="on" label="Arrival Date" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker full-width v-model="arrivalDate"></v-date-picker>
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
            <h1>List Tool Stock By Purchase Item {{this.$route.params.id}}</h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "toolStock"
                >
                <template v-slot:[`item.id`]="{ item }">
                    <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.id}}</span>
                </template>
    
                <template v-slot:[`item.toolTypeCode`]="{ item }">
                    <v-text-field v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.toolTypeCode}}</span>
                </template>


                <template v-slot:[`item.namaToolType`]="{ item }">
                    <v-text-field v-model="editedItem.namaToolType" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.namaToolType}}</span>
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
                            <span>Tambah Tool Stock</span>
                        </v-tooltip>
                    </router-link>

                    <router-link :to="{name : 'List Detail Tool Stock By Tool Stock', params:{id : `${item.toolTypeCode}`}}">
                        <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn 
                                class="mx-1" 
                                x-small
                                color="yellow"
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
                    {text : 'ID Tool Stock', value : 'id'},
                    {text : 'ID Tool Type', value : 'toolTypeCode'},
                    {text : 'Nama Tool Type', value : 'namaToolType'},
                    {text : 'Merk', value : 'merk'},
                    {text : 'Quantity', value : 'quantity'},
                    {text : 'Satuan', value : 'unit'},
                    {text : 'Action',value : 'aksi'}
                ],
                toolStock : [],
                list_unit: [],
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
                merk : '',
                arrivalDate : undefined,
                quantity : '',
                unit : undefined
            }
        },
    
        mounted(){
            this.fetchData(),
            this.fetchUnit()
        },
    
        methods : {
            validate () {
                if(this.$refs.form.validate()){
                    this.addToolStock()
                }
            },

            async fetchData(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/tools/get_toolstock_by_purchaseitem/' + this.$route.params.id)
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

            async fetchUnit(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/unit/get_unit_instock')
                    if (res.data == null){
                        alert("Material Unit Kosong")
                    }else{
                        this.list_unit = res.data
                        console.log(res,this.list_unit)
                    }
                }catch(error){
                    alert(error)
                    console.log(error)
                }   
            },
            async addToolStock(){
                try{
                    const axios = require('axios')  
                    const res = await axios.post('/tools/add_toolstock_by_toolPurchaseItem/' + this.$route.params.id,{
                        merk : this.merk,
                        quantity : this.quantity,
                        unit : this.unit,
                        arrivalDate : this.arrivalDate
                    })
                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                        message : "Insert Tool Stock Berhasil",
                        color : 'green',
                        show : true
                    }
                    location.replace('/listToolStockByPurchaseItem/' + this.$route.params.id)
                    }  
                    else if(res.data.status == 'gagal'){
                        this.snackbar = {
                            message : "Insert Tool Box Gagal",
                            color : 'red',
                            show : true
                        }
                    }
                }catch(error){
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
    
          
        }
    }
    </script>
    