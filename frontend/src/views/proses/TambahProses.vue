<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Proses Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="9"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-select
            item-text="id"
            item-value="id"
            v-model="prosesSesudahnya"
            :items="items"
            label="Proses Sesudahnya"
            ></v-select>

            <v-select
            item-text="idNodal"
            item-value="idNodal"
            v-model="nodalOutput"
            :items="items2"
            label="Nodal Output"
            ></v-select>

            <v-select
            item-text="id"
            item-value="id"
            v-model="jenisProses"
            :items="items3"
            label="Jenis Proses"
            ></v-select>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="durasi"
            label="Durasi"
            ></v-text-field>

            <v-select
            v-model="satuanDurasi"
            :items="items4"
            label="Satuan Durasi"
            ></v-select>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="InsertProses()">
            Submit
            </v-btn>

            <v-btn
            color="error"
            class="mr-4"
            @click="reset">
            Reset
            </v-btn>
        </v-form>
        <v-snackbar top color="green" v-model="snackBar">
            Insert Proses Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
    import axios from 'axios'
    export default {
        data: () => ({
            valid: true,
            snackBar: false,
            id: '',
            idRules: [
                v => !!v || 'ID is required',
                v => (v && v.length <= 9 && v.length >= 7) || 'ID must be 7-9 characters',
            ],
            nama: '',
            durasi: '',
            satuanDurasi: '',
            prosesSesudahnya: undefined,
            nodalOutput: undefined,
            jenisProses: undefined,
            items: undefined,
            items2: undefined,
            items3: undefined,
            items4: [
                "Minutes"
            ]
        }),

        mounted(){
            this.fetchProses(),
            this.fetchJenisProses(),
            this.fetchNodal()
        },

        methods: {
            reset () {
                this.$refs.form.reset()
            },

            submitHandler() {
                console.log(this.id)
                console.log(this.prosesSesudahnya)
                console.log(this.nodalOutput)
            },

            async fetchProses(){
                try{
                    const res = await axios.get('/proses/get_listprocess')
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
                        this.items3 = res.data
                        console.log(res,this.items3)
                    }
                }
                catch(error){
                    alert(error)
                    console.log(error)
                }
            },

            async fetchNodal(){
                try{
                    const res = await axios.get('/sjproduct/get_sjproduct')
                    if (res.data == null){
                        alert("Struktur Jenis Produk Kosong")
                    }else{
                        this.items2 = res.data
                        console.log(res,this.items2)
                    }
                }
                catch(error){
                    alert(error)
                    console.log(error)
                }
            },

            async InsertProses(){
                try{
                    const response = await axios.post('/proses/add_process',
                        {   id: this.id,
                            nama: this.nama,
                            durasi: this.durasi,
                            satuanDurasi: this.satuanDurasi,
                            jenisProses: this.jenisProses,
                            prosesSesudahnya: this.prosesSesudahnya,
                            nodalOutput: this.nodalOutput
                        }
                    );
                    console.log(response,this.data)
                    this.snackBar = true
                }
                catch(error){
                    alert("Insert Proses Failed")
                    console.log(error)
                }
            },
        }
    }
</script>