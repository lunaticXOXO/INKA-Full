<template>
<v-app>
    <v-card
        class="mx-auto text-center mt-6"
        width="1000">
        <br>
        <h1>Tambah Proses Baru Sesuai Strk.Jns.Prod</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation>

            <v-autocomplete
            item-value="id"
            :item-text="items2 => items2.id +' - '+ items2.namaJenisProses"
            v-model="jenisProses"
            :items="items2"
            label="Jenis Proses"
            ></v-autocomplete>

            <v-text-field
            v-model="id"
            :counter="2"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-autocomplete
            item-text="nama"
            item-value="id"
            v-model="prosesSesudahnya"
            :items="items"
            label="Proses Sesudahnya"
            ></v-autocomplete>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="durasi"
            label="Durasi"
            type="number"
            ></v-text-field>

            <v-autocomplete
            v-model="satuanDurasi"
            :items="items3"
            label="Satuan Durasi"
            ></v-autocomplete>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate()">
            Submit
            </v-btn>

            <v-btn
            color="error"
            class="mr-4"
            @click="reset">
            Reset
            </v-btn>
        </v-form>
        <div v-if="snackBar == true">
            <v-snackbar top color="green" v-model="snackBar">
                Insert Proses by SJProduk Sukses!
            </v-snackbar>
        </div>

        <div v-else-if="snackBar == false">
            <v-snackbar top color="red" v-model="snackBar">
                Insert Proses by SJProduk Gagal!
            </v-snackbar>
        </div>

        <v-snackbar :color="snackBar.color" v-model="snackBar.show" top>
            {{snackBar.message}}
        </v-snackbar>
    </v-card>
        <div class="d-flex">
           <v-card class="ml-6 text-center mt-6 mb-10" width="700">
                <v-data-table
                    :headers="column2"
                    :items = "sjproduk">
                </v-data-table>
            </v-card>
            <v-card class="ml-12 text-center mt-6 mb-10" width="700">
                <v-data-table
                    :headers="column3"
                    :items = "sjproduk">
                </v-data-table>
            </v-card>
        </div>
</v-app>
</template>

<script>
    import axios from 'axios'
    export default {
        data: () => ({
            valid: true,
            snackBar: {
                show: false,
                message: null,
                color: null
            },
            id: '',
            idRules: [
                v => !!v || 'ID is required',
                v => (v && v.length <= 2 && v.length >= 2) || 'ID must be 7-9 characters',
            ],
            nama: '',
            durasi: '',
            satuanDurasi: '',
            prosesSesudahnya: null,
            jenisProses: undefined,
            items: undefined,
            items2: undefined,
            items3: [
                "Menit"
            ],
             column2 : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Nama', value : 'nama'},
                {text : 'Induk Nodal',value : 'indukNodal'},
                {text : 'ID Jenis Produk',value : 'IdJenisProduk'},
                {text : 'Nama Jenis Produk',value : 'NamaJenisProduk'},
                {text : 'ID Rincian Proyek',value : 'IdRincian'},
            ],
            column3 : [
                {text : 'ID Nodal', value : 'idNodal'},
                {text : 'Jumlah',value : 'jumlah'},
                {text : 'Due Date Rincian',value : 'dueDateRincian'},
                {text : 'ID Produk',value : 'IdProduk'},
                {text : 'Nama Proyek',value : 'namaProyek'},
                {text : 'ID Customer',value : 'IdCustomer'},
                {text : 'Nama Customer',value : 'namaCustomer'}
            ],
            column4 : [
                {text : 'IdJenis',value : 'id'},
                {text : 'Nama Jenis Proses',value : 'namaJenisProses' }
            ],
            sjproduk : [],
            jenisproses : [],
        }),
     
        mounted(){
            this.fetchProses(),
            this.fetchJenisProses(),
            this.fetchSJProdukInProses()
        },

        methods: {
            validate () {
                if(this.$refs.form.validate()){
                    this.InsertProses()
                }
            },

            reset () {
                this.$refs.form.reset()
            },

            submitHandler() {
                console.log(this.id)
                console.log(this.prosesSesudahnya)
                console.log(this.jenisProses)
                console.log(this.nama)
                console.log(this.durasi)
                console.log(this.satuanDurasi)
            },

            async fetchProses(){
                try{
                    const res = await axios.get('/proses/get_process_dropwdown/' + this.$route.params.id)
                    if (res.data == null){
                        alert("Proses Kosong")
                    }else{
                        this.items = res.data
                        console.log(res,this.items)
                    }
                }
                catch(error){
                    alert(error)
                    console.log(error)
                }
            },

            async fetchJenisProses(){
                try{
                    const res = await axios.get('/jenis_proses/get_jenisproses')
                    if (res.data == null){
                        alert("Jenis Proses Kosong")
                    }else{
                        this.items2 = res.data
                        this.jenisproses = res.data
                        console.log(res,this.items2)
                    }
                }
                catch(error){
                    alert(error)
                    console.log(error)
                }
            },
            
            async fetchSJProdukInProses(){
                try{
                    const res = await axios.get('/proses/get_sjproduct_inprocess/' + this.$route.params.id)
                    if(res.data == null){
                        alert("Data Kosong")
                    }else{
                        this.sjproduk = res.data
                        console.log(res,this.sjproduk)
                    }
                }catch(error){
                    alert("Error")
                    console.log(error)
                }
            },

            async InsertProses(){
                try{
                    const response = await axios.post('/proses/add_process_by_sjproduct/' + this.$route.params.id,
                        {   id: this.id,
                            nama: this.nama,
                            durasi: this.durasi,
                            satuanDurasi: this.satuanDurasi,
                            jenisProses: this.jenisProses,
                            prosesSesudahnya: this.prosesSesudahnya,
                            nodalOutput: this.$route.params.id
                        }
                    );
                    console.log(response,this.data)
                    if(response.data.status == "berhasil"){
                        this.snackbar = {
                        message : "Insert Proses by SJProduk Success",
                        color : 'green',
                        show : true
                    }
                        location.replace('/listProcessbySJProduk/' + this.$route.params.id)
                    }
                    else if(response.data.status == "gagal"){
                        this.snackbar = {
                        message : "Insert Proses by SJProduk Gagal, ID Sudah Tersedia!",
                        color : 'red',
                        show : true
                    }}
                }
                catch(error){
                    this.snackbar = {
                        message : "Insert Proses by SJProduk Error",
                        color : 'error',
                        show : true
                    }
                    console.log(error)
                }
            },
        }
    }
</script>