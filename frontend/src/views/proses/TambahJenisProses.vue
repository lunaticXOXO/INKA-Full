<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1200">
    
    <v-card
          color="#6f6f6f"
          dark
         class="px-5 py-3"
         max-height ="200"
            >
        <v-card-title class="text-h5">
            TAMBAH JENIS PROSES
        </v-card-title>
          
    </v-card>
      <br><br>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>
      
      <v-text-field
      v-model="id"
      :counter="2"
      :rules="idRules"  
      label="ID"
      required
      ></v-text-field>

      <v-text-field
      v-model="namajenisproses"
      label="Nama Jenis Proses"
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
      @click="reset()"
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

  <br>
    <v-card
            color="#6f6f6f"
            dark
            class="px-5 py-3"
            max-height ="50"
        >
    </v-card>

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
    id: '',
    namajenisproses : '',
    idRules: [
      v => !!v || 'ID is required',
      v => (v && v.length <= 3 && v.length >= 3) || 'ID must be 3 characters',
    ],
    snackBar : false,
  }),

 
  methods: {
    validate () {
      if(this.$refs.form.validate()){
        this.InsertJenisProses()
      }
    },

    reset () {
      this.$refs.form.reset()
    },

    async InsertJenisProses(){
      try{
        const response = await axios.post('/jenis_proses/insert_jenisproses',
          { id: this.id,
            namajenisproses: this.namajenisproses
          }
        );
        console.log(response,this.data)
        if(response.data.status == "berhasil"){
            this.snackbar = {
            message : "Insert jenis proses berhasil",
            color : 'green',
            show : true
        }
            location.replace('/listJenisProses')

        }
        else if(response.data.status == "gagal"){
            this.snackbar = {
            message : "Insert jenis proses gagal",
            color : 'red',
            show : true
        }}
      }
      catch(error){
        this.snackbar = {
          message : "Insert jenis proses error",
          color : 'error',
          show : true
        }
        console.log(error)
      }
    },

   
  }
}
</script>