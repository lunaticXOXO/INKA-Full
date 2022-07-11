<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Rincian Proyek Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
            >
            <v-text-field
            v-model="id"
            :counter="4"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="jumlah"
            label="Jumlah"
            ></v-text-field>

            <v-menu>
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field :value="tanggal" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker width="1000" v-model="tanggal"></v-date-picker>
            </v-menu>
              
            <v-select
            v-model="jenisProduk"
            :items="items2"
            item-text="id"
            item-value="id"
            label="Jenis Produk">
            </v-select>

            <v-select 
            v-model="proyek"
            item-text="id"
            item-value="id"
            :items ="items" 
            label="Proyek">
            </v-select>

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
            Insert Rincian Proyek Sukses!
          </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
          <v-snackbar top color="red" v-model="snackBar">
            Insert Rincian Proyek Gagal!
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
      items : undefined,
      items2 : undefined,
      jumlah : '',
      dueDate : null,
      jenisProduk : '',
      proyek : '',
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 1) || 'ID must be 1-4 characters',
      ],
    }),
    
    mounted(){
      this.getProyek()
      this.getJenisProduk()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.addRProyek()
        }
      },

      reset () {
        this.$refs.form.reset()
      },
  
      submitHandler() {
        console.log(this.id)
        console.log(this.jumlah)
        console.log(this.dueDate)
        console.log(this.jenisProduk)
        console.log(this.proyek)
      },

      async addRProyek(){
        try{
          const axios = require('axios')
          const response = await axios.post('/rproyek/add_rproyek',{
            id : this.id,
            jumlah : this.jumlah,
            dueDate : this.dueDate,
            jenisProduk : this.jenisProduk,
            proyek : this.proyek
          })
          console.log(response)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Rincian Proyek Success",
              color : 'green',
              show : true
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Rincian Proyek Gagal, ID sudah tersedia",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            message : "Insert Rincian Proyek Error",
            color : 'error',
            show : true
          }
        }
      },

      async getProyek(){
        try{
          const axios = require('axios')
          const res = await axios.get('/proyek/get_allproyek')
          if(res.data == null){
            console.log("data kosong")
          }else{
            this.items = res.data
            console.log(res,this.items)
          }

        }
        catch(error){
          console.log(error)
        }
      },

      async getJenisProduk(){
        try{

          const axios = require('axios')
          const res = await axios.get('/jproduct/get_jproduct')
          if(res.data == null){
            console.log("data kosong")
          }else{
            this.items2 = res.data
            console.log(res,this.items2)
          }

        }catch(error){
          console.log(error)
        }
      }
    },
  }
</script>