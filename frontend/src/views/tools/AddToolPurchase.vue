<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Tambah Tool Purchase</h1>
      <v-form
        class="pa-6"
        ref="form"
        @submit.prevent="submitHandler"
        v-model="valid"
        lazy-validation>
        
        <v-text-field
        v-model="orderName"
        label="Order Name"
        required
        ></v-text-field>

        <v-text-field
        v-model="purchaserName"
        label="Purchaser Name"
        required
        ></v-text-field>
  
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
  import axios from 'axios'
  export default {
    data: () => ({
      valid: true,  
      snackbar: {
        show: false,
        message: null,
        color: null
      },
      orderName: '',
      purchaserName: '',
    }),
  
    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertToolPurchase()
        }
      },
  
      async InsertToolPurchase(){
        try{
          const response = await axios.post('/tools/add_tool_purchase',
            { orderName: this.orderName,
              purchaserName: this.purchaserName
            }
          );
          console.log(response,this.data)
          if(response.data.status == "berhasil"){
              this.snackbar = {
              message : "Insert Tool Purchase Success",
              color : 'green',
              show : true
          }
          
          location.replace('/listPurchaseTools')
        }
          else if(response.data.status == "gagal"){
              this.snackbar = {
              message : "Insert Tool Purchase Gagal",
              color : 'red',
              show : true
          }}
        }
        catch(error){
          this.snackbar = {
            message : "Insert Tool Purchase Error",
            color : 'error',
            show : true
          }
          console.log(error)
        }
      },
    }
  }
  </script>