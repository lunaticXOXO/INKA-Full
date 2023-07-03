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
import TambahProsesBySJProduk from '../views/proses/TambahProsesBySJProduk.vue'
import ListJenisProses from '../views/proses/ListJenisProses.vue'
import TambahJenisProses from '../views/proses/TambahJenisProses.vue'
import ListKlasifikasiMaterial from '../views/material/ListKlasifikasiMaterial.vue'
import AddKlasifikasiMaterial from '../views/material/AddKlasifikasiMaterial.vue'
import ListGrupMaterial from '../views/material/ListGrupMaterial.vue'
import AddGrupMaterial from '../views/material/AddGrupMaterial.vue'
import ListMaterialType from '../views/material/ListMaterialType.vue'
import ListStockMaterial from '../views/material/ListStockMaterial.vue'
import TambahMaterialKosong from '../views/material/TambahMaterialKosong.vue'
import TambahMaterialConsumable from '../views/material/TambahMaterialConsumable.vue'
import LihatStatusPengerjaanWS from '../views/stasiunKerja/LihatStatusPengerjaanWS.vue'
import LihatStatusPengerjaanProyek from '../views/proyek/StatusPengerjaanProyek.vue'
import OperasibyProduct from '../views/operasi/ListOperasibyProduct.vue'
import ListOperator from '../views/operator/ListOperator.vue'
import ListOperatorRFID from '../views/operator/ListOperatorRFID.vue'
import TambahKemampuanOperator from '../views/operator/TambahKemampuanOperator.vue'
import ListOperatorHadir from '../views/operator/ListOperatorHadir.vue'
import ListRProyekbyProyekDSP from '../views/rincianproyek/ListRProyekbyProyekDSP.vue'
import ListProdukbyRProyekDSP from '../views/produk/ListProdukbyRProyekDSP.vue'
import StatusOperasi from '../views/operasi/StatusOperasi.vue'
import ListTanggalLibur from '../views/referensi/ListTanggalLibur.vue'
import ListMaterialTypeBySupplier from '../views/pemasok/ListMaterialByPemasok.vue'
import TambahMaterialTypeByPemasok from '../views/pemasok/TambahMaterialTypeByPemasok.vue'
import ListPurchaseMaterial from '../views/material/ListPurchaseMaterial.vue'
import PurchaseMaterialItem from '../views/material/PurchaseMaterialItem.vue'
import ListPurchaseMaterialItem from '../views/material/ListPurchaseMaterialItem.vue'
import AddStockMaterial from '../views/material/AddStockMaterial.vue'
import ListStockMaterialByOrders from '../views/material/ListStockMaterialByOrders.vue'
import ListPurchaseItemByPurchaseMaterial from '../views/material/ListPurchaseItembyPurchaseMaterial.vue'
import PurchaseMaterialItemByPurchaseMaterial from '../views/material/PurchaseItemByPurchaseMaterial.vue'
import AddMaterialStockbyPurchaseItem from '../views/material/AddStockMaterialbyPurchaseItem.vue'
import ListPurchaseMaterialStock from '../views/material/ListPurchaseMaterialStock.vue'
import ListPurchaseItemMaterialStock from '../views/material/ListPurchaseItemMaterialStock.vue'
import ListMaterialStockOnWs from '../views/material/ListMaterialStockOnWs.vue'
import StatusBarcode from '../views/material/StatusBarcode.vue'
import MaterialLogin from '../views/material/MaterialLogin.vue'
import ListOperasibyProduct from '../views/operasi/listOperasiByProduk.vue'
import TambahJenisProdukInternal from '../views/produk/TambahJenisProdukInternal.vue'
import TambahStrukturJenisProdukByParent from '../views/produk/TambahStrukturJenisProdukByParent.vue'
import ListKartu from '../views/operator/PendaftaranKartu.vue'
import FormKartu from '../views/operator/FormPendaftaranKartu.vue'
import ListToolBox from '../views/tools/ShowToolBox.vue'
import TambahToolBox from '../views/tools/AddToolBox.vue'
import TambahToolTypeConsume from '../views/tools/AddToolTypeConsume.vue'
import TambahToolTypeNonConsume from '../views/tools/AddToolTypeNonConsume.vue'
import TambahToolStockByBox from '../views/tools/AddToolStockByBox.vue'
import ShowToolPurchase from '../views/tools/ShowToolPurchase.vue'
import AddToolPurchase from '../views/tools/AddToolPurchase.vue'
import ListPesanMaterial from '../views/material/ListPesanMaterial.vue'
import ListPurchaseMaterialNew from '../views/material/ListPurchaseMaterialNew'
import ListPurchaseItembyPurchaseMaterialNew from '../views/material/ListPurchaseItembyPurchaseMaterialNew'
import ListPeringkatSupplier from '../views/pemasok/ListPeringkatSupplier.vue'
import ListDetailPeringkatBySupplier from '../views/pemasok/ListDetailPeringkatBySupplier.vue'
import ListPeringkatKriteria from '../views/pemasok/ListPeringkatKriteria.vue'
import ShowToolPurchaseItemByPurchase from '../views/tools/ShowToolPurchaseItemByPurchase.vue'
import ShowToolStockByPurchaseItem from '../views/tools/ShowToolStockByPurchaseItem.vue'
import ShowToolStock from '../views/tools/ShowToolStock.vue'
import ShowDetailToolStock from '../views/tools/ShowDetailToolStock.vue'
import ChooseKebutuhanTool from '../views/tools/ChooseKebutuhanTool.vue'
import ListKriteriaPemasok from '../views/pemasok/ListKriteriaPemasok.vue'
import PerhitunganKriteria from '../views/pemasok/PerhitunganKriteria.vue'
import AddDistribusiTools from '../views/tools/AddDistribusiTools.vue'
import ListToolNeedByProcess from '../views/tools/ListToolNeedByProcess.vue'
import ListPenghitungKriteria from '../views/pemasok/ListPenghitungKriteria.vue'
import PerhitunganSupplier from '../views/pemasok/PerhitunganSupplier.vue'
import ListToolNeedByWorkstation from '../views/tools/ListToolNeedByWorkstation.vue'
import ChoosePeminjamanTool from '../views/tools/ChoosePeminjamanTool.vue'
import ChooseWorkstation from '../views/tools/ChooseWorkstation.vue'
import ShowToolsOnWorkstation from '../views/tools/ShowToolsOnWorkstation.vue'
import ListHasilPerhitunganKriteria from '../views/pemasok/ListHasilPerhitunganKriteria.vue'
import ListPenghitungSupplier from '../views/pemasok/ListPenghitungSupplier.vue'
import ListHasilPerhitunganSupplier1 from '../views/pemasok/ListHasilPerhitunganSupplier1.vue'
import ListHasilPerhitunganSupplier2 from '../views/pemasok/ListHasilPerhitunganSupplier2.vue'
import HasilPerhitunganKriteriaByAdmin from '../views/pemasok/HasilPerhitunganKriteriaByAdmin.vue'
import ListAdminPenghitung from '../views/pemasok/ListAdminPenghitung.vue'
import HasilPerbandinganSupplierByAdmin from '../views/pemasok/HasilPerbandinganSupplierByAdmin.vue'
import HasilBobotPeringkatSupplierByAdmin from '../views/pemasok/HasilBobotPeringkatSupplierByAdmin.vue'

