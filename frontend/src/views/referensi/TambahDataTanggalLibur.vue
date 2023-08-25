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
             TAMBAH TANGGAL LIBUR
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
            <v-menu>
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field :value="hariLibur" v-bind="attrs" v-on="on" label="Choose Date" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker width="1000" v-model="hariLibur"></v-date-picker>
            </v-menu>

            <v-text-field
            v-model="deskripsi"
            label="Deskripsi"
            ></v-text-field>
            
            <br>
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
            Insert Tanggal Libur Sukses!
          </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
          <v-snackbar top color="red" v-model="snackBar">
            Insert Tanggal Libur Gagal!
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
  export default {
    data: () => ({
      valid: true,
      snackBar: undefined,
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      hariLibur: null,
      deskripsi : null,
      tanggalRules: [
        v => !!v || 'Tanggal is required',
      ],
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertTanggalLibur()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.tanggal)
      },

      async InsertTanggalLibur() {
        try{
          const axios = require('axios');
          const response = await axios.post('/holiday/add_holiday',
            { hariLibur: this.hariLibur,
              deskripsi : this.deskripsi
            }
          );
          console.log(response,this.data)

          if(response.data.status == "berhasil"){
              this.snackbar = {
                message : 'Insert Tanggal Libur Berhasil',
                color : 'green',
                show : true
            }

            location.replace('/listTanggalLibur')
          }
          else if(response.data.status == "gagal"){
              this.snackbar = {
                message : 'Insert Tanggal Libur Gagal',
                color : 'red',
                show : true
              }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
                message : 'Insert Tanggal Libur Error',
                color : 'red',
                show : true
          }
        }
      }
    },
  }
</script>