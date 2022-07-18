<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Jenis Material</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation>

            <v-text-field
            v-model="code"
            :counter="12"
            :rules="kodeRules"
            label="Code"
            required
            ></v-text-field>

            <v-select
            v-model="classificationCode"
            :items="list_klasifikasi"
            item-text="descriptions"
            item-value="code"
            label="Klasifikasi"
            required
            ></v-select>

            <v-select
            v-model="groupCode"
            :items="list_grup"
            item-text="descriptions"
            item-value="code"
            label="Grup"
            required
            ></v-select>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-checkbox
            v-model="isAvailable"
            label="Is Available?"
            required
            ></v-checkbox>

            <v-checkbox
            v-model="isAssy"
            label="Is Assy?"
            required
            ></v-checkbox>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate">
            Submit
            </v-btn>

            <v-btn
            color="error"
            class="mr-4"
            @click="reset">
            Reset
            </v-btn>

        </v-form>
          <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      available: false,
      assy: false,
      nama: '',
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 12 && v.length >= 3) || 'Kode must be 3-12 characters',
      ],
      classificationCode: '',
      groupCode: '',
      list_klasifikasi: undefined,
      list_grup: undefined,
      snackbar : {
        show : false,
        color : null,
        message : null,
      }
    }),

    mounted(){
      this.getClassification(),
      this.getGroups()
    },

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.addJenisMaterial()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.kode)
        console.log(this.assy)
        console.log(this.available)
        console.log(this.nama)
        console.log(this.classificationCode)
        console.log(this.groupCode)
      },

      async getClassification(){
        const axios = require('axios')
        const res = await axios.get('/material/show_classification')
        if(res.data == null){
          console.log('Classification Kosong')
        } else {
          this.list_klasifikasi = res.data
        }
        console.log(res,this.klasifikasi)
      },

      async getGroups(){
        const axios = require('axios')
        const res = await axios.get('/material/show_groups')
        if(res.data == null){
          console.log('Group kosong')
        } else {
          this.list_grup = res.data
        }
        console.log(res,this.list_grup)
      },

      async addJenisMaterial(){
        try{
          const axios = require('axios')
          const res = await axios.post('/material/add_type',{
              code : this.code,
              nama : this.nama,
              isAvailable : this.isAvailable,
              isAssy : this.isAssy,
              classificationCode : this.classificationCode,
              groupCode : this.groupCode
          })
        
           if(res.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Tambah Jenis Material Berhasil",
              color : "green"
            }
          }
          else if(res.data.status == "gagal"){
            this.snackbar = {
              show : true,
              message : "Tambah Jenis Material Gagal",
              color : "red"
            }
          }
        }catch(error){
          console.log(error)
        }
      }
    },
  }
</script>