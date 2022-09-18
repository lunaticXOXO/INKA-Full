<template>
    <div class="app">
      <apexcharts width="550" type="line" :options="chartOptions" :series="series"></apexcharts>
      <div>
        <button @click="updateChart">Update!</button>
    </div>
    </div>
  </template>
  
  <script>
  import VueApexCharts from 'vue-apexcharts'
  
  export default {
    name: 'Chart',
    components: {
      apexcharts: VueApexCharts,
    },
    data: function() {
        return {
          chartOptions: {
            chart: {
              id: 'vuechart-example',
            },
            xaxis: {
              categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
            },
            stroke : {
                curve : 'curve'
            }
          },
          series: [{
            name: 'series-1',
            data: [30, 40, 45, 50, 49, 60, 70, 81]
          }]
        }
      },
      methods: {
        updateChart() {
          const max = 90;
          const min = 20;
          const newData = this.series[0].data.map(() => {
            return Math.floor(Math.random() * (max - min + 1)) + min
          })
          // In the same way, update the series option
          this.series = [{
            data: newData
          }]
        }
      }
  }
  </script>
  <style scoped>
    button {
      background: #26E6A4;
      border: 0;
      font-size: 16px;
      color: '#fff';
      padding: 10px;
      margin-left: 28px;
    }
  </style>
  
  