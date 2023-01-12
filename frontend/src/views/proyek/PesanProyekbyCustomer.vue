<template>
  <v-app>
    <v-card
      class="mx-auto text-center mt-6"
      width="1000">
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
      <div v-if="snackBar == true">
        <v-snackbar top color="green" v-model="snackBar">
          Pesan Proyek Sesuai Customer Sukses!
        </v-snackbar>
      </div>

      <div v-else-if="snackBar == false">
        <v-snackbar top color="red" v-model="snackBar">
          Pesan Proyek Sesuai Customer Gagal!
        </v-snackbar>
      </div>

      <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
      </v-snackbar>
    </v-card>
    
    <div class="d-flex">
      <v-card class="mt-10 text-center mx-10">
        <h3>Customer {{this.$route.params.id}}</h3>   
        <v-data-table 
          :headers="column2"
          :items="customerinproject">
        </v-data-table>
      </v-card>
    </div>
  </v-app>
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
      id: '',
      nama : '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 20 && v.length >= 1) || 'ID must be 1-20 characters',
      ],
      customer: undefined,
      pelanggan: undefined,
        column2 : [
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'}
        ],
        customerinproject : [],
    }),

    mounted(){
      this.ShowCustomer(),
      this.fetchCustomerInProyek()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertProyekByCustomer()
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

      async InsertProyekByCustomer(){
        try{
          const axios = require('axios');
          const response = await axios.post('/proyek/add_newproyek_by_customer/' + this.$route.params.id,
            { id: this.id,
              nama: this.nama,
            }
           );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Pesan Proyek Sesuai Customer Success",
              color : 'green',
              show : true
            
          }
          location.replace('/proyekListbyCustomer/' + this.$route.params.id)
          }
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Pesan Proyek Sesuai Customer Gagal",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Pesan Proyek Sesuai Customer Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

       async fetchCustomerInProyek(){
            const axios = require('axios')
            const res = await axios.get('/proyek/get_customer_inproyek/' + this.$route.params.id)
            if(res.data == null){
                console.log("Data kosong")
            }else{
                this.customerinproject = res.data
                console.log(res,this.customerinproject)
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