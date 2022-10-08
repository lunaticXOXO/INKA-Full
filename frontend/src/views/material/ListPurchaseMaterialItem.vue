<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Purchase Material Item</h1>
        <br>
        <router-link to="/purchaseMaterialItem">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Purchase Material Item
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types">
            <template v-slot:[`item.id_item`]="{ item }">
              <div v-if="item.id_item === editedItem.id_item">
                  <v-text-field disabled v-model="editedItem.id_item" :hide-details="true" dense single-line :autofocus="true" v-if="item.id_item === editedItem.id_item"></v-text-field>
                  <span v-else>{{item.id_item}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.id_item" :hide-details="true" dense single-line :autofocus="true" v-if="item.id_item === editedItem.id_item"></v-text-field>
                  <span v-else>{{item.id_item}}</span>
              </div>
            </template>

            <template v-slot:[`item.supplierCode`]="{ item }">
                <v-text-field v-model="editedItem.supplierCode" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.supplierCode}}</span>
            </template>

            <template v-slot:[`item.materialTypeCode`]="{ item }">
                <v-text-field v-model="editedItem.materialTypeCode" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.materialTypeCode}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.unit`]="{ item }">
                <v-text-field v-model="editedItem.unit" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.unit}}</span>
            </template>
           
            <template v-slot:[`item.schedulledArrival`]="{ item }">
                <v-text-field v-model="editedItem.schedulledArrival" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.schedulledArrival}}</span>
            </template>
           
            <template v-slot:[`item.purchaseId`]="{ item }">
                <v-text-field v-model="editedItem.purchaseId" :hide-details="true" dense single-line v-if="item.id_item === editedItem.id_item" ></v-text-field>
                <span v-else>{{item.purchaseId}}</span>
            </template>
           
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.id_item == editedItem.id_item">
                  <v-icon color="red" class="mr-3" @click="close">
                    mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()">
                    mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <v-btn class="mx-1" x-small color="green" @click="editMaterial(item)">
                    <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="mx-1" x-small color="red" @click="deleteMaterial(item)">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>
              </div>
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
            {text : 'ID Item',              value : 'id_item'},
            {text : 'Supplier',             value : 'supplierCode'},
            {text : 'Material Type',        value : 'materialTypeCode'},
            {text : 'Quantity',             value : 'quantity'},
            {text : 'Unit',                 value : 'unit'},
            {text : 'Schedulled Arrival',   value : 'schedulledArrival'},
            {text : 'Purchase ID',          value : 'purchaseId'},
            {text : 'Action',               value : 'aksi'}
        ],
        types : [],
        editedIndex: -1,
        editedItem: {
          id_item: '',
          supplierCode: '',
          materialTypeCode: '',
          quantity: '',
          unit: '',
          schedulledArrival: '',
          purchaseId: '',
        },
        defaultItem: {
          id_item: '',
          supplierCode: '',
          materialTypeCode: '',
          quantity: '',
          unit: '',
          schedulledArrival: '',
          purchaseId: '',
        },
      }
    },
  
    mounted(){
        this.fetchPurchaseMaterialItem()
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editMaterial(types){
        console.log('ID : ' + types.id_item)
        this.editedIndex = this.types.indexOf(types);
        this.editedItem = Object.assign({},types);
      },

      async fetchPurchaseMaterialItem(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_purchase_item');
          if (res.data == null){
            alert('Purchase Material Item Kosong')
          }else{
            this.types = res.data
            console.log(res,this.types)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },
      
      deleteMaterial(types){
          console.log('ID : ' + types.id_item)
          try{
              const axios = require('axios');
              axios.delete(`/material/delete_purchase_material_item/${types.id_item}`);
              alert("Delete Purchase Material Item Success!")
              this.fetchPurchaseMaterialItem()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.types[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/material/update_purchase_material_item/'+ this.editedItem.id_item,
            { id_item           : this.editedItem.id_item,
              supplierCode      : this.editedItem.supplierCode,
              materialTypeCode  : this.editedItem.materialTypeCode,
              quantity          : this.editedItem.quantity,
              unit              : this.editedItem.unit,
              schedulledArrival : this.editedItem.schedulledArrival,
              purchaseId        : this.editedItem.purchaseId,
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>