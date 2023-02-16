<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Tool Stock By Box {{this.$route.params.id}}</h1>
        <br>
        <v-card
            class="mx-auto text-center"
            max-width="1000">
            <div class="pa-6">
                <v-text-field
                    v-model="search"
                    label="Search"
                    variant="plain"
                ></v-text-field>
            </div>
            <v-data-table
                :headers = "column"
                :items = "toolStock"
                :items-per-page = 100
                :search="search"
            >
            <template v-slot:[`item.id`]="{ item }">
                <v-text-field v-model="editedItem.id" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.id}}</span>
            </template>

            <template v-slot:[`item.merk`]="{ item }">
                <v-text-field v-model="editedItem.merk" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.merk}}</span>
            </template>

            <template v-slot:[`item.quantity`]="{ item }">
                <v-text-field v-model="editedItem.quantity" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.quantity}}</span>
            </template>

            <template v-slot:[`item.unit`]="{ item }">
                <v-text-field v-model="editedItem.unit" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                <span v-else>{{item.unit}}</span>
            </template>

            <template v-slot:[`item.aksi`]="{ item }">
            <div>
                <v-tooltip top>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                        class="mx-1" 
                        x-small
                        color="blue"
                        @click="addStockByBox(item)"
                        v-bind="attrs"
                        v-on="on">
                        <v-icon small dark>mdi-plus</v-icon>
                        </v-btn>
                    </template>
                    <span>Tambah Tool Stock</span>
                </v-tooltip>
            </div>
            </template>
            </v-data-table>
        </v-card>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
export default {
    data(){
        return {
            column : [
                {text : 'ID', value : 'id'},
                {text : 'Merk', value : 'merk'},
                {text : 'Nama', value : 'nama'},
                {text : 'Quantity', value : 'quantity'},
                {text : 'Unit', value : 'unit'},
                {text : 'Action',value : 'aksi'}
            ],
            toolStock : [],
            search: "",
            editedIndex : -1,
            editedItem : {
                id : '',
                nama  : '',
            },
            defaultItem : {
                id : '',
                nama : '',
            },
            snackbar: {
                show: false,
                message: null,
                color: null
            },
        }
    },

    mounted(){
        this.fetchToolStock()
    },

    methods : {
        async fetchToolStock(){
            try{
                const axios = require('axios')
                const res = await axios.get('/tools/show_tools_not_in_box')
                if(res.data == null){
                    alert("Data Tool Stock kosong")
                }else{
                    this.toolStock = res.data
                    console.log(res,this.toolStock)
                }
            }
            catch(error){
                console.log(error)
            }
        },

        async addStockByBox(stock){
            console.log(stock.id)
            try{
                const axios = require('axios')
                const response = await axios.post('/box/add_toolstock_by_box/' + this.$route.params.id,
                    {
                        toolStockId: stock.id
                    }
                );
                console.log(response)
                if(response.data.status == "berhasil"){
                    this.snackbar = {
                        message : "Insert Tool Stock " + stock.nama + " Success",
                        color : 'green',
                        show : true
                    }
                    setTimeout(() => {
                        location.reload()
                    }, 1000)
                }
                else if(response.data.status == "gagal"){
                    this.snackbar = {
                        message : "Insert Tool Stock " + stock.nama + " Gagal",
                        color : 'red',
                        show : true
                    }
                    setTimeout(() => {
                        location.reload()
                    }, 1000)
                }
            }
            catch(error){
                this.snackbar = {
                    message : "Insert Tool Stock Error",
                    color : 'error',
                    show : true
                }
                console.log(error)
            }
        },
    }
}
</script>
