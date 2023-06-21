from distutils.log import Log
from process.controller.ProsesController import *
from process.controller.LiniProduksiController import *
from product.controller.JenisProdukController import *
from product.controller.ProdukController import *
from product.controller.StrukturJenisProdukController import *
from project.controller.ProyekController import *
from workstation.controller.WorkstationController import *
from product.controller.JenisProdukController import *
from country.controller.CountryController import * 
from city.controller.CityController import *
from customer.controller.CustomerController import *
from supplier.controller.SupplierController import *
from material.Classification.controller.MaterialClassificationController import *
from material.GroupMaterial.controller.GroupMaterialController import *
from material.MaterialType.controller.MaterialTypeController import *
from material.SupplierMaterial.controller.SupplierMaterialController import *
from material.purchasematerial.controller.PurchaseMaterialController import *
from material.purchasematerial.controller.PurchaseMaterialItem import *
from material.MaterialStock.controller.MaterialStockController import *
from material.MaterialOnWorkstation.controller.MaterialOnWorkstationController import *
from material.MaterialConsumable.controller.MaterialConsumableController import *
from unit.controller.UnitController import *
from users.controller.UserController import *
from operasi.controller.OperasiController import *
from operators.controller.OperatorController import *
from rfid.controller.ScanBarcodeRFID import *
from material.StatusBarcode.controller.StatusBarcodeController import *
from umum.controller.UmumController import *
from tools.tooltype.ToolTypeController import *
from tools.toolstock.ToolStockController import *
from tools.toolpurchase.ToolPurchaseController import *
from tools.toolpurchase.ToolPurchaseItemController import *
from tools.toolbox.BoxItemController import *
from tools.toolbutuhopr.controller.ToolButuhOpr import *
from tools.toolneed.ToolNeedController import *
from tools.pengembaliantool.PengembalianToolController import *
from ahp.controller.AhpController import *
import psutil

from flask import Flask,session
from flask_cors import CORS
#from flask_restful import Api

app = Flask(__name__)
app.secret_key = "super secret key"
#api = Api(app)
CORS(app)


