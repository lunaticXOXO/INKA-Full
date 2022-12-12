<template>
    <v-main>
        <nav>
            <v-app-bar app color="#6f6f6f">
                <v-img 
                    max-height="50"
                    max-width="50" 
                    src="../assets/itb.png"
                    class="mx-2">
                </v-img>
                <v-img 
                    max-height="70"
                    max-width="70" 
                    src="../assets/lpdp.png"
                    class="mr-3">
                </v-img>
                <v-img 
                    max-height="70"
                    max-width="70" 
                    src="../assets/inka.png"
                    class="mb-1 mr-4">
                </v-img>
                <v-spacer></v-spacer>
                <span class="font-weight-light white--text ">Workstation:</span>
                <span class="white--text mr-6">
                    <v-text-field background-color="#6f6f6f" class="mt-6 white--text font-weight-bold" v-model="namaOperator" disabled solo dense flat>
                    </v-text-field>
                </span>
                <v-btn @click="logout()" color="grey">
                    <span>Sign Out</span>
                    <v-img src="../assets/logo/arrow-right.png"></v-img>
                </v-btn>
            </v-app-bar>
        </nav>
        <div class="d-flex">
            <div class = "ma-6">
                <h3>Operasi</h3>
                <v-card class="mx-auto mb-6 text-center mt-6" width="800">
                    <v-data-table
                        :headers = "headers"
                        :items = "items"                
                        >
                    </v-data-table>
                </v-card>
                <h3>Material yang diperlukan</h3>
                <v-card class="mx-auto mb-6 text-center mt-6" width="700">
                    <v-data-table
                        :headers = "headers2"
                        :items = "items2"
                        >
                    </v-data-table>
                </v-card>
            </div>
            <div class = "ma-6">
                <h3>Operator</h3>
                <div class = "mt-4">
                    <v-container class="white">
                        <v-row>
                            <v-col
                            v-for=" index in listOperatorPhoto"
                            :key="index"
                            cols="4"
                            sm="auto"
                            >
                            <span class="mx-auto"><b>{{index.nama}}</b></span>
                                <v-img
                                    height="100"
                                    width="75" 
                                    :src="require(`@/views/operator/foto/${index.link}`)" 
                                >
                                </v-img>
                            </v-col>
                        </v-row>
                    </v-container>
                </div>
                <div class="mx-auto mt-10">
                    <v-text-field
                    width="300"
                    dense
                    v-model="inputKode"
                    @keyup.enter="parseBarcode"
                    autofocus>
                    </v-text-field>
                    <v-dialog
                        v-model="dialog"
                        width="500">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                v-model = "btn1"
                                :loading="loading"
                                v-if = "visible"
                                class="mx-auto white--text" 
                                elevation = "0"
                                width="250" 
                                :color="btn1.color"
                                v-bind:disabled="hasClicked"
                                v-bind="attrs"
                                v-on="on">
                                {{btn1.text}}
                            </v-btn>
                        </template>
                        <v-card>
                            <div v-if = "btn1.color == 'green'">
                                <v-card-title class="text-h5 grey lighten-2">
                                    Operasi 
                                </v-card-title>
                                <br>
                                <v-card-text>
                                    Mulai Operasi ?
                                </v-card-text>
                                <v-divider></v-divider>
        
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        v-model = "btn2"
                                        color="blue"
                                        text
                                        @click="startOperation()">
                                        Mulai
                                    </v-btn>
                                    <v-btn
                                        v-model = "btn2"
                                        color="red"
                                        text
                                        @click="dialog = false">
                                        Kembali
                                    </v-btn>
                                </v-card-actions>
                            </div>
                            <div v-else>
                                <v-card-title class="text-h5 grey lighten-2">
                                    Operasi 
                                </v-card-title>
                                <br>
                                <v-card-text>
                                    Akhiri Operasi ?
                                </v-card-text>
                                <v-divider></v-divider>
        
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                        v-model = "btn2"
                                        color="blue"
                                        text
                                        @click="akhiriOperation()">
                                        Akhiri
                                    </v-btn>
                                    <v-btn
                                        v-model = "btn2"
                                        color="red"
                                        text
                                        @click="dialog = false">
                                        Kembali
                                    </v-btn>
                                </v-card-actions>   
                            </div>
                        </v-card>
                    </v-dialog>
                    <br><br>
                    <v-btn
                        v-model = "btn2"
                        class = "mx-auto white--text"
                        elevation = "0"
                        width = "250"
                        color="blue"
                        @click="refresh2()">
                        Refresh
                    </v-btn>
                </div>
            </div>
        </div>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-main>
