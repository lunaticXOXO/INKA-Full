<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Pesan Proyek Baru</h1>
    <v-form
        class="pa-6"
        ref="form"
        @submit.prevent="submitHandler"
        v-model="valid"
        lazy-validation>

        <v-text-field
        v-model="id"
        :counter="20"
        :rules="idRules"
        label="ID"
        required
        ></v-text-field>
      
        <v-autocomplete
          item-text="nama"
          item-value="id"
          v-model="pelanggan"
          :items="customer"
          label="Pelanggan"
          required>
        </v-autocomplete>
        
        <v-text-field
        v-model="nama"
        label="Nama"
        ></v-text-field>

        <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="dueDate" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="dueDate"></v-date-picker>
        </v-menu>

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
        Pesan Proyek Sukses!
      </v-snackbar>
    </div>

    <div v-else-if="snackBar == false">
      <v-snackbar top color="red" v-model="snackBar">
        Pesan Proyek Gagal!
      </v-snackbar>
    </div>

    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
      {{snackbar.message}}
    </v-snackbar>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      dueDate: null,
      id: '',
      nama : '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 20 && v.length >= 1) || 'ID must be 1-20 characters',
      ],
      customer: undefined,
      pelanggan: undefined,
    }),

    mounted(){
      this.ShowCustomer()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertProyek()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.name)
        console.log(this.dueDate)
        console.log(this.pelanggan)
      },

      async InsertProyek(){
        try{
          const axios = require('axios');
          const response = await axios.post('/proyek/add_newproyek',
            { id: this.id,
              nama: this.nama,
              dueDate: this.dueDate,
              customerid: this.pelanggan
            }
           );
          console.log(response,this.data)
          if(response.data.Status == "Berhasil"){
             this.snackbar = {
              message : "Pesan Proyek Success",
              color : 'green',
              show : true
          }}
          else if(response.data.Status == "Gagal"){
              this.snackbar = {
              message : "Pesan Proyek Gagal, ID sudah tersedia!",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Pesan Proyek Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

      async ShowCustomer(){
        const axios = require('axios')
        const response = await axios.get('/customers/get_customers');
        if(response.data == null){
          console.log("Customer Empty!")
        }else{
          this.customer = response.data
        }
      },
    }
  }
</script>