class main():

    #COUNTRY
    @app.route('/countries/get_allcountries',methods = ['GET'])
    def get_allcountries():
        hasil = ShowAllCountry()
        return hasil

    @app.route('/countries/add_countries',methods = ['POST'])
    def add_countries():
        hasil = AddNewCountry()
        return hasil

    @app.route('/countries/update_country/<code>',methods = ['POST'])
    def update_country(code):
        hasil = UpdateCountry(code)
        return hasil


    #CITY
    @app.route('/city/get_allcities',methods = ['GET'])
    def get_allcities():
        hasil = GetAllCities()
        return hasil

    @app.route('/city/add_city',methods = ['POST'])
    def add_city():
        hasil = AddCity()
        return hasil 

    @app.route('/city/update_city/<code>',methods = ['POST'])
    def update_city(code):
        hasil = UpdateCity(code)
        return hasil

    @app.route('/city/delete_city/<code>',methods = ['DELETE'])
    def delete_city(code):
        hasil = DeleteCity(code)
        return hasil


    #CUSTOMER
    @app.route('/customers/get_customers',methods = ['GET'])
    def get_customers():
        hasil = ShowAllCustomer()
        return hasil

    @app.route('/customers/get_customers_name',methods = ['GET'])
    def get_customers_name():
        hasil = ShowCustomerNames()
        return hasil

    @app.route('/customers/add_customer',methods = ['POST'])
    def add_customer():
        hasil = AddNewCustomer()
        return hasil

    @app.route('/customer/update_customer/<id>',methods = ['POST'])
    def update_customer(id):
        hasil = UpdateCustomer(id)
        return hasil


    #SUPPLIER
    @app.route('/supplier/get_supplier',methods = ['GET'])
    def get_supplier():
        hasil = GetSupplier()
        return hasil


    @app.route('/supplier/get_supplier_byid/<idSupplier>',methods = ['GET'])
    def get_supplier_byid(idSupplier):
        return GetSupplierById(idSupplier)

    @app.route('/supplier/add_supplier',methods = ['POST'])
    def add_supplier():
        hasil = AddSupplier()
        return hasil

    @app.route('/supplier/update_supplier/<code>',methods = ['POST'])
    def update_supplier(code):
        hasil = UpdateSupplier(code)
        return hasil

    @app.route('/supplier/add_materialtype_bysupplier/<code>',methods = ['POST'])
    def add_materialtype_bysupplier(code):
        hasil = AddMaterialTypeSupplierbySupplier(code)
        return hasil

    @app.route('/supplier/get_materialtype_bysupplier/<code>',methods = ['GET'])
    def get_materialtype_bysupplier(code):
        hasil = ShowMaterialTypeSupplierBySupplier(code)
        return hasil

    @app.route('/supplier/get_supplier_rank',methods = ['GET'])
    def get_supplier_rank():
        return RankingSupplier()



    @app.route('/supplier/detail_get_supplier_rank/<idSupplier>',methods = ['GET'])
    def detail_get_supplier_rank(idSupplier):
        return GetDetailRankingSupplier(idSupplier)


    @app.route('/supplier/get_kriteria_supplier',methods = ['GET'])
    def get_kriteria_supplier():
        return GetKriteriaPemasok()


    @app.route('/supplier/get_matriks_kriteria',methods = ['GET'])
    def get_matriks_kriteria():
        return GetMatriksKriteriaInput()

    @app.route('/supplier/get_matrikskriteria_byadmin/<IdPenghitung>',methods = ['GET'])
    def get_matrikskriteria_byadmin(IdPenghitung):
        return GetMatriksKriteriaInputByAdmin(IdPenghitung)


    @app.route('/supplier/get_matrikssupplier_byadmin/<IdPenghitung>',methods = ['GET'])
    def get_matrikssupplier_byadmin(IdPenghitung):
        return GetPerbandinganSupplierByAdmin(IdPenghitung)


    @app.route('/supplier/add_matriks_kriteria',methods = ['POST'])
    def add_matriks_kriteria():
        return InsertMatriksKriteria()


    @app.route('/supplier/add_matrikskriteria_byadmin/<idPenghitung>',methods = ['POST'])
    def add_matrikskriteria_byadmin(idPenghitung):
        return InsertMatriksKriteriaByAdmin(idPenghitung)

    @app.route('/supplier/show_admin_penghitung',methods = ['GET'])
    def show_admin_penghitung():
        return GetPenghitungMatriks()

    @app.route('/supplier/add_admin_penghitung',methods = ['POST'])
    def add_admin_penghitung():
        return InsertNewPenghitung()

    @app.route('/supplier/get_kriteria_rank',methods = ['GET'])
    def get_kriteria_rank():
        return GetPeringkatKriteria()




    #PROYEK
    @app.route('/proyek/get_allproyek',methods = ['GET'])
    def get_allproyek():
        hasil = GetAllProyek()
        return hasil

    @app.route('/proyek/get_proyek_by_customer/<id>',methods = ['GET'])
    def get_proyek_by_customer(id):
        hasil = GetProyekByCustomer(id)
        return hasil

    @app.route('/proyek/add_newproyek',methods = ['POST'])
    def add_newproyek():
        hasil = AddProyek()
        return hasil

    @app.route('/proyek/add_newproyek_by_customer/<id_customer>',methods = ['POST'])
    def add_newproyek_by_customer(id_customer):
        hasil = AddProyekbyCustomer(id_customer)
        return hasil

    @app.route('/proyek/get_customer_inproyek/<idCustomer>',methods = ['GET'])
    def get_customer_inproyek(idCustomer):
        hasil = GetCustomerInProyek(idCustomer)
        return hasil

    @app.route('/proyek/update_proyek/<id>',methods = ['POST'])
    def update_proyek(id):
        hasil = UpdateProyek(id)
        return hasil

    @app.route('/proyek/accumulate_percentage_proyek/<idOperasi>',methods = ['POST'])
    def accumulate_percentage_proyek(idOperasi):
        hasil = AccumulatePercentageProyek(idOperasi)
        return hasil

    @app.route('/proyek/show_percentage_proyek',methods = ['GET'])
    def show_percentage_proyek():
        hasil = showPercentageAllProyek()
        return hasil

    @app.route('/proyek/show_progress_percentage_proyek/<proyek>',methods = ['GET'])
    def show_progress_proyek(proyek):
        hasil = showpercentageProgressProyek(proyek)
        return hasil

    @app.route('/proyek/show_progress_date_proyek',methods = ['GET'])
    def show_progress_date_proyek():
        hasil = showDateProgressProyek()
        return hasil


    #RINCIAN PROYEK
    @app.route('/rproyek/show_rproyek',methods = ['GET'])
    def show_rproyek():
        hasil = GetAllRincianProyek()
        return hasil

    @app.route('/rproyek/show_rproyek_by_proyek/<id_proyek>',methods = ['GET'])
    def show_rproyek_by_proyek(id_proyek):
        hasil = ShowRincianProyekByProyek(id_proyek)
        return hasil

    @app.route('/rproyek/show_proyek_inrproyek/<id_proyek>',methods = ['GET'])
    def show_proyek_inrproyek(id_proyek):
        hasil = ShowProyekInRProyek(id_proyek)
        return hasil

    @app.route('/rproyek/update_rproyek/<id_rproyek>',methods = ['POST'])
    def update_rproyek(id_rproyek):
        hasil = UpdateRProyek(id_rproyek)
        return hasil

    @app.route('/rproyek/show_duedate_rproyek/<id_proyek>',methods = ['GET'])
    def show_duedate_rproyek(id_proyek):
        hasil = HitungDueDateRProyek(id_proyek)
        return hasil

    @app.route('/rproyek/add_rproyek_byproyek/<id_proyek>',methods = ['POST'])
    def add_rproyek_byproyek(id_proyek):
        hasil = AddRincianProyekByProyek(id_proyek)
        return hasil

    @app.route('/rproyek/add_rproyek',methods = ['POST'])
    def add_rproyek():
        hasil = AddRincianProyek()
        return hasil

    @app.route('/rproyek/update_duedate_rproyek/<id_proyek>',methods = ['POST'])
    def update_duedate_rproyek(id_proyek):
        hasil = UpdateDueDateRProyek(id_proyek)
        return hasil

    @app.route('/rproyek/show_first_operation',methods = ['GET'])
    def show_first_operation():
        hasil = GetFirstOperation()
        return hasil

    @app.route('/rproyek/show_first_operation_dsc',methods = ['GET'])
    def show_first_operation_dsc():
        hasil = GetFirstOperationDsc()
        return hasil

    @app.route('/rproyek/accept_operasi',methods = ['POST'])
    def accept_operasi():
        hasil = TerimaOperasi()
        return hasil

    @app.route('/rproyek/decline_operasi',methods = ['DELETE'])
    def decline_operasi():
        hasil = BatalOperasi()
        return hasil




    #PRODUCT
    @app.route('/product/get_product',methods = ['GET'])
    def get_product():
        hasil = GetAllProduk()
        return hasil

    @app.route('/product/get_product_by_rproyek/<id_rproyek>',methods = ['GET'])
    def get_product_by_rproyek(id_rproyek):
        hasil = GetProdukbyRProyek(id_rproyek)
        return hasil 

    @app.route('/product/get_product_by_rproyekDSP/<id_rproyek>',methods = ['GET'])
    def get_product_by_rproyekDSP(id_rproyek):
        hasil = GetProdukbyRProyekDSP(id_rproyek)
        return hasil

    @app.route('/product/add_product',methods = ['POST'])   
    def add_product():
        hasil = AddProduk()
        return hasil

    @app.route('/product/add_product_by_rproyek/<id_rincian>',methods = ['POST'])
    def add_product_by_rproyek(id_rincian):
        hasil = AddProdukbyRincian(id_rincian)
        return hasil

    @app.route('/product/get_rproyek_inproduct/<id_rproyek>',methods = ['GET'])
    def get_rproyek_inproduct(id_rproyek):
        hasil = GetRProyekInProduk(id_rproyek)
        return hasil


    #JENIS PRODUCT
    @app.route('/jproduct/post_jproduct',methods =['POST'])
    def post_jproduct():
        hasil = AddJenisProductEksternal()
        return hasil

    @app.route('/jproduct/post_jproduct_internal',methods = ['POST'])
    def post_jproduct_internal():
        hasil = AddJenisProductInternal()
        return hasil

    @app.route('/jproduct/get_jproduct',methods = ['GET'])
    def get_jproduct():
        hasil = GetAllJenisProduk()
        return hasil

    @app.route('/jproduct/get_jproduct_by_rproyek/<id_rproyek>',methods = ['GET'])
    def get_jproduct_by_rproyek(id_rproyek):
        hasil = GetJenisProdukbyRincianProyek(id_rproyek)
        return hasil

    @app.route('/jproduct/get_jproduct/<CODE>',methods = ['GET'])
    def get_jproduct_byId(CODE):
        hasil = GetJenisProductById(CODE)
        return hasil

    @app.route('/jproduct/get_rincian_injproduct/<id_rincian>',methods = ['GET'])
    def get_rincian_injproduct(id_rincian):
        hasil = GetRincianInJenisProduk(id_rincian)
        return hasil

    @app.route('/jproduct/update_jproduct/<id>',methods = ['POST'])
    def update_jproduct(id):
        hasil = UpdateJenisProduk(id)
        return hasil

    @app.route('/jproduct/show_jproduct_internal',methods = ['GET'])
    def show_jproduct_internal():
        hasil = ShowJProdukInternal()
        return hasil

    @app.route('/jproduct/show_jproduct_eksternal',methods = ['GET'])
    def show_jproduct_eksternal():
        hasil = ShowJProdukEksternal()
        return hasil


    #STUKTUR JENIS PRODUCT
    @app.route('/sjproduct/get_sjproduct',methods = ['GET'])
    def get_sjproduct():
        hasil = ShowAllSJProduk()
        return hasil

    @app.route('/sjproduct/get_jproduct_sjproduct',methods = ['GET'])
    def get_jproduc_sjproduct():
        hasil = ShowJProdukJoinSJProduk()
        return hasil

    @app.route('/sjproduct/get_sjproduct_by_jproduct/<id>',methods = ['GET'])
    def get_sjproduct_by_jproduct(id):
        hasil = ShowSJProdukbyIDJenisProduk(id)
        return hasil

    @app.route('/sjproduct/insert_sjproduct',methods = ['POST'])
    def insert_sjproduct():
        hasil = AddStrukturJenisProduk()
        return hasil

    @app.route('/sjproduct/get_jproduct_insjproduct/<id_jproduk>',methods = ['GET'])
    def get_jproduct_insjproduct(id_jproduk):
        hasil = ShowJProdukInSJProduk(id_jproduk)
        return hasil

    @app.route('/sjproduct/insert_sjproduct_by_jproduct/<id_jproduk>',methods = ['POST'])
    def insert_sjproduct_by_jproduct(id_jproduk):
        hasil = AddSJProdukByJenisProduk(id_jproduk)
        return hasil

    @app.route('/sjproduct/insert_sjproduct_by_parent/<id_strproduk_parent>',methods = ['POST'])
    def insert_sjproduct_by_parent(id_strproduk_parent):
        hasil = AddStrukturJenisProdukByParent(id_strproduk_parent)
        return hasil

    @app.route('/sjproduct/update_sjproduct/<idNodal>',methods = ['POST'])
    def update_sjproduct(idNodal):
        hasil = UpdateStrukturJenisProduk(idNodal)
        return hasil

    @app.route('/sjproduct/get_parent_sjproduct/<idNodal>',methods = ['GET'])
    def get_parent_sjproduct(idNodal):
        hasil =  GetNodeParentStrJenisProduk(idNodal)
        return hasil


    #PROSES
    @app.route('/proses/get_listprocess',methods = ['GET'])
    def get_listprocess():
        hasil = ShowProses()
        return hasil

    @app.route('/proses/get_process_by_sjproduct/<idNodal>',methods = ['GET'])
    def get_process_by_sjproduct(idNodal):
        hasil = ShowProsesbySJProduk(idNodal)
        return hasil

    @app.route('/proses/get_process_dropwdown/<idNodal>',methods = ['GET'])
    def get_process_dropdown(idNodal):
        hasil = ShowProcessDropDown(idNodal)
        return hasil

    @app.route('/proses/get_lastprocess_product/<id>',methods = ['GET'])
    def get_lastprocess_product(id):
        hasil = ShowLastProcessofProductAPI(id)
        return hasil

    @app.route('/proses/add_process',methods = ['POST'])
    def add_process():
        hasil = AddProses()
        return hasil

    @app.route('/proses/get_sjproduct_inprocess/<id_sjproduk>')
    def get_sjproduct_inprocess(id_sjproduk):
        hasil = ShowSJProdukInProcess(id_sjproduk)
        return hasil

    @app.route('/proses/add_process_by_sjproduct/<id_sjproduk>',methods = ['POST'])
    def add_process_by_sjproduct(id_sjproduk):
        hasil = AddProcessBySJProduk(id_sjproduk)
        return hasil

    @app.route('/proses/update_proses/<id>',methods = ['POST'])
    def update_process(id):
        hasil = UpdateProcess(id)
        return hasil


    #JENIS PROSES
    @app.route('/jenis_proses/get_jenisproses',methods = ['GET'])
    def get_jenisproses():
        hasil = ShowJenisProses()
        return hasil

    @app.route('/jenis_proses/insert_jenisproses',methods = ['POST'])
    def insert_jenisproses():
        hasil = InsertJenisProses()
        return hasil


    #GROUP PROSES
    @app.route('/group_proses/insert_groupproses',methods = ['POST'])
    def insert_groupproses():
        hasil = InsertGroupProses()
        return hasil


    #LINI PRODUKSI
    @app.route('/liniproduksi/show_liniproduksi',methods = ['GET'])
    def show_liniproduksi():
        hasil = GetAllLiniProduksi()
        return hasil

    @app.route('/liniproduksi/add_liniproduksi',methods = ['POST'])
    def add_liniproduksi():
        hasil = AddLiniProduksi()
        return hasil

    @app.route('/liniproduksi/stop_liniproduksi/<id>',methods = ['POST'])
    def stop_liniproduksi(id):
        hasil = StopLiniProduksi(id)
        return hasil


    # WORKSTATION
    @app.route('/stasiun_kerja/show_stasiun_kerja',methods = ['GET'])
    def show_stasiun_kerja():
        hasil = GetAllWorkstation()
        return hasil

    @app.route('/stasiun_kerja/show_stasiun_kerja_by_process/<id_process>',methods = ['GET'])
    def show_stasiun_kerja_by_process(id_process):
        hasil = ShowWorkStationbyProcess(id_process)
        return hasil

    @app.route('/stasiun_kerja/update_stasiun_kerja/<id>',methods = ['POST'])
    def update_stasiun_kerja(id):
        hasil = UpdateWorkstation(id)
        return hasil

    @app.route('/stasiun_kerja/add_stasiun_kerja',methods = ['POST'])
    def add_stasiun_kerja():
        hasil = AddWorkstation()
        return hasil

    @app.route('/stasiun_kerja/status_pengerjaan_stasiunkerja',methods = ['GET'])
    def pemantauan_stasiunkerja():
        hasil = statusPengerjaanWS()
        return hasil

    @app.route('/stasiun_kerja/add_stasiun_by_process/<id_process>',methods = ['POST'])
    def add_stasiun_by_process(id_process):
        hasil = AddWorkStationbyProcess(id_process)
        return hasil


    #MATERIAL Classification
    @app.route('/material/show_classification',methods = ['GET'])
    def show_classification():
        hasil = GetClassification()
        return hasil

    @app.route('/material/add_classification',methods = ['POST'])
    def add_classification():
        hasil = AddClassification()
        return hasil

    @app.route('/material/update_classification/<code>',methods = ['POST'])
    def update_classification(code):
        hasil = UpdateClassification(code)
        return hasil


    #MATERIAL GROUP
    @app.route('/material/show_groups',methods = ['GET'])
    def show_groups():
        hasil = GetGroups()
        return hasil

    @app.route('/material/add_group',methods = ['POST'])
    def add_group():
        hasil = AddGroups()
        return hasil

    @app.route('/material/update_group/<code>',methods = ['POST'])
    def update_group(code):
        hasil = UpdateGroups(code)
        return hasil


    # MATERIAL TYPE
    @app.route('/material/get_type',methods = ['GET'])
    def get_type():
        hasil = GetMaterialType()
        return hasil

    @app.route('/material/get_type_name',methods = ['GET'])
    def get_type_name():
        hasil = GetMaterialTypeDescription()
        return hasil

    @app.route('/material/add_type',methods = ['POST'])
    def add_type():
        hasil = AddMaterialType()
        return hasil

    @app.route('/material/update_type/<code>',methods = ['POST'])
    def update_type(code):
        hasil = UpdateMaterialType(code)
        return hasil

    @app.route('/material/search_type/<nama>',methods = ['GET'])
    def search_type(nama):
        hasil = SearchMaterialType(nama)
        return hasil


    # Material Supplier
    @app.route('/supplier_material/show_material_bysupplier',methods = ['GET'])
    def show_material_supplier():
        hasil = ShowMaterialTypeSupplierBySupplier()
        return hasil

    @app.route('/supplier_material/add_material_supplier',methods = ['POST'])
    def add_material_supplier(code):
        hasil = AddMaterialTypeSupplierbySupplier(code)
        return hasil

    @app.route('/supplier_material/show_material_type_name',methods = ['GET'])
    def show_material_type_name():
        hasil = ShowMaterialTypeName()
        return hasil

    @app.route('/supplier_material/show_materialtype_supplier/<code>',methods = ['GET'])
    def show_materialtype_supplier(code):
        hasil = ShowMaterialTypeInPurchaseItem(code)
        return hasil


    # Material Unit
    @app.route('/unit/get_unit',methods = ['GET'])
    def get_unit():
        hasil = GetUnit()
        return hasil

    @app.route('/unit/get_unit_instock',methods = ['GET'])
    def get_unit_instock():
        hasil = GetUnitInMatStock()
        return hasil


    # Purchase Material
    @app.route('/material/purchase_material',methods = ['POST'])
    def purchase_material():
        hasil = PurchaseMaterial()
        return hasil

    @app.route('/material/get_purchase_material',methods = ['GET'])
    def get_purchase_material():
        hasil = GetPurchaseMaterial()
        return hasil


    # Purchase Material Item
    @app.route('/material/get_purchase_item',methods = ['GET'])
    def get_purchase_item():
        hasil = GetMaterialItem()
        return hasil

    @app.route('/material/add_purchase_item',methods = ['POST'])
    def add_purchase_item():
        hasil = PurchaseMaterialItem()
        return hasil

    @app.route('/material/add_purchase_item_by_idpurchase/<idPurchase>',methods = ['POST'])
    def add_purchase_item_by_idpurchase(idPurchase):
        hasil = PurchaseMaterialItemByIDPurchase(idPurchase)
        return hasil

    @app.route('/material/get_purchasematerial_in_purchaseitem/<idPurchase>',methods = ['GET'])
    def get_purchasematerial_in_purchaseitem(idPurchase):
        hasil = GetPurchaseMaterialinPurchaseItem(idPurchase)
        return hasil

    @app.route('/material/get_material_item_by_idpurchase/<idPurchase>',methods = ['GET'])
    def get_material_item_by_idpurchase(idPurchase):
        hasil = GetMaterialItemByPurchaseMaterial(idPurchase)
        return hasil

    @app.route('/material/get_purchase_item_compare/<idPurchase>',methods = ['GET'])
    def get_purchase_item_compare(idPurchase):
        hasil = GetPurchaseMaterialItemComparedMatStock(idPurchase)
        return hasil

    @app.route('/material/get_requirement_purchase_material/<rencanaMulai>',methods = ['GET'])
    def get_requirement_purchase_material(rencanaMulai):
        hasil = ShowRequirementPurchaseMaterial(rencanaMulai)
        return hasil


    #Material Stock
    @app.route('/material/get_material_stock',methods = ['GET'])
    def get_material_stock():
        hasil = GetMaterialStock()
        return hasil

    @app.route('/material/add_new_materialstock',methods = ['POST'])
    def add_new_materialstock():
        hasil = AddNewMaterialStock()
        return hasil

    @app.route('/material/get_materialstock_by_order/<order>',methods = ['GET'])
    def get_materialstock_by_order(order):
        hasil = GetMaterialStockbyOrder(order)
        return hasil

    @app.route('/material/add_material_stock_by_order/<orders>',methods = ['POST'])
    def add_material_stock_by_order(orders):
        hasil = AddMaterialStockbyOrders(orders)
        return hasil

    @app.route('/material/get_purchase_item_in_matstock/<orders>',methods = ['GET'])
    def get_purchase_item_in_matstock(orders):
        hasil = GetPurchaseItemInMatStock(orders)
        return hasil

    @app.route('/material/add_batas_material_requirement',methods = ['POST'])
    def add_batas_material_requirement():
        hasil = InsertBatasMaterialRequirement()
        return hasil

    @app.route('/material/show_material_requirement',methods = ['GET'])
    def show_material_requirement():
        hasil = ShowBatasMaterialRequirement()
        return hasil

    @app.route('/material/message_material_login/<id>',methods = ['GET'])
    def message_material_login(id):
        hasil = GetMaterialBerhasilLogin(id)
        return hasil


    #MATERIAL ON WS
    @app.route('/material_ws/get_material_onws',methods = ['GET'])
    def get_material_onws():
        hasil = GetMaterialOnWS()
        return hasil

    @app.route('/material_ws/get_material_onws_by_idstock/<idStock>',methods = ['GET'])
    def get_material_onws_by_idstock(idStock):
        hasil = GetMaterialStockOnWsByIdStock(idStock)
        return hasil

    @app.route('/material_ws/add_material_login/<idOperasi>',methods = ['POST'])
    def add_material_login(idOperasi):
        hasil = AddMaterialLogin(idOperasi)
        return hasil

    @app.route('/material/get_material_login',methods = ['GET'])
    def get_material_login():
        hasil = GetMaterialLogin()
        return hasil


    #Status Barcode
    @app.route('/status_barcode/get_status_barcode',methods = ['GET'])
    def get_status_barcode():
        hasil = ShowStatusBarcode()
        return hasil


    #MATERIAL CONSUMABLE
    @app.route('/material_consumable/get_material_consumable',methods = ['GET'])
    def get_material_consumable():
        hasil = GetMaterialConsumable()
        return hasil

    @app.route('/material_consumable/add_material_consumable',methods = ['POST'])
    def add_material_consumable():
        hasil = addMaterialConsumable()
        return hasil


    #OPERASI
    @app.route('/operasi/generate_operasi/<idProduk>',methods = ['POST'])
    def generate_operasi(idProduk):
        hasil = GenerateOperation(idProduk)
        return hasil


    #buat di tabel bawah 
    @app.route('/operasi/get_operasi_byproduk/<idProduk>',methods = ['GET'])
    def get_operasi_byproduk(idProduk):
        hasil = ShowOperasiFromProduct(idProduk)
        return hasil

    @app.route('/operasi/pantau_operasi/<idProduct>',methods = ['GET'])
    def pantau_operasi(idProduct):
        hasil = PantauOperasi(idProduct)
        return hasil

    @app.route('/operasi/start_operasi/<idOperasi>',methods = ['POST'])
    def start_operasi(idOperasi):
        hasil = StartOperation(idOperasi)
        return hasil

    @app.route('/operasi/end_operasi/<idOperasi>',methods = ['POST'])
    def end_operasi(idOperasi):
        hasil = EndOperation(idOperasi)
        return hasil


    #tabel buat yang di atas
    @app.route('/operasi/show_product_inoperasi/<id_product>',methods = ['GET'])
    def show_product_inoperasi(id_product):
        hasil = ShowProductInOperasi(id_product)
        return hasil

    @app.route('/operasi/show_product_inpantauoperasi',methods = ['GET'])
    def show_product_inpantauoperasi():
        hasil = ShowProductInPantauOperasi()
        return hasil

    @app.route('/operasi/generate_date_str',methods = ['POST'])
    def generate_date_str():
        hasil = ConvertDateOperation()
        return hasil

    @app.route('/operasi/get_operasi_gantt/<stasiunKerja>',methods = ['GET'])
    def get_operasi_gantt(stasiunKerja):
        hasil = GetOperasiGanttChart(stasiunKerja)
        return hasil

    @app.route('/operasi/response_operasi_mulai/<nomorWS>',methods = ['POST'])
    def response_operasi_mulai(nomorWS):
        hasil = StartResponseOperasi(nomorWS)
        return hasil

    @app.route('/operasi/response_operasi_selesai/<nomorWS>',methods = ['POST'])
    def response_operasi_selsai(nomorWS):
        hasil = EndResponseOperasi(nomorWS)
        return hasil

    @app.route('/operasi/get_response_operasi_mulai/<idOperasi>',methods = ['GET'])
    def get_response_operasi_mulai(idOperasi):
        hasil = GetResponseStartOperasi(idOperasi)
        return hasil

    @app.route('/operasi/get_response_operasi_selesai/<idOperasi>',methods = ['GET'])
    def get_response_operasi_selesai(idOperasi):
        hasil = GetResponseEndOperasi(idOperasi)
        return hasil

    @app.route('/operasi/show_operasilayak/<username>',methods = ['GET'])
    def show_operasilayak(username):
        hasil = ShowOperasiLayak(username)
        return hasil

    @app.route('/operasi/get_operasi_siap/<username>',methods = ['GET'])
    def get_operasi_siap(username):
        hasil = IfOperasiSiap(username)
        return hasil

    @app.route('/operasi/get_operasi_by_product/<idProduct>', methods = ['GET'])
    def get_operasi_by_product(idProduct):
        hasil = ShowOperasiByProduct(idProduct)
        return hasil

    @app.route('/operasi/get_operasi_byws/<ws>',methods = ['GET'])
    def get_operasi_byws(ws):
        return ShowOperationByWorkstation(ws)


    #Operator
    @app.route('/operator/add_operator',methods = ['POST'])
    def add_operator():
        hasil = AddOperator()
        return hasil

    @app.route('/operator/get_operator',methods = ['GET'])
    def get_operator():
        print('RAM memory % used after:', psutil.virtual_memory()[2])
        hasil = ShowOperator()
        return hasil

    @app.route('/operator/get_operator_uuid',methods = ['GET'])
    def get_operator_uuid():
        hasil = ShowOperatorUUID()
        return hasil

    @app.route('/operator/get_operator_rfid',methods = ['GET'])
    def get_operator_rfid():
        hasil = ShowOperatorRfid()
        return hasil

    @app.route('/qualification/add_qualification',methods = ['POST'])
    def add_qualification():
        hasil = AddQualification()
        return hasil

    @app.route('/qualification/get_qualification',methods = ['POST'])
    def get_qualification():
        hasil = GetQualification()
        return hasil

    @app.route('/operator/add_operatorlevel/<code>',methods = ['POST'])
    def add_operatorlevel(code):
        hasil = AddLevelByOperator(code)
        return hasil

    @app.route('/operator/get_oplevel_byoperator/<code>',methods = ['POST'])
    def get_oplevel_byoperator(code):
        hasil = ShowOperatorLevelbyOperator(code)
        return hasil

    @app.route('/operator/get_operasi_byoperator/<username>',methods = ['GET'])
    def get_operasi_byoperator(username):
        hasil = GetOperasiByOperatorLogin(username)
        return hasil

    @app.route('/operator/get_material_byoperator/<username>',methods = ['GET'])
    def get_material_byoperator(username):
        hasil = GetMaterialbyOperatorLogin(username)
        return hasil

    @app.route('/operator/get_operator_requirement_byprocess/<idProcess>',methods = ['GET'])
    def get_operator_requirement_byprocess(idProcess):
        hasil = GetOperatorRequirementByProcess(idProcess)
        return hasil

    @app.route('/operator/add_operator_requirement_byprocess/<id>',methods = ['POST'])
    def add_operator_requirement_byprocess(id):
        hasil = AddOperatorRequirementByProcess(id)
        return hasil

    @app.route('/operator/get_scan_operator/<code>',methods = ['GET'])
    def get_scan_operator(code):
        hasil = ScanOperator(code)
        return hasil

    @app.route('/operator/get_link_operator/<code>',methods = ['GET'])
    def get_link_operator(code):
        hasil = GetLinkOperator(code)
        return hasil

    @app.route('/operator/get_operator_hadir',methods = ['GET'])
    def get_operator_hadir():
        hasil = GetOperatorHadir()
        return hasil

    @app.route('/operator/daftarKartu/<code>',methods = ['POST'])
    def daftarKartu(code):
        hasil = AddCardByIdOperator(code)
        return hasil

    @app.route('/operator/get_operator_on_ws',methods = ['GET'])
    def get_operator_on_ws():
        hasil = GetOperatorOnWS()
        return hasil

    @app.route('/operator/get_operator_on_ws01',methods = ['GET'])
    def get_operator_on_ws01():
        hasil = GetOperatorOnWS01()
        return hasil

    @app.route('/operator/get_operator_on_ws02',methods = ['GET'])
    def get_operator_on_ws02():
        hasil = GetOperatorOnWS02()
        return hasil

    @app.route('/operator/get_operator_on_ws03',methods = ['GET'])
    def get_operator_on_ws03():
        hasil = GetOperatorOnWS03()
        return hasil

    @app.route('/operator/get_operator_on_ws04',methods = ['GET'])
    def get_operator_on_ws04():
        hasil = GetOperatorOnWS04()
        return hasil

    @app.route('/operator/get_operator_on_ws05',methods = ['GET'])
    def get_operator_on_ws05():
        hasil = GetOperatorOnWS05()
        return hasil

    @app.route('/operator/get_operator_on_ws06',methods = ['GET'])
    def get_operator_on_ws06():
        hasil = GetOperatorOnWS06()
        return hasil

    @app.route('/operator/get_operator_on_ws07',methods = ['GET'])
    def get_operator_on_ws07():
        hasil = GetOperatorOnWS07()
        return hasil

    @app.route('/operator/get_operator_on_ws08',methods = ['GET'])
    def get_operator_on_ws08():
        hasil = GetOperatorOnWS08()
        return hasil

    @app.route('/operator/get_operator_on_ws09',methods = ['GET'])
    def get_operator_on_ws09():
        hasil = GetOperatorOnWS09()
        return hasil


    # Process Requirement
    @app.route('/requirement/add_process_requirement/<id>',methods = ['POST'])
    def add_process_requirement(id):
        hasil = AddRequirementByProcess(id)
        return hasil

    @app.route('/requirement/get_requirement_allprocess',methods = ['GET'])
    def get_requirement_allprocess():
        hasil = ShowRequirementProcess()
        return hasil

    @app.route('/requirement/get_requirement_byprocess/<idProcess>')
    def get_requirement_byprocess(idProcess):
        hasil = ShowRequirmentByIdProcess(idProcess)
        return hasil


    #RFID
    @app.route('/rfid/insert_material',methods = ['POST'])
    def scan_barcode_rfid():
        hasil = ScanBarcodeRFID()
        return hasil


    #Tanggal Libur
    @app.route('/holiday/add_holiday',methods = ['POST'])
    def add_holiday():
        hasil = AddNewTanggalLibur()
        return hasil

    @app.route('/holiday/get_all_holiday',methods = ['GET'])
    def get_all_holiday():
        hasil = GetAllTanggalLibur()
        return hasil


    #Tools
    #Tool Type
    @app.route('/tools/show_tooltype',methods = ['GET'])
    def show_tooltype():
        return ShowToolType()

    @app.route('/tools/add_tooltype_consumable',methods = ['POST'])
    def add_tooltype_consumable():
        hasil = AddToolTypeConsumable()
        return hasil

    @app.route('/tools/add_tooltype_nonconsumable',methods = ['POST'])
    def add_tooltype_nonconsumable():
        hasil = AddToolTypeNonConsumable()
        return hasil

    @app.route('/tools/show_tooltype_consumable',methods = ['GET'])
    def show_tooltype_consumable():
        hasil = ShowToolTypeConsumable()
        return hasil


    @app.route('/tools/show_tooltype_nonconsumable',methods = ['GET'])
    def show_tooltype_nonconsumable():
        hasil = ShowToolTypeNonConsumable()
        return hasil

    #Tool Purchase
    @app.route('/tools/add_tool_purchase',methods = ['POST'])
    def add_tool_purchase():
        hasil = AddToolPurchase()
        return hasil


    @app.route('/tools/show_tool_purchase',methods = ['GET'])
    def show_tool_purchase():
        hasil = ShowToolPurchase()
        return hasil



    # Tool Purchase Item
    @app.route('/tools/add_toolpurchase_by_purchasetools/<toolPurchase>',methods = ['POST'])
    def add_toolpurchase_by_purchasetools(toolPurchase):
        hasil = AddToolPurchaseItemByToolPurchase(toolPurchase)
        return hasil


    @app.route('/tools/show_purchase_item_bypurchase/<toolPurchase>',methods = ['GET'])
    def show_purchase_item_bypurchase(toolPurchase):
        hasil = ShowToolPurchaseItemByPurchase(toolPurchase)
        return hasil



    #Tool Stock
    @app.route('/tools/add_toolstock_by_toolPurchaseItem/<toolPurchaseItem>',methods = ['POST'])
    def add_toolstock_by_toolPurchaseItem(toolPurchaseItem):
        hasil = AddToolStockByToolPurchaseItem(toolPurchaseItem)
        return hasil

    @app.route('/tools/show_tools_not_in_box',methods = ['GET'])
    def show_tools_not_in_box():
        hasil = ShowToolStockNotRegisteredInBox()
        return hasil


    @app.route('/tools/get_toolstock_by_purchaseitem/<purchaseItem>',methods = ['GET'])
    def get_toolstock_by_purchaseitem(purchaseItem):
        return ShowToolStockByPurchaseItem(purchaseItem)

    # @app.route('/tools/get_toolstock',methods = ['GET'])
    # def get_toolstock():
    #     return ShowToolStock()

    @app.route('/tools/show_tooltype_detailstock/<toolTypeCode>')
    def show_tooltype_detailstock(toolTypeCode):
        return ShowToolTypeInDetailStock(toolTypeCode)


    @app.route('/tools/detail_toolstock/<toolTypeCode>',methods = ['GET'])
    def detail_toolstock(toolTypeCode):
        return ShowToolStockByToolType(toolTypeCode)


    # Tool Butuh Opr
    @app.route('/tools/show_tool_butuhopr/<username>',methods = ['GET'])
    def show_tool_butuhopr(username):
        return GetToolButuhOpr(username)


    # Tool Need
    @app.route('/tools/show_toolneed_byprocess/<idProcess>',methods = ['GET'])
    def show_toolneed_byprocess(idProcess):
        return ShowToolNeedByProcess(idProcess)

    # Ketersediaan Perkakas
    @app.route('/tools/ketersediaan_perkakas',methods = ['GET'])
    def ketersediaan_perkakas():
        return jumlahToolTypeKeseluruhanDiWorkshop()

    @app.route('/tools/request_kebutuhan_perkakas',methods = ['POST'])
    def kebutuhan_perkakas_byws():
        return RequestKebutuhanToolByWorkstation()

    @app.route('/tools/get_request_kebutuhantool_byws/<workstation>',methods = ['GET'])
    def get_request_kebutuhantool_byws(workstation):
        return GetRequestToolNeedByWorkstation(workstation)

    @app.route('/tools/add_toolneed_idProcess/<idProcess>',methods = ['POST'])
    def add_toolneed_byprocess(idProcess):
        return insertToolNeedByProcess(idProcess)

    # Box
    @app.route('/box/add_toolbox',methods = ['POST'])
    def add_toolbox():
        hasil = AddToolBox()
        return hasil

    @app.route('/box/show_toolbox',methods = ['GET'])
    def show_toolbox():
        hasil = ShowToolBox()
        return hasil

    @app.route('/box/add_toolstock_by_box/<boxId>',methods = ['POST'])
    def add_toolstock_by_box(boxId):
        hasil = AddToolStockToBox(boxId)
        return hasil


    # Pengembalian Tools
    @app.route('/tools/show_tools_onws/<ws>',methods = ['GET'])
    def show_tools_onws(ws):
        return ShowToolOnWorkstation(ws)

    #USERS 
    @app.route('/register',methods = ['POST'])
    def register():
        hasil = Register()
        return hasil


    #AHP
    @app.route('/ahp/merge_count_bobot',methods = ['POST'])
    def calculate_bobot():
        return MergeCountBobotGlobal()

    @app.route('/login',methods = ['POST'])
    def login():
        hasil = Login()
        return hasil

    @app.route('/logout')
    def logout():
        hasil = Logout()
        return hasil
        
    if __name__ =="__main__":
        app.run(host='0.0.0.0',debug = True,port = 8181) 
        print("Connected to port 8181")