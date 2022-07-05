<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Pesan Proyek Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="20"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>
          
            <v-select
              item-text="nama"
              item-value="id"
              v-model="pelanggan"
              :items="customer"
              label="Pelanggan"
              required>
            </v-select>
            
            <v-text-field
            v-model="name"
            label="Nama"
            ></v-text-field>

            <v-menu>
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field :value="dueDate" v-bind="attrs" v-on="on" label="Due Date" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker width="1000" v-model="dueDate"></v-date-picker>
            </v-menu>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="InsertProyek()"
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
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      name: '',
      dueDate: null,
      id: '',
      nama : '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 20 && v.length >= 1) || 'ID must be 1-20 characters',
      ],
      customer: undefined,
      pelanggan: undefined,
    }),

    mounted(){
      this.ShowCustomer()
    },

    methods: {
      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.name)
        console.log(this.dueDate)
        console.log(this.pelanggan)
      },

      async InsertProyek(){
        try{
          const axios = require('axios');
          const response = await axios.post('/proyek/add_newproyek',
            { id: this.id,
              nama: this.name,
              dueDate: this.dueDate,
              customerid: this.pelanggan
            }
           );
          console.log(response,this.data)
          alert("Insert Proyek Success")
        }
        catch(error){
          alert("Insert Proyek Failed")
          console.log(error)
        }
      },

      async ShowCustomer(){
        const axios = require('axios')
        const response = await axios.get('/customers/get_customers');
        if(response.data == null){
          console.log("Customer Empty!")
        }else{
          this.customer = response.data
        }
      },
    }
  }
</script>