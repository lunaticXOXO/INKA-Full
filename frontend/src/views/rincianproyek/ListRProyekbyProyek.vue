<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>List Rincian Proyek by Proyek</h1>
        <br>
        <v-card
        class="mx-auto text-center"
        max-width="1000">
            <v-data-table
                :headers = "headers"
                :items = "rincianbyproyek">
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
                 <template v-slot:[`item.jumlah`]="{ item }">
                    <v-text-field v-model="editedItem.jumlah" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.jumlah}}</span>
                </template>

                <template v-slot:[`item.dueDate`]="{ item }">
                    <div v-if="item.id === editedItem.id">
                        <v-text-field disabled v-model="editedItem.dueDate" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.dueDate}}</span>
                    </div>
                    <div v-else>
                        <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                        <span v-else>{{item.dueDate}}</span>
                    </div>
                </template>

                <template v-slot:[`item.proyek`]="{ item }">
                    <v-text-field v-model="editedItem.proyek" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.proyek}}</span>
                </template>

                <template v-slot:[`item.jenisProduk`]="{ item }">
                    <v-text-field v-model="editedItem.jenisProduk" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.jenisProduk}}</span>
                </template>
                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.id == editedItem.id">
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                         <v-icon color="green" class="mr-3" @click="updateData()">
                            mdi-content-save
                         </v-icon>
                    </div>
                    <div>
                    <v-btn class="mx-1" x-small color="blue" @click="selectRProyektoProduct(item)">
                        <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                      <v-btn class="mx-1" x-small color="brown" @click="selectRProyektoJProduct(item)">
                        <v-icon small dark>mdi-check</v-icon>
                    </v-btn>
                    <v-btn class="mx-1" x-small color="green" @click="editRProyek(item)">
                        <v-icon small dark>mdi-pencil</v-icon>
                    </v-btn>
                    <v-btn class="mx-1" x-small color="red" @click="deleteRProyek(item)">
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
        return{
            headers : [
                {text : 'ID Rincian Proyek',value : 'id'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date',value : 'dueDate'},
                {text : 'Proyek',value : 'proyek'},
                {text : 'Jenis Produk',value : 'jenisProduk'},
                {text : 'Action', value : 'aksi'}
            ],
            rincianbyproyek : [],
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
        this.fetchRProyekbyProyek()
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
            async updateData(){
                if(this.editedIndex > -1){
                    Object.assign(this.rincianbyproyek[this.editedIndex],this.editedItem)
                }
                this.close()
                try{
                    const axios = require('axios')
                    const res = await axios.post('/rproyek/update_rproyek/' + this.editedItem.id,{ 
                        id : this.editedItem.id,
                        jumlah : this.editedItem.jumlah,
                        dueDate : this.editedItem.dueDate,
                        proyek : this.editedItem.proyek,
                        jenisProduk : this.editedItem.jenisProduk
                    })
                    console.log(res)                    
                }catch(error){
                    console.log(error)
                }
            },
        selectRProyektoProduct(rincianbyproyek){
            console.log(rincianbyproyek.id)
            open(`/listProdukbyRProyek/${rincianbyproyek.id}`)
        },
        selectRProyektoJProduct(rincianbyproyek){
             console.log(rincianbyproyek.id)
             open(`/listJenisProdukbyRProyek/${rincianbyproyek.id}`)

        },
         editRProyek(rincianbyproyek){
                this.editedIndex = this.rincianbyproyek.indexOf(rincianbyproyek)
                this.editedItem = Object.assign({},rincianbyproyek)
            },

            close(){
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                }, 300)
            },
    }
}

</script>