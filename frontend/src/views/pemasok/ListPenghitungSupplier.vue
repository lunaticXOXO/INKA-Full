<template>
    <v-app>

        <v-card class="text-center mt-4 ml-3" max-width="1200">
    
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>

      <v-text-field
      v-model="idPenghitung"
      label="ID Penghitung"
      required
      ></v-text-field>

      <v-text-field
      v-model="namaPenghitung"
      label="Nama Penghitung"
      required
      ></v-text-field>
    

      <div class="d-flex">
        <v-menu 
          class="mt-6"
          transition="scale-transition"
          offset-y
          max-width="290px"
          min-width="290px"
        >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field class="mx-10" :value="tglPenghitung" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
        </template>
        <v-date-picker full-width v-model="tglPenghitung"></v-date-picker>
      </v-menu>
      
    </div>
     
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
</v-card>

      <v-card 
          class="text-center mt-10 ml-3"
          max-width = "1200">
          <br>
          <h1> List Penghitung Matriks Kriteria</h1>
          <br>
         
          <v-data-table 
            :headers = "column"
            :items = "penghitung"
            :items-per-page="5"
            >
            <template v-slot:[`item.idPenghitung`]="{ item }">
              <div v-if="item.idPenghitung === editedItem.idPenghitung">
                  <v-text-field disabled v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.idPenghitung == editedItem.idPenghitung"></v-text-field>
                  <span v-else>{{item.idPenghtiung}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.idPenghitung" :hide-details="true" dense single-line :autofocus="true" v-if="item.idPenghitung == editedItem.idPenghitung"></v-text-field>
                  <span v-else>{{item.idPenghitung}}</span>
              </div>
            </template>
  
            <template v-slot:[`item.namaPenghitung`]="{ item }">
              <v-text-field v-model="editedItem.namaPenghitung" :hide-details="true" dense single-line v-if="item.idPenghitung == editedItem.idPenghitung" ></v-text-field>
              <span v-else>{{item.namaPenghitung}}</span>
            </template>
  
            <template v-slot:[`item.tglPenghitung`]="{ item }">
              <v-text-field v-model="editedItem.tglPenghitung" :hide-details="true" dense single-line v-if="item.idPenghitung == editedItem.idPenghitung" ></v-text-field>
              <span v-else>{{item.tglPenghitung}}</span>
            </template>
  
            
            
            <template v-slot:[`item.aksi`]="{ item }">
            <div v-if="item.idPenghitung == editedItem.idPenghitung">
              <v-icon color="red" class="mr-3" @click="close">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="updateData()">
                mdi-content-save
              </v-icon>
            </div>
            <div v-else>
              <router-link :to="{name : 'Perhitungan Kriteria',params:{id : `${item.idPenghitung}`}}">
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
                  <span>List Perhitungan Matriks Kriteria</span>
                </v-tooltip>
              </router-link>

              <router-link :to="{name : 'Perhitungan Supplier',params:{id : `${item.idPenghitung}`}}">
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                  </template>
                  <span>List Perhitungan Matriks Supplier</span>
                </v-tooltip>
              </router-link>
              
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn 
                    class="mx-1" 
                    x-small
                    color="green"
                    @click="editMaterial(item)"
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
      </v-card>
    </v-app>
  </template>
  
  <script>
    export default {
      data(){
        return {
          valid : true,
          column : [
              {text : 'ID Penghitung',    value : 'idPenghitung'},
              {text : 'Nama Penghitung',             value : 'namaPenghitung'},
              {text : 'Create Date',    value : 'tglPenghitung'},
              {text : 'Action',           value : 'aksi'}
          ],
          penghitung : [],
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
          dueDate: undefined,
          datetime: undefined,
          idPenghitung : '',
          namaPenghitung : '',
          tglPenghitung : undefined,

          snackbar: {
                    show: false,
                    message: null,
                    color: null
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
  
        validate () {
                if(this.$refs.form.validate()){
                    if(this.snackbar.color == "red"){
                        this.loading = false
                        this.dialog = false
                    }else{
                        this.loading = true
                        this.dialog = true
                    }
                    this.addPenghitung()
                }
            },

        editMaterial(types){
          console.log('ID : ' + types.id)
          this.editedIndex = this.types.indexOf(types);
          this.editedItem = Object.assign({},types);
        },
  
        async fetchData(){
          try{
            const axios = require('axios');
            const res = await axios.get('/supplier/show_admin_penghitung');
            if (res.data == null){
              alert('Material Kosong')
            }else{
              this.penghitung = res.data
              console.log(res,this.penghitung)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },
        
       
  
        async addPenghitung(){
            try{
                const axios = require('axios')
                const res = await axios.post('/supplier/add_admin_penghitung',{
                    idPenghitung : this.idPenghitung,
                    namaPenghitung : this.namaPenghitung,
                    tglPenghitung : this.tglPenghitung
                })

                if(res.data.status == 'berhasil'){
                        this.snackbar = {
                        message : "Insert Penghitung Berhasil",
                        color : 'green',
                        show : true
                    }
                    setTimeout(() => {
                        location.replace('/listPenghitungMatriks')
                    }, 1000)

                    }
                    else if(res.data.status == "gagal"){
                            this.loading = false
                            this.snackbar = {
                                message : "Insert Penghitung Gagal ",
                                color : 'red',
                                show : true
                            }
                    }

            }catch(error){
                console.log(error)
            }
        }
        
        
      }
    }
  </script>