<template>
    <v-card 
        class="mt-10 text-center mx-auto"
        max-width = "1700">
      
        <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             DAFTAR OPERATOR
            </v-card-title>
        </v-card>
        <br><br>

        <router-link to="/tambahOperator">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Tambah Data Operator
            </v-btn>
        </router-link>

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
              <div v-if="item.code == editedItem.code">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green"  @click="updateData()">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
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
                    <span>Tambah UUID Operator</span>
                  </v-tooltip>
                </router-link>
                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editOperator(item)"
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
                      @click="deleteOperator(item)"
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
        <br>
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
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      editOperator(operators){
        console.log('Code : ' + operators.code)
        this.editedIndex = this.operators.indexOf(operators);
        this.editedItem = Object.assign({}, operators);
      },

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

      deleteOperator(operators){
          console.log('Deleted Operator : ' + operators.code)
          try{
              const axios = require('axios');
              axios.delete(`/operator/delete_operator/${operators.code}`);
              alert("Delete Operator Success!")
              this.fetchOperator()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.operators[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/operator/update_operator/'+ this.editedItem.code,
            { code: this.editedItem.code,
              nama: this.editedItem.nama,
              email: this.editedItem.email,
              adress1: this.editedItem.adress1,
              city: this.editedItem.city,
              phone: this.editedItem.phone,
              postalcode: this.editedItem.postalcode,
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>