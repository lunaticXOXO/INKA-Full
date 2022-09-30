<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Tambah Stasiun Kerja Baru by Proses</h1>
    <br>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>

      <v-autocomplete
      item-text="nama"
      item-value="id"
      v-model="stasiunKerja"
      :items="items"
      label="Stasiun Kerja"
      ></v-autocomplete>
      
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
      @click="reset">
      Reset
      </v-btn>
    </v-form>
    
    <div v-if="snackBar == true">
      <v-snackbar top color="green" v-model="snackBar">
        Insert Stasiun Kerja Sukses!
      </v-snackbar>
    </div>

    <div v-else-if="snackBar == false">
      <v-snackbar top color="red" v-model="snackBar">
        Insert Stasiun Kerja Gagal!
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
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 3) || 'ID must be 3-4 characters',
      ],
      stasiunKerja : undefined,
      items: [],
  
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertStasiunKerjabyProcess()
        }
      },

      reset() {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.stasiunKerja)
      },

      async fetchData(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/stasiun_kerja/show_stasiun_kerja`);
            if(res.data == null){
                alert("Stasiun Kerja Kosong")
            }else{
                this.items = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async InsertStasiunKerjabyProcess(){
        try{
          const axios = require('axios');
          const response = await axios.post('/stasiun_kerja/add_stasiun_by_process/' + this.$route.params.id,
          { 
            stasiunKerja : this.stasiunKerja
          }
          );
          console.log(response)
          if(response.data.Status == "Berhasil"){
             this.snackbar = {
              message : "Insert Stasiun Kerja Success",
              color : 'green',
              show : true
          }

            location.replace('/listStasiunKerjabyProcess/' + this.$route.params.id)
          
          }
          else if(response.data.Status == "Gagal"){
              this.snackbar = {
              message : "Insert Stasiun Kerja Gagal, Kode sudah tersedia",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            message : "Insert Stasiun Kerja Error",
            color : 'error',
            show : true
          }
        }
      },
    }
  }
</script>