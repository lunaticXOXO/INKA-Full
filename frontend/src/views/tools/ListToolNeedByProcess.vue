<template>
    <v-app>

    <v-card class="text-center mt-4 ml-3" max-width="1350">

      <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
            >
      <v-card-title class="text-h5">
        TAMBAH KEBUTUHAN PERKAKAS PROSES {{ this.$route.params.id }}
      </v-card-title>
            
      </v-card> 
      <br><br>
<v-form
  class="pa-6"
  ref="form"
  @submit.prevent="submitHandler"
  v-model="valid"
  lazy-validation> 

  <v-autocomplete
      item-text="nama"
      item-value="codes"
      v-model="toolTypeCode"
      :items="tooltype"
      label="Tool Type"
  ></v-autocomplete>

  <v-text-field
  v-model="quantity"
  label="Quantity"
  required
  ></v-text-field>

  <v-autocomplete
        item-text="nama"
        item-value="id"
        v-model="unit"
        :items="units"
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
<v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
  </v-snackbar>
<br>
  <v-card
      color="#6f6f6f"
      dark
      class="px-5 py-3"
      max-height ="50"
    >
  </v-card>

</v-card>
    
      <v-card 
          class="text-center mt-10 ml-4"
          max-width = "1300">
       
          <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
            >
        <v-card-title class="text-h5">
          DAFTAR KEBUTUHAN PERKAKAS PROSES {{ this.$route.params.id }}
          </v-card-title>
            
        </v-card> 
        <br><br>
         
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
     tooltype : [],
     units : [],
     toolTypeCode : '',
     unit : '',
     quantity : '',
      editedIndex: -1,
      editedItem: {
       toolTypeCode: '',
        quantity: '',
        unit : ''
      },
      defaultItem: {
        id: '',
        nama: '',
        purchaseDate: '',
        purchaserName: '',
      },
      dueDate: undefined,
      datetime: undefined,
      snackbar: {
        show: false,
        message: null,
        color: null
      },
    }
  },

  mounted(){
      this.fetchData(),
      this.fetchToolType(),
      this.fetchUnit()
  },

  methods: {
    validate () {
        if(this.$refs.form.validate()){
          this.insertToolNeed()
        }
    },

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

    async insertToolNeed(){
      try{
        const axios = require('axios')
        const res = await axios.post('/tools/add_toolneed_idProcess/' + this.$route.params.id,{
          toolTypeCode : this.toolTypeCode,
          quantity : this.quantity,
          unit : this.unit
        }
        )
        if (res.data.status == "berhasil"){
            console.log('berhasil')
            this.snackbar = {
              message : "Insert Tool By Process Berhasil",
              color : 'green',
              show : true
          }
          
          location.replace('/listToolNeedByProcess/' + this.$route.params.id)
        }
        else if(res.data.status == 'gagal'){
            this.snackbar = {
                message : "Insert Tool Box Gagal",
                color : 'red',
                show : true
           }
        }
      }catch(error){
         console.log(error)
      }
    },

    async fetchToolType(){
       try{
          const axios = require('axios')
          const res = await axios.get('/tools/show_tooltype')
          if(res.data == null){
            console.log("kosong")
          }else{

            this.tooltype = res.data
            console.log(res,this.tooltype)

          }
       }catch(error){
          console.log(error)
       }
    },

    async fetchUnit(){
      try{
        const axios = require('axios')
        const res = await axios.get('/unit/get_unit')
        if(res.data == null){
           console.log("kosong")
        }else{
            this.units = res.data
            console.log(res,this.unit)
        }
      }
      catch(error){
         console.log(error)
      }
    }
    
    
    
  }
}


</script>
