<template>
  <v-app>
    <v-card
      class="mx-auto text-center mt-10"
      width = "1450">
        <br>
        <h1>Purchase Material Item for {{this.$route.params.id}}</h1>
        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="type"
          :items="materialType"
          label="Material Type"
          @change="updateSupplier()"
          ></v-autocomplete>

          <v-autocomplete
          item-text="namaSupplier"
          item-value="code"
          v-model="supply"
          :items="supplier"
          label="Supplier"
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
            <v-date-picker width="500" v-model="tanggalPurchase"></v-date-picker>
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
      
    <v-card 
        class="mx-auto text-center mt-10 pa-6 mb-10"
        max-width = "1450">
        <br>
        <div class="d-flex">
            <v-menu class="ml-4 mt-6">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker width="250" v-model="dueDate"></v-date-picker>
          </v-menu>
          <v-menu class="ml-4 mt-6">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="datetime" v-bind="attrs" v-on="on" label="Due Time" prepend-icon="mdi-clock"></v-text-field>
            </template>
            <v-time-picker v-model="datetime"></v-time-picker>
          </v-menu>
        </div>
        <br>
        <v-btn
          :loading="loading"
          color="primary"
          class="d-flex mx-auto"
          @click="showRequirementPurchaseMaterial()"
          >
          Search
        </v-btn>
        <br><br>
        <v-data-table
          :headers = "column3"
          :items = "requirmentMaterial">
      </v-data-table>
    </v-card>
  </v-app>
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
      materialType: [],
      unit: '',
      units: undefined,
      quantity: '',
      tanggalPurchase : null,
      dueDate : '',
      datetime : '',
      fullDate : '',
      loading : false,
      snackbar : {
        show : false,
        color : null,
        message : null,
      },
      requirmentMaterial : [],
      column3 : [
        {text : 'Material Code',    value : 'code'},
        {text : 'Nama Material',    value : 'nama'},
        {text : 'Jumlah',           value : 'jumlah'}
      ],
    }),

    mounted(){
      this.fetchMaterialTypeName(),
      this.fetchUnit(),
      this.showMaterialBatas()
      //this.showRequirementPurchaseMaterial()
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

      async updateSupplier() {
        try{
          const axios = require('axios')
          const res = await axios.get('/supplier_material/show_materialtype_supplier/' + this.type)
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

      async fetchMaterialTypeName(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier_material/show_material_type_name')
            if (res.data == null){
                alert("Material Type Kosong")
            }else{
                this.materialType = res.data
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

            location.replace('/listPurchaseItemByPurchaseMaterial/' + this.$route.params.id)
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

      async showRequirementPurchaseMaterial(){
        this.loading = true
          try{
            console.log(this.dueDate + " " + this.datetime)
            const axios = require('axios');
            this.fullDate = this.dueDate + " " + this.datetime
            console.log("Full Date : ",this.fullDate)
            const res = await axios.post('/material/add_batas_material_requirement',{fullDate : this.fullDate})
            setTimeout(() => {
              if (res.data.status == "berhasil"){
                this.snackbar = {
                  show : true,
                  message : "Pencarian Kebutuhan Material Berhasil",
                  color : "green"
                }
                const res2 = axios.get('/material/show_material_requirement')
                if(res2.data == null){
                  console.log("")
                }
                else{
                  this.requirmentMaterial = res2.data
                  console.log(res2,this.requirmentMaterial)
                }
                this.loading = false
              }else if(res.data.status == "gagal"){
                this.snackbar = {
                  show : true,
                  message : "Pencarian Kebutuhan Material Gagal",
                  color : "red"
                }
                console.log("Gagal")
                this.loading = false
              }
            }, 2000)
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        
      },

        async showMaterialBatas(){
            try{
              const axios = require('axios');
              const res3 = await axios.get('/material/show_material_requirement')
              if(res3.data == null){
                  console.log("material kosong")
                }
                else{
                    this.requirmentMaterial = res3.data
                    console.log(res3,this.requirmentMaterial)
                }
            }catch(error){
              console.log("error")
            }
        }
    },
  }


</script>