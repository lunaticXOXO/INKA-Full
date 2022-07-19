<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Material Kosong</h1>
        <h1>{{this.$route.params.id}}</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-banner></v-banner>
            <v-banner>
                Minimum Quantity: {{quantity}}
            </v-banner>

            <v-text-field
            v-model="quantity2"
            :rules="quanRules"
            label="New Quantity"
            type="number"
            required
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
      quantity: null,
      quantity2: null,
      quanRules: [
        v => !!v || 'Quantity is required',
        v => v >= 10 || 'Quantity must be 1 or more'
      ],
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
      validate(){
        if(this.$refs.form.validate()){
            console.log(this.quantity2)
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
            const res = await axios.get('/material/min_quantity/' + this.$route.params.id)
            if (res.data == null){
                alert("Quantity Kosong")
            }else{
                this.quantity = res.data[0].jumlah
                console.log(res)
                console.log(this.quantity)
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