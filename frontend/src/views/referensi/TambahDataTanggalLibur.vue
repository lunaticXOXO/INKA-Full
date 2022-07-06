<template>
    <v-card
        class="mx-auto text-center mt-6"
        max-width="1000">
        <br>
        <h1>Tambah Tanggal Libur</h1>
        <v-form
            class="pa-6"
            ref="form"
            @submit.prevent="submitHandler"
            v-model="valid"
            lazy-validation
        >
            <v-menu>
                <template v-slot:activator="{ on, attrs }">
                    <v-text-field :value="tanggal" v-bind="attrs" v-on="on" label="Choose Date" prepend-icon="mdi-calendar"></v-text-field>
                </template>
                <v-date-picker width="1000" v-model="tanggal"></v-date-picker>
            </v-menu>
            
            <br>
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
            Insert Tanggal Libur Sukses!
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      snackBar: false,
      tanggal: null,
      tanggalRules: [
        v => !!v || 'Tanggal is required',
      ],
    }),

    methods: {
      validate () {
        if(this.$refs.form.validate()){
          this.InsertTanggalLibur()
        }
      },

      reset () {
        this.$refs.form.reset()
      },

      submitHandler() {
        console.log(this.tanggal)
      },
    },
  }
</script>