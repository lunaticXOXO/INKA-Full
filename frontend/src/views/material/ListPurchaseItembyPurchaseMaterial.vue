<template>
  <v-app>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
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
            :items = "prcItembyprcMat"
            :items-per-page="5">
            <template v-slot:[`item.aksi`]="{ item }">
                <!--
                <router-link :to="{name : 'List Stock Material By Orders',params : {id : `${item.id_item}`}}">
                  <v-btn class="mx-1" x-small color="blue">
                      <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                </router-link>
                -->
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editMaterial(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-pencil</v-icon>
                    </v-btn>
                  </template>
                  <span>Edit</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="red"
                      @click="deleteMaterial(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-trash-can-outline</v-icon>
                    </v-btn>
                  </template>
                  <span>Delete</span>
                </v-tooltip>
            </template>
        </v-data-table>
    </v-card>
    
    <v-card
      class="mx-auto text-center mt-10"
        max-width = "1000">
      <h2>Detail Purchase Material</h2>
      <v-data-table 
          :headers="column2"
          :items="purchasematerial">
        </v-data-table>
    </v-card>

    
  </v-app>
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
              {text : 'Unit',               value : 'namaUnit'},
              {text : 'Action',           value : 'aksi'}
          ],
          column2 : [
            {text : 'ID',               value : 'id'},
            {text : 'Nama',             value : 'nama'},
            {text : 'Purchase Date',    value : 'purchaseDate'},
            {text : 'Purchaser Name',   value : 'purchaserName'},
          ],
          column3 : [
            {text : 'Material Code',    value : 'codeMaterial'},
            {text : 'Nama Material',    value : 'namaMaterial'},
            {text : 'Jumlah',           value : 'jumlah'}
        ],
          prcItembyprcMat : [],
          requirmentMaterial : [],
          purchasematerial : [],
          dueDate: undefined
        }
      },
  
      mounted(){
        this.fetchPrcItemByPrcMat(),
        this.fetchPurchaseMaterialInItem()
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

        async fetchPurchaseMaterialInItem(){
          try{
            const axios = require('axios');
            const res = await axios.get('/material/get_purchasematerial_in_purchaseitem/' + this.$route.params.id);
            if (res.data == null){
              alert('Purchase Item Kosong')
            }else{
              this.purchasematerial = res.data
              console.log(res,this.prcItembyprcMat)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
        
        async showRequirementPurchaseMaterial(){
          try{
            console.log(this.dueDate + " " + this.datetime)
            const axios = require('axios');
            const res = await axios.get('/material/get_requirement_purchase_material/' + this.dueDate);
            if (res.data == null){
              alert('Data Kosong')
            }else{
              this.requirmentMaterial = res.data
              console.log(res,this.requirmentMaterial)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        }
      }
    }
  </script>
