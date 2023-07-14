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
            <div>
                <v-menu     
                  class="mt-6"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal Pengerjaan" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker full-width v-model="dueDate"></v-date-picker>
              </v-menu>
              
            
            </div>
        
          
            <v-autocomplete 
            v-model="workstation"
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
            @click="validate()"
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
                
               
                dueDate : undefined,     
                menu : false,
                valid : true,
                items : [],
                items2 : [],
                workstation : undefined, 
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
    
                 
           
    
    
        }
    
     }
    </script>
    