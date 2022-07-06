import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GraphView from '../views/GraphView.vue'
import FormView from '../views/FormView.vue'
import LoginView from '../views/LoginView.vue'
import TableView from '../views/TableView.vue'
import TambahPelanggan from '../views/pelanggan/TambahDataPelanggan.vue'
import TambahPemasok from '../views/pemasok/TambahDataPemasok.vue'
import TambahKota from '../views/kota/TambahDataKota.vue'
import TambahNegara from '../views/negara/TambahDataNegara.vue'
import TambahOperator from '../views/operator/TambahDataOperator.vue'
import TambahTanggalLibur from '../views/referensi/TambahDataTanggalLibur.vue'
import TambahJnsProd from '../views/produk/TambahJenisProduk.vue'
import TambahStrProd from '../views/produk/TambahStrukturProduk.vue'
import TambahJnsMaterial from '../views/material/JenisMaterial.vue'
import PesanMaterial from '../views/material/PesanMaterial.vue'
import KelolaMaterial from '../views/material/KelolaMaterial.vue'
import TambahProyek from '../views/proyek/PesanProyek.vue'
import ProsesTerakhir from '../views/proyek/ProsesTerakhir.vue'
import TambahStasiunKerja from '../views/stasiunKerja/TambahStasiunKerja.vue'
import TambahLiniProduksi from '../views/stasiunKerja/TambahLiniProduksi.vue'
import LihatStasiunKerja from '../views/stasiunKerja/LihatStasiunKerja.vue'
import PantauOperasi from '../views/operasi/PantauOperasi.vue'
import LihatProyek from '../views/proyek/ProyekList.vue'
import ListPelanggan from '../views/pelanggan/ListPelanggan.vue'
import ProyekListbyCustomer from '../views/proyek/ProyekListByCustomer.vue'
import ListKota from '../views/kota/ListKota.vue'
import ListNegara from '../views/negara/ListNegara.vue'
import ListPemasok from '../views/pemasok/ListPemasok.vue'
import ListStasiun from '../views/stasiunKerja/ListStasiunKerja.vue'
import ListLiniProduksi from '../views/stasiunKerja/ListLiniProduksi.vue'
import ListRincianProyek from '../views/rincianproyek/ListRincianProyek.vue'
import ListRProyekbyProyek from '../views/rincianproyek/ListRProyekbyProyek.vue'
import ListOperasi from '../views/operasi/ListOperasi.vue'
import ListProduk from '../views/produk/ListProduk.vue'
import ListProdukbyRProyek from '../views/produk/ListProdukbyRProyek.vue'
import ListJenisProduk from '../views/produk/ListJenisProduk.vue'
import ListJenisProdukbyRProyek from '../views/produk/ListJenisProdukbyRProyek.vue'
import ListStruktrJenisProduk from '../views/produk/ListStrukturJenisProduk.vue'
import ListSJProdukbyJProduk from '../views/produk/ListSJProdukbyJProduk.vue'
import ListProses from '../views/proses/ListProses.vue'
import ListProsesbySJProduk from '../views/proses/ListProsesbySJProduk.vue'
import ListStasiunKerjabyProcess from '../views/stasiunKerja/ListStasiunKerjabyProcess.vue'
import TambahProses from '../views/proses/TambahProses.vue'
import AddRincianProyek from '../views/rincianproyek/AddRincianProyek.vue'
import AddRincianProyekbyProyek from '../views/rincianproyek/AddRincianProyekbyProyek.vue'
import TambahProduk from '../views/produk/TambahProduk.vue'
import TambahProdukbyRProyek from '../views/produk/TambahProdukbyRProyek.vue'
import TambahStrukturProdukbyProduk from '../views/produk/TambahStrukturProdukbyProduk.vue'
import PesanProyekbyCustomer from '../views/proyek/PesanProyekbyCustomer.vue'
import TambahStasiunKerjabyProcess from '../views/stasiunKerja/TambahStasiunKerjabyProcess.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomeView,
    meta: {
      title: "Home - PT.INKA"
    }
  },

  {
    path: '/graph',
    name: 'GraphPage',
    component: GraphView,
    meta: {
      title: "Graph - PT.INKA"
    }
  },

  {
    path: '/form',
    name: 'FormPage',
    component: FormView,
    meta: {
      title: "Form - PT.INKA"
    }
  },

  {
    path: '/login',
    name: 'LoginPage',
    component: LoginView,
    meta: {
      title: "Login - PT.INKA"
    }
  },

  {
    path: '/table',
    name: 'TablePage',
    component: TableView,
    meta: {
      title: "Table - PT.INKA"
    }
  },

  {
    path: '/tambahPelanggan',
    name: 'Tambah Data Pelanggan',
    component: TambahPelanggan,
    meta: {
      title: "Tambah Pelanggan - PT.INKA"
    }
  },

  {
    path: '/tambahPemasok',
    name: 'Tambah Data Pemasok',
    component: TambahPemasok,
    meta: {
      title: "Tambah Pemasok - PT.INKA"
    }
  },

  {
    path: '/tambahKota',
    name: 'Tambah Data Kota',
    component: TambahKota,
    meta: {
      title: "Tambah Kota - PT.INKA"
    }
  },
  
  {
    path: '/tambahNegara',
    name: 'Tambah Data Negara',
    component: TambahNegara,
    meta: {
      title: "Tambah Negara - PT.INKA"
    }
  },

  {
    path: '/tambahOperator',
    name: 'Tambah Data Operator',
    component: TambahOperator,
    meta: {
      title: "Tambah Operator - PT.INKA"
    }
  },

  {
    path: '/tambahLibur',
    name: 'Tambah Data Libur',
    component: TambahTanggalLibur,
    meta: {
      title: "Tambah Tanggal Libur - PT.INKA"
    }
  },

  {
    path: '/jenisProduk',
    name: 'Tambah Jenis Produk',
    component: TambahJnsProd,
    meta: {
      title: "Jenis Produk - PT.INKA"
    }
  },

  {
    path: '/strukturProduk',
    name: 'Tambah Struktur Produk',
    component: TambahStrProd,
    meta: {
      title: "Struktur Produk - PT.INKA"
    }
  },

  {
    path: '/pesanMaterial',
    name: 'Pesan Material',
    component: PesanMaterial,
    meta: {
      title: "Pesan Material - PT.INKA"
    }
  },

  {
    path: '/jenisMaterial',
    name: 'Tambah Jenis Material',
    component: TambahJnsMaterial,
    meta: {
      title: "Jenis Material - PT.INKA"
    }
  },

  {
    path: '/kelolaMaterial',
    name: 'Kelola Material',
    component: KelolaMaterial,
    meta: {
      title: "Kelola Material - PT.INKA"
    }
  },

  {
    path: '/lihatProyek',
    name: 'Lihat Proyek',
    component: LihatProyek,
    meta: {
      title: "List Proyek - PT.INKA"
    }
  },

  {
    path: '/pesanProyek',
    name: 'Tambah Proyek',
    component: TambahProyek,
    meta: {
      title: "Proyek Baru - PT.INKA"
    }
  },

  {
    path: '/prosesTerakhir',
    name: 'Proses Terakhir',
    component: ProsesTerakhir,
    meta: {
      title: "Proses Terakhir - PT.INKA"
    }
  },

  {
    path: '/tambahStasiunKerja',
    name: 'Tambah Stasiun Kerja',
    component: TambahStasiunKerja,
    meta: {
      title: "Stasiun Kerja - PT.INKA"
    }
  },

  {
    path: '/tambahLiniProduksi',
    name: 'Tambah Lini Produksi',
    component: TambahLiniProduksi,
    meta: {
      title: "Lini Produksi - PT.INKA"
    }
  },

  {
    path: '/lihatStasiunKerja',
    name: 'Lihat Stasiun Kerja',
    component: LihatStasiunKerja,
    meta: {
      title: "Lihat Stasiun Kerja - PT.INKA"
    }
  },

  {
     path : '/listStasiunKerjabyProcess/:id',
     name : 'List Stasiun Kerja by Process',
     component : ListStasiunKerjabyProcess,
     meta : {
        title : "List Stasiun Kerja by Process - PT. INKA"
     }

  },

  {
    path: '/pantauOperasi',
    name: 'Pantau Operasi',
    component: PantauOperasi,
    meta: {
      title: "Pantau Operasi - PT.INKA"
    }
  },

  {
    path : '/listPelanggan',
    name : 'List Pelanggan',
    component : ListPelanggan,
    meta :{
      title : "List Pelanggan - PT.INKA"
    }
  },

  {
    path : '/proyekListbyCustomer/:id',
    name : 'Proyek by Customer',
    component : ProyekListbyCustomer,
    meta :{
      title : "Proyek by Customer - PT.INKA"
    }
  },

  {
    path : '/listKota',
    name : 'List Kota',
    component : ListKota,
    meta :{
      title : "List Kota - PT.INKA"
    }
  },

  {
    path : '/listNegara',
    name : 'List Negara',
    component : ListNegara,
    meta :{
      title : "List Negara - PT.INKA"
    }
  },

  {
    path : '/listPemasok',
    name : 'List Pemasok',
    component : ListPemasok,
    meta :{
      title : "List Pemasok - PT.INKA"
    }
  },

  {
    path : '/listStasiun',
    name : 'List Stasiun',
    component : ListStasiun,
    meta : {
      title : "List Stasiun - PT.INKA"
    }
  },

  {
    path : '/listRincianProyek',
    name : 'List Rincian Proyek',
    component : ListRincianProyek,
    meta : {
      title : "List Rincian Proyek - PT.INKA"
    }
  },

  {
    path : '/listRProyekbyProyek/:id',
    name : 'List Rincian Proyek by Proyek',
    component : ListRProyekbyProyek,
    meta : {
        title : "List Rincian Proyek by Proyek - PT.INKA"
    }
  },

  {
    path : '/listOperasi',
    name : 'List Operasi',
    component : ListOperasi,
    meta : {
      title : "List Operasi - PT.INKA"
    }
  },

  {
    path : '/listProduk',
    name : 'List Produk',
    component : ListProduk,
    meta: {
      title : "List Produk - PT.INKA"
    }
  },  
  
  {
    path : '/listProdukbyRProyek/:id',
    name : 'List Produk by Rincian Proyek',
    component : ListProdukbyRProyek,
    meta : {
      title : "List Produk by Rincian Proyek - PT.INKA"
    }
  },

  {
    path : '/listJenisProduk',
    name : 'List Jenis Produk',
    component : ListJenisProduk,
    meta : {
      title : "List Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listJenisProdukbyRProyek/:id',
    name : 'List Jenis Produk by RProyek',
    component : ListJenisProdukbyRProyek,
    meta : {
      title : "List Jenis Produk by R.Proyek - PT.INKA"
    }
  },

  {
    path : '/listStrukturJenisProduk',
    name : 'List Struktur Jenis Produk',
    component : ListStruktrJenisProduk,
    meta : {
      title : "List Struktur Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listStrukturJenisProduk/:id',
    name : 'List Struktur Jenis Produk by Jenis Produk',
    component :  ListSJProdukbyJProduk,
    meta : {
      title : "List Struktur Jenis Produk by Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listProcess',
    name : 'List Process',
    component : ListProses,
    meta : {
      title : "List Proses - PT.INKA"
    }
  },

  {
    path : '/listProcessbySJProduk/:id',
    name : 'List Process by Struktur Jenis Produk',
    component : ListProsesbySJProduk,
    meta : {
      title : "List Process by Struktur Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listLiniProduksi',
    name : 'List Lini Produksi',
    component : ListLiniProduksi,
    meta : {
      title : "List Lini Produksi - PT.INKA"
    }
  },

  {
    path : '/tambahProses',
    name : 'Tambah Proses Baru',
    component : TambahProses,
    meta : {
      title : "Tambah Proses - PT.INKA"
    }
  },

  {
    path : '/tambahRincianProyek',
    name : 'Tambah Rincian Proyek',
    component : AddRincianProyek,
    meta : {
      title : "Tambah Rincian Proyek - PT.INKA"
    }
  },
  {
    path : '/tambahRProyekbyProyek/:id',
    name : 'Tambah Rincian Proyek by Proyek',
    component : AddRincianProyekbyProyek,
    meta : {
      title : "Tambah Rincian Proyek by Proyek - PT INKA"
    }
  },

  {
    path : '/tambahProduk',
    name : 'Tambah Produk',
    component : TambahProduk,
    meta : {
      title : "Tambah Produk - PT.INKA"
    }
  },
  {
    path : '/tambahProdukbyRProyek/:id',
    name : 'Tambah Produk by RProyek',
    component : TambahProdukbyRProyek,
    meta : {
      title : "Tambah Produk by Rincian Proyek - PT.INKA"
    }
  },
  {
    path : '/tambahSJProdukbyProduk/:id',
    name : 'Tambah Struktur Jenis Produk by Jenis Produk',
    component : TambahStrukturProdukbyProduk,
    meta : {
      title : "Tambah Sturktur Jenis Produk by Jenis Produk - PT.INKA"
    }
  },
  {
    path : '/pesanProyekbyCustomer/:id',
    name : 'Tambah Proyek by Customer',
    component : PesanProyekbyCustomer,
    meta : {
        title : "Tambah Proyek by Customer - PT.INKA"
    }
  },
  {
    path : '/addStasiunKerjabyProcess/:id',
    name : 'Tambah Stasiun Kerja by Process',
    component : TambahStasiunKerjabyProcess,
    meta : {
      title : "Memilih Stasiun Kerja by Process - PT.INKA"
    }
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// This callback runs before every route change, including on page load.
router.beforeEach((to, from, next) => {
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // e.g., if we have `/some/deep/nested/route` and `/some`, `/deep`, and `/nested` have titles,
  // `/nested`'s will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if(nearestWithTitle) {
    document.title = nearestWithTitle.meta.title;
  } else if(previousNearestWithMeta) {
    document.title = previousNearestWithMeta.meta.title;
  }

  // Remove any stale meta tags from the document using the key attribute we set below.
  Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));

  // Skip rendering meta tags if there are none.
  if(!nearestWithMeta) return next();

  // Turn the meta tag definitions into actual elements in the head.
  nearestWithMeta.meta.metaTags.map(tagDef => {
    const tag = document.createElement('meta');

    Object.keys(tagDef).forEach(key => {
      tag.setAttribute(key, tagDef[key]);
    });

    // We use this to track which meta tags we create so we don't interfere with other ones.
    tag.setAttribute('data-vue-router-controlled', '');

    return tag;
  })
  // Add the meta tags to the document head.
  .forEach(tag => document.head.appendChild(tag));

  next();
});

export default router
