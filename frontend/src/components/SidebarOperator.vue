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
                <span class="white--text mr-6">ws0001</span>
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
                <h3>Material</h3>
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
                    outlined
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
                {text : 'Code',         value : 'code'},
                {text : 'Nama',         value : 'nama'},
                {text : 'Email',        value : 'email'},
                {text : 'Alamat 1',     value : 'adress1'},
                {text : 'Kota',         value : 'city'},
                {text : 'Phone',        value : 'phone'},
                {text : 'Kode Pos',     value : 'postalcode'}
            ],
            headers2 : [
                {text : 'Code',         value : 'code'},
                {text : 'Nama',         value : 'nama'},
                {text : 'Email',        value : 'email'},
                {text : 'Alamat 1',     value : 'adress1'},
                {text : 'Kota',         value : 'city'},
                {text : 'Phone',        value : 'phone'},
                {text : 'Kode Pos',     value : 'postalcode'}
            ],
            items: undefined,
            items2: undefined,
        }
    },

    methods: {
        logout() {
            this.route = "/login"
            location.replace("/login")
            this.loginService.removeUserType()
        },
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