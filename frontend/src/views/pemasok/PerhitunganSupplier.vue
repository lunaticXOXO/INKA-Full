<template>
    <v-app>
    
    
        <v-card class="text-center mt-4 ml-3" max-width="900">
    
            <v-form
              class="pa-6"  
              ref="form"
              @submit.prevent="submitHandler"
              v-model="valid"
              lazy-validation>

          
              <v-autocomplete
                 item-text="namaKriteria"
                 item-value="IdKriteria"
                 v-model="criteria01"
                 :items="criteriaDesc"
                 label="Criteria 01"
            ></v-autocomplete>
            

            <v-autocomplete
                 item-text="nama"
                 item-value="code"
                 v-model="supplier01"
                 :items="supplier"
                 label="Supplier 01"
            ></v-autocomplete>

            <v-autocomplete
                 item-text="nama"
                 item-value="code"
                 v-model="supplier02"
                 :items="supplier"
                 label="Supplier 02"
            ></v-autocomplete>

              <v-text-field
              v-model="Nilai"
              label="Nilai"
              required
              ></v-text-field>
    
    
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
        
            <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
                {{snackbar.message}}
            </v-snackbar>
        </v-card>
    
        <v-card
            class="text-center mt-10 ml-3"
            max-width="1000">
            <br>
            <h1>Matriks Supplier Input </h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="900">
                <v-data-table
                    :headers = "column"
                    :items = "matrixSupplierByAdmin"
                    :items-per-page="5"
                >
                <template v-slot:[`item.IDKriteria`]="{ item }">
                    <v-text-field v-model="editedItem.IDKriteria" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDKriteria == editedItem.IDKriteria"></v-text-field>
                    <span v-else>{{item.IDKriteria}}</span>
                </template>
    
                <template v-slot:[`item.IDSupplier01`]="{ item }">
                    <v-text-field v-model="editedItem.IDSupplier01" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDSupplier01 == editedItem.IDSupplier01"></v-text-field>
                    <span v-else>{{item.IDSupplier01}}</span>
                </template>
        
                <template v-slot:[`item.IDSupplier02`]="{ item }">
                    <v-text-field v-model="editedItem.IDSupplier02" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDSupplier02 == editedItem.IDSupplier02"></v-text-field>
                    <span v-else>{{item.IDSupplier02}}</span>
                </template>
    
    
                <template v-slot:[`item.nilai`]="{ item }">
                    <v-text-field v-model="editedItem.nilai" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDKriteria == editedItem.IDKriteria"></v-text-field>
                    <span v-else>{{item.nilai}}</span>
                </template>
                
    
                <!-- <template v-slot:[`item.aksi`]="{ item }">
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
                </template> -->
                </v-data-table>
                <v-form
                    class="pa-6"
                    ref="form2"
                    v-model="valid2"
                    @submit.prevent="submitHandler"
                    lazy-validation>
                        <v-btn 
                            color="primary" 
                            class="mx-auto text-center mb-7"
                            @click = "validate2()">
                            Calculate
                        </v-btn>
                </v-form>
            </v-card>
        </v-card>
    
    </v-app>
    </template>
    
    <script>
    export default {
        data(){
            return {
                column : [
                    {text : 'ID Kriteria', value : 'IDKriteria'},
                    {text : 'ID Supplier 01', value : 'IDSupplier01'},
                    {text : 'ID Supplier 02', value : 'IDSupplier02'},
                    {text : 'Nilai', value : 'nilai'},
                    {text : 'ID Penghitung', value : 'idPenghitung'},
                    {text : 'Action',value : 'aksi'}
                ],

                snackbar: {
                    show: false,
                    message: null,
                    color: null
                },
                criteria : [],
                criteriaDesc : [],
                matrixSupplierByAdmin : [],
                supplier : [],
                editedIndex : -1,
                criteria01 : '',
                supplier01 : '',
                supplier02 : '',
                Nilai : '',
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
            this.fetchData2(),
            this.fetchData3(),
            this.fetchDataSupplier()

        },
        
       
     

        methods : {


            validate () {
                if(this.$refs.form.validate()){
                    if(this.snackbar.color == "red"){
                        this.loading = false
                        this.dialog = false
                    }else{
                        this.loading = true
                        this.dialog = true
                    }
                    this.addPerhitungan()
                }
            },

            validate2(){

                if(this.$refs.form2.validate()){
                    if(this.snackbar.color == "red"){
                        this.loading = false
                        this.dialog = false
                    }else{
                        this.loading = true
                        this.dialog = true
                    }
                    this.countSupplier()
                }
            },

            refresh() {
            setTimeout(() => {
                this.timer.setInterval(location.replace('/hasilPerhitunganKriteriaAdmin/' + this.$route.params.id), 2000)
                this.$forceUpdate();  
            }, 2000)
                location.reload()
            },

            async fetchData(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/supplier/get_matriks_kriteria')
                    if(res.data == null){
                        alert("Data Tool Box kosong")
                    }else{
                        this.criteria = res.data
                        console.log(res,this.criteria)
                    }
                }
                catch(error){
                    console.log(error)
                }
            },

            async fetchDataSupplier(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/supplier/get_supplier')
                    if(res.data == null){
                        console.log("supplier kosong")
                    }else{
                        this.supplier = res.data
                        console.log(res,this.supplier)
                    }
                }catch(error){
                    console.log(error)
                }
            },

            async fetchData2(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/supplier/get_kriteria_supplier')
                    if(res.data == null){
                        alert("Data Tool Box kosong")
                    }else{
                        this.criteriaDesc = res.data
                        console.log(res,this.criteriaDesc)
                    }
                }
                catch(error){
                    console.log(error)
                }
            },

            async fetchData3(){

                try{
                    const axios = require('axios')
                    const res = await axios.get('/supplier/get_matrikssupplier_byadmin/' + this.$route.params.id)
                    if(res.data == null){
                        console.log("data kosong")
                    }else{
                        this.matrixSupplierByAdmin = res.data
                        console.log(res,this.matrixSupplierByAdmin)
                    }

                }catch(error){
                    console.log(error)
                }
            },
            
            async addPerhitungan(){
                try{
                    const axios = require('axios')
                    const res = await axios.post('/supplier/add_matrikssupplier_byadmin/' + this.$route.params.id,{
                        criteria01 : this.criteria01,
                        supplier01 : this.supplier01,
                        supplier02 : this.supplier02,
                        Nilai : this.Nilai

                    })

                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                        message : "Insert Matrix Supplier Berhasil",
                        color : 'green',
                        show : true
                    }
                    setTimeout(() => {
                        location.replace('/perhitunganSupplier/' + this.$route.params.id )
                    }, 1000)
                    }
                    else if(res.data.status == "gagal"){
                            this.loading = false
                            this.snackbar = {
                                message : "Insert Matrix Supplier Gagal ",
                                color : 'red',
                                show : true
                            }
                    }
                }catch(error){
                    console.log(error)
                }
            },

            countSupplier(){
                this.loading = true
                setTimeout(() => {
                try{
                    const axios = require('axios')
                    const res = axios.post('/ahp/merge_count_supplier/' + this.$route.params.id)
                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                            message : "Perhitungan Kriteria Berhasil",
                            color : 'green',
                            show : true
                        }
                        setTimeout(() => {
                            location.replace('/hasilPerhitunganKriteriaAdmin/' + this.$route.params.id )
                        }, 2000)

                    }else if(res.data.status == 'gagal'){
                        this.loading = false
                            this.snackbar = {
                                message : "Perhitungan Kriteria Gagal",
                                color : 'red',
                                show : true
                        }
                    }   
                    }catch(error){
                        console.log(error)
                    }
                this.refresh()       
                }, 2000)
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
    