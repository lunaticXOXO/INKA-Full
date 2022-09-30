<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Tambah Produk Baru Sesuai R.Proyek</h1><h1>{{this.$route.params.id}}</h1>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>
      
      <v-text-field
      v-model="id"
      :counter="9"
      :rules="idRules"
      label="ID"
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
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 9 && v.length >= 5) || 'ID must be 5-9 characters',
      ],
     
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertProduk()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
      },

      async InsertProduk(){
        try{
          const response = await axios.post('/product/add_product_by_rproyek/'+ this.$route.params.id,
            { id: this.id
            }
          );
          console.log(response,this.data)
          if(response.data.Status == "Berhasil"){
             this.snackbar = {
              message : "Insert Produk by R.Proyek Success",
              color : 'green',
              show : true
          }
            location.replace('/listProdukbyRProyek/' + this.$route.params.id)
          }
          else if(response.data.Status == "Gagal"){
              this.snackbar = {
              message : "Insert Produk by R.Proyek Gagal, ID Sudah Tersedia!",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Produk by R.Proyek Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },
    }
  }
</script>