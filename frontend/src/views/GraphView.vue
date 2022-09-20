<template>
  <v-app>
    <div class="d-flex">
      <v-card
        class="mx-auto text-center mt-6"
        color="black"
        dark
        max-width="1000"
      >
      <v-card>
        <!--
        <v-sheet color="rgba(0, 0, 0, .12)">
          <v-sparkline
            :value="value"
            color="rgba(255, 255, 255, .7)"
            height="100"
            padding="24"
            stroke-linecap="round"
            curve
            type="trend"
          >
            <template v-slot:label="item">
              {{ item.value }} Proyek
            </template>
          </v-sparkline>
        </v-sheet>
        -->
        <div class="app">
      <apexcharts width="550" type="line" :options="chartOptions" :series="series"></apexcharts>
    </div>
    <v-card-text>
        <div class="text-h4 font-weight-thin">
          Persentasi Progress Proyek
        </div>
      </v-card-text>
      </v-card>
   


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

    <v-card
      class="mx-14"
    >
      <vue-bar-line
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

      >
      </vue-bar-line>

    </v-card>
    

  </div>
  
  </v-app>
</template>

<script>
  import VueBarGraph from '../components/VueBarGraph.vue';
  import VueApexCharts from 'vue-apexcharts'

  export default {
    components:{
      VueBarGraph,
      apexcharts: VueApexCharts,
    },
    
    data : function(){
    return {
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

      
      chartOptions: {
            chart: {
              id: 'vuechart-example',
            },
            xaxis: {
              categories: ['Sat, 17 Sep 2022 22:28:34 GMT','Sun, 18 Sep 2022 16:29:57 GMT','Sun, 18 Sep 2022 21:37:49 GMT','Sun, 18 Sep 2022 21:37:50 GMT'],
              categories2 : undefined
            },
            stroke : {
                curve : 'smooth'
            }
          },
          series: [{
           
            data: [25, 50, 75,100],
            data2 : undefined
          }]
    }

    },
    mounted(){
      this.fetchProgressProyek()
    },
    methods: {
        updateChart() {
      
          const newData = this.series[0].data.map
          this.series = [{
            data: newData
          }]
        },

        async fetchProgressProyek(){
            const axios = require('axios')
            const res = await axios.get('/proyek/show_progress_proyek')
            if(res.data == null){
               console.log("Data kosong")
            }else{
              this.chartOptions.xaxis.categories2 = res.data[0].selesai
              this.chartOptions.series.data2 = res.data[0].percentage
              //console.log(this.chartOptions.xaxis.categories2,this.chartOptions.series.data2)
              console.log(res)
            }            

        }
        

      
      }
  }
</script>