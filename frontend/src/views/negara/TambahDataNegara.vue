<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1500">

        <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             TAMBAH NEGARA
            </v-card-title>
        </v-card>
        <br><br>

        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="kode"
            :counter="3"
            :rules="kodeRules"
            label="Kode"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            label="Nama"
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
  export default {
    data: () => ({
      valid: true,
      nama: '',
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 3 && v.length >= 3) || 'Kode must be 3 characters',
      ],
      snackbar : {
        show : false,
        color : null,
        message : null,

      }
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertNegara()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.kode)
        console.log(this.nama)
      },

      async InsertNegara(){
        try{
          const axios = require('axios');
          const response = await axios.post('/countries/add_countries',
            { code: this.kode,
              nama: this.nama
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){

              this.snackbar = {
                show : true,
                message : "Insert negara berhasil",
                color : "green"
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
                show : true,
                message : "Insert negara gagal,code sudah tersedia",
                color : "red"
              }
          }

        }
        catch(error){
          alert("Insert Negara Failed")
          console.log(error)
           this.snackbar = {
                show : true,
                message : "Insert negara gagal",
                color : "red"
              }
        }
      },
    },
  }
</script>