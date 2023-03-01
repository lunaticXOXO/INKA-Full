<template>
  <v-app>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Tambah Tool Box</h1>
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

    <v-card>
      <v-data-table
          :headers = "column"
          :items = "box"
          :items-per-page = 5
          >
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
      box : [],
      column : [
      {text   : 'Id',   value : 'id'},
        {text : 'Nama', value : 'nama'},
      ],
    }),
    
    mounted(){
      this.showToolBox()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertToolBox()
        }
      },
  
      async InsertToolBox(){
        try{
          const response = await axios.post('/box/add_toolbox',
            { nama: this.nama
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
              this.snackbar = {
              message : "Insert Tool Box Success",
              color : 'green',
              show : true
          }
          
          location.replace('/showToolBox')

        }

          
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Tool Box Gagal",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Tool Box Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

      async showToolBox(){
        try{
                const axios = require('axios')
                const res = await axios.get('/box/show_toolbox')
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.box = res.data
                    console.log(res,this.box)
                }
            }
            catch(error){
                console.log(error)
            }

      }


    }
  }
  </script>