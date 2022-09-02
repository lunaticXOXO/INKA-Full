<template>
    <v-main>
        <nav>
            <v-app-bar app color="#6f6f6f">
                <v-app-bar-title class="text-uppercase">
                    <span class="font-weight-light white--text">Smart</span>
                    <span class="white--text">Works 4.0 | WS</span>
                </v-app-bar-title>
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
                <span class="white--text mr-6"></span>
                <v-btn @click="logout()" color="grey">
                    <span>Sign Out</span>
                    <v-icon right>mdi-arrow-right</v-icon>
                </v-btn>
            </v-app-bar>
        </nav>
        <div class="d-flex">
            <div class = "ma-6">
                <h3>Operasi</h3>
                <v-card class="mx-auto mb-6 text-center mt-6" width="900">
                    <v-data-table
                        :headers = "headers"
                        :items = "items">
                    </v-data-table>
                </v-card>
                <h3>Material yang diperlukan</h3>
                <v-card class="mx-auto mb-6 text-center mt-6" width="900">
                    <v-data-table
                        :headers = "headers2"
                        :items = "items2">
                    </v-data-table>
                </v-card>
            </div>
            <div class = "ma-6">
                <h3>Operator</h3>
                <div class="mx-auto mt-6">
                    <span class="mr-10">Foto</span>
                    <span class="ml-10">Nama</span>
                </div>
                <div class="mt-10">
                    <v-text-field
                    v-model="kodeMaterial"
                    disabled
                    >
                    </v-text-field>
                    <v-btn class="mx-auto blue white--text" width="350">
                        OPERASI SELESAI
                    </v-btn>
                </div>
            </div>
        </div>
    </v-main>
</template>

<script>
import Login from "../services/Login.js"
export default {
    data(){
        return {
            loginService: new Login(),
            route: "/login",
            routeHome: "/",
            drawer: false,
            headers : [
                {text : 'Code',               value : 'idOperasi'},
                {text : 'Nama',               value : 'namaProses'},
                {text : 'Rencana Mulai',      value : 'rencanaMulai'},
                {text : 'Rencana Selesai',    value : 'rencanaSelesai'},
                {text : 'Mulai',              value : 'mulai'},
                {text : 'Selesai',            value : 'selesai'},
              
            ],
            headers2 : [
                {text : 'Code',         value : 'code'},
                {text : 'Nama',         value : 'nama'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Satuan',value : 'satuan'}
            ],
            items: undefined,
            items2: undefined,
           
        }
    },
    mounted(){
        this.fetchOperasi(),
        this.fetchMaterial()
    },
    methods: {
        logout() {
            this.route = "/login"
            location.replace("/login")
            this.loginService.removeUserType()
        },

       async fetchOperasi(){
            try{

            const axios = require('axios')
            console.log(this.loginService.getCurrentUsername())
            const res =  await axios.get('/operator/get_operasi_byoperator/' + this.loginService.getCurrentUsername() );
            if(res.data == null){
                console.log("Data kosong")
            }else{
                this.items = res.data
                console.log(res,this.items)
            }
            }catch(error){
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