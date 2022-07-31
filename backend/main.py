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
from material.MaterialOnWorkstation.controller.MaterialOnWorkstationController import *
from material.MaterialConsumable.controller.MaterialConsumableController import *
from unit.controller.UnitController import *
from users.controller.UserController import *
from operasi.controller.OperasiController import *
from flask import Flask,session
from flask_cors import CORS
#from flask_restful import Api

app = Flask(__name__)
app.secret_key = "super secret key"
#api = Api(app)
CORS(app)

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

@app.route('/supplier/add_supplier',methods = ['POST'])
def add_supplier():
    hasil = AddSupplier()
    return hasil

@app.route('/supplier/update_supplier/<code>',methods = ['POST'])
def update_supplier(code):
    hasil = UpdateSupplier(code)
    return hasil

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

#PRODUCT
@app.route('/product/get_product',methods = ['GET'])
def get_product():
    hasil = GetAllProduk()
    return hasil


@app.route('/product/get_product_by_rproyek/<id_rproyek>',methods = ['GET'])
def get_product_by_rproyek(id_rproyek):
    hasil = GetProdukbyRProyek(id_rproyek)
    return hasil 

@app.route('/product/add_product',methods = ['POST'])   
def add_product():
    hasil = AddProduk()
    return hasil

@app.route('/product/add_product_by_rproyek/<id_rincian>',methods = ['POST'])
def add_product_by_rproyek(id_rincian):
    hasil = AddProdukbyRincian(id_rincian)
    return hasil

@app.route('/product/get_rpoyek_inproduct/<id_rproyek>',methods = ['GET'])
def get_rproyek_inproduct(id_rproyek):
    hasil = GetRProyekInProduk(id_rproyek)
    return hasil

#JENIS PRODUCT
@app.route('/jproduct/post_jproduct',methods =['POST'])
def post_jproduct():
    hasil = AddJenisProduct()
    return hasil

@app.route('/jproduct/get_jproduct',methods = ['GET'])
def get_jproduct():
   hasil = GetAllJenisProduk()
   return hasil

@app.route('/jproduct/get_jproduct_by_rproyek/<id_rproyek>',methods = ['GET'])
def get_jproduct_by_rproyek(id_rproyek):
    hasil = GetJenisProdukbyRincianProyek(id_rproyek)
    return hasil

@app.route('/jproduct/get_jproduct/<id>',methods = ['GET'])
def get_jproduct_byId(id):
    hasil = GetJenisProductById(id)
    return hasil

@app.route('/jproduct/get_rincian_injproduct/<id_rincian>',methods = ['GET'])
def get_rincian_injproduct(id_rincian):
    hasil = GetRincianInJenisProduk(id_rincian)
    return hasil

@app.route('/jproduct/update_jproduct/<id>',methods = ['POST'])
def update_jproduct(id):
    hasil = UpdateJenisProduk(id)
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

@app.route('/sjproduct/update_sjproduct/<idNodal>',methods = ['POST'])
def update_sjproduct(idNodal):
    hasil = UpdateStrukturJenisProduk(idNodal)
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
@app.route('/supplier_material/show_material_supplier',methods = ['GET'])
def show_material_supplier():
    hasil = ShowSupplierWithMaterialType()
    return hasil


@app.route('/supplier_material/add_material_supplier',methods = ['POST'])
def add_material_supplier():
    hasil = AddSupplierMaterialType()
    return hasil

# Material Unit
@app.route('/unit/get_unit',methods = ['GET'])
def get_unit():
    hasil = GetUnit()
    return hasil

# Purchase Material
@app.route('/material/purchase_material',methods = ['POST'])
def purchase_material():
    hasil = PurchaseMaterial()
    return hasil

@app.route('/material/order_material/<id>',methods = ['POST'])
def order_material(id):
    hasil = PurchaseMaterialFromStock(id)
    return hasil

@app.route('/material/min_quantity/<id>',methods = ['GET'])
def min_quantity(id):
    hasil = MinimalQuantity(id)
    return hasil

@app.route('/stock/get_stock',methods = ['GET'])
def get_stock():
    hasil = GetMaterialFromStock()
    return hasil

@app.route('/material/order_new_material',methods = ['POST'])
def order_new_material():
    hasil = PurchaseNewMaterial()
    return hasil

#MATERIAL ON WS
@app.route('/material_ws/get_material_onws',methods = ['GET'])
def get_material_onws():
    hasil = GetMaterialOnWS()
    return hasil


@app.route('/material_ws/add_material_onws',methods = ['POST'])
def add_material_onws():
    hasil = AddMaterialOnWS()
    return hasil

@app.route('/material_ws/update_material_onws/<id>',methods = ['POST'])
def update_material_onws(id):
    hasil = UpdateMaterialOnWS(id)
    return hasil

#MATERIAL CONSUMABLE
@app.route('/material_consumable/get_material_byproses/<idProcess>',methods = ['GET'])
def get_material_byproses(idProcess):
    hasil = GetMaterialConsumablebyProcess(idProcess)
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

#USERS 
@app.route('/register',methods = ['POST'])
def register():
    hasil = Register()
    return hasil

@app.route('/login',methods = ['POST'])
def login():
    hasil = Login()
    return hasil

@app.route('/logout')
def logout():
    hasil = Logout()
    return hasil
    
if __name__ =="__main__":
    app.run(debug = True,port = 8181) 
    print("Connected to port 8181")