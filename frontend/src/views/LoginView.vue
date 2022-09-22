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
        <div v-if="snackBar == true">
        <v-snackbar top color="green" v-model="snackBar">
            Login Success!
        </v-snackbar>
        </div>

        <div v-if="snackBar2 == true">
        <v-snackbar top color="red" v-model="snackBar2">
            Wrong Username or Password!
        </v-snackbar>
        </div>
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
        snackBar2: false,
        username: '',
        passwords: '',
        passwordRules: [
            v => !!v || 'Password is required',
        ],
        loginService: new Login(),
    }),

    methods: {
        submitHandler() {
            console.log(this.username)
            if(this.$refs.form.validate()){
                this.loading = true
                setTimeout(() => {
                    axios.post("/login", 
                    { username: this.username,
                      passwords: this.passwords
                    })
                    .then((response) => {
                        if(response.data.status == 'berhasil'){
                            let tipeUser
                            let uname
                            tipeUser = response.data.userType
                            uname = response.data.username
                            this.loginService.addToUserType(tipeUser)
                            this.loginService.addToUsername(uname)
                            this.loading = false
                            this.snackBar = true
                            location.replace("/")
                        }else if(response.data.status == 'gagal'){
                            this.loading = false
                            this.snackBar2 = true
                            location.replace("/login")
                        }
                        console.log(response)
                    })
                    .catch((error) => {
                        console.log(error)
                    });
                }, 2000)
            }
        }
    }
}
</script>