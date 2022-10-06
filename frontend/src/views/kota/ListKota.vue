<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Kota</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "kota">
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
                <template v-slot:[`item.country`]="{ item }">
                    <v-select v-model="editedItem.country" item-text="nama" item-value="code" :items="negara" v-if="item.code == editedItem.code"></v-select>
                    <span v-else>{{item.country}}</span>
                </template>
                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.code == editedItem.code">
                        <v-icon color="red" class="mr-3" @click="close">
                        mdi-window-close
                        </v-icon>
                        <v-icon color="green"  @click="updateData()">
                        mdi-content-save
                        </v-icon>
                    </div>
                    <div v-else>
                        <v-btn class="mx-1" x-small color="green" @click="editKota(item)">
                            <v-icon small dark>mdi-pencil</v-icon>
                        </v-btn>
                        <v-btn class="mx-1" x-small color="red" @click="deleteKota(item)">
                            <v-icon small dark>mdi-trash-can-outline</v-icon>
                        </v-btn>
                    </div>
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
        {text : 'Kode', value : 'code'},
        {text : 'Nama', value : 'nama'},
        {text : 'Negara', value : 'country'},
        {text : 'Action', value : 'aksi'}
      ],
      kota:[],
      negara:[],
      editedIndex: -1,
      editedItem: {
        code: '',
        nama: '',
        country: ''
      },
      defaultItem: {
        code: '',
        nama: '',
        country: ''
      }
    }),

    mounted(){
        this.fetchData(),
        this.fetchDataNegara()
    },

    methods: {
        close () {
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        editKota(kota){
            console.log('Kode : ' + kota.code)
            this.editedIndex = this.kota.indexOf(kota);
            this.editedItem = Object.assign({}, kota);
        },

        deleteKota(kota){
            console.log('Deleted City : ' + kota.code)
            try{
                const axios = require('axios');
                axios.delete(`/kota/deleteKota/${kota.code}`);
                alert("Delete Kota Success!")
                this.fetchData()
            }
            catch(error){
                console.log(error)
            }
        },

        async fetchData(){
            try{
                const res = await axios.get(`/city/get_allcities`);
                if(res.data == null){
                    alert("Kota Kosong")
                }else{
                    this.kota = res.data;
                    console.log(res, this.kota)
                }
            }catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async fetchDataNegara(){
            try{
                const res = await axios.get(`/countries/get_allcountries`);
                if(res.data == null){
                    alert("Negara Kosong")
                }else{
                    this.negara = res.data;
                    console.log(res,this.data)
                }
            } 
            catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async updateData(){
            if (this.editedIndex > -1) {
                Object.assign(this.kota[this.editedIndex], this.editedItem)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/city/update_city/'+ this.editedItem.code,
                { code : this.editedItem.code,
                  nama : this.editedItem.nama,
                  country : this.editedItem.country 
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        }
    }
  }
</script>