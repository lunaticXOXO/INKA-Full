<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Purchase Material Item for {{this.$route.params.id}}</h1>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>
        
          <v-text-field
          v-model="id_item"
          :counter="3"
          :rules="idRules"
          label="ID Item"
          required
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="supply"
          :items="supplier"
          label="Supplier"
          @change="updateMaterialType()"
          ></v-autocomplete>

          <v-autocomplete
          item-text="namaMaterialType"
          item-value="materialTypeCode"
          v-model="type"
          :items="materialType"
          label="Material Type Code"
          ></v-autocomplete>
      
          <v-text-field
          v-model="quantity"
          label="Quantity"
          type="number"
          ></v-text-field>

          <v-autocomplete
          item-text="nama"
          item-value="id"
          v-model="unit"
          :items="units"
          label="Unit"
          ></v-autocomplete>

          <v-menu>
            <template v-slot:activator="{ on, attrs }">
                <v-text-field :value="tanggalPurchase" v-bind="attrs" v-on="on" label="Schedulled Arrival" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="1000" v-model="tanggalPurchase"></v-date-picker>
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
      id_item : '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID must be 1-11 characters',
      ],
      supply: '',
      supplier: undefined,
      type: '',
      materialType: undefined,
      unit: '',
      units: undefined,
      quantity: '',
      tanggalPurchase : null,
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchSupplierName(),
      this.fetchMaterialTypeSupplier(),
      this.fetchUnit()
    },
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertMaterialItemByPurchaseMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id_item)
        console.log(this.supply)
        console.log(this.type)
        console.log(this.quantity)
        console.log(this.unit)
        console.log(this.tanggalPurchase)
      },  

      updateMaterialType() {
        this.materialType
      },
      
      async fetchSupplierName(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier_material/show_supplier_name')
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

      async fetchMaterialTypeSupplier(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier_material/show_materialtype_supplier')
            if (res.data == null){
                alert("Material Type/Supplier Kosong")
            }else{
                //this.supplier = res.data
                this.materialType = res.data
                console.log(res,this.supplier)
                console.log(res,this.materialType)
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

      async InsertMaterialItemByPurchaseMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/add_purchase_item_by_idpurchase/'  + this.$route.params.id,
            { 
              id_item : this.id_item,
              supplierCode: this.supply,
              materialTypeCode: this.type,
              quantity: this.quantity,
              unit: this.unit,
              schedulledArrival: this.tanggalPurchase
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Item Berhasil",
              color : "green"
            }

            location.replace('/listPurchaseMaterialItem')
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Pesan Material Item Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Pesan Material Item Error",
            color : "red"
          }
        }
      },
    },
  }
</script>