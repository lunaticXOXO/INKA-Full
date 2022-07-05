<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Rincian Proyek Baru</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="id"
            :counter="4"
            :rules="idRules"
            label="ID"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
            type="submit"
            @click="validate"
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
            Insert Jenis Produk Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      nama: '',    
      id: '',
      idRules: [
        v => !!v || 'ID is required',
        v => (v && v.length <= 4 && v.length >= 1) || 'Kode must be 1-4 characters',
      ],
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      submitHandler() {
        console.log(this.id)
        console.log(this.nama)
      },
    },
  }
</script>