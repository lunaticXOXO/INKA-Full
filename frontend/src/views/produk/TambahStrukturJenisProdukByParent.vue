<template>
<v-app>
    <v-card
      class="ml-11 mt-6"
      width="1200">
      <v-card
        color="#6f6f6f"
        dark
        class="px-5 py-3"
        max-height ="200"
            >
      <v-card-title class="text-h5">
          TAMBAH NODE STRUKTUR PRODUK {{ this.$route.params.id }}
        </v-card-title>
            
      </v-card> 
      <br><br>
      <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-text-field
          v-model="idNode"
          :counter="3"
          :rules="idNodeRules"
          label="ID Nodal"
          required
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="materialTypeCode"
          :items="items3"
          label="Material Type"
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
      <br>
      <v-card
            color="#6f6f6f"
            dark
            class="px-5 py-3"
            max-height ="50"
        >
        </v-card>

    </v-card>
    <div class="d-flex">
      <v-card class="ml-11 mt-10" width="1300">
        
        <v-card
        color="#6f6f6f"
        dark
        class="px-5 py-3"
        max-height ="200"
            >
      <v-card-title class="text-h5">
          PARENT STRUKTUR PRODUK {{ this.$route.params.id }}
        </v-card-title>
            
      </v-card> 
      <br><br>

        <v-data-table
          :headers = "column2"
          :items = "jenisProduk">
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
      materialTypeCode : '',
      idNodeRules: [
        v => !!v || 'ID Nodal is required',
        v => (v && v.length <= 3 && v.length >= 3) || 'ID Nodal must be 3 characters',
      ],
      nodeParent: '',
      unit: undefined,
      items: [],
      items2: [
        'Unit',
        'Set'
      ],
      items3 : [],
      jenisProduk : [],      
      column2 : [
        {text : 'ID Nodal',value : 'idNodal'},
        {text : 'Nama Node',value : 'nama'},
        
      ],
      jproduk : '',
    }),

    mounted(){
        this.fetchData(),
        this.fetchJProductInSJProduk(),
        this.fetchMaterialTypeName()
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
        console.log(this.jproduk)
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

        /*async fetchDataMaterial(){
        try{
            const res = await axios.get(`/material/get_type`);
            if(res.data == null){
                console.log("Material Kosong")
            }else{
                this.items3 = res.data
                console.log(res,this.items3)
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },*/

      async InsertStrukturProdukbyJProduk(){
        try{
          const response = await axios.post('/sjproduct/insert_sjproduct_by_parent/' + this.$route.params.id,
            { idNodal: this.idNode,
              indukNodal: this.nodeParent,
              materialTypeCode : this.materialTypeCode,
              jproduk: this.jproduk,
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
            location.replace('/listJenisProduk')
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

      async fetchMaterialTypeName(){
        const res = await axios.get('/material/get_type_name')
        if(res.data == null){
            console.log('Data kosong')
        }else{
            this.items3 = res.data
            console.log(res,this.items3)
        }
      }, 

      async fetchJProductInSJProduk(){
        const res = await axios.get('/sjproduct/get_parent_sjproduct/' + this.$route.params.id)
        if(res.data == null){
          console.log("Data Kosong")
        }else{
          this.jenisProduk = res.data
          console.log(res,this.jproduk)
        }
      },
    }
  }
</script>