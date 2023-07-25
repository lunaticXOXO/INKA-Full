<template>
    <v-app>
        <h1 class="mx-auto text-center mt-15">Peminjaman Perkakas</h1>
        <v-card class="mx-auto text-center mt-15 mb-10" width="750" height="400">
           <v-form
                class="pa-6"
              ref="form"
              @submit.prevent="submitHandler"
              v-model="valid"
              lazy-validation
           >
            <div class="d-flex">
                <v-menu     
                  class="mt-6"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field class="mx-10" :value="tgl00" v-bind="attrs" v-on="on" label="Tanggal Rencana Mulai" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker full-width v-model="tgl00"></v-date-picker>
              </v-menu>

              <v-menu     
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="tgl01" v-bind="attrs" v-on="on" label="Tanggal Rencana Selesai" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker full-width v-model="tgl01"></v-date-picker>
          </v-menu>
              
            
            </div>
        
          
            <v-autocomplete 
            v-model="ws00"
            item-text="nama"
            item-value="id"
            :items ="items" 
            label="Stasiun Kerja">
            </v-autocomplete>
    
        <div class="d-flex" >
               
            <v-btn
            :disabled="!valid"
            color="success"
            class="mx-auto text-center"
            type="submit"
            @click="RequestPeminjamanTools()"
            >
            Submit
            </v-btn>
       
    
        </div>
        </v-form>
    
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
                {{snackbar.message}}
            </v-snackbar>
    
        </v-card>
    
    </v-app>
    
    </template>
    
    <script>
     export default{
    
        data(){
            return {
                
               
                tgl00 : undefined,     
                menu : false,
                valid : true,
                items : [],
                items2 : [],
                ws00 : undefined, 
                snackbar : {
                    show : false,
                    color : null,
                    message : null,
                },

    
            }
    
           
        },
    
    
        mounted(){
            this.fetchData()
        },
    
        methods : {
    
        validate() {
             location.replace('/hasilRequestPeminjaman/' + this.workstation + '?tanggal=' + this.dueDate)
          },
    
            async fetchData(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/stasiun_kerja/show_stasiun_kerja')
                    if (res == null){
                        alert("Stasiun Kerja Kosong")  
                    }
                    else{
                        this.items = res.data
                        console.log(res,this.items)
                    }
                }
                catch(error){
                    alert("Error")
                    console.log(error)
                }
            },
    
                 
           async RequestPeminjamanTools(){
                try{

                    const axios = require('axios')
                    const res = await axios.post('/tools/request_peminjaman_tools',{
                        tgl00 : this.tgl00,
                        tgl01 : this.tgl01,
                        ws00  : this.ws00
                    })

                    if(res.data.status == 'berhasil'){
                        this.snackbar = {
                        show : true,
                        message : "Request Berhasil",
                        color : "green"

                    }
                    setTimeout(() => {
                    location.replace('/hasilRequestPeminjaman/' + this.ws00 + '?tanggal=' + this.tgl00)
                    }, 1000)

                }
                    else if(res.data.status == 'gagal'){
                        this.snackbar = {
                            show : true,
                            message : "Request Failed",
                            color : "red"

                        }
                }   

                }
                catch(error){
                    this.snackbar = {
                            show : true,
                            message : "Reques Error",
                            color : "red"

                        }  
                    console.log(error)
                }
           }
    
    
        }
    
     }
    </script>
    