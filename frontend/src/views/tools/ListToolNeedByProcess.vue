<template>
    <v-app>

    <v-card class="text-center mt-4 ml-3" max-width="1350">

<v-form
  class="pa-6"
  ref="form"
  @submit.prevent="submitHandler"
  v-model="valid"
  lazy-validation> 

  <v-autocomplete
        item-text="id"
        item-value="id"
        v-model="prosesSesudahnya"
        :items="items"
        label="Tool Type"
        ></v-autocomplete>

  <v-text-field
  v-model="quantity"
  label="Quantity"
  required
  ></v-text-field>

  <v-autocomplete
        item-text="id"
        item-value="id"
        v-model="prosesSesudahnya"
        :items="items"
        label="Unit"
        ></v-autocomplete>



 
 
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

</v-card>
    
      <v-card 
          class="text-center mt-10 ml-4"
          max-width = "1300">
          <br>
          <h2>List Kebutuhan Perkakas Berdasarkan Proses {{this.$route.params.id}}</h2>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "toolNeed"
            :items-per-page="5"
            >
            <template #[`item.toolTypeCode`]="{ item }">
              <div v-if="item.toolTypeCode === editedItem.toolTypeCode">
                  <v-text-field disabled v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                  <span v-else>{{item.toolTypeCode}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                  <span v-else>{{item.toolTypeCode}}</span>
              </div>
            </template>
  
        <template v-slot:[`item.namaTool`]="{ item }">
            <v-text-field v-model="editedItem.namaTool" :hide-details="true" dense single-line v-if="item.toolTypeCode == editedItem.toolTypeCode" ></v-text-field>
            <span v-else>{{item.namaTool}}</span>
          </template>

          <template v-slot:[`item.quantity`]="{ item }">
              <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line v-if="item.toolTypeCode == editedItem.toolTypeCode" ></v-text-field>
              <span v-else>{{item.quantity}}</span>
            </template>
  
          <template v-slot:[`item.processCode`]="{ item }">
            <v-text-field v-model="editedItem.processCode" :hide-details="true" dense single-line v-if="item.toolTypeCode == editedItem.toolTypeCode" ></v-text-field>
            <span v-else>{{item.processCode}}</span>
          </template>

  
            <template v-slot:[`item.namaProses`]="{ item }">
              <v-text-field v-model="editedItem.namaProses" :hide-details="true" dense single-line v-if="item.toolTypeCode == editedItem.toolTypeCode" ></v-text-field>
              <span v-else>{{item.namaProses}}</span>
            </template>
            
          
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
          {text : 'ID Tool Type',               value : 'toolTypeCode'},
          {text : 'Nama Tool',                  value : 'namaTool'},
          {text : 'Quantity',                   value : 'quantity'},
          {text : 'Process Code',               value : 'processCode'},
          {text : 'Nama Proses',                value : 'namaProses'},
         
      ],
     toolNeed : [],
      editedIndex: -1,
      editedItem: {
        id: '',
        nama: '',
        purchaseDate: '',
        purchaserName: '',
      },
      defaultItem: {
        id: '',
        nama: '',
        purchaseDate: '',
        purchaserName: '',
      },
      dueDate: undefined,
      datetime: undefined
    }
  },

  mounted(){
      this.fetchData()
  },

  methods: {
    close () {
      setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem);
          this.editedIndex = -1;
      }, 300)
    },

   
    async fetchData(){
      try{
        const axios = require('axios');
        const res = await axios.get('/tools/show_toolneed_byprocess/' + this.$route.params.id);
        if (res.data == null){
          alert('Material Kosong')
        }else{
          this.toolNeed = res.data
          console.log(res,this.toolNeed)
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
