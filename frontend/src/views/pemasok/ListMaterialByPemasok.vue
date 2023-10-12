<template>
    <v-card 
        class="mx-auto text-center mx-10"
        max-width = "1450">

        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
               DAFTAR JENIS MATERIAL PEMASOK {{ this.$route.params.id }}
        </v-card-title>

        </v-card>
        <br>

        <router-link :to="{name : 'Tambah Material Type By Pemasok', params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Material Type 
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "materialbysupplier">
        </v-data-table>

        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="50"
        >
      
        </v-card>

    </v-card>
</template>

<script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'Supplier', value : 'code'},
              {text : 'Nama Supplier', value : 'namaSupplier'},
              {text : 'Code',     value : 'materialTypeCode'},
              {text : 'Nama',     value : 'namaMaterialType'},
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
