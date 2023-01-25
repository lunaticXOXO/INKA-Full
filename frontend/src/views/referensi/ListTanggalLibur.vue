<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Tanggal Libur</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "tglLibur">
                <template v-slot:[`item.tanggal`]="{ item }">
                    <div v-if="item.tanggal === editedItem.tanggal">
                        <v-text-field disabled v-model="editedItem.tanggal" :hide-details="true" dense single-line :autofocus="true" v-if="item.tanggal == editedItem.tanggal"></v-text-field>
                        <span v-else>{{item.tanggal}}</span>
                    </div>
                    <div v-else>
                        <v-text-field v-model="editedItem.tanggal" :hide-details="true" dense single-line :autofocus="true" v-if="item.tanggal == editedItem.tanggal"></v-text-field>
                        <span v-else>{{item.tanggal}}</span>
                    </div>
                </template>
                <template v-slot:[`item.deskripsi`]="{ item }">
                    <v-text-field v-model="editedItem.deskripsi" :hide-details="true" dense single-line v-if="item.tanggal == editedItem.tanggal" ></v-text-field>
                    <span v-else>{{item.deskripsi}}</span>
                </template>
               
                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.tanggal == editedItem.tanggal">
                        <v-icon color="red" class="mr-3" @click="close">
                        mdi-window-close
                        </v-icon>
                        <v-icon color="green" @click="updateData()">
                        mdi-content-save
                        </v-icon>
                    </div>
                    <div v-else>
                        <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn 
                                class="mx-1" 
                                x-small
                                color="green"
                                @click="editTglLibur(item)"
                                v-bind="attrs"
                                v-on="on">
                                <v-icon small dark>mdi-pencil</v-icon>
                                </v-btn>
                            </template>
                            <span>Edit</span>
                        </v-tooltip>

                        <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn 
                                class="mx-1" 
                                x-small
                                color="red"
                                @click="deleteTglLibur(item)"
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
        </v-card>
    </v-card>
</template>

<script>
import axios from 'axios'
export default {    
    data: () => ({
      valid: true,
      headers:[
        {text : 'Tanggal', value : 'hariLibur'},
        {text : 'Deskripsi', value : 'deskripsi'},
        {text : 'Action', value : 'aksi'}  
      ],
      tglLibur:[],
      editedIndex: -1,
      editedItem: {
        tanggal: '',
        deskripsi: ''
      },
      defaultItem: {
        tanggal: '',
        deskripsi: ''
      }
    }),

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

        editTglLibur(tglLibur){
            console.log('Tanggal Libur : ' + tglLibur.code)
            this.editedIndex = this.kota.indexOf(tglLibur);
            this.editedItem = Object.assign({}, tglLibur);
        },

        deleteTglLibur(tglLibur){
            console.log('Deleted Date : ' + tglLibur.code)
            try{
                const axios = require('axios');
                axios.delete(`/holiday/delete_holiday/${tglLibur.code}`);
                alert("Delete Tanggal Libur Success!")
                this.fetchData()
            }
            catch(error){
                console.log(error)
            }
        },

        async fetchData(){
            try{
                const res = await axios.get(`/holiday/get_all_holiday`);
                if(res.data == null){
                    alert("Kota Kosong")
                }else{
                    this.tglLibur = res.data;
                    console.log(res, this.kota)
                }
            }catch(error){
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