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
  
            <v-autocomplete
            item-text="descriptions"
            item-value="codes"
            v-model="kemampuan"
            :items="listKemampuan"
            label="Kemampuan Operator"
            ></v-autocomplete>

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
          <div v-if="snackbar == true">
            <v-snackbar top color="green" v-model="snackbar">
                Tambah Kemampuan Operator Sukses!
            </v-snackbar>
          </div>
  
          <div v-else-if="snackbar == false">
            <v-snackbar top color="red" v-model="snackbar">
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
            const response = await axios.post('/operator/add_operatorlevel/' + this.$route.params.id,
              { qualificationCode: this.kemampuan,
              }
             );
            console.log(response,this.data)
            if(response.data.status == "berhasil"){
                this.snackbar = {
                    message : "Insert Kemampuan Opr. Success",
                    color : 'green',
                    show : true
                }
            }
            else if(response.data.status == "gagal"){
                this.snackbar = {
                    message : "Insert Kemampuan Opr. Failed, Kemampuan Sudah Terdaftar!",
                    color : 'red',
                    show : true
                }
            }
          }
          catch(error){
            this.snackbar = {
              message : "Insert Kemampuan Opr. Error",
              color : 'error',
              show : true
            }
            console.log(error)
          }
        },
      }
    }
  </script>