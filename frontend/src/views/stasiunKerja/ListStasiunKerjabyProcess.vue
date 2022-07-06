<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Stasiun Kerja by Process</h1><h1>{{this.$route.params.id}}</h1>
        <br>
        <router-link :to="{name : 'Tambah Stasiun Kerja by Process',params : {id : `${this.$route.params.id}`}}">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Pilih Stasiun Kerja
            </v-btn>
        </router-link>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "column"
                :items = "stasiunkerja">
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
                    <v-text-field v-model="editedItem.nama" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.nama}}</span>
                </template>

                 <template v-slot:[`item.liniproduksi`]="{ item }">
                   <v-select v-model="editedItem.liniproduksi" item-text="id" item-value="id" :items="lini" v-if="item.id == editedItem.id"></v-select>
                  <span v-else>{{item.liniproduksi}}</span>
                </template>

                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.id==editedItem.id">
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                        <v-icon color="green" @click="updateData()">
                            mdi-content-save
                        </v-icon>
                    </div>
                    <div v-else>
                        <v-btn class="mx-1" x-small color="blue" @click="selectWorkstation(item)">
                            <v-icon small dark>mdi-check</v-icon>
                        </v-btn>
                        <v-btn class="mx-1" x-small color="green" @click="editWorkstation(item)">
                            <v-icon small dark>mdi-pencil</v-icon>
                        </v-btn>
                        <v-btn class="mx-1" x-small color="red" @click="deleteWorkstation(item)">
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
    data(){
        return {
            column : [
                {text : 'ID Workstation', value : 'stasiunKerja'},
                {text : 'Nama', value : 'nama'},
                {text : 'Dibuat', value : 'dibuat'},
                {text : 'Berlaku', value : 'berlaku'},
                {text : 'Proses', value : 'proses'},
                {text : 'Lini Produksi',value : 'liniproduksi'}
            ],
            stasiunkerja : [],
            lini : [],
            editedIndex : -1,
        editedItem : {
            id : '',
            nama : '',
            liniproduksi : '',
        },
        defaultItem : {
            id : '',
            nama : '',
            liniproduksi : ''
        },
        }
    },

    mounted(){
        this.fetchStasiunKerjabyProcess(),
        this.fetchLini()
    },

    methods : {
        async fetchStasiunKerjabyProcess(){
            const axios = require('axios')
            const res = await axios.get('/stasiun_kerja/show_stasiun_kerja_by_process/' + this.$route.params.id)
            try{
                if(res.data == null){
                    alert("Data kosong")
                }
                else{
                    this.stasiunkerja = res.data
                    console.log(res,this.stasiunkerja)

                }
            } catch(error){
                console.log(error)
            }
        },

        async fetchLini(){
            try{
                const axios = require('axios')
                const res = await axios.get('/liniproduksi/show_liniproduksi')
                if(res.data == null){
                    console.log("Data lini kosong")
                }else{
                    this.lini = res.data;
                    console.log(res,this.lini)
                }
            }catch(error){
                console.log(error)
            }
        },

        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.stasiun[this.editedIndex],this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/stasiun_kerja/update_stasiun_kerja/' + this.editedItem.id,{ 
                    id : this.editedItem.id,
                    nama : this.editedItem.nama,
                    liniproduksi : this.editedItem.liniproduksi
                })

                console.log(res)
                
            }catch(error){
                console.log(error)
            }
        }
    }
}

</script>