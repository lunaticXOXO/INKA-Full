<template>
    <nav>
        <v-app-bar app color="#6f6f6f">
            <v-app-bar-title class="text-uppercase">
                <span class="font-weight-light white--text">Smart</span>
                <span class="white--text">Works 4.0</span>
            </v-app-bar-title>
            <v-img 
                max-height="50"
                max-width="50" 
                src="../assets/itb.png"
                class="mx-2">
            </v-img>
            <v-img 
                max-height="70"
                max-width="70" 
                src="../assets/lpdp.png"
                class="mr-3">
            </v-img>
            <v-img 
                max-height="70"
                max-width="70" 
                src="../assets/inka.png"
                class="mb-1 mr-4">
            </v-img>
            <v-spacer></v-spacer>
            <v-btn :to="route" color="grey">
                <span>Login</span>
                <v-icon right>mdi-key</v-icon>
            </v-btn>
        </v-app-bar>
    </nav>
</template>

<script>
export default {
    data(){
        return {
            route: "/login",
            routeHome: "/",
        }
    }
}
</script>

<style>
    #border{
        border-radius: 50%;
    }
</style>