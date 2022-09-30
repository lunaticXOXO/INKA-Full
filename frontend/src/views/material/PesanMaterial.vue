<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Material Masuk</h1>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>
        
          <v-text-field
          v-model="id_item"
          label="Id Order"
          ></v-text-field>

          <v-text-field
          v-model="nama"
          label="Nama"
          ></v-text-field>

          <v-text-field
          v-model="purchaser"
          label="Purchaser Name"
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="supply"
          :items="supplier"
          label="Supplier"
          ></v-autocomplete>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="type"
          :items="materialType"
          label="Material Type"
          ></v-autocomplete>


          <v-autocomplete
          item-text="nama"
          item-value="id"
          v-model="unit"
          :items="units"
          label="Unit"
          ></v-autocomplete>


          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="tanggalPurchase" v-bind="attrs" v-on="on" label="Purchase Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="tanggalPurchase"></v-date-picker>
          </v-menu>

          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="tanggal" v-bind="attrs" v-on="on" label="Schedulled Arrival Date" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="tanggal"></v-date-picker>
          </v-menu>

          <v-text-field
          v-model="id_stock"
          :counter="11"
          :rules="id_stockRules"
          label="ID Stock"
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
      nama: '',
      purchaser: '',
      id_stock: '',
      id_stockRules: [
        v => !!v || 'ID Stock is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID must be 1-11 characters',
      ],
      id_item : '',
      supply: '',
      supplier: undefined,
      type: '',
      materialType: undefined,
      unit: '',
      units: undefined,
      quantity: '',
      tanggal: null,
      tanggalPurchase : null,
      merk: '',
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchSupplier(),
      this.fetchMaterialType(),
      this.fetchUnit()
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
        console.log(this.nama)
        console.log(this.purchaser)
        console.log(this.supply)
        console.log(this.type)
        console.log(this.quantity)
        console.log(this.unit)
        console.log(this.tanggal)
        console.log(this.id_stock)
        console.log(this.merk)
      },  

      async fetchSupplier(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier/get_supplier')
            if (res.data == null){
                alert("Supplier Kosong")
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
            { 
              id_item : this.id_item,
              nama: this.nama,
              purchaserName: this.purchaser,
              supplierCode: this.supply,
              materialTypeCode: this.type,
              quantity: this.quantity,
              unit: this.unit,
              id: this.id_stock,
              merk: this.merk,
              schedulledArrival: this.tanggal,
              purchaseDate : this.tanggalPurchase
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