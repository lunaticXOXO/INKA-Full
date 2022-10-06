<template>
    <v-card  class="mx-auto text-center mt-6"
      max-width="1000">
        <br>
        <h1>Tambah Material Type By Pemasok</h1>
        <v-form
         class="pa-6"
          ref="form"
          v-model="valid"
          @submit.prevent="submitHandler"
          lazy-validation
        >
          <v-autocomplete
          item-text="nama"
          item-value="code"
          v-model="materialTypeCode"
          :items="items"
          label="Material Type"
          ></v-autocomplete>

          <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          type="submit"
          @click="addMaterialbySupplier()"
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
        data : () => ({
            valid: true,
            snackbar: {
                show: false,
                message: null,
                color: null
            },
            materialTypeCode : null,
            items : []
        }),

        mounted(){
            this.fetchData()
        },
            
        methods: {
            async fetchData(){
                try{
                    const axios = require('axios');
                    const res = await axios.get(`/material/get_type`);
                    console.log(res.data)
                    if(res.data == null){
                        alert("Kota Kosong")
                    }else{
                        this.items = res.data
                    }
                } 
                catch(error){
                    alert("Error")
                    console.log(error)
                }
            },

            async addMaterialbySupplier(){
                const axios = require('axios')
                const res = await axios.post('/supplier/add_materialtype_bysupplier/' + this.$route.params.id,{
                    materialTypeCode : this.materialTypeCode
                })
                console.log(res)
        
                if(res.data.status == "berhasil"){
                    this.snackbar = {
                        message : "Insert Data Pemasok Success",
                        color : 'green',
                        show : true
                    }
                    location.replace('/listMaterialTypeBySupplier/' + this.$route.params.id)
                }
                else if(res.data.status == "gagal"){
                    this.snackbar = {
                        message : "Insert Data Pemasok Gagal, Code Sudah Tersedia!",
                        color : 'red',
                        show : true
                    }
                }
            }
        }
    }
</script>