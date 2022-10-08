<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Purchase Material</h1>
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

          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="tanggalPurchase" v-bind="attrs" v-on="on" label="Purchase Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="tanggalPurchase"></v-date-picker>
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
      nama: '',
      purchaser: '',
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
          const response = await axios.post('/material/purchase_material',
            { 
              id : this.id,
              nama: this.nama,
              purchaserName: this.purchaser,
              purchaseDate : this.tanggalPurchase
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Berhasil",
              color : "green"
            }
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