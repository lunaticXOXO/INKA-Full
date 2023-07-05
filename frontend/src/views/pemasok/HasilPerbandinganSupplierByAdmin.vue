<template>
    <v-app>


      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> Hasil Perbandingan Supplier </h1>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "hasilperbandingan"
            :items-per-page="5"
            >
            <template v-slot:[`item.IDKriteria`]="{ item }">
              <div v-if="item.IDKriteria === editedItem.IDKriteria">
                  <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDKriteria == editedItem.IDKriteria"></v-text-field>
                  <span v-else>{{item.IDKriteria}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.IDKriteria" :hide-details="true" dense single-line :autofocus="true" v-if="item.IDKriteria == editedItem.IDKriteria"></v-text-field>
                  <span v-else>{{item.IDKriteria}}</span>
              </div>
            </template>
  
            <template v-slot:[`item.IDSupplier01`]="{ item }">
              <v-text-field v-model="editedItem.IDSupplier01" :hide-details="true" dense single-line v-if="item.IDKriteria == editedItem.IDKriteria" ></v-text-field>
              <span v-else>{{item.IDSupplier01}}</span>
            </template>
  
            <template v-slot:[`item.IDSupplier02`]="{ item }">
              <v-text-field v-model="editedItem.IDSupplier02" :hide-details="true" dense single-line v-if="item.IDKriteria == editedItem.IDKriteria" ></v-text-field>
              <span v-else>{{item.IDSupplier02}}</span>
            </template>
            
            <template v-slot:[`item.Nilai`]="{ item }">
              <v-text-field v-model="editedItem.Nilai" :hide-details="true" dense single-line v-if="item.IDKriteria == editedItem.IDKriteria" ></v-text-field>
              <span v-else>{{item.Nilai}}</span>
            </template>

            <template v-slot:[`item.Nilai02`]="{ item }">
              <v-text-field v-model="editedItem.Nilai02" :hide-details="true" dense single-line v-if="item.IDKriteria == editedItem.IDKriteria" ></v-text-field>
              <span v-else>{{item.Nilai02}}</span>
            </template>
            
            <template v-slot:[`item.idPenghitung`]="{ item }">
              <v-text-field v-model="editedItem.idPenghitung" :hide-details="true" dense single-line v-if="item.IDKriteria == editedItem.IDKriteria" ></v-text-field>
              <span v-else>{{item.idPenghitung}}</span>
           </template>

          </v-data-table>
       
            <v-btn 
                    class="mx-auto text-center mb-5" 
                    color="green"
                v-bind="attrs"
                v-on="on"
                @click="validate()"
                >
                Bobot & Peringkat
            </v-btn>
      
                
                
      </v-card>
    </v-app>
  </template>
  
  <script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'ID Kriteria',                value : 'IDKriteria'},
              {text : 'ID Supplier 01',             value : 'IDSupplier01'},
              {text : 'ID Supplier 02',             value : 'IDSupplier02'},
              {text : 'Nilai',                      value : 'Nilai'},
              {text : 'Nilai 02',                   value : 'Nilai02'},
              {text : 'ID Penghitung',                   value : 'idPenghitung'}
              //{text : 'Action',                     value : 'aksi'}
          ],
          hasilperbandingan : [],
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
  
      validate(){

        location.replace('/hasilBobotPeringkatSupplierAdmin/' + this.$route.params.id)

      },

        editMaterial(types){
          console.log('ID : ' + types.id)
          this.editedIndex = this.types.indexOf(types);
          this.editedItem = Object.assign({},types);
        },
  
        async fetchData(){
          try{
            const axios = require('axios');
            const res = await axios.get('/ahp/hasil_perbandingan/' + this.$route.params.id);
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.hasilperbandingan = res.data
              console.log(res,this.penghitung)
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