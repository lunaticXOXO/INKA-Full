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
            v-model="jnsStasiunKerja"
            :items="items"
            label="Jenis Stasiun Kerja"
            ></v-select>

            <v-select
            item-text="nama"
            item-value="id"
            v-model="liniProduksi"
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
        <v-snackbar top color="green" v-model="snackBar">
            Insert Stasiun Kerja Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackBar: false,
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 3) || 'ID must be 3-4 characters',
      ],
      jnsStasiunKerja: undefined,
      liniProduksi: undefined,
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
              nama: this.jnsStasiunKerja,
              liniproduksi: this.liniProduksi,
            }
          );
          console.log(response,this.data)
          this.snackBar = true
        }
        catch(error){
          alert("Insert Stasiun Kerja Failed")
          console.log(error)
        }
      },
    }
  }
</script>