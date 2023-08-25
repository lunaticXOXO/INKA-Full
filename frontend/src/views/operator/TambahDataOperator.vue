<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
  
    <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
    >
      <v-card-title class="text-h5">
             TAMBAH DATA OPERATOR
      </v-card-title>
      </v-card>
      <br><br>

    <v-form
      class="pa-6"
      ref="form"
      v-model="valid"
      @submit.prevent="submitHandler"
      lazy-validation>
      
      <v-text-field
      v-model="id"
      :rules="idRules"
      label="ID"
      required
      ></v-text-field>

      <v-text-field
      v-model="nama"
      label="Nama"
      ></v-text-field>

      <v-text-field
      v-model="alamat"
      label="Alamat"
      ></v-text-field>

      <v-autocomplete
      item-text="nama"
      item-value="code"
      v-model="kota"
      :items="items"
      label="Kota"
      ></v-autocomplete>

      <v-text-field
      v-model="kodePos"
      label="Kode Pos"
      ></v-text-field>

      <v-text-field
      v-model="noTelepon"
      label="No Telepon"
      ></v-text-field>

      <v-text-field
      v-model="email"
      :rules="emailRules"
      label="Email"
      ></v-text-field>

      <v-text-field
      v-model="userName"
      :rules="userRules"
      label="Username"
      ></v-text-field>

      <!--
      <v-file-input
        required
        v-model="gambar"
        :rules="gambarRules"
        accept="image/*"
        label="Unggah Gambar"
        prepend-icon="mdi-camera"
        @change="onAddFiles">
      </v-file-input>
      -->

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
  export default {
    data: () => ({
      valid: true,
      nama: '',
      alamat: '',
      kodePos: '',
      noTelepon: '',
      id: '',
      userName: '',
      //gambar: '',
      idRules: [
        v => !!v || 'ID is required',
      ],
      userRules: [
        v => !!v || 'Username is required',
      ],
      //gambarRules: [
      //  v => !!v || 'Photo is required',
      //],
      email: '',
      emailRules: [
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      kota: undefined,
      items: undefined,
      snackbar:{
        show : false,
        message : null,
        color : null
      },

    }),

    mounted(){
        this.fetchData()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertOperator()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
        console.log(this.alamat)
        console.log(this.kota)
        console.log(this.kodePos)
        console.log(this.noTelepon)
        console.log(this.email)
        //console.log(this.gambar)
      },

      onAddFiles(files) {
        const reader = new FileReader();
        console.log(reader.readAsDataURL(files));
      },

      async fetchData(){
        try{
          const axios = require('axios');
          const res = await axios.get(`/city/get_allcities`);
          if(res.data == null){
              alert("Kota Kosong")
          }else{
              this.items = res.data;
              console.log(res,this.data)
          }
        }catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async InsertOperator(){
        try{
          const axios = require('axios');
          const response = await axios.post('/operator/add_operator',
            { id: this.id,
              nama: this.nama,
              adress1: this.alamat,
              city : this.kota,
              postalcode : this.kodePos,
              phone : this.noTelepon,
              email : this.email,
              username : this.userName
            }
          );
          console.log(response,this.data)

          if(response.data.status == "berhasil"){
              this.snackbar = {
                message : 'Insert Data Operator Berhasil',
                color : 'green',
                show : true
            }

            location.replace('/listOperator')
          }
          else if(response.data.status == "gagal"){
              this.snackbar = {
                message : 'Insert Data Operator gagal',
                color : 'red',
                show : true
              }
          }
        }
        catch(error){
          alert("Insert Data Operator Failed")
          console.log(error)
          this.snackbar = {
                message : 'Insert Data Operator error',
                color : 'red',
                show : true
          }
        }
      },
    },
  }
</script>