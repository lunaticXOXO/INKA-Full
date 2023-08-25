<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1200">
    <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             TAMBAH STASIUN KERJA
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
        <v-text-field
        v-model="id"
        :counter="6"
        :rules="idRules"
        label="ID"
        required
        ></v-text-field>

        <v-text-field
        v-model="nama"
        label="Jenis Stasiun Kerja"
        ></v-text-field>

        <v-autocomplete
        item-text="id"
        item-value="id"
        v-model="liniproduksi"
        :items="items2"
        label="Lini Produksi"
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
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 3) || 'ID must be 3-4 characters',
      ],
      nama: undefined,
      liniproduksi: undefined,
      items: undefined,
      items2: undefined,
    }),

    mounted(){
        this.fetchData(),
        this.fetchData2()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertStasiunKerja()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.jnsStasiunKerja)
        console.log(this.liniProduksi)
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

      async fetchData2(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/liniproduksi/show_liniproduksi`);
            if(res.data == null){
                alert("Lini Produksi Kosong")
            }else{
                this.items2 = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async InsertStasiunKerja(){
        try{
          const axios = require('axios');
          const response = await axios.post('/stasiun_kerja/add_stasiun_kerja',
            { id: this.id,
              nama: this.nama,
              liniproduksi: this.liniproduksi,
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Stasiun Kerja Success",
              color : 'green',
              show : true
          }

            location.replace('/listStasiun')
          
          }
          else if(response.data.status == "gagal"){
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