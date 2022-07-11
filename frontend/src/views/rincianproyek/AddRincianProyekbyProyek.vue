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
                <v-text-field :value="dueDate" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
                <v-date-picker width="1000" v-model="dueDate"></v-date-picker>
            </v-menu>
            
           <v-select 
            v-model="jenisProduk"
            item-text="id"
            item-value="id"
            :items ="items" 
            label="Jenis Produk">
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
            Insert Rincian Proyek by Proyek Sukses!
          </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
          <v-snackbar top color="red" v-model="snackBar">
            Insert Rincian Proyek by Proyek Gagal!
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
      jumlah : '',
      dueDate : null,
      jenisProduk : '',
      items : undefined,
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 5 && v.length >= 1) || 'ID must be 1-4 characters',
      ],
    }),

    mounted(){
      this.fetchJenisProduk()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.addRProyekbyProyek()
        }
      },
     
      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.jumlah)
        console.log(this.dueDate)
        console.log(this.proyek)
      },

      async addRProyekbyProyek(){
        try{
          const axios = require('axios')
          const response = await axios.post('/rproyek/add_rproyek_byproyek/' + this.$route.params.id,{
            id : this.id,
            jumlah : this.jumlah,
            dueDate : this.dueDate,
            jenisProduk : this.jenisProduk
          })
          console.log(response)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Rincian Proyek by Proyek Success",
              color : 'green',
              show : true
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Rincian Proyek by Proyek Gagal, ID sudah tersedia",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Rincian Proyek by Proyek Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

      async fetchJenisProduk(){
        try{
          const axios = require('axios')
          const res = await axios.get('/jproduct/get_jproduct')
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
    }
  }
</script>