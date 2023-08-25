<template>
    <v-app>
      <v-card
        class="mx-auto text-center mt-6"
        width="1000">
      
        <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             TAMBAH UUID OPERATOR {{this.$route.params.id}}
            </v-card-title>
        </v-card>
        <br><br>

        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <span class="font-weight-light black--text ">Silahkan Input Kartu RFID</span>
          <br><br>
          <v-text-field
           dense
           v-model="uuid"
           @keyup.enter="validate()"
           autofocus>
          </v-text-field>
        </v-form>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
          {{snackbar.message}}
        </v-snackbar>
      </v-card>
    </v-app>
  </template>
  
  <script>
    export default {
      data: () => ({
        valid: true,
        snackbar: {
          show: false,
          message: null,
          color: null
        },
        uuid: '',
      }),
  
      methods: {
        validate () {
          if(this.$refs.form.validate()){
            this.InsertKartu()
          }
        },
  
        submitHandler() {
          console.log(this.id)
        },
  
        async InsertKartu(){
          try{
            const axios = require('axios');
            const response = await axios.post('/operator/daftarKartu/' + this.$route.params.id,
              { uuid: this.uuid
              }
             );
            console.log(response,this.data)
            if(response.data.status == "berhasil"){
               this.snackbar = {
                message : "Daftar Kartu RFID Berhasil",
                color : 'green',
                show : true
              
            }
            location.replace('/listKartu')
            }
            else if(response.data.status == "gagal"){
                this.snackbar = {
                message : "Daftar Kartu RFID Gagal",
                color : 'red',
                show : true
            }}
          }
          catch(error){
            this.snackbar = {
              message : "Daftar Kartu RFID Error",
              color : 'error',
              show : true
            }
            console.log(error)
          }
        },
      }
    }
  </script>