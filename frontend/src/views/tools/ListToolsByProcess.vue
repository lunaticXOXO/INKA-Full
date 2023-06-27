<template>
    <v-app>
        <v-card class="mx-auto text-center mt-6" max-width="1000">
            <br>
            <h1>List Proses by Struktur Jenis Produk</h1><h1>{{this.$route.params.id}}</h1>
            <br>
            <router-link :to="{name : 'Tambah Proses by Struktur Jenis Produk', params:{id : `${this.$route.params.id}`}}">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Process by Struktur Jenis Produk
                </v-btn>
            </router-link>
            <v-card class="mx-auto text-center" max-width="1000">
                <v-data-table
                    :headers = "column"
                    :items = "toolneed">
                    <template v-slot:[`item.toolTypeCode`]="{ item }">
                        <div v-if="item.toolTypeCode === editedItem.toolTypeCode">
                            <v-text-field disabled v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                            <span v-else>{{item.toolTypeCode}}</span>
                        </div>
                        <div v-else>
                            <v-text-field v-model="editedItem.toolTypeCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                            <span v-else>{{item.toolTypeCode}}</span>
                        </div>
                    </template>
                    <template v-slot:[`item.namaTool`]="{ item }">
                        <v-text-field v-model="editedItem.namaTool" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                        <span v-else>{{item.namaTool}}</span>
                    </template>

                    <template v-slot:[`item.processCode`]="{ item }">
                        <v-text-field v-model="editedItem.processCode" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                        <span v-else>{{item.processCode}}</span>
                    </template>
                  
                    <template v-slot:[`item.namaProses`]="{ item }">
                        <v-text-field v-model="editedItem.namaProses" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                        <span v-else>{{item.namaProses}}</span>
                    </template>
                    
                    <template v-slot:[`item.quantity`]="{ item }">
                        <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                        <span v-else>{{item.quantity}}</span>
                    </template>
                    
                     
                    <template v-slot:[`item.isConsumable`]="{ item }">
                        <v-text-field v-model="editedItem.isConsumable" :hide-details="true" dense single-line :autofocus="true" v-if="item.toolTypeCode == editedItem.toolTypeCode"></v-text-field>
                        <span v-else>{{item.isConsumable}}</span>
                    </template>

                </v-data-table>
            </v-card>
        </v-card>
    </v-app>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            column : [
                {text : 'Tool Type Code', value : 'toolTypeCode'},
                {text : 'Nama Tool',value : 'namaTool'},
                {text : 'Process Code', value : 'Process Code'},
                {text : 'Nama Proses', value : 'namaProses'},
                {text : 'Quantity', value : 'quantity'},
                {text : 'Is Consumable', value : 'isConsumable'}
            ],
          
            toolneed : [],
           
            editedIndex : -1,
            editedItem : {
                id: '',
                prosesSesudahnya: '',
                nama: '',
                durasi: '',
                satuanDurasi: '',
                jenisProses: '',
                idNodal: ''
            },
            defaultItem : {
                id: '',
                prosesSesudahnya: '',
                nama: '',
                durasi: '',
                satuanDurasi: '',
                jenisProses: '',
                idNodal: ''
            },
        }
    },

    mounted(){
        this.fetchToolsByProses()
    },

    methods : {
        close(){
            setTimeout(()=>{
            this.editedItem = Object.assign({},this.defaultItem)
            this.editedIndex = -1;
            },300)
        },

        editProses(prosesItem){
            console.log(prosesItem.id)
            this.editedIndex = this.proses.indexOf(prosesItem)
            this.editedItem = Object.assign({},prosesItem)
        },

   
        async fetchToolsByProses(){
            try{
                const res = await axios.get('/tools/show_toolneed_byprocess/' + this.$route.params.id)
                if(res.data == null){
                    alert("Data Kosong")
                }else{
                    this.toolneed = res.data
                    console.log(res,this.toolneed)
                }
                
            } catch(error){
                alert("Error")
                console.log(error)
            }
        },

       
        selectProsestoWorkStation(proses){
            console.log(proses.id)
        }
    }
}
</script>
