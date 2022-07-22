<template>
    <div class="background">
        <v-main class="d-flex justify-center align-center">
            <v-col cols="10" lg="4" class="mx-auto">
                <v-card class="pa-4">
                    <div class="text-center">
                        <v-avatar size="100" color="grey lighten-2">
                            <v-icon size="40" color="#555555">mdi-lock</v-icon>
                        </v-avatar>
                        <h2 class="#555555--text mt-4">Login Page</h2>
                    </div>
                    <v-form @submit.prevent="submitHandler" ref="form">
                        <v-card-text>
                            <v-text-field
                                v-model="username"
                                type="text"
                                label="Username"
                                placeholder="Username"
                                prepend-inner-icon="mdi-account"/>
                            <v-text-field
                                v-model="passwords"
                                :rules="passwordRules"
                                :type="passwordShow?'text':'password'"
                                label="Password"
                                placeholder="Password"
                                prepend-inner-icon="mdi-key"
                                :append-icon="passwordShow ? 'mdi-eye':'mdi-eye-off'"
                                @click:append="passwordShow = !passwordShow">
                            </v-text-field>
                        </v-card-text>
                        <v-card-actions class="justify-center">
                            <v-btn :loading="loading" type="submit" color="#555555">
                                <span class="white--text px-8">Login</span>
                            </v-btn>
                        </v-card-actions>
                    </v-form>
                </v-card>
            </v-col>
        </v-main>
        <v-snackbar top color="green" v-model="snackBar" open="/">
            Login Success!
        </v-snackbar>
    </div>
</template>

<script>
import axios from "axios";
import Login from "../services/Login.js"

export default {
    name: 'LoginPage',
    data: () => ({
        passwordShow: false,
        loading: false,
        snackBar: false,
        username: '',
        passwords: '',
        passwordRules: [
            v => !!v || 'Password is required',
        ],
        loginService: new Login(),
    }),

    methods: {
        submitHandler() {
            // if(this.$refs.form.validate()){
            //     this.loading = true
            //     this.route = "/"
            //     setTimeout(() => {
            //         this.loading = false
            //         this.snackBar = true
            //         this.route = "/"
            //     }, 3000)
            // }
            console.log(this.username)

            if(this.$refs.form.validate()){
                this.loading = true
                let tipeUser
                setTimeout(() => {
                    axios.post("/login", 
                    { username: this.username,
                      passwords: this.passwords
                    })
                    .then((response) => {
                        console.log(response.data.userType)
                        tipeUser = response.data.userType
                        this.loginService.addToUserType(tipeUser)
                        this.loading = false
                        this.snackBar = true
                        location.replace("/")
                        open("/")
                    })
                    .catch((error) => {
                        console.log(error)
                    });
                }, 3000)
            }
        }
    }
}
</script>