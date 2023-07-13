<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Daftar Kotak Perkakas</h1>
        <br>
        <v-card
            class="mx-auto text-center"
            max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "toolBox"
            >
            <template v-slot:[`item.id`]="{ item }">
                <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.id}}</span>
            </template>

            <template v-slot:[`item.nama`]="{ item }">
                <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
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
</template>

<script>
export default {
    data(){
        return {
            column : [
                {text : 'ID', value : 'id'},
                {text : 'Nama Tool Box', value : 'nama'},
                {text : 'Action',value : 'aksi'}
            ],
            toolBox : [],
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
        this.fetchToolBox()
    },

    methods : {
        async fetchToolBox(){
            try{
                const axios = require('axios')
                const res = await axios.get('/box/show_toolbox')
                if(res.data == null){
                    alert("Data Tool Box kosong")
                }else{
                    this.toolBox = res.data
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
