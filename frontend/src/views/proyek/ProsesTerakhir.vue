<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Melihat Proses Terakhir</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="5"
            :rules="idRules"
            label="Input ID Produk"
            required
            ></v-text-field>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="fetchData(id)"
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
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "process">
            </v-data-table>
        </v-card>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'Jenis Proses',value : 'id'},
        {text : 'Nodal Output',value : 'nodalOutput'},
        {text : 'Nama',value : 'nama'},
        {text : 'Durasi', value : 'durasi'},
        {text : 'Satuan Durasi', value : 'satuanDurasi'},
        {text : 'ID Jenis Proses', value : 'idjenisproses'},
        {text : 'Nama Jenis Proses', value : 'namajenisproses'},
        {text : 'Stasiun Kerja', value : 'stasiunkerja'}        
      ],
      process:[],
      id: '',
      idRules: [
        v => !!v || 'ID Proyek is required',
        v => (v && v.length <= 5 && v.length >= 5) || 'ID Proyek must be 5 characters',
      ],
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      submitHandler() {
        console.log(this.id)
      },
      
      async fetchData(id){
        try{
          const axios = require('axios');
          const res = await axios.get(`/proses/get_lastprocess_product/${id}`);
          if(res.data == null){
              alert("Proses Kosong")
          }else{
              this.process = res.data;
              console.log(res,this.data)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)

        }
      },
    }
  }
</script>