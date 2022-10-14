<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Purchase Item by Purchase Material {{this.$route.params.id}}</h1>
        <br>
        <router-link :to="{name : 'Tambah Purchase Item By Purchase Material', params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Purchase Item 
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "prcItembyprcMat">
        </v-data-table>
    </v-card>
</template>

<script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'ID',                 value : 'id_item'},
              {text : 'Material Type Code', value : 'materialTypeCode'},
              {text : 'Purchase ID',        value : 'purchaseId'},
              {text : 'Quantity',           value : 'quantity'},
              {text : 'Schedulled Arrival', value : 'schedulledArrival'},
              {text : 'Supplier',           value : 'supplierCode'},
              {text : 'Unit',               value : 'unit'},
          ],
          prcItembyprcMat : []
        }
      },
  
      mounted(){
        this.fetchPrcItemByPrcMat()
      },
  
      methods: {
        close () {
          setTimeout(() => {
              this.editedItem = Object.assign({}, this.defaultItem);
              this.editedIndex = -1;
          }, 300)
        },
  
        async fetchPrcItemByPrcMat(){
          try{
            const axios = require('axios');
            const res = await axios.get('/material/get_material_item_by_idpurchase/' + this.$route.params.id);
            if (res.data == null){
              alert('Purchase Item Kosong')
            }else{
              this.prcItembyprcMat = res.data
              console.log(res,this.prcItembyprcMat)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
  
      }
    }
  </script>
