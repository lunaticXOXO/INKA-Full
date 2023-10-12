<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1200">

    <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
               TAMBAH KELOMPOK MATERIAL
        </v-card-title>

        </v-card>
        <br>

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

      <v-text-field
      v-model="remark"
      label="Remark"
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
    remark : '',
    idRules: [
      v => !!v || 'ID is required',
      v => (v && v.length <= 3 && v.length >= 3) || 'ID must be 3 characters',
    ],
    rincianProyek: undefined,
    snackBar : false,
  
  }),


  methods: {
    validate() {
      if(this.$refs.form.validate()){
        this.InsertClassification()
      }
    },

    reset () {
      this.$refs.form.reset()
    },

    async InsertClassification(){
      try{
        const response = await axios.post('/material/add_group',
          { code: this.code,
            descriptions: this.descriptions,
            remark : this.remark
          }
        );
        console.log(response,this.data)
        if(response.data.status == "berhasil"){
            this.snackbar = {
            message : "Insert Group Material Success",
            color : 'green',
            show : true
        }
            location.replace('/listGrupMaterial')
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