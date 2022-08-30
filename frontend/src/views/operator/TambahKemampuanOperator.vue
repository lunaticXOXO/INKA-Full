<template>
    <v-app>
        <v-card
          class="mx-auto text-center mt-6"
          width="1000">
          <br>
          <h1>Tambah Kemampuan Operator</h1>
          <h2>{{this.$route.params.id}}</h2>
          <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation>
  
            

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
          <div v-if="snackBar == true">
            <v-snackbar top color="green" v-model="snackBar">
                Tambah Kemampuan Operator Sukses!
            </v-snackbar>
          </div>
  
          <div v-else-if="snackBar == false">
            <v-snackbar top color="red" v-model="snackBar">
                Tambah Kemampuan Operator Gagal!
            </v-snackbar>
          </div>
  
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
        kemampuan: undefined,
        listKemampuan: undefined,
      }),
  
      mounted(){
        this.fetchKemampuan()
      },
  
      methods: {
        validate () {
          if(this.$refs.form.validate()){
            this.InsertKemampuanOperator()
          }
        },
  
        reset () {
          this.$refs.form.reset()
        },
  
        submitHandler() {
          console.log(this.kemampuan)
        },
  
        async fetchKemampuan(){
        try{
          const axios = require('axios');
          const res = await axios.get('/qualification/get_qualification');
          if (res.data == null){
            alert('Kualifikasi Operator Kosong')
          }else{
            this.listKemampuan = res.data
            console.log(res,this.listKemampuan)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

        async InsertKemampuanOperator(){
          try{
            const axios = require('axios');
            const response = await axios.post('/proyek/add_newproyek_by_customer/' + this.$route.params.id,
              { id: this.id,
                nama: this.nama,
              }
             );
            console.log(response,this.data)
            if(response.data.status == "berhasil"){
               this.snackbar = {
                message : "Pesan Proyek Sesuai Customer Success",
                color : 'green',
                show : true
              
            }
            location.replace('/proyekListbyCustomer/' + this.$route.params.id)
            }
            else if(response.data.status == "gagal"){
                this.snackbar = {
                message : "Pesan Proyek Sesuai Customer Gagal",
                color : 'red',
                show : true
            }}
          }
          catch(error){
            this.snackbar = {
              message : "Pesan Proyek Sesuai Customer Error",
              color : 'error',
              show : true
            }
            console.log(error)
          }
        },
      }
    }
  </script>