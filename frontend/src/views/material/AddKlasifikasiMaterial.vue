<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Tambah Klasifikasi</h1>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>
      
      <v-text-field
      v-model="code"
      :counter="3"
      :rules="idRules"
      label="ID"
      required
      ></v-text-field>

      <v-text-field
      v-model="descriptions"
      label="Descriptions"
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

    <div v-if="snackBar == true">
      <v-snackbar top color="green" v-model="snackBar">
        Insert Produk Sukses!
      </v-snackbar>
    </div>

    <div v-else-if="snackBar == false">
      <v-snackbar top color="red" v-model="snackBar">
        Insert Produk Gagal!
      </v-snackbar>
    </div>
    
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
    code: '',
    descriptions : '',
    idRules: [
      v => !!v || 'ID is required',
      v => (v && v.length <= 1 && v.length >= 1) || 'ID must be 1 characters',
    ],
    rincianProyek: undefined,
    snackBar : false,
  
  }),


  methods: {
    validate () {
      if(this.$refs.form.validate()){
        this.InsertClassification()
      }
    },

    reset () {
      this.$refs.form.reset()
    },

    async InsertClassification(){
      try{
        const response = await axios.post('/material/add_classification',
          { code: this.code,
            descriptions: this.descriptions
          }
        );
        console.log(response,this.data)
        if(response.data.status == "berhasil"){
            this.snackbar = {
            message : "Insert Classification Success",
            color : 'green',
            show : true
        }
            location.replace('/listKlasifikasiMaterial')
        }
        else if(response.data.status == "gagal"){
            this.snackbar = {
            message : "Insert Classification Gagal!",
            color : 'red',
            show : true
        }}
      }
      catch(error){
        this.snackbar = {
          message : "Insert Produk Error",
          color : 'error',
          show : true
        }
        console.log(error)
      }
    },

  }
}
</script>