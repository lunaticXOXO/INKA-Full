<template>
  <v-card 
    class="mx-auto text-center mt-10"
    max-width = "1600">
    <v-card
        color="#6f6f6f"
        dark
        class="px-5 py-3"
        max-height ="200"
        >
        <v-card-title class="text-h5">
              TERIMA BATAL OPERASI  PRODUK {{this.$route.params.id}}
          </v-card-title>
      </v-card>
    <br>
    
    <br>
    <v-data-table 
        :headers = "column"
        :items = "operation">
        <template v-slot:[`item.id`]="{ item }">
          <div v-if="item.id === editedItem.id">
            <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
            <span v-else>{{item.id}}</span>
          </div>
          <div v-else>
            <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
            <span v-else>{{item.id}}</span>
          </div>
        </template>

        <template v-slot:[`item.rencanaMulai`]="{ item }">
            <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.rencanaMulai}}</span>
        </template>

        <template v-slot:[`item.rencanaSelesai`]="{ item }">
            <v-text-field v-model="editedItem.purchaseDate" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.rencanaSelesai}}</span>
      </template>

        <template v-slot:[`item.mulai`]="{ item }">
            <v-text-field v-model="editedItem.mulai" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.mulai}}</span>
      </template>

      <template v-slot:[`item.selesai`]="{ item }">
            <v-text-field v-model="editedItem.selesai" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.selesai}}</span>
      </template>

      <template v-slot:[`item.proses`]="{ item }">
            <v-text-field v-model="editedItem.proses" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.proses}}</span>
      </template>

      <template v-slot:[`item.stasiunKerja`]="{ item }">
            <v-text-field v-model="editedItem.stasiunKerja" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.stasiunKerja}}</span>
      </template>

      <template v-slot:[`item.produk`]="{ item }">
            <v-text-field v-model="editedItem.produk" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
            <span v-else>{{item.produk}}</span>
      </template>
    </v-data-table>
    
    <div class="d-flex">
    <v-btn color="primary" class="d-flex ml-4 mb-6"  @click="terimaOperasi()" :disabled="isActive">
      Terima Operasi
    </v-btn>
    <v-btn color="red" class="d-flex ml-4 mb-6" @click="batalOperasi()" :disabled="isActive">
      Batal Operasi
    </v-btn>
  </div>

  <br>
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
        
        isActive : false,
        valid : true,
        column : [
          {text : 'ID',               value : 'id'},
          {text : 'Rencana Mulai',    value : 'rencanaMulai'},
          {text : 'Rencana Selesai',  value : 'rencanaSelesai'},
          {text : 'Mulai',            value : 'mulai'},
          {text : 'Selesai',          value : 'selesai'},
          {text : 'Proses',           value : 'proses'},
          {text : 'Stasiun Kerja',    value : 'stasiunKerja'},
          {text : 'Produk',           value : 'produk'}
        ],
        operation : [],
        produk : undefined,
        editedItem : {},
        defaultItem : {},
      }
    },

    mounted(){
      this.fetchOperasi()
      // window.setInterval(() => {
      //   this.fetchOperasi()
      // }, 1000)
    },

    methods : {
      async fetchOperasi(){
        try{
          const axios = require('axios');
          const res = await axios.get('/operasi/get_operasi_by_product/' + this.$route.params.id);
          if (res.data == null){
            console.log('Operasi Kosong')
          }else{

            this.operation = res.data
            if(res.data[0].confirm == 1){
                
                this.isActive = true
              
            }
            console.log(res,this.operation)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async terimaOperasi(){
        try{
          const axios = require('axios')
          const res = await axios.post('/rproyek/accept_operasi')
          if(res.data.status == "berhasil"){
            console.log("Penerimaan operasi berhasil")
            this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Berhasil",
              color : "green"
            }
            
            setTimeout(() => {
              location.replace('/listOperasiByProduk/' + this.$route.params.id)
            }, 1000)
            console.log("terima operasi")
          }
          else if(res.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Gagal",
              color : "red"
            }
            
          }
        }catch(error){
          this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Error",
              color : "red"
            }
            console.log("")
        }
      },
      async batalOperasi(){
        try{
          const axios = require('axios')
          const res = await axios.delete('/rproyek/decline_operasi')
          if(res.data.status == "berhasil"){
            console.log("Penerimaan operasi berhasil")
            this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Berhasil",
              color : "green"
            }
            console.log("batal operasi")
            
          }
          else if(res.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Gagal",
              color : "red"
            }
            console.log("disable button")
            
          }

           
        setTimeout(() => {
          location.replace('/lihatProyek')
            }, 1000)
        }
        
        catch(error){
          this.snackbar = {
              show : true,
              message : "Penerimaan Operasi Error",
              color : "red"
            }
            console.log("")
        }
      }
    }

  }
</script>