//import ListToolsByProcess from '../views/tools/ListToolsByProcess.vue'

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
    path: '/tambahJenisProduk',
    name: 'Tambah Jenis Produk',
    component: TambahJnsProd,
    meta: {
      title: "Tambah Jenis Produk - PT.INKA"
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
    path : '/listPurchaseMaterial',
    name : 'List Purchase Material',
    component : ListPurchaseMaterial,
    meta : {
        title : "List Purchase Material - PT.INKA"
    }
  },

  {

    path : '/purchaseMaterialItem',
    name : 'Purchase Material Item',
    component : PurchaseMaterialItem,
    meta : {
        title : "Purchase Material Item - PT.INKA"
    }

  },


  {
      path : '/listPurchaseMaterialItem',
      name : 'List Purchase Material Item',
      component : ListPurchaseMaterialItem,
      meta : {
          title : "List Purchase Material Item - PT.INKA"
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

      path : '/listJenisProses',
      name : 'List Jenis Proses',
      component : ListJenisProses,
      meta : {
         title : "List Jenis Proses - PT.INKA"
      }
       
    },

    {

      path : '/addJenisProses',
      name : 'Tambah Jenis Proses',
      component : TambahJenisProses,
      meta : {
        title : "Tambah Jenis Proses - PT.INKA"
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
  },

  {
    path : '/tambahProsesbySJProduk/:id',
    name : 'Tambah Proses by Struktur Jenis Produk',
    component : TambahProsesBySJProduk,
    meta : {
      title : "Tambah Proses by Struktur Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listMaterialType',
    name : 'List Tipe Material',
    component : ListMaterialType,
    meta : {
      title : "List Tipe Material - PT.INKA"
    }
  },

  {
    path : '/listStockMaterial',
    name : 'List Stock Material',
    component : ListStockMaterial,
    meta : {
      title : "List Stock Material - PT.INKA"
    }
  },

  {
    path : '/addStockMaterial',
    name : 'Add Stock Material',
    component : AddStockMaterial,
    meta : {
      title : "Add Stock Material - PT.INKA"
    }
  },

  {
    path : '/tambahMaterialKosong/:id',
    name : 'Tambah Material Kosong',
    component : TambahMaterialKosong,
    meta : {
      title : "Tambah Material Kosong - PT.INKA"
    }
  },
  {
    path : '/listKlasifikasiMaterial',
    name : 'List Klasifikasi Material',
    component : ListKlasifikasiMaterial,
    meta : {
      title : "List Klasifikasi Material - PT.INKA"
    },
  },
  {
     path : '/addKlasifikasiMaterial',
     name : 'Tambah Klasifikasi Material',
     component : AddKlasifikasiMaterial,
     meta : {
         title : "Tambah Klasifikasi Material"
     }
  },

  {
    path : '/addGrupMaterial',
    name : 'Add Grup Material',
    component : AddGrupMaterial,
    meta : {
      title : "Tambah Grup Material"
    },
  },
  {
    path : '/listGrupMaterial',
    name : 'List Grup Material',
    component : ListGrupMaterial,
    meta : {
      title : "List Grup Material - PT.INKA"
    },
  },
  {
    path : '/tambahMaterialConsumable',
    name : 'Tambah Material Consumable',
    component : TambahMaterialConsumable,
    meta : {
      title : "Tambah Material Consumable - PT.INKA"
    }
  },

  {
    path : '/statusPengerjaanWS',
    name : 'Status Pengerjaan WS',
    component : LihatStatusPengerjaanWS,
    meta : {
      title : "Status Pengerjaan WS - PT.INKA"
    }
  },

  {
    path : '/statusPengerjaanProyek',
    name : 'Status Pengerjaan Proyek',
    component : LihatStatusPengerjaanProyek,
    meta : {
      title : "Status Pengerjaan Proyek - PT.INKA"
    }
  },

  {
    path : '/operasibyProduct/:id',
    name : 'Operasi by Produk',
    component : OperasibyProduct,
    meta : {
      title : "Operasi by Produk - PT.INKA"
    }
  },

  {
    path : '/listOperator',
    name : 'List Operator',
    component : ListOperator,
    meta : {
      title : "List Operator - PT.INKA"
    }
  },

  {
    path : '/listOperatorRFID',
    name : 'List Operator RFID',
    component : ListOperatorRFID,
    meta : {
      title : "List Operator RFID - PT INKA"
    }
  },

  {
    path : '/tambahKemampuanOperator/:id',
    name : 'Tambah Kemampuan Operator',
    component : TambahKemampuanOperator,
    meta : {
      title : "Tambah Kemampuan Operator - PT.INKA"
    }
  },

  {
    path : '/listOperatorHadir',
    name : 'List Operator Hadir',
    component : ListOperatorHadir,
    meta : {
      title : "List Operator Hadir - PT.INKA"
    }
  },

  {
    path : '/listRProyekbyProyekDSP/:id',
    name : 'List Rincian Proyek by Proyek DSP',
    component : ListRProyekbyProyekDSP,
    meta : {
      title : "List Rincian Proyek by Proyek DSP - PT.INKA"
    }
  },

  {
    path : '/listProdukbyRProyekDSP/:id',
    name : 'List Produk by Rproyek DSP',
    component : ListProdukbyRProyekDSP,
    meta : {
      title : "List Produk by Rincian Proyek DSP - PT.INKA"
    }
  },

  {
    path : '/statusOperasi',
    name : 'Status Operasi',
    component : StatusOperasi,
    meta : {
      title : "Status Operasi - PT.INKA"
    }
  },

  {
    path : '/listTanggalLibur',
    name : 'List Tanggal Libur',
    component : ListTanggalLibur,
    meta : {
      title : "List Tanggal Libur - PT.INKA"
    }
  },

  {
    path : '/listMaterialTypeBySupplier/:id',
    name : 'List Material Type By Supplier',
    component : ListMaterialTypeBySupplier,
    meta : {
      title : "List Material Type By Supplier - PT.INKA"
    }
  },

  {
    path : '/tambahMaterialTypeByPemasok/:id',
    name : 'Tambah Material Type By Pemasok',
    component : TambahMaterialTypeByPemasok,
    meta : {
      title : "Tambah Material Type By Pemasok - PT.INKA"
    }
  },

  {
    path : '/listPurchaseItemByPurchaseMaterial/:id',
    name : 'List Purchase Item By Purchase Material',
    component : ListPurchaseItemByPurchaseMaterial,
    meta : {
      title : "List Purchase Item By Purchase Material - PT.INKA"
    }  
  },
  
  {
    path : '/tambahPurchaseItemByPurchaseMaterial/:id',
    name : 'Tambah Purchase Item By Purchase Material',
    component : PurchaseMaterialItemByPurchaseMaterial,
    meta : {
      title : "Tambah Purchase Item By Purchase Material - PT.INKA"
    }
  },

  {
    path : '/listStockMaterialbyOrder/:id',
    name : 'List Stock Material By Orders',
    component : ListStockMaterialByOrders,
    meta : {
      title : "List Stock Material by Orders - PT.INKA"
    }
  },

  {
    path : '/addStockMaterialbyPurchaseItem/:id',
    name : 'Add Material Stock By Purchase Item',
    component : AddMaterialStockbyPurchaseItem,
    meta : {
      title : "Add Material Stock By Purchase Item - PT.INKA"
    }
  },

  {
    path : '/listPurchaseMaterialStock',
    name : 'List Purchase Material Stock',
    component : ListPurchaseMaterialStock,
    meta : {

       title : "List Purchase Material Stock - PT.INKA"

    }
  },

  {
    path : '/listPurchaseItemMaterialStock/:id',
    name : 'List Purchase Item Material Stock',
    component : ListPurchaseItemMaterialStock,
    meta : {

        title : "List Purchase Item Material Stock - PT.INKA"
    }
  },

  {
    path : '/listStockMaterialOnWS/:id',
    name : 'List Stock Material On WS',
    component : ListMaterialStockOnWs,
    meta : {
      title : "List Stock Material On WS - PT.INKA "
    }
  },

  {

    path : '/listHarusPesanMaterial',
    name : 'List Harus Pesan Material New',
    component : ListPesanMaterial,
    meta : {
      title : "List Material Yang Harus Dipesan"
    }

  },

  {
    path : '/statusBarcode',
    name : 'Status Barcode',
    component : StatusBarcode,
    meta : {
      title : "Status Barcode - PT.INKA"
    }
  },

  {
    path : '/listMatLogin',
    name : 'Material Login',
    component : MaterialLogin,
    meta : {
      title : "List Material Loin - PT.INKA"
    }
  },

  {
    path : '/listOperasiByProduk/:id',
    name : 'List Operasi By Produk Tabel',
    component : ListOperasibyProduct,
    meta : {
      title : "List Operasi By Produk - PT. INKA"
    }
  },

  {
    path : '/tambahJenisProdukInternal',
    name : 'Tambah Jenis Produk Internal',
    component : TambahJenisProdukInternal,
    meta : {
        title : "Tambah Jenis Produk Internal - PT.INKA"
    }
  },

  {
    path : '/tambahStrukturJenisProdukByParent/:id',
    name : 'Tambah Struktur Jenis Produk By Parent',
    component : TambahStrukturJenisProdukByParent,
    meta : {
      title : "Tambah Node Sturktur Jenis Produk - PT.INKA"
    }
  },

  {
    path : '/listKartu',
    name : 'Daftar RFID',
    component : ListKartu,
    meta : {
      title : "Daftar RFID - PT.INKA"
    }
  },

  {
    path : '/daftarKartu/:id',
    name : 'Form Daftar RFID',
    component : FormKartu,
    meta : {
      title : "Form Daftar RFID - PT.INKA"
    }
  },
  
  {
    path : '/showToolBox',
    name : 'List Tool Box',
    component : ListToolBox,
    meta : {
      title : "List Tool Box - PT.INKA"
    }
  },

  {
    path : '/addToolBox',
    name : 'Tambah Tool Box',
    component : TambahToolBox,
    meta : {
      title : "Tambah Tool Box - PT.INKA"
    }
  },

  {
    path : '/addToolTypeConsume',
    name : 'Tambah Tool Type Consumable',
    component : TambahToolTypeConsume,
    meta : {
      title : "Tambah Tool Type Consumable - PT.INKA"
    }
  },

  {
    path : '/addToolTypeNonConsume',
    name : 'Tambah Tool Type Non Consumable',
    component : TambahToolTypeNonConsume,
    meta : {
      title : "Tambah Tool Type Non Consumable - PT.INKA"
    }
  },

  {
    path : '/addToolStockByBox/:id',
    name : 'Tambah Tool Stock By Box',
    component : TambahToolStockByBox,
    meta : {
      title : "Tambah Tool Stock By Box - PT.INKA"
    }
  },

  {
    path : '/listPurchaseTools',
    name : 'List Purchase Tools',
    component : ShowToolPurchase,
    meta : {
        title : "List Purchase Tools - PT.INKA"
    }
  },
 {
    path : '/purchaseTools',
    name : 'Purchase Tools',
    component : AddToolPurchase,
    meta : {
      title : "Add Purchase Tools - PT.INKA"
    }

 },

 {

    path : '/listPurchaseItemByPurchaseMaterialNew/:id',
    name : 'List Purchase Item By Purchase Material New',
    component : ListPurchaseItembyPurchaseMaterialNew,
    meta : {
        title : "List Purchase Item By Purchase Material - PT.INKA"
    }

 },

 {
    path : '/listPurchaseMaterialNew',
    name : 'List Purchase Material New',
    component : ListPurchaseMaterialNew,
    meta : {
      title : "List Purchase Material New - PT.INKA"
    }
 },

//  {
//    path : '/listPurchaseItemToolsByPurchase/:id',
//    name : 'List Purchase Item By Tool Purchase',
//    component : ShowToolPurchaseItemByPurchase,
//    meta : {
//       title : "List Purchase Item By Tool Purchase - PT.INKA "
//    }

//  ,


{
    path : '/listPeringkatSupplier',
    name : 'List Peringkat Supplier',
    component : ListPeringkatSupplier,
    meta : {
        title : "List Peringkat Supplier - PT.INKA"
    }
},

{
  path : '/listDetailPeringkatSupplier/:id',
  name : 'List Detail Peringkat By Supplier',
  component : ListDetailPeringkatBySupplier,
  meta : {
      title : "List Detail Peringkat Supplier - PT.INKA"
  }
},

{
     
    path : '/listPeringkatKriteria',
    name : 'List Peringkat Kriteria',
    component : ListPeringkatKriteria,
    meta : {
      title : "List Peringkat Kriteria - PT.INKA"
    }


},

{

    path : '/listPurchaseItemByPurchaseTools/:id',
    name : 'List Purchase Item By Purchase Tools',
    component : ShowToolPurchaseItemByPurchase,
    meta : {
        title : "List Purchase Item By Purchase - PT.INKA"
    }

},

{
   path : '/listToolStockByPurchaseItem/:id',
   name : 'List Tools Stock By Purchase Item',
   component : ShowToolStockByPurchaseItem,
   meta : {
      title : "List Tool Stock By Purchase Item - PT.INKA"
   }

},

{
  path : '/listToolStock',
  name : 'List Tool Stock',
  component : ShowToolStock,
  meta : {
    title : "List Tool Stock - PT.INKA"
  }

},
      
{
  path : '/listDetailToolStock/:id',
  name : 'List Detail Tool Stock By Tool Stock',
  component : ShowDetailToolStock,
  meta : {
    title : "List Detail Tool Stock - PT.INKA"
  }
},

{

   path : '/chooseKebutuhanTool',
   name : 'Choose Kebutuhan Tool',
   component : ChooseKebutuhanTool,
   meta : {
      title : "Kebutuhan Perkakas - PT.INKA"
   }

},

{

    path : '/perhitunganKriteria/:id',
    name : 'Perhitungan Kriteria',
    component : PerhitunganKriteria,
    meta : {
       title : "Perhitungan Kriteria - PT.INKA"
    }

},

{

  path : '/perhitunganSupplier/:id',
  name : 'Perhitungan Supplier',
  component : PerhitunganSupplier,
  meta : {
    titlee : "Perhitungan Supplier - PT.INKA"
  }

},

{
   path : '/listKriteriaPemasok',
   name : 'List Kriteria Pemasok',
   component : ListKriteriaPemasok,
   meta : {
    title : "List Kriteria Pemasok - PT.INKA"
   }

},

{
   path : '/addDistribusiTools',
   name : 'Add Distribusi Tools',
   component : AddDistribusiTools,
   meta : {
       title : "Add Distribusi Tools - PT.INKA"
   }

},

{
  path : '/listToolNeedByProcess/:id',
  name : 'List Tool Need By Process',
  component : ListToolNeedByProcess,
  meta : {
     title : "List Tool Need By Process - PT.INKA"
  }
},

{
   path : '/listPenghitungMatriks',
   name : 'List Penghitung Matrix',
   component : ListPenghitungKriteria,
   meta : {
      title : "List Penghitung Kriteria - PT.INKA"
   }

},

{

  path : '/listAdminPenghitung',
  name : 'List Admin Penghitung',
  component : ListAdminPenghitung,
  meta : {

      title : "List Admin Penghitung - PT.INKA" 
  }
},


{
    path : '/hasilPerbandinganSupplierAdmin/:id',
    name : 'List Hasil Perbandingan Supplier Admin',
    component : HasilPerbandinganSupplierByAdmin,
    meta : {
      title : "Hasil Perbandingan Supplier By Admin - PT.INKA"
    }

},


{

  path : '/listKebutuhanPerkakasByWorkstation/:id',
  name : 'List Tool Need By Workstation',
  component : ListToolNeedByWorkstation,
  meta : {

    title : "List Tool Need By Workstation - PT.INKA"
  },


},
{

  
  path : '/choosePeminjamanTool',
  name : 'Choose Peminjaman Tool',
  component : ChoosePeminjamanTool,
  meta : {
      title : "Choose Peminjaman Tool - PT.INKA"
  }

},

{

  path : '/chooseWorkstation',
  name : 'Choose Workstation Pengembalian Perkakas',
  component : ChooseWorkstation,
  meta : {
     title : "Choose Workstation Pengembalian Tool - PT.INKA"
  }

},

{
    path : '/showToolsOnWorkstation/:id',
    name : 'Show Tools On Workstation',
    component : ShowToolsOnWorkstation,
    meta : {

      title : "Show Tools On Workstation - PT.INKA"

    }

},
{
     path : '/listHasilPerhitunganKriteria',
     name : 'List Hasil Perhitungan Kriteria',
     component : ListHasilPerhitunganKriteria,
     meta : {
        title : "List Hasil Perhitungan Kriteria - PT.INKA"
     }

},

{

  path : 'listPenghitungSupplier',
  name : 'List Penghitung Supplier',
  component : ListPenghitungSupplier,
  meta : {
 
      title : "List Penghitung Supplier - PT.INKA"
  }
},

{
   path : '/listHasilPerhitunganSupplier1',
   name : 'List Hasil Perhitungan Supplier 1',
   component : ListHasilPerhitunganSupplier1,
   meta : {
      title : "List Hasil Perhitungan Supplier 1 - PT.INKA"
   }

},

{
   path : '/listHasilPerhitunganSupplier2',
   name : 'List Hasil Perhitungan Supplier 2',
   component : ListHasilPerhitunganSupplier2,
   meta : {

      title : "List Hasil Perhitungan Supplier 2 - PT.INKA"
   }

},

{
    path : '/hasilPerhitunganKriteriaAdmin/:id',
    name : 'List Hasil Perhitungan Kriteria By Admin',
    component : HasilPerhitunganKriteriaByAdmin,
    meta : {
       title : "Hasil Perhitungan Kriteria By Admin - PT.INKA"
    }

},

{
  path : '/hasilBobotPeringkatSupplierAdmin/:id',
  name : 'Hasil Perhitungan Bobot Peringkat Supplier By Admin',
  component : HasilBobotPeringkatSupplierByAdmin,
  meta : {
    title : "Hasil Bobot dan Peringkat Supplier - PT.INKA"
  }

}

// {

//    path : '/listToolNeedByProcess/:id',
//    name : 'List Tool Need By Process',
//    component : ListToolsByProcess,
//    meta : {
//       title : "List Tool Need By Process - PT.INKA"

//    }
// }



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
