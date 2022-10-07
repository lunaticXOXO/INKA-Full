<template>
    <nav>
        <v-app-bar app color="#6f6f6f">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-btn icon :to="routeHome" class="mr-2">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <v-app-bar-title class="text-uppercase">
                <span class="font-weight-light white--text">Smart</span>
                <span class="white--text">Works 4.0 | Material</span>
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
            <v-img
                id="border" 
                max-height="40"
                max-width="40" 
                src="../assets/contoh-profile.jpg"
                class="mr-3 ml-6">
            </v-img>
            <span class="font-weight-light white--text ">Welcome,</span>
            <span class="white--text mr-6">material</span>
            <v-btn @click="logout()" color="grey">
                <span>Sign Out</span>
                <v-icon right>mdi-arrow-right</v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer app v-model="drawer" color="#555555" width="22%">
            <v-list>
                <v-list-group
                    v-for="item in items"
                    :key="item.title"
                    v-model="item.active"
                    >
                    <template v-slot:activator>
                    <v-list-item-action>
                        <v-icon class="white--text">{{item.action}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title class="white--text" v-text="item.title"></v-list-item-title>
                    </v-list-item-content>
                    </template>

                    <v-list-item
                    v-for="child in item.items"
                    :key="child.title"
                    :to="child.route"
                    >
                        <v-list-item-action>
                            <v-icon class="white--text ml-6">{{child.icon}}</v-icon>
                        </v-list-item-action>
                        <v-list-item-content>
                            <v-list-item-title class="white--text" v-text="child.title"></v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-navigation-drawer>
    </nav>
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
            items: [

                {
                   action: 'mdi-svg',
                    active: false,
                    items: [
                        {title : 'List Klasifikasi Material',icon : 'mdi-playlist-check',route : '/listKlasifikasiMaterial'},
                        {title : 'Add Klasifikasi Material',icon : 'mdi-plus',route : '/addKlasifikasiMaterial'}
                    ],  
                    title: 'Klasifikasi Material',  
                },
            
                 {
                   action: 'mdi-book',
                    active: false,
                    items: [
                       {title : 'List Grup Material',icon : 'mdi-playlist-check',route : '/listGrupMaterial'},
                       {title : 'Add Grup Material',icon : 'mdi-plus',route : '/addGrupMaterial'}
                    ],
                    title: 'Group Material',  
                },


                {
                    action: 'mdi-account-star',
                    active: false,
                    items: [
                        {title : 'List Pemasok',icon : 'mdi-playlist-check',route : '/listPemasok'},
                        { title: 'Tambah Pemasok', icon: 'mdi-account-plus', route: '/tambahPemasok'},
                    ],
                    title: 'Pemasok',
                },

                {
                    action: 'mdi-wrench',
                    active: false,
                    items: [
                        { title: 'Tambah Tipe Material', icon: 'mdi-sort-variant', route: '/jenisMaterial'},
                        { title: 'List Tipe Material', icon : 'mdi-filter-variant', route : '/listMaterialType'},
                    ],
                    title: 'Jenis Material',
                },

                {
                action: 'mdi-svg',
                active: false,
                items: [
                    { title: 'Purchase Material', icon: 'mdi-plus', route: '/pesanMaterial'},
                    {title : 'List Purchase Material', icon : 'mdi-filter-variant', route : '/listPurchaseMaterial'},
                    {title : 'Purchase Material Item',icon : 'mdi-plus',route : 'purchaseMaterialItem'},
                    {title : 'List Purchase Material Item',icon : 'mdi-gavel',route : '/listPurchaseMaterialItem'}
                    
                ],
                title: 'Purchase',
                },

                {
                action: 'mdi-blur',
                active: false,
                items: [

                    { title: 'List Stock Material', icon : 'mdi-filter-variant', route : '/listStockMaterial'},
                    { title : 'Add Stock Material', icon : 'mdi-plus',route : '/addStockMaterial'},
                    { title: 'Tambah Material Consumable', icon : 'mdi-plus', route : '/tambahMaterialConsumable'},
                ],
                title: 'Stock Material',
                },
             
            ],

        }
    },

    methods: {
        logout() {
            this.route = "/login"
            location.replace("/login")
            this.loginService.removeUserType()
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