<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Negara Baru</h1>
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
            @click="InsertNegara()"
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
        <v-snackbar top color="green" v-model="snackBar">
            Insert Negara Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackBar: false,
      nama: '',
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 3 && v.length >= 3) || 'Kode must be 3 characters',
      ],
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
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
          this.snackBar = true
        }
        catch(error){
          alert("Insert Negara Failed")
          console.log(error)
        }
      },
    },
  }
</script>