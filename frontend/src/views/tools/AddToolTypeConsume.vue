<template>
  <v-app>
   
    <v-card
      class="mx-auto text-center mt-10"
      width = "1150">
        <br>
        <h1>Tambah Tool Type Consumable</h1>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-text-field
          v-model="nama"
          label="Nama"
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
    <br><br>
    <v-card max-width="1500" class="mx-auto text-center mt-10 pa-2 mb-10">
      <h1>Jenis Perkakas Consumable Yang Sudah Tersedia</h1>
      
      <v-data-table
          :headers = "column"
          :items = "consumbale"
          :items-per-page = 5>
      </v-data-table>

    </v-card>
  </v-app>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data: () => ({
      valid: true,  
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      nama: '',
      consumbale : [],
      nonconsume : [],
      column : [
          {text : 'Code',   value : 'codes'},
          {text : 'Nama',value : 'nama'},
 
        ],
    }),
    
    mounted(){
      this.ShowToolTypeConsumable()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertToolTypeConsume()
        }
      },
  
      async InsertToolTypeConsume(){
        try{
          const response = await axios.post('/tools/add_tooltype_consumable',
            { nama: this.nama
            }
          );
          console.log(response,this.data)
          if(response.data.Status == "Berhasil"){
              this.snackbar = {
              message : "Insert Tool Type Success",
              color : 'green',
              show : true
          }}
          else if(response.data.Status == "Gagal"){
              this.snackbar = {
              message : "Insert Tool Type Gagal",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Tool Type Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

      async ShowToolTypeConsumable(){
        try{
                const axios = require('axios')
                const res = await axios.get('/tools/show_tooltype_consumable')
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.consumbale = res.data
                    console.log(res,this.consumbale)
                }
            }
            catch(error){
                console.log(error)
            }
      }
    }
  }
  </script>