<template>
  <v-card
    class="mx-auto text-center mt-6"
    max-width="1000">
  
    <br>
        <v-card
        color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
        >
        <v-card-title class="text-h4">
               TAMBAH JENIS MATERIAL
        </v-card-title>

        </v-card>
        <br>
    <v-form
      class="pa-6"
      ref="form"
      @submit.prevent="submitHandler"
      v-model="valid"
      lazy-validation>

      <v-text-field
      v-model="kode"
      :counter="12"
      :rules="kodeRules"
      label="Code"
      required
      ></v-text-field>

      <!-- <v-autocomplete
      v-model="classificationCode"
      :items="list_klasifikasi"
      item-text="descriptions"
      item-value="code"
      label="Klasifikasi"
      required
      ></v-autocomplete>

      <v-autocomplete
      v-model="groupCode"
      :items="list_grup"
      item-text="descriptions"
      item-value="code"
      label="Grup"
      required
      ></v-autocomplete> -->

      <v-text-field
      v-model="nama"
      label="Nama"
      ></v-text-field>
<!-- 
      <v-checkbox
      v-model="isAvailable"
      label="Is Available?"
      required
      ></v-checkbox> -->

      <!-- <v-checkbox
      v-model="isAssy"
      label="Is Assy?"
      required
      ></v-checkbox> -->

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
      isAvailable: false,
      isAssy: false,
      nama: '',
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 12 && v.length >= 3) || 'Kode must be 3-12 characters',
      ],
      classificationCode: null,
      groupCode: null,
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
              code : this.kode,
              nama : this.nama
              // isAvailable : this.isAvailable,
              // isAssy : this.isAssy,
              // classificationCode : this.classificationCode,
              // groupCode : this.groupCode
          })
        
          if(res.data.status == "berhasil"){
            this.snackbar = {
              show : true,
              message : "Tambah Jenis Material Berhasil",
              color : "green"
            }
            location.replace('/listMaterialType')
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