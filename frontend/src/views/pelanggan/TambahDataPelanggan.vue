<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1200"
      
      >
      <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="400"
        >
        <v-card-title class="text-h4">
              TAMBAH DATA PELANGGAN
            </v-card-title>
        </v-card>
        <br>
      <v-form
        class="pa-6"
        ref="form"
        v-model="valid"
        @submit.prevent="submitHandler"
        lazy-validation>
        
        <v-text-field
        v-model="id"
        :rules="idRules"
        label="ID"
        required
        ></v-text-field>

        <v-text-field
        v-model="nama"
        label="Nama"
        ></v-text-field>

        <v-text-field
        v-model="alamat1"
        label="Alamat 1"
        ></v-text-field>

        <v-text-field
        v-model="alamat2"
        label="Alamat 2"
        ></v-text-field>

        <v-select
        item-text="nama"
        item-value="code"
        v-model="kota"
        :items="items"
        label="Kota"
        ></v-select>

        <v-text-field
        v-model="kodePos"
        label="Kode Pos"
        ></v-text-field>

        <v-text-field
        v-model="noTelepon"
        label="Telepon"
        ></v-text-field>

        <v-text-field
        v-model="fax"
        label="Fax."
        ></v-text-field>

        <v-text-field
        v-model="email"
        :rules="emailRules"
        label="Email"
        ></v-text-field>

        <v-text-field
        v-model="situs"
        label="Situs"
        ></v-text-field>

        <v-text-field
        v-model="pic"
        label="PIC"
        ></v-text-field>

        <v-text-field
        v-model="catatan"
        label="Catatan"
        ></v-text-field>
        
        <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        type="submit"
        @click="validate();"
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
    
      fax: '',
      situs: '',
      pic: '',
      catatan: '',
      nama: '',
      alamat1: '',
      alamat2: '',
      kodePos: '',
      noTelepon: '',
      id: '',
      idRules: [
        v => !!v || 'ID is required',
      ],
      kota: undefined,
      items: undefined,
      email: '',
      emailRules: [
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],

      snackbar: {
        show: false,
        message: null,
        color: null
      },
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertPelanggan()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
        console.log(this.alamat1)
        console.log(this.alamat2)
        console.log(this.kota)
        console.log(this.kodePos)
        console.log(this.noTelepon)
        console.log(this.fax)
        console.log(this.email)
        console.log(this.situs)
        console.log(this.pic)
        console.log(this.catatan)
      },

      async fetchData(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/city/get_allcities`);
            console.log(res.data)
            if(res.data == null){
                alert("Kota Kosong")
            }else{
                this.items = res.data
            }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async InsertPelanggan(){
        try{
          const axios = require('axios');
          const response = await axios.post('/customers/add_customer',
            { id: this.id,
              nama: this.nama,
              adress1: this.alamat1,
              adress2: this.alamat2,
              postalcode: this.kodePos,
              phone: this.noTelepon,
              fax: this.fax,
              email: this.email,
              situs: this.situs,
              pic: this.pic,
              remark: this.catatan,
              city: this.kota
            }
          );
          console.log(response,this.data)
         if(response.data.Status == "Berhasil"){
             this.snackbar = {
              message : "Insert Customer Success",
              color : 'green',
              show : true
          }
          location.replace('/listPelanggan')
        }
          else if(response.data.Status == "Gagal"){
              this.snackbar = {
              message : "Insert Customer Gagal, Kode sudah tersedia",
              color : 'red',
              show : true
          }}
          
        }
        catch(error){
          alert("Insert Pelanggan Failed")
          console.log(error)
          this.snackbar = {
              message : "Insert Customer Error",
              color : 'red',
              show : true}
          
        }
      },

    },
  }
</script>