</template>

<script>
import Login from "../services/Login.js"
export default {
    data(){
        return {
            visible : true,
            itemKey: undefined,
            singleSelect: false,
            selected: [],
            loginService: new Login(),
            inputKode: undefined,
            namaOperator: undefined,
            route: "/login",
            routeHome: "/",
            drawer: false,
            dialog : false,
            hasClicked: false,
            headers : [
                {text : 'Code',               value : 'id'},
                {text : 'Nama',               value : 'nama'},
                {text : 'Rencana Mulai',      value : 'rencanaMulai'},
                {text : 'Rencana Selesai',    value : 'rencanaSelesai'},
                {text : 'Mulai',              value : 'mulai'},
                {text : 'Selesai',            value : 'selesai'}
            ],
            headers2 : [
                {text : 'Nama Material',    value : 'nama'},
                {text : 'Butuh',            value : 'butuh'},
                {text : 'Kurang',           value : 'kurang'},
            ],
            items: undefined,
            items2: undefined,
            items3 : undefined,
            index : 0,
            btn1 : {
                text : '',
                color: '#FFFFFF',
                
            },
            btn2 : undefined,
            snackbar : {
                show : false,
                color : null,
                message : null,
            },
            timer: '',
            timer2 : '',
            loading : false,
            listOperator : [],
            listOperatorPhoto : [],
        }
    },

    mounted() {
        //this.fetchOperasi(),
        this.fetchMaterial(),
        this.fetchOperasiSiap(),
        this.fetchOperasiLayak(),
        this.getLinkOperator()
    },

    methods: {
        refresh() {
            setTimeout(() => {
                this.timer.setInterval(location.replace("/"), 2000)
                this.$forceUpdate();  
            }, 2000)
            location.reload()
        },

        refresh2() {
            location.reload()
        },

        logout() {
            this.route = "/login"
            location.replace("/login")
            this.loginService.removeUserType()
        },

        async parseBarcode(){
            console.log(this.inputKode)
            console.log(this.namaOperator)

            try{
                const axios = require('axios');

                const response = await axios.post('/rfid/insert_material',
                    { 
                        stasiunKerja : this.namaOperator,
                        idMat : this.inputKode
                    }
                );
                console.log(response)

                const res = axios.get('/operator/get_link_operator/<code>' + this.inputKode)
                if(res.data == null){
                    console.log("Bukan Operator")
                }else{
                    this.listOperator = res.data
                    console.log(res,this.listOperator)
                }
            }
            catch(error){
                console.log(error)
            }
            
            setTimeout(() => {
                try{
                    const axios = require('axios')
                    const res =  axios.get('/material/message_material_login/' + this.kodeMaterial)
                    console.log(res.data[0].keterangan)
                    if(res.data.length == null){
                        console.log("Data kosong")
                    }
                    else if(res.data[0].keterangan == "material berhasil login"){
                        this.items = res.data
                        console.log(res,this.items)
                        this.snackbar = {
                            show : true,
                            message : res.data[0].keterangan,
                            color : "green"
                        }
                    }
                    else if(res.data[0].keterangan == "material gagal login"){
                        this.items = res.data
                        console.log(res,this.items)
                        this.snackbar = {
                            show : true,
                            message : res.data[0].keterangan,
                            color : "red"
                        }
                    }
                }
                catch(error){
                    console.log(error)
                    this.snackbar = {
                        show : true,
                        message : "material berhasil login",
                        color : "green"
                    }
                }
            }, 3000)

            setTimeout(() => {
                location.reload("/")
            }, 3000)
        },

        /*async fetchOperasi(){
            try{
                const axios = require('axios')
                console.log(this.loginService.getCurrentUsername())
                this.namaOperator = this.loginService.getCurrentUsername()
                const res =  await axios.get('/operator/get_operasi_byoperator/' + this.loginService.getCurrentUsername());
                if(res.data == null){
                    console.log("Data kosong")
                }else{
                    this.items = res.data
                    console.log(res,this.items)
                }
                console.log('Item : ',this.items)
                console.log("length : ",this.items.length)
                for(this.index in this.items){
                    if( this.items[this.index].mulai == null && this.items[this.index].selesai == null){
                        this.btn1 = {
                            color : 'green',
                            text : 'Operasi Mulai'
                        }
                        break
                    }
                    if( this.items[this.index].mulai != null && this.items[this.index].selesai == null){
                        this.btn1 = {
                            color : 'blue',
                            text : 'Operasi Selesai'
                        }
                        break
                    }
                    if( this.items[this.index].mulai != null && this.items[this.index].selesai != null && this.index == this.items.length-1){
                        this.btn1 = {
                            color : 'red',
                            text : 'Operasi Selesai Semua',
                            disabled : true
                        }
                        this.hasClicked = true
                    }   
                }
               
                if(this.itemKey[0].selesai != null){
                    this.hasClicked = true
                    const res2 =  await axios.post('/proyek/accumulate_percentage_proyek/' +  this.itemKey[0].id );
                    if(res2.data.status == 'berhasil'){
                        console.log(res2)
                    }else{
                    console.log(res2)
                    }   
                }
            }catch(error){
                console.log(error)
            }
        },*/

        async fetchOperasiLayak(){
            try{
                const axios = require('axios')
                const res = await axios.get('/operasi/show_operasilayak/' + this.loginService.getCurrentUsername())
                if(res.data.length == null){
                    console.log("Data kosong")
                }
                else if(res.data.length > 0){
                    this.items = res.data
                    console.log(res,this.items)
                }

            }catch(error){
                console.log(error)
            }  
        },

        async fetchOperasiSiap(){
            try{
                const axios = require('axios')
                console.log(this.loginService.getCurrentUsername())
                this.namaOperator = this.loginService.getCurrentUsername()
                const res = await axios.get('/operasi/get_operasi_siap/' + this.loginService.getCurrentUsername())
                if(res.data.length == 0){
                    console.log("Data kosong")
                    this.visible = false
                }else if(res.data.length > 0){
                    this.visible = true
                    this.items3 = res.data
                    console.log(res,this.items3)
                }

                for(this.index in this.items3){
                    if( this.items3[this.index].mulai == null && this.items3[this.index].selesai == null){
                        this.btn1 = {
                            color : 'green',
                            text : 'Operasi Mulai'
                        }
                        break
                    }
                    if( this.items3[this.index].mulai != null && this.items3[this.index].selesai == null){
                        this.btn1 = {
                            color : 'blue',
                            text : 'Operasi Selesai'
                        }
                        break
                    }
                    if( this.items3[this.index].mulai != null && this.items3[this.index].selesai != null && this.index == this.items3.length-1){
                        this.btn1 = {
                            color : 'red',
                            text : 'Operasi Selesai Semua',
                            disabled : true
                        }
                        this.hasClicked = true
                        this.visible = false
                    }   
                }
            }
            catch(error){
                console.log(error) 
            }
        },

        async fetchMaterial(){
            try{
                const axios = require('axios')
                const res = await axios.get('/operator/get_material_byoperator/' + this.loginService.getCurrentUsername())
                if(res.data == null){
                    console.log("Data kosong")
                }else{
                    this.items2 = res.data
                    console.log(res,this.items2)
                }
            }catch(error){
                console.log(error)
            }
        },

        startOperation(){
            this.loading = true
            setTimeout(() => {
                try{
                    //this.singleSelect = true
                    const axios = require('axios')
                    const res = axios.post('/operasi/response_operasi_mulai')
                    if(res.data.status == 'berhasil'){
                        console.log(res)
                    }
                }
                catch(error){
                    console.log(error)
                }
                this.dialog = false
                this.refresh()
            }, 2000)
        },
    
        akhiriOperation(){
            this.loading = true
            setTimeout(() => {
                try{
                    const axios = require('axios')
                    const res = axios.post('/operasi/response_operasi_selsai')
                    if(res.data.status == 'berhasil'){
                        console.log(res)
                    }
                }catch(error){
                    console.log(error)
                }
                this.refresh()
            }, 5000)
        },
        

        async getLinkOperator(){
            try{

                const axios = require('axios')
                const res = await axios.get('/operator/get_link_operator/' + this.loginService.getCurrentUsername())
                if (res.data == null){
                    console.log("data kosong")
                }else{
                    this.listOperatorPhoto = res.data
                    console.log("data terisi")
                    console.log(res,this.listOperatorPhoto)
                }

            }catch(error){
                console.log(error)
            }
        }
    },
   
}
</script>

<style>
    .v-navigation-drawer__content::-webkit-scrollbar-track{
        -webkit-box-shadow: inset 0 0 6px #5d5d5d;
        background-color: #5d5d5d;
    }
    .v-navigation-drawer__content::-webkit-scrollbar{
        width: 0px;
    }
    .v-navigation-drawer__content::-webkit-scrollbar-thumb{
        -webkit-box-shadow: inset 0 0 6px #424242;
        background-color: #424242;
    }
    #border{
        border-radius: 50%;
    }
</style>