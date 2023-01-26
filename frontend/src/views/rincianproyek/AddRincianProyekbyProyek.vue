<template>
<v-app>
    <v-card
      class="mx-auto text-center mt-6"
      width="1000">
      <br>
      <h1>Tambah Rincian Proyek Baru</h1>

      <v-form
        class="pa-6"
        ref="form"
        @submit.prevent="submitHandler"
        v-model="valid"
        lazy-validation>
      
        <v-text-field
        v-model="jumlah"
        label="Jumlah"
        type="number"
        ></v-text-field>

        <v-date-picker width="800" v-model="dueDate" color="grey"></v-date-picker>

        <v-menu>
        <template v-slot:activator="{ on, attrs }">
            <v-text-field :value="dueDate" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
        </template>
        </v-menu>

        <v-time-picker width="300" v-model="datetime" format="24hr" color="grey"></v-time-picker>

        <v-menu>
        <template v-slot:activator="{ on, attrs }">
            <v-text-field :value="datetime" v-bind="attrs" v-on="on" label="Due Time" prepend-icon="mdi-clock"></v-text-field>
        </template>
        </v-menu>
        
        <v-autocomplete 
        v-model="jenisProduk"
        item-text="nama"
        item-value="id"
        :items ="items" 
        label="Jenis Produk">
        </v-autocomplete>

        <v-btn
        :disabled="dialog"
        :loading="loading"
        color="success"
        class="mr-4"
        type="submit"
        @click="validate()"
        >
        Submit
        </v-btn>

        <v-dialog
          v-model="dialog"
          width="500">
          <v-card class="pa-6">
            <v-card-title class="text-h5 grey lighten-2">
              Pembuatan Operasi
            </v-card-title>
            <br>
            <div class="mx-auto text-center">
              <v-progress-circular
                :size="70"
                :width="7"
                indeterminate
                color="grey darken-2"
              ></v-progress-circular>
              <br>
              <v-data-table
                hide-default-header
                hide-default-footer
                :headers = "headers4"
                :items = "listOperasiBaru">
              </v-data-table>
              <v-text-field
                dense
                flat
                v-model="listKeterangan"
                class="font-weight-bold mx-auto text-center"
                solo
                readonly
                disabled
              ></v-text-field>
            </div>
          </v-card>
        </v-dialog>

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

    <div class="d-flex text-center mx-auto">
      <v-card class="ml-14 text-center mt-6" width="500">
        <h3>Proyek {{this.$route.params.id}}</h3>
        <v-data-table
            :headers = "headers2"
            :items = "proyekinrincian">
        </v-data-table>
      </v-card>

      <v-card class="ml-15 text-center mt-6" width = "400">
        <h3>Customer Proyek {{this.$route.params.id}}</h3>
          <v-data-table
            :headers = "headers3"
            :items = "customer">
          </v-data-table>
      </v-card>
    </div>
    <br><br>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      loading : false,
      dialog : false,
      valid: true,
        headers2 : [
          {text : 'ID Proyek', value : 'IdProyek'},
          {text : 'Nama Proyek', value : 'NamaProyek'}
        ],
        headers3 : [
          {text : 'ID Customer', value : 'IdCustomer'},
          {text : 'Nama Customer',value : 'NamaCustomer'}
        ],
        headers4 : [
          {text : 'ID Operasi',   value : 'id'},
          {text : 'Rencana Mulai',value : 'rencanaMulai'},
          {text : 'Keterangan',   value : 'keterangan'}
        ],
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      jumlah : '',
      datetime: null,
      dueDate : null,
      gabunganTanggal : null,
      jenisProduk : '',
      items : undefined,
      proyekinrincian : [],
      customer : [],
      listOperasiBaru : [],
      listKeterangan : [],
      keterangan: null
    }),

    watch: {
      dialog (val) {
        if (!val) return

        if(this.snackbar.color == "green"){
          this.dialog = false
        }
      },
    },

    mounted(){
      this.fetchJenisProduk(),
      this.fetchProyekInRProyek(),
      window.setInterval(() => {
        this.fetchOperasiAwal(),
        this.fetchOperasiAwalDsc()
      }, 2000)
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          if(this.snackbar.color == "red"){
            this.loading = false
            this.dialog = false
          }else{
            this.loading = true
            this.dialog = true
          }
          this.addRProyekbyProyek()
        }
      },
     
      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.jumlah)
        console.log(this.dueDate)
      },

      async fetchOperasiAwal(){
        try{
          const axios = require('axios')
          const res = await axios.get('/rproyek/show_first_operation')
          if(res == null){
              console.log("Data kosong")
          }else{
              this.listOperasiBaru = res.data
              console.log(res,this.listOperasiBaru)
          }
        }catch(error){
            console.log(error)
        }
      },

      async fetchOperasiAwalDsc(){
        try{
          const axios = require('axios')
          const res = await axios.get('/rproyek/show_first_operation_dsc')
          if(res == null){
              console.log("Data kosong")
          }else{
              this.listKeterangan = res.data
              console.log(res,this.listKeterangan)
          }
        }catch(error){
            console.log(error)
        }
      },

      async addRProyekbyProyek(){
        try{
          const axios = require('axios')
          const response = await axios.post('/rproyek/add_rproyek_byproyek/' + this.$route.params.id,{
            id : this.id,
            jumlah : this.jumlah,
            gabunganTanggal : this.dueDate + ' ' +this.datetime,
            jenisProduk : this.jenisProduk
          })
          console.log(response)
          if(response.data.status == "berhasil"){
            this.loading = false
            this.dialog = false
            this.snackbar = {
              message : "Insert Rincian Proyek by Proyek Success",
              color : 'green',
              show : true
            }
            setTimeout(() => {
              location.replace('/listRProyekbyProyek/' + this.$route.params.id)
            }, 1000)
          }
          else if(response.data.status == "gagal"){
            this.loading = false
            this.snackbar = {
              message : "Insert Rincian Proyek by Proyek Gagal, ID sudah tersedia",
              color : 'red',
              show : true
            }
          }
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

      async fetchProyekInRProyek(){
        try{
          const axios = require('axios')
          const res = await axios.get('/rproyek/show_proyek_inrproyek/' + this.$route.params.id)
          if(res == null){
              console.log("Data kosong")
          }else{
              this.proyekinrincian = res.data
              this.customer = res.data
              console.log(res,this.proyekinrincian)
          }
        }catch(error){
            alert("Error")
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