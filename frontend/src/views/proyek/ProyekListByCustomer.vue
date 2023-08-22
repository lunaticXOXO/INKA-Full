<template>
    <v-app>
    <br>
    <div class="d-flex">
        <v-card class="mt-10 text-center mx-10">
           
            <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
              PELANGGAN {{this.$route.params.id}}
            </v-card-title>
        </v-card>

            <v-data-table 
                :headers="column2"
                :items="customerinproject">
            </v-data-table>
        </v-card>
    </div>
    <div class="tabelproyek">
        <v-card class="mt-10 text-center mx-10" max-width="1800">

            <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="400"
            >
            <v-card-title class="text-h4">
              PROYEK PELANGGAN {{this.$route.params.id}}
            </v-card-title>
        </v-card>
        <br><br>

            <router-link :to="{name : 'Tambah Proyek by Customer', params : {id : `${this.$route.params.id}`}}">
                <v-btn color="primary" class="d-flex ml-4 mb-6">
                    Add Proyek by Customer
                </v-btn>
            </router-link>
            <v-data-table 
                :headers="column"
                :items="project"
                :items-per-page="5"
                >
                <template v-slot:[`item.id`]="{ item }">
                    <div v-if="item.id == editedItem.id">
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
                <template v-slot:[`item.customerid`]="{ item }">
                    <div v-if="item.id == editedItem.id">
                    <v-text-field disabled v-model="editedItem.customerid" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.customerid}}</span>
                    </div>
                    <div v-else>
                    <v-text-field v-model="editedItem.customerid" :hide-details="true" dense single-line :autofocus="true" v-if="item.id == editedItem.id"></v-text-field>
                    <span v-else>{{item.customerid}}</span>
                    </div>
                </template>
                <template v-slot:[`item.aksi`]="{ item }">
                    <div v-if="item.id==editedItem.id">
                        <v-icon color="red" class="mr-3" @click="close()">
                            mdi-window-close
                        </v-icon>
                        <v-icon color="green" class="mr-3" @click="updateData()">
                            mdi-content-save
                        </v-icon>
                    </div>
                    <div v-else>
                        <router-link :to="{name : 'List Rincian Proyek by Proyek',params:{id : `${item.id}`}}">
                            <v-tooltip top>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn 
                                    class="mx-1" 
                                    x-small
                                    color="blue"
                                    @click="selectProject(item)"
                                    v-bind="attrs"
                                    v-on="on">
                                    <v-icon small dark>mdi-check</v-icon>
                                    </v-btn>
                                </template>
                                <span>List Rincian Proyek By Proyek</span>
                            </v-tooltip>
                        </router-link>

                        <v-tooltip top>
                            <template v-slot:activator="{ on, attrs }">
                                <v-btn 
                                class="mx-1" 
                                x-small
                                color="green"
                                @click="editProject(item)"
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
                                @click="deleteProject(item)"
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
            <br>
            <v-card
            color="#6f6f6f"
            dark
            class="px-5 py-3"
            max-height ="50"
        >
      </v-card>

        </v-card>   
    </div> 
    </v-app>
</template>

<script>
export default {
    data(){
        return{
            valid : true,
            column : [
                {text : 'ID Proyek',value : 'id'},
                {text : 'Nama Proyek',value : 'nama'},
                {text : 'Tanggal Dibuat',value : 'tglDibuat'},
                {text : 'Customer ID',value : 'customerid'},
                {text : 'Action',value : 'aksi'}
            ],
            column2 : [
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'NamaCustomer'}
            ],
            project : [],
            customerinproject : [],
            editedIndex : -1,
            editedItem : {
                id : '',
                nama : '',
                customerid : ''
            },
            defaultItem : {
                id : 'New ID',
                nama : 'New Nama',
                customerid : 'New Customer'
            }
        }
    },

    mounted() {
      this.fetchProyekByCustomer(),
      this.fetchCustomerInProyek()
    },
    
    methods: {
        async fetchProyekByCustomer(){
          try{
            const axios = require('axios');
            const res = await axios.get('/proyek/get_proyek_by_customer/' + this.$route.params.id)
            if (res.data == null){
              alert('Project Kosong')
            }else{
              this.project = res.data
              console.log(res,this.project)
            }
          }
          catch(error){
            alert("Error")
            console.log(error)
          }
        },

        async updateData(){
            if(this.editedIndex > -1){
                Object.assign(this.project[this.editedIndex],this.editedItem)
            }
            this.close()
            try{
                const axios = require('axios')
                const res = await axios.post('/proyek/update_proyek/' + this.editedItem.id,{
                    id : this.editedItem.id,
                    nama : this.editedItem.nama,
                    customerid : this.editedItem.customerid
                })
                console.log(res)

            }catch(error){
                console.log(error)
            }
        },

        async fetchCustomerInProyek(){
            const axios = require('axios')
            const res = await axios.get('/proyek/get_customer_inproyek/' + this.$route.params.id)
            if(res.data == null){
                console.log("Data kosong")
            }else{
                this.customerinproject = res.data
                console.log(res,this.customerinproject)
            }
        },

        selectProject(project){
            console.log('ID : ' + project.id)
        },

        editProject(project){
          this.editedIndex = this.project.indexOf(project)
          this.editedItem = Object.assign({},project)
        },

        close(){
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem);
                this.editedIndex = -1;
            }, 300)
        },
        
        deleteProject(project){
            console.log('ID : ' + project.id)
            try{
                const axios = require('axios');
                axios.delete(`/proyek/deleteProject/${project.id}`);
                alert("Delete Proyek Success!")
                this.fetchProyekByCustomer()
            }
            catch(error){
                console.log(error)
            }
        },
    },
}
</script>