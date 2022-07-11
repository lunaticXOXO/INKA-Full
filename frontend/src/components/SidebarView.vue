<template>
    <nav>
        <v-app-bar app color="#6f6f6f">
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-btn icon :to="routeHome" class="mr-2">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <v-app-bar-title class="text-uppercase">
                <span class="font-weight-light white--text">Smart</span>
                <span class="white--text">Works 4.0</span>
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
            <span class="white--text mr-6">Username</span>
            <v-btn :to="route" color="grey">
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
export default {
    data(){
        return {
            route: "/login",
            routeHome: "/",
            drawer: false,
            items: [
                {
                action: 'mdi-checkbox-multiple-blank-outline',
                active: false,
                items: [
                    { title: 'Pemesanan', icon: 'mdi-pencil', route: '/pesanMaterial'},
                    { title: 'Pengelolaan', icon: 'mdi-laptop', route: '/kelolaMaterial'},
                    { title: 'Jenis Material', icon: 'mdi-cards-variant', route: '/jenisMaterial'},
                ],
                title: 'Material',
                },

                {
                action: 'mdi-chart-ppf',
                active: false,
                items: [
                    { title: 'Lihat Produk', icon: 'mdi-eye',route : '/listProduk'},
                    { title: 'Lihat Jenis Produk',icon : 'mdi-eye',route : '/listJenisProduk'},
                    { title: 'Lihat Struktur Tipe Produk',icon : 'mdi-eye',route : '/listStrukturJenisProduk'},
                    { title: 'Tambah Produk', icon: 'mdi-plus', route: '/tambahProduk'},
                    { title: 'Tambah Jenis Produk', icon: 'mdi-plus', route: '/jenisProduk'},
                    { title: 'Tambah Struktur Tipe Produk', icon: 'mdi-plus', route: '/strukturProduk'},
                ],
                title: 'Produk',
                },

                {
                action: 'mdi-projector-screen-variant-outline',
                active: false,
                items: [
                    { title: 'List Proyek', icon: 'mdi-filter-variant', route: '/lihatProyek'},
                    { title: 'Tambah Proyek', icon: 'mdi-plus', route: '/pesanProyek'},
                    { title: 'Proses Terakhir', icon: 'mdi-state-machine', route: '/prosesTerakhir'},
                ],
                title: 'Proyek',
                },

                {
                action: 'mdi-book-open-outline',
                active: false,
                items: [
                    { title: 'List Rincian Proyek', icon: 'mdi-filter-variant', route: '/listRincianProyek'},
                    { title: 'Tambah Rincian Proyek', icon: 'mdi-plus', route: '/tambahRincianProyek'},
                ],
                title: 'Rincian Proyek',
                },
                
                {
                action: 'mdi-book-open-outline',
                active: false,
                items: [
                    { title: 'Lihat List Proses', icon: 'mdi-eye', route: '/listProcess'},
                    { title: 'Tambah Proses', icon: 'mdi-plus', route: '/tambahProses'},
                ],
                title: 'Proses',
                },
                
                {
                action: 'mdi-view-list',
                active: false,
                items: [
                    { title: 'List', icon: 'mdi-filter-variant', route: '/listOperasi'},
                    { title: 'Pantau Operasi', icon: 'mdi-eye', route: '/pantauOperasi'},
                ],
                title: 'Operasi',
                },

                {
                action: 'mdi-blur',
                active: false,
                items: [
                    { title: 'Pemesanan Material', icon: 'mdi-reorder-vertical', route: '/pesanMaterial'},
                    { title: 'Pengelolaan Material', icon: 'mdi-key-outline', route: '/kelolaMaterial'},
                    { title: 'Jenis Material', icon: 'mdi-sort-variant', route: '/jenisMaterial'},
                ],
                title: 'Material',
                },

                {
                action: 'mdi-garage-variant',
                active: false,
                items: [
                    { title: 'Tambah', icon: 'mdi-plus', route: '/tambahStasiunKerja'},
                    { title: 'Tambah Lini Produksi', icon: 'mdi-plus', route: '/tambahLiniProduksi'},
                    { title: 'Lihat Stasiun Kerja', icon: 'mdi-eye', route: '/lihatStasiunKerja'},
                    { title: 'List Stasiun Kerja', icon: 'mdi-filter-variant', route: '/listStasiun'},
                    { title: 'List Lini Produksi', icon: 'mdi-filter-variant', route: '/listLiniProduksi'},
                ],
                title: 'Stasiun Kerja',
                },

                {
                action: 'mdi-account-multiple',
                active: false,
                items: [
                    { title: 'List Pelanggan', icon: 'mdi-playlist-check', route: '/listPelanggan'},
                    { title: 'Tambah Pelanggan', icon: 'mdi-account-plus', route: '/tambahPelanggan'},
                ],
                title: 'Pelanggan',
                },

                {
                action: 'mdi-database',
                active: false,
                items: [
                    { title: 'Tambah Pemasok', icon: 'mdi-account-plus', route: '/tambahPemasok'},
                ],
                title: 'Pemasok',
                },

                {
                action: 'mdi-account-star',
                active: false,
                items: [
                    { title: 'Tambah Operator', icon: 'mdi-account-plus', route: '/tambahOperator'},
                ],
                title: 'Operator',
                },

                {
                action: 'mdi-city',
                active: false,
                items: [
                    { title: 'Lihat Kota', icon: 'mdi-eye', route: '/listKota'},
                    { title: 'Tambah Kota', icon: 'mdi-plus', route: '/tambahKota'},
                ],
                title: 'Kota',
                },

                {
                action: 'mdi-flag',
                active: false,
                items: [
                    { title: 'Lihat Negara', icon: 'mdi-eye', route: '/listNegara'},
                    { title: 'Tambah Negara', icon: 'mdi-plus', route: '/tambahNegara'},
                ],
                title: 'Negara',
                },

                {
                action: 'mdi-code-brackets',
                active: false,
                items: [
                    { title: 'Tanggal Libur', icon: 'mdi-calendar-range', route: '/tambahLibur'},
                ],
                title: 'Referensi',
                },

                {
                action: 'mdi-book-variant',
                active: false,
                items: [
                    { title: 'Form', icon: 'mdi-note-plus-outline', route: '/form'},
                    { title: 'Graph', icon: 'mdi-chart-line-variant', route: '/graph'},
                    { title: 'Table', icon: 'mdi-table', route: '/table'},
                ],
                title: 'Dummy',
                },
            ],
        }
    },
    methods: {

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