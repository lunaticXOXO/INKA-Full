<template>
    <v-app>
      <v-card 
          class="mt-10 ml-5"
          max-width = "1300">
          <br>
          <h2 class="mx-auto text-center">Daftar Pengembalian Perkakas</h2>
          <br>
        
          <div class="d-flex">
          
          
          <v-text-field
          class="custom-v-select mx-auto text-center"
        
        
            v-model="uuid"
          label="UUID Operator"
      ></v-text-field>
      </div>
      <v-btn
        :loading="loading"
        color="primary"
        class="d-flex mx-auto mt-10 mb-3"
        @click = "fetcPeminjamanByUUID()"
        >
        Search
      </v-btn>

          <v-data-table 
            :headers = "column"
            :items = "peminjaman"
            :items-per-page="5"
            id="mytable"
            show-select = "true"
            v-model="selected"
            item-key="toolId"
            >
         
            <template v-slot:[`item.aksi`]="{ item }">
             
              <div>
                <router-link :to="{name : 'List Purchase Item By Purchase Tools',params:{id : `${item.toolPurchaseId}`}}">
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn 
                        class="mx-1" 
                        x-small
                        color="blue"
                        v-bind="attrs"
                        v-on="on">
                        <v-icon small dark>mdi-check</v-icon>
                      </v-btn>
                    </template>
                    <span>Accept Pengembalian Perkakas</span>
                  </v-tooltip>
                </router-link>
                
                
                
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
              </div>
            </template>  
          
          </v-data-table>
        
          <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>

      </v-card>
    </v-app>
 </template>
 
 
<script> 
export default {
  data(){
    return {
      valid : true,
      column : [
          {text : 'Box ID',               value : 'boxId'},
          {text : 'Tool Id',       value : 'toolId'},
          {text : 'Operator Id',    value : 'operatorId'},
          {text : 'Tanggal Peminjaman',   value : 'tanggalPinjam'},
          {text : 'Action',           value : 'aksi'}
      ],
      peminjaman : [],
      selected : [],
      mytable : false,
      uuid : '',
    
      snackbar : {
        show : false,
        color : null,
        message : null,
      },
      
    }
  },

  mounted(){
      this.fetcPeminjamanByUUID(),
      this.fetchPeminjamanAll()
  },

  methods: {
    
    async fetcPeminjamanByUUID(){
      try{
        const axios = require('axios');
        const res = await axios.get('/tools/show_pengembalian_perkakas_byuuid',{
            params : {
                uuid : this.uuid
            }
        });
        if (res.data.length == 0){
            this.snackbar = {
                show : true,
                message : "No Search Data",
                color : "red"
            }
        }else{

            window.setTimeout(() => {  
                this.peminjaman = res.data
                console.log(res,this.peminjaman)
            }, 1500)

            
            this.snackbar = {
                show : true,
                message : "Showing Pengembalian",
                color : "green"
            }
        }
      }
      catch(error){
        alert("Error")
        console.log(error)
      }
    },
    
    async fetchPeminjamanAll(){
        try{
        const axios = require('axios');
        const res = await axios.get('/tools/show_pengembalian_perkakas')
        if (res.data == null){
          alert('Material Kosong')
        }else{
          this.peminjaman = res.data
          console.log(res,this.peminjaman)
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
