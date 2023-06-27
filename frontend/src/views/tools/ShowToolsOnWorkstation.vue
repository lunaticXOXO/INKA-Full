<template>
    <v-card 
        class="mx-auto text-center mt-6"
        max-width = "1450">
        <br>
        <h1>List Tools On Workstation</h1>
        <br>
        

        <v-data-table 
            :headers = "column"
            :items = "toolonws"
            :items-per-page="5"
            >
            <template v-slot:[`item.idToolStock`]="{ item }">
              <div v-if="item.idToolStock === editedItem.idToolStock">
                  <v-text-field disabled v-model="editedItem.idToolStock" :hide-details="true" dense single-line :autofocus="true" v-if="item.idToolStock == editedItem.idToolStock"></v-text-field>
                  <span v-else>{{item.idToolStock}}</span>
              </div>
              <div v-else>
                  <v-text-field v-model="editedItem.idToolStock" :hide-details="true" dense single-line :autofocus="true" v-if="item.idToolStock == editedItem.idToolStock"></v-text-field>
                  <span v-else>{{item.idToolStock}}</span>
              </div>
            </template>
            <template v-slot:[`item.idToolType`]="{ item }">
                <v-text-field v-model="editedItem.idToolType" :hide-details="true" dense single-line v-if="item.idToolStock == editedItem.idToolStock" ></v-text-field>
                <span v-else>{{item.idToolType}}</span>
            </template>
            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line v-if="item.idToolStock == editedItem.idToolStock" ></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>
            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line v-if="item.idToolStock == editedItem.idToolStock" ></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

          <template v-slot:[`item.unit`]="{ item }">
              <v-select v-model="editedItem.unit" item-text="nama" item-value="code" :items="cities" v-if="item.idToolStock == editedItem.idToolStock"></v-select>
              <span v-else>{{item.unit}}</span>
          </template>

            <template v-slot:[`item.aksi`]="{ item }">
              <div v-if="item.idToolStock == editedItem.idToolStock">
                  <v-icon color="red" class="mr-3" @click="close">
                  mdi-window-close
                  </v-icon>
                  <v-icon color="green"  @click="updateData()">
                  mdi-content-save
                  </v-icon>
              </div>
              <div v-else>
                <router-link :to="{name : 'Show Tools On Workstation',params:{id : `${item.idToolStock}`}}">
                
                  <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn 
                        class="mx-1" 
                        x-small
                        color="green"
                        @click="selectToolStock()"
                        v-bind="attrs"
                        v-on="on">
                        <v-icon small dark>mdi-check</v-icon>
                      </v-btn>
                    </template>
                    <span>Checklist Kondisi Perkakas</span>
                  </v-tooltip>
                </router-link>
             

                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="red"
                      @click="deleteCustomer(item)"
                      v-bind="attrs"
                      v-on="on">
                      <v-icon small dark>mdi-cancel</v-icon>
                    </v-btn>
                  </template>
                  <span>Delete</span>
                </v-tooltip>
              </div>
            </template>

        </v-data-table>
        <div class="d-flex">
            <v-text-field
                    max-width="10"
                    dense
                    v-model="inputKode"
                    @keyup.enter="parseBarcode"
                    autofocus
                    single-line 
                    class="shrink ml-4"
                    label="ID Operator"
                    >
                    </v-text-field>
        <v-btn color="green" class="mb-5 ml-4">
                Submit
        </v-btn>
        </div>
    </v-card>
</template>

<script>
  export default {
    data(){
      return {
        valid : true,
        column : [
            {text : 'ID Tool Stock',        value : 'idToolStock'},
            {text : 'ID Tool Type',         value : 'idToolType'},
            {text : 'Nama Tool Type',       value : 'nama'},
            {text : 'Quantity',             value : 'quantity'},
            {text : 'Unit',                 value : 'unit'},
            {text : 'Action',               value : 'aksi'},
        
        ],
        toolonws : [],
     
        editedIndex: -1,
        editedItem: {
          id: '',
          nama: '',
          email: '',
          adress1: '',
          city: '',
          phone: '',
          postalcode: '',
        },
        defaultItem: {
          id: '',
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
        this.fetchToolOnWorkstation()
       
    },

    methods: {
      close () {
        setTimeout(() => {
            this.editedItem = Object.assign({}, this.defaultItem);
            this.editedIndex = -1;
        }, 300)
      },

      selectToolStock(){
          location.replace('')
          //open(`/proyekListbyCustomer/${customers.id}`)
      },

      async fetchToolOnWorkstation(){
        try{
          const axios = require('axios');
          const res = await axios.get('/tools/show_tools_onws/' + this.$route.params.id);
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.toolonws = res.data
            console.log(res,this.toolonws)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },


      deleteCustomer(customers){
          console.log('ID : ' + customers.id)
          try{
              const axios = require('axios');
              axios.delete(`/customer/deleteCustomer/${customers.id}`);
              alert("Delete Customer Success!")
              this.fetchCustomer()
          }
          catch(error){
              console.log(error)
          }
      },

      async updateData(){
        if (this.editedIndex > -1) {
            Object.assign(this.customers[this.editedIndex], this.editedItem)
            console.log(this.editedItem)
        }
        this.close()
        try{
            const axios = require('axios')
            const res = await axios.post('/customer/update_customer/'+ this.editedItem.id,
            { id: this.editedItem.id,
              nama: this.editedItem.nama,
              email: this.editedItem.email,
              adress1: this.editedItem.adress1,
              city: this.editedItem.city,
              phone: this.editedItem.phone,
              postalcode: this.editedItem.postalcode,
              
              //Data yang tidak ditampilkan
              adress2: this.editedItem.adress2,
              fax: this.editedItem.fax,
              pic: this.editedItem.pic,
              situs: this.editedItem.situs,
              remark: this.editedItem.remark,
            })
            console.log(res)
        }catch(error){
            console.log(error)
        }
      } 
    }
  }
</script>