<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Material Type by {{this.$route.params.id}}</h1>
        <br>
        <router-link :to="{name : 'Tambah Material Type by Pemasok', params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Material Type 
            </v-btn>
        </router-link>

        <v-data-table 
            :headers = "column"
            :items = "materialbysupplier">
        </v-data-table>
    </v-card>
</template>


<script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'Code',                   value : 'code'},
              {text : 'Nama Supplier',          value : 'nama'},
              {text : 'Code Tipe Material',     value : 'materialTypeCode'},
              {text : 'Nama Tipe Material',     value : 'namaMaterialType'},
             
          ],
            
          materialbysupplier : []
        }
      },
  
      mounted(){
        this.fetchMaterialBySupplier()
      },
  
      methods: {
        close () {
          setTimeout(() => {
              this.editedItem = Object.assign({}, this.defaultItem);
              this.editedIndex = -1;
          }, 300)
        },
  
        async fetchMaterialBySupplier(){
          try{
            const axios = require('axios');
            const res = await axios.get('/supplier/get_materialtype_bysupplier/' + this.$route.params.id);
            if (res.data == null){
              alert('Customer Kosong')
            }else{
              this.materialbysupplier = res.data
              console.log(res,this.materialbysupplier)
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
