<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
    <br>
    <h1>Tambah Material Consumable</h1>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>
    
      <v-autocomplete
        item-text="idNodal"
        item-value="idNodal"
        v-model="proses"
        :items="prosesList"
        label="ID Proses"
      ></v-autocomplete>

      <v-autocomplete
        item-text="id"
        item-value="id"
        v-model="stock"
        :items="materialStock"
        label="Material Stock"
      ></v-autocomplete>

      <v-text-field
        v-model="quantity"
        label="Quantity"
        type="number"
      ></v-text-field>

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
      stock: '',
      materialStock: undefined,
      proses: '',
      prosesList: undefined,
      quantity: '',
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchStock(),
      this.fetchProses()
    },
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertMaterialConsumable()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.proses)
        console.log(this.stock)
        console.log(this.quantity)
      },  

      async fetchStock(){
        try{
            const axios = require('axios')
            const res = await axios.get('/material/get_material_stock')
            if (res.data == null){
                alert("Stok Material Kosong")
            }else{
                this.materialStock = res.data
                console.log(res,this.materialStock)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async fetchProses(){
        try{
            const axios = require('axios')
            const res = await axios.get('/proses/get_listprocess')
            if (res.data == null){
                alert("Proses Kosong")
            }else{
                this.prosesList = res.data
                console.log(res,this.prosesList)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async InsertMaterialConsumable(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material_consumable/add_material_consumable',
            { processCode: this.proses,
              materialStock: this.stock,
              quantity: this.quantity
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Tambah Material Consumable Berhasil",
              color : "green"
            }
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Tambah Material Consumable Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Tambah Material Consumable Gagal",
            color : "red"
          }
        }
      },
    },
  }
</script>