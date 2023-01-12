<template>
  <v-card 
    class="mx-auto text-center mt-10"
    max-width = "1450">
    <br>
    <h1>List Operasi By Produk {{this.$route.params.id}}</h1>
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
  </v-card>
</template>

<script>
  export default {
    data(){
      return {
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
            console.log(res,this.operation)
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