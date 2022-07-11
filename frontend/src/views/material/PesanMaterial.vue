<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Pesan Material</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="3"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="purchaser"
            label="Purchaser Name"
            ></v-text-field>

            <v-text-field
            v-model="purchase_date"
            label="Purchase Date"
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
  export default {
    data: () => ({
      valid: true,
      nama: '',
      purchaser: '',
      purchase_date: '',
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
          this.InsertMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.kode)
        console.log(this.nama)
      },

      async InsertMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/add_material',
            { code: this.kode,
              nama: this.nama
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){

              this.snackbar = {
                show : true,
                message : "Pesan Material Berhasil",
                color : "green"
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
                show : true,
                message : "Pesan Material Gagal",
                color : "red"
              }
          }
        }
        catch(error){
          alert("Pesan Material Failed")
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Pesan Material Gagal",
            color : "red"
          }
        }
      },
    },
  }
</script>