<template>
  <v-app>
    <div class="d-flex">
      <v-card
        class="mx-auto text-center mt-6"
        color="gray"
        dark
        max-width="1000"
      >
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)">
          <v-sparkline
            :value="value"
            color="rgba(255, 255, 255, .7)"
            height="100"
            padding="24"
            stroke-linecap="round"
            smooth
            type="trend"
          >
            <template v-slot:label="item">
              {{ item.value }} Proyek
            </template>
          </v-sparkline>
        </v-sheet>
      </v-card-text>

      <v-card-text>
        <div class="text-h4 font-weight-thin">
          Jumlah Proyek Dipesan 1 Minggu
        </div>
      </v-card-text>

    <v-divider></v-divider>
    </v-card>

    <v-card
      class="mx-auto text-center mt-6"
      color="gray"
      dark
      max-width="1000"
    >
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :value="value2"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
          type="bar"
        >
          <template v-slot:label="item">
            {{ item.value }} Jam
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Jumlah Jam Kerja Operator di WS1
      </div>
    </v-card-text>

    <v-divider></v-divider>
    </v-card>
  </div>

  <div class="mx-auto mt-8">
    <v-data-table
      :headers = "column"
      :items = "jenisproduk">
    </v-data-table>
  </div>

  <div class="d-flex mx-auto mt-8">
    <v-card
      class="mx-14"
    >
      <vue-bar-graph
      :show-y-axis="true"
      :show-x-axis="true"
      :show-values="true"
      :points="[3,5,2,1,4]"
      :width="400"
      :height="200"
      :use-custom-labels="true"
      :custom-labels="monthLabels"
    />
    </v-card>
    
    <v-card
      class="mx-14"
    >
      <vue-bar-graph
      :show-y-axis="true"
      :show-x-axis="true"
      :show-values="true"
      :points="[3,5,2,1,4]"
      :width="400"
      :height="200"
      :use-custom-labels="true"
      :custom-labels="wsLabels"
      :show-trend-line="true"
      :trend-line-width="2"
      trend-line-color="red"
    />
    </v-card>
  </div>
  
  </v-app>
</template>

<script>
  import VueBarGraph from '../components/VueBarGraph.vue';
  export default {
    components:{
      VueBarGraph
    },

    data: () => ({
      value: [
        2,
        6,
        7,
        9,
        11,
        12,
        15,
      ],
      value2: [
        4,
        2,
        3,
        1,
        7,
        6,
        5,
      ],
      monthLabels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
      wsLabels: ['WS1', 'WS2', 'WS3', 'WS4', 'WS5', 'WS6', 'WS7', 'WS8', 'WS9', 'WS10'],
    }),
  }
</script>