<template>
<v-app>


    <v-card class="text-center mt-4 ml-3" max-width="1350">

        <v-form
          class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation>

          <v-text-field
          v-model="nama"
          label="Order Name"
          required
          ></v-text-field>

          <v-text-field
          v-model="quantity"
          label="Quantity"
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
              <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker full-width v-model="dueDate"></v-date-picker>
          </v-menu>
          
          <v-menu
            ref="menu"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="mx-10"
                v-model="datetime"
                label="Due Time"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menu2"
              v-model="datetime"
              full-width
              format="24hr"
              @click:minute="$refs.menu.save(time)"
            ></v-time-picker>
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

    </v-card>



    <v-card
        class="text-center mt-10 ml-3"
        max-width="1000">
        <br>
        <h1>List Tool Purchase Item</h1>
        <br>
        <v-card
            class="mx-auto text-center"
            max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "toolPurchaseItem"
            >
            <template v-slot:[`item.purchaseItemId`]="{ item }">
                <v-text-field v-model="editedItem.purchaseItemId" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.purchaseItemId}}</span>
            </template>

            <template v-slot:[`item.namaToolType`]="{ item }">
                <v-text-field v-model="editedItem.namaToolType" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.namaToolType}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>

            
            <template v-slot:[`item.arrivalDatePlan`]="{ item }">
                <v-text-field v-model="editedItem.arrivalDatePlan" :hide-details="true" dense single-line :autofocus="true" v-if="item.purchaseItemId == editedItem.purchaseItemId"></v-text-field>
                <span v-else>{{item.nama}}</span>
            </template>



            <template v-slot:[`item.aksi`]="{ item }">
            <div v-if="item.id==editedItem.id">
                <v-icon color="red" class="mr-3" @click="close()">
                    mdi-window-close
                </v-icon>
                <v-icon color="green" @click="updateToolBox()">
                    mdi-content-save
                </v-icon>
            </div>
            <div v-else>
                <router-link :to="{name : 'Tambah Tool Stock By Box', params:{id : `${item.id}`}}">
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
                        <span>Tambah Tool Stock</span>
                    </v-tooltip>
                </router-link>

                <v-tooltip top>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn 
                      class="mx-1" 
                      x-small
                      color="green"
                      @click="editToolBox(item)"
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
                      @click="deleteToolBox(item)"
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

</v-app>
</template>

<script>
export default {
    data(){
        return {
            column : [
                {text : 'ID Purchase Item', value : 'purchaseItemId'},
                {text : 'Nama Tool Type', value : 'namaToolType'},
                {text : 'Quantity', value : 'quantity'},
                {text : 'Satuan', value : 'nama'},
                {text : 'Action',value : 'aksi'}
            ],
            toolPurchaseItem : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                nama  : '',
            },
            defaultItem : {
                id : '',
                nama : '',
            },
        }
    },

    mounted(){
        this.fetchData()
    },

    methods : {
        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/show_purchase_item_bypurchase/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.toolPurchaseItem = res.data
                    console.log(res,this.toolBox)
                }
            }
            catch(error){
                console.log(error)
            }
        },
        
        editToolBox(toolBox){
            console.log('ID : ' + toolBox.id)
            this.editedIndex = this.toolBox.indexOf(toolBox)
            this.editedItem = Object.assign({},toolBox)
        },
        
        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        async updateToolBox(){
            if (this.editedIndex > -1) {
                Object.assign(this.toolBox[this.editedIndex], this.toolBox)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/box/update_toolbox/' + this.editedItem.id,
                { id : this.editedItem.id,
                  nama : this.editedItem.nama
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        }
    }
}
</script>
