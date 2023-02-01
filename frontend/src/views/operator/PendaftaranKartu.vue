<template>
    <v-card 
        class="mt-10 text-center mx-auto"
        max-width = "1450">
        <br>
        <h1>List Operator</h1>
        <br>

        <v-data-table 
            :headers = "column"
            :items = "operators">
            <template v-slot:[`item.code`]="{ item }">
              <div v-if="item.code === editedItem.code">
                  <v-text-field disabled v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
            </template>
            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>
            <template v-slot:[`item.email`]="{ item }">
                <v-text-field v-model="editedItem.email" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.email}}</span>
            </template>
            <template v-slot:[`item.adress1`]="{ item }">
                <v-text-field v-model="editedItem.adress1" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.adress1}}</span>
            </template>

          <template v-slot:[`item.city`]="{ item }">
              <v-select v-model="editedItem.city" item-text="nama" item-value="code" :items="cities" v-if="item.code == editedItem.code"></v-select>
              <span v-else>{{item.city}}</span>
          </template>

            <template v-slot:[`item.phone`]="{ item }">
                <v-text-field v-model="editedItem.phone" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.phone}}</span>
            </template>

            <template v-slot:[`item.postalcode`]="{ item }">
                <v-text-field v-model="editedItem.postalcode" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.postalcode}}</span>
            </template>
            <template v-slot:[`item.aksi`]="{ item }">
              <div>
                <router-link :to="{name : 'Form Daftar RFID',params:{id : `${item.code}`}}">
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
                    <span>Pendaftaran RFID</span>
                  </v-tooltip>
                </router-link>
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
            {text : 'Code',         value : 'code'},
            {text : 'Nama',         value : 'nama'},
            {text : 'Email',        value : 'email'},
            {text : 'Alamat',     value : 'adress1'},
            {text : 'Kota',         value : 'city'},
            {text : 'Phone',        value : 'phone'},
            {text : 'Kode Pos',     value : 'postalcode'},
            {text : 'Action',       value : 'aksi'}
        ],
        operators : [],
        editedIndex: -1,
        editedItem: {
          code: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
        defaultItem: {
          code: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
      }
    },

    mounted(){
        this.fetchOperator()
    },

    methods: {
      async fetchOperator(){
        try{
          const axios = require('axios');
          const res = await axios.get('/operator/get_operator');
          if (res.data == null){
            alert('Operator Kosong')
          }else{
            this.operators = res.data
            console.log(res,this.operators)
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