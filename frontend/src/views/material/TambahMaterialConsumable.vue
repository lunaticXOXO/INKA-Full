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
        
          <v-text-field
          v-model="id_proses"
          :counter="9"
          :rules="id_prosesRules"
          label="ID Proses"
          required
          ></v-text-field>

          <v-select
          item-text="id"
          item-value="id"
          v-model="stock"
          :items="materialStock"
          label="Material Stock"
          ></v-select>

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
      id_proses: '',
      id_prosesRules: [
        v => !!v || 'ID Proses is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID Proses must be 1-11 characters',
      ],
      stock: '',
      materialStock: undefined,
      quantity: '',
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchSupplier()
    },
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.stock)
        console.log(this.quantity)
      },  

      async fetchStock(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier/get_supplier')
            if (res.data == null){
                alert("Stok Material Kosong")
            }else{
                this.supplier = res.data
                console.log(res,this.supplier)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async fetchMaterialType(){
        try{
            const axios = require('axios')
            const res = await axios.get('/material/get_type')
            if (res.data == null){
                alert("Material Type Kosong")
            }else{
                this.materialType = res.data
                console.log(res,this.materialTypeCode)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async fetchUnit(){
        try{
            const axios = require('axios')
            const res = await axios.get('/unit/get_unit')
            if (res.data == null){
                alert("Material Unit Kosong")
            }else{
                this.units = res.data
                console.log(res,this.units)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async InsertMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/order_new_material',
            { nama: this.nama,
              purchaserName: this.purchaser,
              supplierCode: this.supply,
              materialTypeCode: this.type,
              quantity: this.quantity,
              unit: this.unit,
              id: this.id_stock,
              merk: this.merk,
              schedulledArrival: this.tanggal
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Berhasil",
              color : "green"
            }
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Pesan Material Gagal",
            color : "red"
          }
        }
      },
    },
  }
</script>