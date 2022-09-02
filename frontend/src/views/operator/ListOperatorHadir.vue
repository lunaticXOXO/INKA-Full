<template>
    <v-app>
        <v-card class="mx-auto text-center mt-6 mb-6" max-width="1000" elevation="0">
            <h1>Operator Hadir</h1>
        </v-card>
        <div class="d-flex mx-auto text-center" max-width="1000">
            <v-card v-for="item in items" :key="item" class="mx-2" width="150">
                <div class="">
                    <v-img
                        max-height="80"
                        max-width="80" 
                        src="../operator/contoh-profile.jpg"
                        class="ma-6 ml-9">
                    </v-img>
                    <p>{{ item.title }}</p>
                    <p>{{ item.name }}</p>
                </div>
            </v-card>
        </div>
        
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { title: '651100028', name: 'SAEPUDIN' },
                { title: '999900105', name: 'PURYADI' },
                { title: '651400111', name: 'WAHYUDI' },
                { title: '651100023', name: 'MUHAMMAD AZIZ K' },
                { title: '651600506', name: 'JEMY HERDIAN NUR' },
                { title: '651400110', name: 'KUSANTOK'},
                { title: '651600010', name: 'ERWIN DWI ANDRIYANTO'},
                { title: '651600437', name: 'DANY WAHYU S'},
                { title: '651600475', name: 'BAGAS LIDAKDHO'},
                { title: '651500190', name: 'PUPUT ABDUL SAPUTRA'},
            ]
        }
    }
}
</script>