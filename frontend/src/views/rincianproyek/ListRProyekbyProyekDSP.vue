<template>
    <v-app>
        <div class="d-flex ml-14">
            <v-card class="ml-8 text-center mt-6" width="600">
                <h3>Info Proyek {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "headers2"
                    :items = "proyekinrincian">
                </v-data-table>
            </v-card>
      
            <v-card class="ml-15 text-center mt-6" width = "500">
                  <h3>Customer Proyek {{this.$route.params.id}}</h3>
                <v-data-table
                    :headers = "headers3"
                    :items = "customer"
                >
                </v-data-table>
            </v-card>
        </div>
        <v-card class="mx-auto text-center mt-6" width="1000">
            <br>
            <h1>Pilih Item Proyek</h1><h1>{{this.$route.params.id}}</h1>
            <br>
            <v-card class="mx-auto text-center" max-width="1000">
                <v-data-table
                    :headers = "headers"
                    :items = "rincianbyproyek">
                    <template v-slot:[`item.aksi`]="{ item }">
                        <router-link :to="{name:'List Produk by Rproyek DSP',params:{'id': `${item.id}`}}">
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
                                <span>List Produk By Rincian Proyek</span>
                            </v-tooltip>
                        </router-link>
                    </template>
                </v-data-table>
            </v-card>
        </v-card>
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            headers : [
                {text : 'ID Item',value : 'id'},
                {text : 'Nama',value : 'nama'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Action', value : 'aksi'}
            ],
            headers2 : [
                {text : 'ID Proyek', value : 'IdProyek'},
                {text : 'Nama Proyek', value : 'NamaProyek'}
            ],
            headers3 : [
                {text : 'ID Customer', value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'},
            ],
            customer : [],
            rincianbyproyek : [],
            proyekinrincian : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                jumlah : '',
                dueDate : '',
                proyek : '',
                jenisProduk : ''
            },
            defaultItem : {
                id : 'New ID',
                jumlah : 'New Jumlah',
                dueDate : 'New Due Date',
                proyek : 'New Proyek',
                jenisProduk : 'New Jenis Produk'
            }
        }
    },

    mounted(){
        this.fetchRProyekbyProyek(),
        this.fetchProyekInRProyek()
    },
    
    methods : {
        async fetchRProyekbyProyek(){
            try{
                const axios = require('axios')
                const res = await axios.get('/rproyek/show_rproyek_by_proyek/' + this.$route.params.id)
                if (res == null){
                    alert("Rincian Proyek Kosong")  
                }
                else{
                    this.rincianbyproyek = res.data
                    console.log(res,this.rincianbyproyek)
                }
            }
            catch(error){
                alert("Error")
                console.log(error)
            }
        },

        async fetchProyekInRProyek(){
            try{
                
                const axios = require('axios')
                const res = await axios.get('/rproyek/show_proyek_inrproyek/' + this.$route.params.id)
                if(res == null){
                    console.log("Data kosong")
                }else{
                    this.proyekinrincian = res.data
                    this.customer = res.data
                    console.log(res,this.proyekinrincian)
                }

            }catch(error){
                alert("Error")
                console.log(error)
            }
        },
    }
}
</script>