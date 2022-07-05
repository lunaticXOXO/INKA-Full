<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Rincian Proyek Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="4"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="jumlah"
            label="Jumlah"
            ></v-text-field>

            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="dueDate" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
                <v-date-picker width="1000" v-model="dueDate"></v-date-picker>
            

            <v-text-field 
            v-model="proyek" 
            label="Proyek">
            </v-text-field>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="addRProyekbyProyek()"
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
        <v-snackbar top color="green" v-model="snackBar">
            Insert Rincian Proyek by Proyek Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      
      id: '',
      jumlah : '',
      dueDate : null,
      proyek : '',

      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 1) || 'Kode must be 1-4 characters',
      ],
    }),

    methods: {
     
      reset () {
        this.$refs.form.reset()
      },
      submitHandler() {
        console.log(this.id)
        console.log(this.jumlah)
        console.log(this.dueDate)
        console.log(this.proyek)

      },

      async addRProyekbyProyek(){
        try{
          const axios = require('axios')
          const res = await axios.post('/rproyek/add_rproyek',{
            id : this.id,
            jumlah : this.jumlah,
            dueDate : this.dueDate,
            proyek : this.proyek
          })
          console.log(res)
        }catch(error){
           console.log(error)
        }
      }
    },
  }
</script>