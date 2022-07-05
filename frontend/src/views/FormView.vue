<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1 class="font-weight-thin">Tambah Tipe Produk</h1>
        <v-form
            class="pa-6"
            ref="form"
            v-model="valid"
            lazy-validation
        >
            <v-text-field
            v-model="kode"
            :counter="4"
            :rules="kodeRules"
            label="Kode"
            required
            ></v-text-field>

            <v-text-field
            v-model="nama"
            :rules="namaRules"
            label="Nama"
            required
            ></v-text-field>

            <v-text-field
            v-model="deskripsi"
            :rules="deskripsiRules"
            label="Deskripsi"
            required
            ></v-text-field>

            <v-select
            v-model="select"
            :items="items"
            :rules="[v => !!v || 'Item is required']"
            label="Item"
            required
            ></v-select>

            <v-checkbox
            v-model="checkbox"
            :rules="[v => !!v || 'You must agree to continue!']"
            label="Is the information correct?"
            required
            ></v-checkbox>

            <v-btn
            :disabled="!valid"
            color="success"
            class="mr-4"
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

            <v-btn
            color="warning"
            @click="resetValidation"
            >
            Reset Validation
            </v-btn>
        </v-form>
    </v-card>
    <!--v => /.+@.+\..+/.test(v) || 'E-mail must be valid',-->
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      nama: '',
      namaRules: [
        v => !!v || 'Name is required',
      ],
      kode: '',
      kodeRules: [
        v => !!v || 'Kode is required',
        v => (v && v.length <= 4 && v.length >=4) || 'Kode must be 4 characters',
      ],
      deskripsi: '',
      deskripsiRules: [
        v => !!v || 'Deskripsi is required',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  }
</script>