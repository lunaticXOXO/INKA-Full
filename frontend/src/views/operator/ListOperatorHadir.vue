<template>
    <v-app>
        <v-card class="mx-auto text-center mt-6 mb-6" max-width="1000" elevation="0">
            <h1>Operator Hadir</h1>
        </v-card>
        <v-card class="mx-auto" max-width="1250" elevation="0">
            <v-container fluid>
                <v-row dense>
                    <v-col
                        v-for="item in items"
                        :key="item"
                        :cols="item.flex"
                    >
                        <v-card class="mx-auto justify-center text-center" elevation="0" outlined>
                            <v-img
                                max-height="80"
                                max-width="80" 
                                src="../operator/contoh-profile.jpg"
                                class="ma-6 ml-14">
                            </v-img>
                            <p>{{ item.title }}</p>
                            <p>{{ item.name }}</p>  
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { title: '651100028', name: 'SAEPUDIN', flex: 2 },
                { title: '999900105', name: 'PURYADI', flex: 2 },
                { title: '651400111', name: 'WAHYUDI', flex: 2 },
                { title: '651100023', name: 'MUHAMMAD AZIZ K', flex: 2 },
                { title: '651600506', name: 'JEMY HERDIAN NUR', flex: 2 },
                { title: '651400110', name: 'KUSANTOK', flex: 2},
                { title: '651600010', name: 'ERWIN DWI ANDRIYANTO', flex: 2},
                { title: '651600437', name: 'DANY WAHYU S', flex: 2},
                { title: '651600475', name: 'BAGAS LIDAKDHO', flex: 2},
                { title: '651500190', name: 'PUPUT ABDUL SAPUTRA', flex: 2},
            ],
        }
    }
}
</script>