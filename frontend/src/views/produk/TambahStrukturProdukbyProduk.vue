<template>
<v-app>
    <v-card
      class="mx-auto text-center mt-6"
      width="1000">
      <br>
      <h1>Tambah Struktur Produk Baru</h1>
      <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-text-field
          v-model="idNode"
          :counter="7"
          :rules="idNodeRules"
          label="ID Nodal"
          required
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="idNodal"
          v-model="nodeParent"
          :items="items"
          label="Induk Nodal"
          ></v-autocomplete>

          <v-text-field
          v-model="nama"
          label="Nama"
          ></v-text-field>

          <v-text-field
          v-model="jumlah"
          label="Jumlah"
          type="number"
          ></v-text-field>

          <v-autocomplete
          v-model="unit"
          :items="items2"
          label="Unit"
          ></v-autocomplete>

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
          Insert Struktur Produk by Jenis Produk Sukses!
        </v-snackbar>
      </div>

      <div v-else-if="snackBar == false">
        <v-snackbar top color="red" v-model="snackBar">
          Insert Struktur Produk by Jenis Produk Gagal!
        </v-snackbar>
      </div>

      <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
      </v-snackbar>
    </v-card>
    <div class="d-flex">
      <v-card class="mx-auto text-center mt-10" width="1300">
        <h3>Jenis Produk {{this.$route.params.id}}</h3>
        <v-data-table
          :headers = "column2"
          :items = "jproduk">
        </v-data-table>
      </v-card>
    </div>
  </v-app>
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
      jumlah: '',
      idNode: '',
      idNodeRules: [
        v => !!v || 'ID Nodal is required',
        v => (v && v.length <= 5 && v.length >= 5) || 'ID Nodal must be 7 characters',
      ],
      nodeParent: '',
      unit: undefined,
      items: [],
      items2: [
        'Unit',
        'Set'
      ],
      column2 : [
                {text : 'ID Jenis Produk',value : 'IdJenisProduk'},
                {text : 'Nama Jenis Produk',value : 'NamaJenisProduk'},
                {text : 'ID Produk',value : 'IdProduk'},
                {text : 'Due Date Produk',value : 'dueDateProduk'},
                {text : 'ID Rincian Proyek',value : 'IdRincian'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date Rincian',value : 'dueDateRincian'},
                {text : 'ID Proyek', value : 'IdProyek'},
                {text : 'Nama Proyek',value : 'namaProyek'},
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'namaCustomer'}
            ],
            jproduk : [],
    }),

    mounted(){
        this.fetchData(),
        this.fetchJProductInSJProduk()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertStrukturProdukbyJProduk()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.idNode)
        console.log(this.nama)
        console.log(this.jumlah)
        console.log(this.nodeParent)
        console.log(this.unit)
      },

      async fetchData(){
        try{
            const res = await axios.get(`/sjproduct/get_sjproduct`);
            if(res.data == null){
                alert("Struktur Produk Kosong")
            }else{
                this.items = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async InsertStrukturProdukbyJProduk(){
        try{
          const response = await axios.post('/sjproduct/insert_sjproduct_by_jproduct/' + this.$route.params.id,
            { idNodal: this.idNode,
              indukNodal: this.nodeParent,
              jnsProduk: this.$route.params.id,
              nama: this.nama,
              jumlah: this.jumlah,
              satuan: this.unit
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Struktur Produk by Jenis Produk Success",
              color : 'green',
              show : true
          }
            location.replace('/listStrukturJenisProduk/' + this.$route.params.id)
          }
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Struktur Produk by Jenis Produk Gagal, ID Nodal Sudah Tersedia!",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Struktur Produk by Jenis Produk Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

      async fetchJProductInSJProduk(){
        const res = await axios.get('/sjproduct/get_jproduct_insjproduct/' + this.$route.params.id)
        if(res.data == null){
          console.log("Data Kosong")
        }else{
          this.jproduk = res.data
          console.log(res,this.jproduk)
        }
      },
    }
  }
</script>