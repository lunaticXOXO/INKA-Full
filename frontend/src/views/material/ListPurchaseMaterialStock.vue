<template>
    <v-card 
        class="mx-auto text-center mt-10"
        width = "1500">
       
        <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
              DAFTAR PEMESAN MATERIAL
        </v-card-title>

        </v-card>
        <br>

        <router-link to="/pesanMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Purchase Material
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types"
            :items-per-page="5"
            >
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

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>

           <template v-slot:[`item.purchaseDate`]="{ item }">
                <v-text-field v-model="editedItem.purchaseDate" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.purchaseDate}}</span>
          </template>

            <template v-slot:[`item.purchaserName`]="{ item }">
                <v-text-field v-model="editedItem.purchaserName" :hide-details="true" dense single-line v-if="item.id == editedItem.id" ></v-text-field>
                <span v-else>{{item.purchaserName}}</span>
          </template>
           
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.id == editedItem.id">
                  <v-icon color="red" class="mr-3" @click="close">
                    mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()">
                    mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <router-link :to="{name : 'List Purchase Item Material Stock',params:{id : `${item.id}`}}">
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
                    <span>List Purchase Item by Material Stock</span>
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
        valid : true,
        column : [
            {text : 'ID',               value : 'id'},
            {text : 'Nama',             value : 'nama'},
            {text : 'Purchase Date',    value : 'purchaseDate'},
            {text : 'Purchaser Name',   value : 'purchaserName'},
            {text : 'Action',           value : 'aksi'}
        ],
        types : [],
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
        this.fetchMaterial()
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editMaterial(types){
        console.log('ID : ' + types.id)
        this.editedIndex = this.types.indexOf(types);
        this.editedItem = Object.assign({},types);
      },

      async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_purchase_material');
          if (res.data == null){
            alert('Material Kosong')
          }else{
            this.types = res.data
            console.log(res,this.types)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },
      
      deleteMaterial(types){
          console.log('ID : ' + types.id)
          try{
              const axios = require('axios');
              axios.delete(`/material/delete_purchase_material/${types.id}`);
              alert("Delete Purchase Material Success!")
              this.fetchMaterial()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.types[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/material/update_purchase_material/'+ this.editedItem.id,
            { id     : this.editedItem.id,
              nama     : this.editedItem.nama,
              purchaseDate    : this.editedItem.purchaseDate,
              purchaserName : this.editedItem.purchaserName,
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>