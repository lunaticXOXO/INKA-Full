<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Negara</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "negara">
                <!--Text Box di Table-->
                <template v-slot:[`item.code`]="{ item }">
                    <v-text-field v-model="editedItem.code" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                    <span v-else>{{item.code}}</span>
                </template>

                 <template v-slot:[`item.nama`]="{ item }">
                    <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.code == editedItem.code"></v-text-field>
                    <span v-else>{{item.nama}}</span>
                </template>

                <!--Fungsi fungsi Button-->
                <template v-slot:[`item.aksi`]="{ item }">
                    <!--Jika mengklik tombol pensil/update-->
                    <div v-if="item.code == editedItem.code">
                        <!--Maka muncul tombol untuk close dan save-->
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                        <v-icon color="green" @click="updateData()">
                            mdi-content-save
                        </v-icon>
                    </div>
                    <!--Jika tidak mengklik tombol update-->
                    <div v-else>
                        <v-btn class="mx-1" x-small color="green" @click="editNegara(item)">
                            <v-icon small dark>mdi-pencil</v-icon>
                        </v-btn>
                        <v-btn class="mx-1" x-small color="red" @click="deleteNegara(item)">
                            <v-icon small dark>mdi-trash-can-outline</v-icon>
                        </v-btn>
                    </div>

                </template>

            </v-data-table>
        </v-card>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      headers:[
        {text : 'Kode', value : 'code'},
        {text : 'Nama', value : 'nama'},
        {text : 'Action', value : 'aksi'}      
      ],
      negara:[],
      editedIndex : -1,
      editedItem : {
        code : '',
        nama : ''
      },
      defaultItem : {
        code : '',
        nama : ''
      }
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
        editNegara(negara){
            console.log('ID : ' + negara.code)
            this.editedIndex = this.negara.indexOf(negara)
            this.editedItem = Object.assign({}, negara)
        },

        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },

        async updateData(){
            if (this.editedIndex > -1) {
                Object.assign(this.negara[this.editedIndex], this.editedItem)
                console.log(this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/countries/update_country/' + this.editedItem.code,
                { code : this.editedItem.code,
                  nama : this.editedItem.nama
                })
                console.log(res)
            }catch(error){
                console.log(error)
            }
        },

        deleteNegara(negara){
            console.log('Deleted Country : ' + negara.code)
            try{
                const axios = require('axios');
                axios.delete(`/negara/deleteNegara/${negara.code}`);
                alert("Delete Negara Success!")
                this.fetchData()
            }
            catch(error){
                console.log(error)
            }
        },

        async fetchData(){
            try{
                const axios = require('axios');
                const res = await axios.get(`/countries/get_allcountries`);
                if(res.data == null){
                    alert("Negara Kosong")
                }else{
                    this.negara = res.data;
                    console.log(res,this.data)
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