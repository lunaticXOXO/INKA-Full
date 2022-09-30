<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Pilih Proyek untuk Melihat Status Pengerjaan</h1>
      <br>
      <v-card
        class="mx-auto text-center"
        max-width="1000">
          <v-data-table
            :headers = "headers"
            :items = "proyek"> 
              <template v-slot:[`item.aksi`]="{ item }">
                <router-link :to="{name: 'List Rincian Proyek by Proyek DSP', params: {id : `${item.id}`}}">
                  <v-btn class="mx-1" x-small color="blue" >
                    <v-icon small dark>mdi-check</v-icon>
                  </v-btn>
                </router-link>
              </template>
              <template v-slot:[`item.id`]="{ item }">
                  <span>{{item.id}}</span>
              </template>
              <template v-slot:[`item.nama`]="{ item }">
                  <span>{{item.nama}}</span>
              </template>
              <template v-slot:[`item.customerid`]="{ item }">
                  <span>{{item.customerid}}</span>
              </template>
              <template v-slot:[`item.percentage`]="{ item }">
                  <span>{{item.percentage}}%</span>
              </template>
          </v-data-table>
        </v-card>
    </v-card>
</template>

<script>
  import axios from 'axios'
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'Action',           value : 'aksi'},     
        {text : 'ID',               value : 'id'},
        {text : 'Nama',             value : 'nama'},
        {text : 'Customer ID',      value : 'customerid'},
        {text : 'Progress',         value : 'percentage'},
      ],
      proyek:[],
      customer:[],
    }),

    mounted(){
        this.fetchData(),
        this.fetchCustomer()
    },

    methods: {
      async fetchData(){
        try{
          const res = await axios.get(`/proyek/get_allproyek`);
          if(res.data == null){
              alert("Proyek Kosong")
          }else{
              this.proyek = res.data;
              console.log(res,this.data)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async fetchCustomer(){
        try{
          const res = await axios.get('/customers/get_customers');
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.customer = res.data
            console.log(res,this.customer)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      selectProyek(proyek){ 
        console.log(proyek.id)
      }
    }
  }
</script>