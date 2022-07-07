<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Jenis Produk Baru</h1>
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
            Insert Jenis Produk Sukses!
          </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
          <v-snackbar top color="red" v-model="snackBar">
            Insert Jenis Produk Gagal!
          </v-snackbar>
        </div>

        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
          {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      valid: true,
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      nama: '',    
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 3) || 'ID must be 3-4 characters',
      ],
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertJenisProduk()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
      },

      async InsertJenisProduk(){
        try{
          const response = await axios.post('/jproduct/post_jproduct',
            { id: this.id,
              nama: this.nama
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Jenis Produk Success",
              color : 'green',
              show : true
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Jenis Produk Gagal, ID Sudah Tersedia!",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Jenis Produk Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },
    },
  }
</script>