<template>
  <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Tambah Pemasok Baru</h1>
      <v-form
          class="pa-6"
          ref="form"
          v-model="valid"
          @submit.prevent="submitHandler"
          lazy-validation>
          
          <v-text-field
          v-model="code"
          :rules="idRules"
          label="Code"
          required
          ></v-text-field>

          <v-text-field
          v-model="nama"
          label="Nama"
          ></v-text-field>

          <v-text-field
          v-model="adress1"
          label="Alamat 1"
          ></v-text-field>

          <v-text-field
          v-model="adress2"
          label="Alamat 2"
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="city"
          :items="items"
          label="Kota"
          ></v-autocomplete>

          <v-text-field
          v-model="postalcode"
          label="Kode Pos"
          ></v-text-field>

          <v-text-field
          v-model="phone"
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
          v-model="remark"
          label="Catatan"
          ></v-text-field>
          
          <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          type="submit"
          @click="addSupplier()"
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

      snackbar: {
        show: false,
        message: null,
        color: null
      },

      code: '',
      nama: '',
      adress1: '',
      adress2: '',
      postalcode: '',
      phone: '',
      fax: '',
      email: '',
      situs: '',
      pic: '',
      remark: '',
      city: null,
      idRules: [
        v => !!v || 'ID is required',
      ],
     
      items: [],
    
      emailRules: [
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    }),

    mounted(){
      this.fetchData()
    },
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertPemasok()
        }
      },

      reset () {
        this.$refs.form.reset()
      },
      
      submitHandler() {
        console.log(this.code)
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

      async addSupplier(){
        const axios = require('axios')
        const res = await axios.post('/supplier/add_supplier',{
          code : this.code,
          nama : this.nama,
          adress1 : this.adress1,
          adress2 : this.adress2,
          postalcode : this.postalcode,
          phone : this.phone,
          fax : this.fax,
          email : this.email,
          situs : this.situs,
          pic : this.pic,
          remark : this.remark,
          city : this.city
          
        })
        console.log(res)
       
       if(res.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Data Pemasok Success",
              color : 'green',
              show : true
          }
        
          location.replace('/listPemasok')
        }
          else if(res.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Data Pemasok Gagal, Code Sudah Tersedia!",
              color : 'red',
              show : true
          }}

      }
    },
  }
</script>