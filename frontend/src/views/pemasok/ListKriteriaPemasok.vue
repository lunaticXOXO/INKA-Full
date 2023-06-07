<template>
    <v-card
      class="mx-auto text-center mt-6"
      max-width="1000">
      <br>
      <h1>Kriteria Pemasok</h1>
      <br>
      <v-card
        class="mx-auto text-center"
        max-width="1000">

        <router-link to="/tambahKriteria">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Kriteria
            </v-btn>
        </router-link>
          <v-data-table
            :headers = "headers"
            :items = "kriteriaSupplier"
            :items-row-page = 5> 


            <template v-slot:[`item.IdKriteria`]="{ item }">
              <div v-if="item.IdKriteria === editedItem.IdKriteria">
                  <v-text-field disabled v-model="editedItem.IdKriteria" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria == editedItem.IdKriteria"></v-text-field>
                  <span v-else>{{item.IdKriteria}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.IdKriteria" :hide-details="true" dense single-line :autofocus="true" v-if="item.IdKriteria == editedItem.IdKriteria"></v-text-field>
                  <span v-else>{{item.IdKriteria}}</span>
              </div>
            </template>

            <template v-slot:[`item.namaKriteria`]="{ item }">
                <v-text-field v-model="editedItem.namaKriteria" :hide-details="true" dense single-line v-if="item.IdKriteria == editedItem.IdKriteria" ></v-text-field>
                <span v-else>{{item.namaKriteria}}</span>
            </template>

            <template v-slot:[`item.mulai`]="{ item }">
                <v-text-field v-model="editedItem.mulai" :hide-details="true" dense single-line v-if="item.IdKriteria == editedItem.IdKriteria" ></v-text-field>
                <span v-else>{{item.mulai}}</span>
            </template>
            <template v-slot:[`item.selesai`]="{ item }">
                <v-text-field v-model="editedItem.selesai" :hide-details="true" dense single-line v-if="item.IdKriteria == editedItem.IdKriteria" ></v-text-field>
                <span v-else>{{item.selesai}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.IdKriteria == editedItem.IdKriteria">
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
                      @click="editSupplier(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-pencil</v-icon>
                    </v-btn>
                  </template>
                  <span>Edit</span>
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
          {text : 'ID Kriteria',                value : 'IdKriteria'},
          {text : 'Nama Kriteria',              value : 'namaKriteria'},
          {text : 'Mulai',                      value : 'mulai'},
          {text : 'Selesai',                    value : 'selesai'},
          {text : 'Aksi', value : 'aksi'}
         
        ],
        kriteriaSupplier :[],
        
        editedIndex : -1,
        editedItem : {
          id : '',
          nama : '',
          customerid : ''
        },
  
        defaultItem : {
          id : 'New ID',
          nama : 'New Nama',
          customerid : 'New Customer'
         },
         'id' : '',
         'nama' : '',
         'customerid' : ''
      }),
  
      mounted(){
          this.fetchData()
        
      },
  
      methods: {
        async fetchData(){
          try{
            const res = await axios.get(`/supplier/get_kriteria_supplier`);
            if(res.data == null){
                alert("Proyek Kosong")
            }else{
                this.kriteriaSupplier = res.data;
                console.log(res,this.kriteriaSupplier)
            }
          } 
          catch(error){
              alert("Error")
              console.log(error)
          }
        },
  
       
  
       
        selectProyek(proyek){ 
          console.log(proyek.id)
          //open(`/listRProyekbyProyek/${proyek.id}`)
        },
  
        close(){
          setTimeout(()=>{
            this.editedItem = Object.assign({},this.defaultItem)
            this.editedIndex = -1;
  
          },300)
        },
  
        updateProyek(proyek){
          console.log(proyek.id)
          this.editedIndex = this.proyek.indexOf(proyek)
          this.editedItem = Object.assign({},proyek)
        },
  
        deleteProyek(proyek){
          console.log(proyek.id)
        }
      }
    }
  </script>