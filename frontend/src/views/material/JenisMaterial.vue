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
            v-model="kode"
            :counter="12"
            :rules="kodeRules"
            label="Kode"
            required
            ></v-text-field>

            <v-select
            v-model="klasifikasi"
            :items="list_klasifikasi"
            label="Klasifikasi"
            required
            ></v-select>

            <v-select
            v-model="grup"
            :items="list_grup"
            label="Grup"
            required
            ></v-select>

            <v-text-field
            v-model="nama"
            label="Nama"
            ></v-text-field>

            <v-checkbox
            v-model="available"
            label="Is Available?"
            required
            ></v-checkbox>

            <v-checkbox
            v-model="assy"
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
        v => (v && v.length <= 12 && v.length >= 9) || 'Kode must be 9-12 characters',
      ],
      klasifikasi: null,
      grup: null,
      list_klasifikasi: undefined,
      list_grup: undefined,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      submitHandler() {
        console.log(this.kode)
        console.log(this.klasifikasi)
        console.log(this.grup)
        console.log(this.nama)
        console.log(this.checkbox)
      },
    },
  }
</script>