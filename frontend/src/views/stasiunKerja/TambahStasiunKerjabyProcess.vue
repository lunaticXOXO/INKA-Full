<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Stasiun Kerja Baru</h1>
        <br>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation
          >
            <v-select
            item-text="nama"
            item-value="id"
            v-model="stasiunKerja"
            :items="items"
            label="Stasiun Kerja"
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