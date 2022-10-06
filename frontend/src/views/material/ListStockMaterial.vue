<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Stok Material</h1>
        <br>
        <router-link to="/pesanMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Stock Material Baru
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types">
            <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
            </template>

            <template v-slot:[`item.purchaseId`]="{ item }">
                <span>{{item.purchaseId}}</span>
            </template>

            <template v-slot:[`item.orders`]="{ item }">
                <span>{{item.orders}}</span>
            </template>

            <template v-slot:[`item.merk`]="{ item }">
                <span>{{item.merk}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
              <span>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.unit`]="{ item }">
              <span>{{item.unit}}</span>
            </template>

            <template v-slot:[`item.arrivalDate`]="{ item }">
              <span>{{item.arrivalDate}}</span>
            </template>
           
            <template v-slot:[`item.aksi`]="{ item }">
                <router-link :to="{name : 'Tambah Material Kosong', params:{id : `${item.id}`}}">
                    <v-btn class="mx-1" x-small color="blue" @click="selectStock(item)">
                        <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                </router-link>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'ID',                   value : 'id'},
            {text : 'Purchase ID',          value : 'purchaseId'},
            {text : 'Order',                value : 'orders'},
            {text : 'Merk',                 value : 'merk'},        
            {text : 'Quantity',             value : 'quantity'},
            {text : 'Unit',                 value : 'unit'},
            {text : 'Arrival Date',         value : 'arrivalDate'},
            {text : 'Action',               value : 'aksi'}
        ],
        types : [],
      }
    },
  
    mounted(){
        this.fetchMaterial()
    },

    methods: {
      async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_material_stock');
          if (res.data == null){
            alert('Stock Kosong')
          }else{
            this.types = res.data
            console.log(res,this.types)
          }
        }
        catch(error){
          console.log(error)
        }
      },
    
      selectStock(types){
          console.log('ID : ' + types.id)
      },
      
    }
  }
</script>