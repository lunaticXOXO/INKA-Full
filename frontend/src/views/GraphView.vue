<template>
  <v-app>
     
      <v-card
        class="mx-auto text-center mt-6"
        width="1500" 
        
        >

      <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
            >
      <v-card-title class="text-h5">
        PROGRESS PERSENTASE PROYEK
      </v-card-title>
            
      </v-card> 
      <br> 

      <v-card>
     
        <div class="app">
          <apexchart ref="realtimeChart" type="line" height="550" :options="chartOptions" :series="chartSeries"></apexchart>
        </div>
        <v-card-text>
          <div class="text-h4">
            Kurva S
          </div>
        </v-card-text>
      </v-card>
      <v-divider></v-divider>
    </v-card>

    <!-- <v-card
      class="mx-auto text-center mt-6"
      color="gray"
      dark
      max-width="500"
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
    </v-card> -->
 

    <br><br>
  <!-- BAR GRAPH
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
  -->
  </v-app>
</template>

<script>
  //import VueBarGraph from '../components/VueBarGraph.vue';
  import VueApexCharts from 'vue-apexcharts'

  export default {
    components:{
      //VueBarGraph,
      apexchart: VueApexCharts,
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

    
        index : undefined,
        proyekname : '',
        
        chartSeries : [],

        chartOptions: {
         
          dataLabels: {
            enabled: true,
            group : true
          },

          stroke: {
            curve: 'smooth'
          },

          grid: {
            row: {
              colors: ['#f3f3f3', 'transparent'],
              opacity: 0.5
            },
          },
        },
      }
    },

    mounted(){
      this.fetchProgressProyek()
    },

    methods: {
      async fetchProgressProyek(){
        const axios = require('axios')
        const res = await axios.get('/proyek/show_progress_percentage_proyek')
        if(res.data == null){
            console.log("Data kosong")
        }else{
            const data = res.data
            this.chartSeries = this.processChartData(data)

        } 
      },

      processChartData(rawData){

        const groupedData = {}
        rawData.forEach(item => {
           const label = item.z;
           if (!groupedData[label]){
              groupedData[label] = {name : label, data : []};

           }
           groupedData[label].data.push(item.y)

        })
        return Object.values(groupedData);
      }


    }
  }
</script>