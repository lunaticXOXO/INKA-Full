<template>
    <v-app>
        <div class="d-flex ma-8">
            <h2>Stasiun Kerja</h2>
        </div>
        <div class="d-flex ma-8">
            <v-card v-for="item in items" :key="item" class="pa-4 mx-8">
                <v-icon large>mdi-space-station</v-icon>
                <p>{{ item.title }}</p>
                <p>{{ item.name }}</p>
            </v-card>
        </div>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { title: 'WS1', name: 'Welding' },
                { title: 'WS2', name: 'Fabrikasi' },
                { title: 'WS3', name: 'Elektrikal' },
                { title: 'WS4', name: 'Laser Machine' },
                { title: 'WS5', name: 'Workbench' },
                { title: 'WS6', name: 'Fabrikasi'},
                { title: 'WS7', name: 'Welding'},
                { title: 'WS8', name: 'Laser Machine'},
                { title: 'WS9', name: 'Workbench'},
                { title: 'WS10', name: 'Elektrikal'},
            ]
        }
    }
}
</script>