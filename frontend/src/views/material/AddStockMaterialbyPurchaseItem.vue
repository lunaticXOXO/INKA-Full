<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Add Material Stock for Purchase Item {{this.$route.params.id}}</h1>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>
        
          <v-text-field
          v-model="id"
          :counter="11"
          :rules="idRules"
          label="ID"
          required
          ></v-text-field>

          <v-text-field
          v-model="merk"
          label="Merk"
          ></v-text-field>
          
          <v-text-field
          v-model="quantity"
          label="Quantity"
          type="number"
          ></v-text-field>
         
          <v-autocomplete
          item-text="nama"
          item-value="id"
          v-model="unit"
          :items="list_unit"
          label="Unit"
          ></v-autocomplete>

          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="arrivalDate" v-bind="attrs" v-on="on" label="Arrival Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="arrivalDate"></v-date-picker>
          </v-menu>

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
            @click="reset"
            >
            Reset
          </v-btn>
        </v-form>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      id : '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID must be 1-11 characters',
      ],
      merk: '',
      quantity: null,
      unit: '',
      list_unit: undefined,
      arrivalDate: '',
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchUnit()
    },
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertStokMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.merk)
        console.log(this.quantity)
        console.log(this.unit)
        console.log(this.arrivalDate)
      },  

      async fetchUnit(){
        try{
            const axios = require('axios')
            const res = await axios.get('/unit/get_unit_instock')
            if (res.data == null){
                alert("Material Unit Kosong")
            }else{
                this.list_unit = res.data
                console.log(res,this.list_unit)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async InsertStokMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/add_material_stock_by_order/' + this.$route.params.id,
            { 
                id : this.id,
                merk : this.merk,
                quantity : this.quantity,
                unit : this.unit,
                arrivalDate : this.arrivalDate
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Tambah Stok Material Berhasil",
              color : "green"
            }

            location.replace('/listStockMaterial')
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Tambah Stok Material Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Tambah Stok Material Error",
            color : "red"
          }
        }
      },
    },
  }
</script>