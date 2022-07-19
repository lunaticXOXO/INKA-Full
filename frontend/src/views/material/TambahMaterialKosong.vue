<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Material Kosong</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >

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
      quantity: '',
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.fetchQuantity()
    },
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.UpdateStock()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.quantity)
      },  

      async fetchQuantity(){
        try{
            const axios = require('axios')
            const res = await axios.get('/supplier/get_supplier')
            if (res.data == null){
                alert("Quantity Kosong")
            }else{
                this.quantity = res.data
                console.log(res,this.supplier)
            }
        }catch(error){
            alert(error)
            console.log(error)
        }
      },

      async UpdateStock(){
        try{
          const axios = require('axios');
          const response = await axios.post('/material/purchase_material',
            { id: this.id,
              nama: this.nama,
              purchaserName: this.purchaser,
              id_item: this.id_item,
              supplierCode: this.supply,
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
              message : "Tambah Stok Berhasil",
              color : "green"
            }
          }
          else if(response.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Tambah Stok Gagal",
              color : "red"
            }
          }
        }
        catch(error){
          console.log(error)
          this.snackbar = {
            show : true,
            message : "Tambah Stok Gagal",
            color : "red"
          }
        }
      },
    },
  }
</script>