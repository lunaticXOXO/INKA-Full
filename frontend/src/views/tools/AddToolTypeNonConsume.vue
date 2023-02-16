<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Tambah Tool Type Non Consumable</h1>
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
    }),
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertToolTypeNonConsume()
        }
      },
  
      async InsertToolTypeNonConsume(){
        try{
          const response = await axios.post('/tools/add_tooltype_nonconsumable',
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
    }
  }
  </script>