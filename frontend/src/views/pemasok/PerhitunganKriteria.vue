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
                 label="Kriteria 01"
            ></v-autocomplete>
            

            <v-autocomplete
                 item-text="namaKriteria"
                 item-value="IdKriteria"
                 v-model="criteria02"
                 :items="criteriaDesc"
                 label="Kriteria 02"
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
            <h1>Matriks Kriteria Input </h1>
            <br>
            <v-card
                class="mx-auto text-center"
                max-width="900">
                <v-data-table
                    :headers = "column"
                    :items = "matrixCriteriaByAdmin"
                    :items-per-page="5"
                >
                <template v-slot:[`item.IdKriteria01`]="{ item }">
                    <v-text-field v-model="editedItem.IdKriteria01" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria01 == editedItem.IdKriteria01"></v-text-field>
                    <span v-else>{{item.IdKriteria01}}</span>
                </template>
    
                <template v-slot:[`item.namaKriteria`]="{ item }">
                    <v-text-field v-model="editedItem.namaKriteria" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria01 == editedItem.IdKriteria01"></v-text-field>
                    <span v-else>{{item.namaKriteria}}</span>
                </template>


            
                <template v-slot:[`item.IdKriteria02`]="{ item }">
                    <v-text-field v-model="editedItem.IdKriteria02" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria02 == editedItem.IdKriteria02"></v-text-field>
                    <span v-else>{{item.IdKriteria02}}</span>
                </template>
    
                <template v-slot:[`item.namaKriteria02`]="{ item }">
                    <v-text-field v-model="editedItem.namaKriteria02" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria02 == editedItem.IdKriteria02"></v-text-field>
                    <span v-else>{{item.namaKriteria02}}</span>
                </template>
    
                <template v-slot:[`item.nilai`]="{ item }">
                    <v-text-field v-model="editedItem.nilai" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria01 == editedItem.IdKriteria01"></v-text-field>
                    <span v-else>{{item.nilai}}</span>
                </template>
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
                            @click = "countKriteria()">
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
                    {text : 'ID Kriteria', value : 'IdKriteria01'},
                    {text : 'Nama Kriteria', value : 'namaKriteria01'},
                    {text : 'ID Kriteria 02', value : 'IdKriteria02'},
                    {text : 'Nama Kriteria 02', value : 'namaKriteria02'},
                    {text : 'Nilai', value : 'Nilai'},
                    {text : 'Action',value : 'aksi'}
                ],

                snackbar: {
                    show: false,
                    message: null,
                    color: null
                },
                criteria : [],
                criteriaDesc : [],
                matrixCriteriaByAdmin : [],
                editedIndex : -1,
                criteria01 : '',
                criteria02 : '',
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
            this.fetchData3()

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
                    this.countKriteria()
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
                    const res = await axios.get('/supplier/get_matrikskriteria_byadmin/' + this.$route.params.id)
                    if(res.data == null){
                        console.log("data kosong")
                    }else{
                        this.matrixCriteriaByAdmin = res.data
                        console.log(res,this.matrixCriteriaByAdmin)
                    }

                }catch(error){
                    console.log(error)
                }
            },
            
            async addPerhitungan(){
                try{
                    const axios = require('axios')
                    const res = await axios.post('/supplier/add_matrikskriteria_byadmin/' + this.$route.params.id,{
                        criteria01 : this.criteria01,
                        criteria02 : this.criteria02,
                        Nilai : this.Nilai

                    })

                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                        message : "Insert Matrix Kriteria Berhasil",
                        color : 'green',
                        show : true
                    }
                    setTimeout(() => {
                        location.replace('/perhitunganKriteria/' + this.$route.params.id )
                    }, 1000)

                    }
                    else if(res.data.status == "gagal"){
                            this.loading = false
                            this.snackbar = {
                                message : "Insert Matrix Kriteria Gagal ",
                                color : 'red',
                                show : true
                            }
                    }

                }catch(error){
                    console.log(error)
                }
            },
             countKriteria(){
                this.loading = true
                setTimeout(() => {
                try{
                    const axios = require('axios')
                    const res = axios.post('/ahp/merge_count_kriteria/' + this.$route.params.id)
                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                            message : "Perhitungan Kriteria Berhasil",
                            color : 'green',
                            show : true
                        }
                        setTimeout(() => {
                            location.replace('/hasilPerhitunganKriteriaAdmin/' + this.$route.params.id )
                        }, 1000)

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
                }, 1000)
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
    