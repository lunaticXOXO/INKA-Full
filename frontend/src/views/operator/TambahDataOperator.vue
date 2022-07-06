<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Operator Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            v-model="valid"
            @submit.prevent="submitHandler"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-text-field
            v-model="alamat"
            label="Alamat"
            ></v-text-field>

            <v-select
            item-text="nama"
            item-value="id"
            v-model="kota"
            :items="items"
            label="Kota"
            ></v-select>

            <v-text-field
            v-model="kodePos"
            label="Kode Pos"
            ></v-text-field>

            <v-text-field
            v-model="noTelepon"
            label="No Telepon"
            ></v-text-field>

            <v-text-field
            v-model="email"
            :rules="emailRules"
            label="Email"
            ></v-text-field>

            <v-file-input
                required
                v-model="gambar"
                :rules="gambarRules"
                accept="image/*"
                label="Unggah Gambar"
                prepend-icon="mdi-camera"
                @change="onAddFiles">
            </v-file-input>
            
            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate()"
            >
            Submit
            </v-btn>

            <v-btn
            color="error"
            class="mr-4"
            @click="reset"
            >
            Reset
            </v-btn>
        </v-form>
        <v-snackbar top color="green" v-model="snackBar">
            Insert Operator Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackBar: false,
      nama: '',
      alamat: '',
      kodePos: '',
      noTelepon: '',
      id: '',
      gambar: '',
      idRules: [
        v => !!v || 'ID is required',
      ],
      gambarRules: [
        v => !!v || 'Photo is required',
      ],
      email: '',
      emailRules: [
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      kota: undefined,
      items: undefined,
    }),

    mounted(){
        this.fetchData()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertOperator()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
        console.log(this.alamat)
        console.log(this.kota)
        console.log(this.kodePos)
        console.log(this.noTelepon)
        console.log(this.email)
        console.log(this.gambar)
      },

      onAddFiles(files) {
        const reader = new FileReader();
        console.log(reader.readAsDataURL(files));
      },

      async fetchData(){
        try{
          const axios = require('axios');
          const res = await axios.get(`/city/get_allcities`);
          if(res.data == null){
              alert("Kota Kosong")
          }else{
              this.items = res.data;
              console.log(res,this.data)
          }
        }catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async InsertOperator(){
        try{
          const axios = require('axios');
          const response = await axios.post('/operator/add_operator',
            { id: this.id,
              nama: this.nama,
              alamat: this.alamat,
              kota : this.kota,
              kodepos : this.kodePos,
              noTelepon : this.noTelepon,
              email : this.email,
              profile : this.gambar
            }
          );
          console.log(response,this.data)
          this.snackBar = true
        }
        catch(error){
          alert("Insert Kota Failed")
          console.log(error)
        }
      },

    },
  }
</script>