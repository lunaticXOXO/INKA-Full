<template>
    <v-card
        class="mx-auto text-center mt-6"
        width="1200">

        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
               TAMBAH KRITERIA PEMASOK
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
          v-model="id"
          :counter="11"
          :rules="idRules"
          label="ID Kriteria"
          required
          ></v-text-field>

          <v-text-field
          v-model="namaKriteria"
          label="Nama Kriteria"
          ></v-text-field>

      

          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="mulai" v-bind="attrs" v-on="on" label="Mulai" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="800" v-model="mulai"></v-date-picker>
          </v-menu>

          <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate()">
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
      namaKriteria: '',
      mulai: '',
      id : '',
      idRules: [
        v => !!v || 'ID Stock is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID must be 1-11 characters',
      ],
      tanggalPurchase : null,
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
        console.log(this.purchaser)
        console.log(this.tanggalPurchase)
      },  

      async InsertMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/supplier/add_kriteria',
            {   
              id : this.id,
              namaKriteria: this.namaKriteria,
               mulai : this.mulai,
    
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Berhasil",
              color : "green"
            }

            location.replace('/listKriteriaPemasok')
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Pesan Material Error",
            color : "red"
          }
        }
      },
    },
  }
</script>