<template>
    <div class="background">
        <v-main class="d-flex justify-center align-center">
            <v-col cols="10" lg="4" class="mx-auto">
                <v-card class="pa-4">
                    <div class="text-center">
                        <v-avatar size="100" color="grey lighten-2">
                            <v-icon size="40" color="#555555">mdi-lock</v-icon>
                        </v-avatar>
                        <h2 class="#555555--text">Login Page</h2>
                    </div>
                    <v-form @submit.prevent="submitHandler" ref="form">
                        <v-card-text>
                            <v-text-field
                                v-model="email"
                                :rules="emailRules"
                                type="email"
                                label="Email"
                                placeholder="Email"
                                prepend-inner-icon="mdi-account"/>
                            <v-text-field
                                v-model="password"
                                :rules="passwordRules"
                                :type="passwordShow?'text':'password'"
                                label="Password"
                                placeholder="Password"
                                prepend-inner-icon="mdi-key"
                                :append-icon="passwordShow ? 'mdi-eye':'mdi-eye-off'"
                                @click:append="passwordShow = !passwordShow">
                            </v-text-field>
                            <v-switch label="Remember Me" color="gray"></v-switch>
                        </v-card-text>
                        <v-card-actions class="justify-center">
                            <v-btn :loading="loading" :to="route" type="submit" color="#555555">
                                <span class="white--text px-8">Login</span>
                            </v-btn>
                        </v-card-actions>
                    </v-form>
                </v-card>
            </v-col>
        </v-main>
        <v-snackbar top color="green" v-model="snackBar">
            Login Success!
        </v-snackbar>
    </div>
</template>
<script>
export default {
    name: 'LoginPage',
    data: () => ({
        route: "",
        passwordShow: false,
        loading: false,
        snackBar: false,
        password: '',
        passwordRules: [
            v => !!v || 'Password is required',
        ],
        email: '',
        emailRules: [
            v => !!v || 'Email is required',
            v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
    }),
    methods: {
        submitHandler() {
            if(this.$refs.form.validate()){
                this.loading = true
                this.route = "/"
                setTimeout(() => {
                    this.loading = false
                    this.snackBar = true
                    this.route = "/"
                }, 3000)
            }
            console.log(this.email)
            console.log(this.password)
        }
    }
}
</script>