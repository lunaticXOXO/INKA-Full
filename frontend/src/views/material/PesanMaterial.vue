<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Pesan Material</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="11"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="purchaser"
            label="Purchaser Name"
            ></v-text-field>

            <v-select
            item-text="nama"
            item-value="code"
            v-model="supply"
            :items="supplier"
            label="Supplier"
            ></v-select>

            <v-select
            item-text="nama"
            item-value="code"
            v-model="type"
            :items="materialType"
            label="Material Type"
            ></v-select>

            <v-text-field
            v-model="quantity"
            label="Quantity"
            type="number"
            ></v-text-field>

            <v-select
            v-model="unit"
            :items="units"
            label="Unit"
            ></v-select>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate()"
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
      supply: '',
      type: '',
      quantity: '',
      unit: '',
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 11 && v.length >= 1) || 'ID must be 1-11 characters',
      ],
      supplier: undefined,
      materialType: undefined,
      units: [
        "Set",
        "Lembar",
        "Pack"
      ],
      snackbar : {
        show : false,
        color : null,
        message : null,

      }
    }),

    mounted(){
        this.fetchSupplier(),
        this.fetchMaterialType()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertMaterial()
          this.InsertMaterial2()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
        console.log(this.purchaser)
        console.log(this.supply)
        console.log(this.type)
        console.log(this.quantity)
        console.log(this.unit)
      },

      async fetchSupplier(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/supplier/show_supplier`);
            if(res.data == null){
                alert("Supplier Kosong")
            }else{
                this.supplier = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async fetchMaterialType(){
        try{
            const axios = require('axios');
            const res = await axios.get(`/material/show_material_type`);
            if(res.data == null){
                alert("Material Type Kosong")
            }else{
                this.materialType = res.data
            }
        } 
        catch(error){
            alert("Error" + error)
            console.log(error)
        }
      },

      async InsertMaterial(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/add_purchaseMaterial',
            { id: this.id,
              nama: this.nama,
              purchaserName: this.purchaser
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
              this.snackbar = {
                show : true,
                message : "Pesan Material Berhasil",
                color : "green"
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
                show : true,
                message : "Pesan Material Gagal",
                color : "red"
              }
          }
        }
        catch(error){
          alert("Pesan Material Failed")
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Pesan Material Gagal",
            color : "red"
          }
        }
      },

      async InsertMaterial2(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/add_purchaseItem',
            { supplierCode: this.supply,
              materialTypeCode: this.type,
              quantity: this.quantity,
              unit: this.unit,
              purchaseId: this.id
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
              this.snackbar = {
                show : true,
                message : "Pesan Material Berhasil",
                color : "green"
          }}
          else if(response.data.status == "gagal"){
              this.snackbar = {
                show : true,
                message : "Pesan Material Gagal",
                color : "red"
              }
          }
        }
        catch(error){
          alert("Pesan Material Failed")
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