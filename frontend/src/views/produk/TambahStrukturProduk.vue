<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Struktur Produk Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="idNode"
            :counter="7"
            :rules="idNodeRules"
            label="ID Nodal"
            required
            ></v-text-field>

            <v-select
            item-text="idNodal"
            item-value="idNodal"
            v-model="nodeParent"
            :items="items"
            label="Induk Nodal"
            ></v-select>
            
            <v-select
            item-text="nama"
            item-value="id"
            v-model="jnsProduk"
            :items="items2"
            label="Jenis Produk"
            ></v-select>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="jumlah"
            label="Jumlah"
            type="number"
            ></v-text-field>

            <v-select
            v-model="unit"
            :items="items3"
            label="Unit"
            ></v-select>

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
            Insert Struktur Produk Sukses!
          </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
          <v-snackbar top color="red" v-model="snackBar">
            Insert Struktur Produk Gagal!
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
      jumlah: '',
      idNode: '',
      idNodeRules: [
        v => !!v || 'ID Nodal is required',
        v => (v && v.length <= 7 && v.length >= 5) || 'ID Nodal must be 5-7 characters',
      ],
      jnsProduk: undefined,
      nodeParent: undefined,
      unit: undefined,
      items: [],
      items2: [],
      items3: [
        'Unit',
        'Set'
      ],
    }),

    mounted(){
        this.fetchData(),
        this.fetchData2()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertStrukturProduk()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.idNode)
        console.log(this.nama)
        console.log(this.jumlah)
        console.log(this.jnsProduk)
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

      async fetchData2(){
        try{
            const res = await axios.get(`/jproduct/get_jproduct`);
            if(res.data == null){
                alert("Jenis Produk Kosong")
            }else{
                this.items2 = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async InsertStrukturProduk(){
        try{
          const response = await axios.post('/sjproduct/insert_sjproduct',
            { idNodal: this.idNode,
              indukNodal: this.nodeParent,
              jnsProduk: this.jnsProduk,
              nama: this.nama,
              jumlah: this.jumlah,
              satuan: this.unit
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
             this.snackbar = {
              message : "Insert Struktur Produk Success",
              color : 'green',
              show : true
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Struktur Produk Gagal, ID Nodal Sudah Tersedia!",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Struktur Produk Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },

    }
  }
</script>