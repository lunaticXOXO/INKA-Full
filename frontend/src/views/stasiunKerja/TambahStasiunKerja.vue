<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Stasiun Kerja Baru</h1>
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

            <v-select
            item-text="nama"
            item-value="id"
            v-model="nama"
            :items="items"
            label="Jenis Stasiun Kerja"
            ></v-select>

            <v-select
            item-text="id"
            item-value="nama"
            v-model="liniproduksi"
            :items="items2"
            label="Lini Produksi"
            ></v-select>

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
        
       <div v-if="snackBar === true">
        <v-snackbar top color="green" v-model="snackBar">
            Insert Stasiun Kerja Sukses!
        </v-snackbar>
     </div>
     <div v-else-if="snackBar === false">
     <v-snackbar top color="red" v-model="snackBar">
            Insert Stasiun Kerja Gagal!
        </v-snackbar>
     </div>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackBar: false,
    
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 3) || 'ID must be 3-4 characters',
      ],
      id: '',
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
         
          if(response.data.status == 200){
              this.snackBar = false
          }else if(response.data == "berhasil"){
            this.snackBar = true
          }
        
        }
        catch(error){
          alert("Insert Stasiun Kerja Failed")
          console.log(error)
          this.snackBar = false
        }
      },
    }
  }
</script>