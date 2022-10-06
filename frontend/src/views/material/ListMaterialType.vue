<template>
    <v-card 
        class="mt-10 text-center mx-10"
        max-width = "1450">
        <br>
        <h1>List Material Type</h1>
        <br>
        <router-link to="/jenisMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Material Type
            </v-btn>
        </router-link>
        <v-data-table 
            :headers = "column"
            :items = "types">
            <template v-slot:[`item.code`]="{ item }">
              <div v-if="item.id === editedItem.id">
                  <v-text-field disabled v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                  <span v-else>{{item.code}}</span>
              </div>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>

            <template v-slot:[`item.isAvailable`]="{ item }">
                <v-text-field v-model="editedItem.isAvailable" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>
                  <div v-if="item.isAvailable == 0">
                    No
                  </div>
                  <div v-if="item.isAvailable == 1">
                    Yes
                  </div>
                </span>
            </template>

            <template v-slot:[`item.isAssy`]="{ item }">
                <v-text-field v-model="editedItem.isAssy" :hide-details="true" dense single-line v-if="item.code == editedItem.code" ></v-text-field>
                <span v-else>
                  <div v-if="item.isAssy == 0">
                    No
                  </div>
                  <div v-if="item.isAssy == 1">
                    Yes
                  </div>
                </span>
            </template>

           <template v-slot:[`item.Classification`]="{ item }">
              <v-select v-model="editedItem.Classification" item-text="Classification" item-value="Classification" :items="types" v-if="item.code == editedItem.code"></v-select>
              <span v-else>{{item.Classification}}</span>
          </template>

            <template v-slot:[`item.Group`]="{ item }">
              <v-select v-model="editedItem.Group" item-text="Group" item-value="Group" :items="types" v-if="item.code == editedItem.code"></v-select>
              <span v-else>{{item.Group}}</span>
          </template>
           
            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.code == editedItem.code">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="updateData()">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <v-btn class="mx-1" x-small color="green" @click="editMaterial(item)">
                    <v-icon small dark>mdi-pencil</v-icon>
                </v-btn>
                <v-btn class="mx-1" x-small color="red" @click="deleteMaterial(item)">
                    <v-icon small dark>mdi-trash-can-outline</v-icon>
                </v-btn>
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
            {text : 'Code',           value : 'code'},
            {text : 'Nama',           value : 'nama'},
            {text : 'Is Available',   value : 'isAvailable'},
            {text : 'Is Assy',        value : 'isAssy'},        
            {text : 'Classification', value : 'descriptionClassification'},
            {text : 'Group Material', value : 'descriptionGroup'},
            {text : 'Action',         value : 'aksi'}
        ],
        types : [],
        editedIndex: -1,
        editedItem: {
          code: '',
          nama: '',
          isAvailable: '',
          isAssy: '',
          Classification : '',
          Group: '',
        },
        defaultItem: {
          code: '',
          nama: '',
          isAvailable: '',
          isAssy: '',
          Classification : '',
          Group: '',
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
        console.log('ID : ' + types.code)
        this.editedIndex = this.types.indexOf(types);
        this.editedItem = Object.assign({},types);
      },

      async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/get_type');
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
          console.log('ID : ' + types.code)
          try{
              const axios = require('axios');
              axios.delete(`/material/deleteMaterialType/${types.code}`);
              alert("Delete Material Type Success!")
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
            const res = await axios.post('/material/update_type/'+ this.editedItem.code,
            { code     : this.editedItem.code,
              nama     : this.editedItem.nama,
              isAvailable    : this.editedItem.isAvailable,
              isAssy : this.editedItem.isAssy,
              classificationCode : this.editedItem.classificationCode,
              groupCode : this.editedItem.groupCode
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>