<template>
  <v-app>
    <v-card class="mx-auto text-center" max-width="1000" elevation="0">
      <p id="judul" class="font-weight-thin">SmartWorks 4.0</p>
    </v-card>
   

    <v-carousel cycle :show-arrows="false" delimiter-icon="mdi-minus" height="850" :interval="5000">
      
      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir
        </div>
         
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
        
          <v-col
          
          v-for=" index in listOperator"
          :key="index"
          cols="4"
          sm="auto"
          >

          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>

      </v-carousel-item>
      
      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS01
        </div>
         
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS01"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS02
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS02"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS03
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS03"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS04
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS04"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS05
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS05"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS06
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS06"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
         <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS07
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS07"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS08
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS08"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Operator Hadir Pada WS09
        </div>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperatorWS09"
          :key="index"
          cols="8"
          sm="auto"
          >
          <v-card width ="350" height ="300" class="mt-5">
            <v-img
                height="200"
                width="200" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
                class="mx-auto text-center mt-7"
            >
            </v-img>
            <v-card-title class="text-black" v-text="index.nama"></v-card-title>
            <v-card-text class="text-black" v-text="index.uuid"></v-card-text>
            
          </v-card>
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
            Jadwal Pengerjaan Operasi
        </div>
        <v-card class="mt-10 mx-10">
          <g-gantt-chart
            :chart-start="myChartStartCustom"
            :chart-end="myChartEndCustom"
            :row-label-width="`${rowLabelWidth}%`"
            :row-height="rowHeight"
            :grid="grid"
            :theme="selectedTheme"
          >
            <g-gantt-row
              label="WS00 Plan"
              :bars="itemsWS00"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS00 Actual"
              :bars="itemsWS00"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS01 Plan"
              :bars="itemsWS01"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS01 Actual"
              :bars="itemsWS01"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS02 Plan"
              :bars="itemsWS02"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS02 Actual"
              :bars="itemsWS02"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS03 Plan"
              :bars="itemsWS03"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS03 Actual"
              :bars="itemsWS03"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS04 Plan"
              :bars="itemsWS04"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS04 Actual"
              :bars="itemsWS04"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS05 Plan"
              :bars="itemsWS05"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

              <g-gantt-row
              label="WS05 Actual"
              :bars="itemsWS05"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS06 Plan"
              :bars="itemsWS06"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS06 Actual"
              :bars="itemsWS06"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS07 Plan"
              :bars="itemsWS07"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS07 Actual"
              :bars="itemsWS07"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS08 Plan"
              :bars="itemsWS08"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS08 Actual"
              :bars="itemsWS08"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS09 Plan"
              :bars="itemsWS09"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

              <g-gantt-row
              label="WS09 Actual"
              :bars="itemsWS09"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

          </g-gantt-chart>
        </v-card>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Ketersediaan Material Pada Gudang
        </div>
        <v-data-table>

        </v-data-table>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Persentase Proyek
        </div>
        <v-row
          class="fill-height"
          :align="center"
          justify="center"
        >
          <v-card
            class="mx-auto my-auto text-center"
            width="1000">
            <v-data-table
              :headers = "headers"
              :items = "proyek"> 
              <!-- <template v-slot:[`item.id`]="{ item }">
                  <span>{{item.id}}</span>
              </template>
              <template v-slot:[`item.nama`]="{ item }">
                  <span>{{item.nama}}</span>
              </template>
              <template v-slot:[`item.customerid`]="{ item }">
                  <span>{{item.customerid}}</span>
              </template>
              <template v-slot:[`item.percentage`]="{ item }">
                  <span>{{item.percentage}}%</span>
              </template> -->
            </v-data-table>
          </v-card>
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
        <div class="text-h3 mx-auto text-center">
             Summary
        </div>


    <v-container
    id="dashboard"
    fluid
    tag="section"
  >
    <v-row   class="fill-height"
          :align="center"
          justify="center">
    
      >
      <v-col cols="12" lg="4">  
      
        
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
       
      </v-col>
      </v-row>
      </v-container>
      </v-carousel-item>

    </v-carousel>
  </v-app>
</template>

<script>
  import {GGanttChart, GGanttRow} from 'vue-ganttastic'
  //import VueApexCharts from 'vue-apexcharts'

  var today = new Date();
  var newDate = new Date(Date.now()+1*24*60*60*1000);
  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var date2 = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+ newDate.getDate();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  var dateTime = date+' '+time;
  var dateTime2 = date2+' '+time;

  export default {
    components:{
      GGanttChart,
      GGanttRow,
     
    },

    data(){
      return {

        emailsSubscriptionChart: {
          data: {
            labels: ['Ja', 'Fe', 'Ma', 'Ap', 'Mai', 'Ju', 'Jul', 'Au', 'Se', 'Oc', 'No', 'De'],
            series: [
              [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],

            ],
          },
          options: {
            axisX: {
              showGrid: false,
            },
            low: 0,
            high: 1000,
            chartPadding: {
              top: 0,
              right: 5,
              bottom: 0,
              left: 0,
            },
          },
          responsiveOptions: [
            ['screen and (max-width: 640px)', {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function (value) {
                  return value[0]
                },
              },
            }],
          ],
        },

        headers:[   
          {text : 'ID',               value : 'id'},
          {text : 'Nama',             value : 'nama'},
          {text : 'Customer ID',      value : 'customerid'},
          {text : 'Progress',         value : 'percentage'},
        ],
        headers2:[   
          {text : 'ID',         value : 'operatorid'},
          {text : 'WS',         value : 'workstationCode'},
          {text : 'Login',      value : 'login'},
        ],
        proyek:[],
        customer:[],
        colors: [
          'white',
          'white',
          'white',
          'white',
          'white',
        ],
        slides: [
          'Operator Hadir',
          'Operator pada WS01',
          'Operator pada WS02',
          'Operator pada WS03',
          'Operator pada WS04',
          'Operator pada WS05',
          'Operator pada WS06',
          'Operator pada WS07',
          'Operator pada WS08',
          'Operator pada WS09',
          'Jadwal Operasi WS',
          'Material pada Gudang',
          'Persentase Proyek',
        ],
        listOperator: [],
        listOperatorWS01: [],
        listOperatorWS02: [],
        listOperatorWS03: [],
        listOperatorWS04: [],
        listOperatorWS05: [],
        listOperatorWS06: [],
        listOperatorWS07: [],
        listOperatorWS08: [],
        listOperatorWS09: [],
        itemsWS00: undefined,
        itemsWS01: undefined,
        itemsWS02: undefined,
        itemsWS03: undefined,
        itemsWS04: undefined,
        itemsWS05: undefined,
        itemsWS06: undefined,
        itemsWS07: undefined,
        itemsWS08: undefined,
        itemsWS09: undefined,
        rowHeight: 30,
        rowLabelWidth: 15,
        grid: true,
        selectedTheme: "vue",
        dialogWS00: undefined,
        dialogWS01: undefined,
        dialogWS02: undefined,
        dialogWS03: undefined,
        dialogWS04: undefined,
        dialogWS05: undefined,
        dialogWS06: undefined,
        dialogWS07: undefined,
        dialogWS08: undefined,
        dialogWS09: undefined,
        tanggalPencarian: dateTime,
        tanggalPencarian2: dateTime2,
        myChartStartCustom: dateTime,
        myChartEndCustom: dateTime2,
        itemsWS: [
          { name: 'WORKSTATION00',   flex: 2 },
          { name: 'WORKSTATION01',   flex: 2 },
          { name: 'WORKSTATION02',   flex: 2 },
          { name: 'WORKSTATION03',   flex: 2 },
          { name: 'WORKSTATION04',   flex: 2 },
          { name: 'WORKSTATION05',   flex: 2 },
          { name: 'WORKSTATION06',   flex: 2 },
          { name: 'WORKSTATION07',   flex: 2 },
          { name: 'WORKSTATION08',   flex: 2 },
          { name: 'WORKSTATION09',   flex: 2 },
        ],

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
      }
    },

    mounted(){
      this.getLinkOperator(),
      this.fetchDataStatusWS00(),
      this.fetchDataStatusWS01(),
      this.fetchDataStatusWS02(),
      this.fetchDataStatusWS03(),
      this.fetchDataStatusWS04(),
      this.fetchDataStatusWS05(),
      this.fetchDataStatusWS06(),
      this.fetchDataStatusWS07(),
      this.fetchDataStatusWS08(),
      this.fetchDataStatusWS09(),
      this.fetchData(),
      this.fetchCustomer(),
      this.tanggal(),
      this.fetchOperatorOnWS(),
      this.fetchOperatorOnWS01(),
      this.fetchOperatorOnWS02(),
      this.fetchOperatorOnWS03(),
      this.fetchOperatorOnWS04(),
      this.fetchOperatorOnWS05(),
      this.fetchOperatorOnWS06(),
      this.fetchOperatorOnWS07(),
      this.fetchOperatorOnWS08(),
      this.fetchOperatorOnWS09()
    },

    methods : {
      async tanggal() {
        const date = new Date(this.tanggalPencarian)
        date.setDate(date.getDate() + 1);
        this.myChartStartCustom = this.tanggalPencarian

        const date2 = new Date(this.tanggalPencarian2)
        date2.setDate(date2.getDate() + 1);
        this.myChartEndCustom = this.tanggalPencarian2
        
        console.log(this.myChartStartCustom)
        console.log(this.myChartEndCustom)
      },

      async fetchData(){
        try{
          const axios = require('axios')
          const res = await axios.get(`/proyek/get_allproyek`);
          if(res.data == null){
              alert("Proyek Kosong")
          }else{
              this.proyek = res.data;
              console.log(res,this.data)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async fetchOperatorOnWS(){
        try{
          const axios = require('axios')
          const res = await axios.get(`/operator/get_operator_on_ws`);
          if(res.data == null){
              console.log("Operator Kosong")
          }else{
              this.listOperatorOnWS = res.data;
              console.log(res,this.listOperatorOnWS)
          }
        } 
        catch(error){
            alert("Error")
            console.log(error)
        }
      },

      async fetchCustomer(){
        try{
          const axios = require('axios')
          const res = await axios.get('/customers/get_customers');
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.customer = res.data
            console.log(res,this.customer)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async getLinkOperator(){
        try{
          const axios = require('axios')
          const res = await axios.get('/operator/get_operator_hadir')
          if (res.data == null){
              console.log("data kosong")
          }else{
              this.listOperator = res.data
              console.log(res,this.listOperator)
          }
        }catch(error){
            console.log(error)
        }
      },

      async fetchDataStatusWS00(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws00')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS00 = res.data
          console.log(res,this.itemsWS00)
        }
      },

      async fetchDataStatusWS01(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws01')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS01 = res.data
          console.log(res,this.itemsWS01)
        }
      },

      async fetchDataStatusWS02(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws02')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS02 = res.data
          console.log(res,this.itemsWS02)
        }
      },

      async fetchDataStatusWS03(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws03')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS03 = res.data
          console.log(res,this.itemsWS03)
        }
      },

      async fetchDataStatusWS04(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws04')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS04 = res.data
          console.log(res,this.itemsWS04)
        }
      },

      async fetchDataStatusWS05(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws05')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS05 = res.data
          console.log(res,this.itemsWS05)
        }
      },

      async fetchDataStatusWS06(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws06')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS06 = res.data
          console.log(res,this.itemsWS06)
        }
      },

      async fetchDataStatusWS07(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws07')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS07 = res.data
          console.log(res,this.itemsWS07)
        }
      },

      async fetchDataStatusWS08(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws08')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS08 = res.data
          console.log(res,this.itemsWS08)
        }
      },

      async fetchDataStatusWS09(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_gantt/ws09')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS09 = res.data
          console.log(res,this.itemsWS09)
        }
      },

      async fetchOperatorOnWS01(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws01')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS01 = res.data
          console.log(res,this.listOperatorWS01)
        }
      },

      async fetchOperatorOnWS02(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws02')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS02 = res.data
          console.log(res,this.listOperatorWS02)
        }
      },

      async fetchOperatorOnWS03(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws03')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS03 = res.data
          console.log(res,this.listOperatorWS03)
        }
      },

      async fetchOperatorOnWS04(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws04')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS04 = res.data
          console.log(res,this.listOperatorWS04)
        }
      },

      async fetchOperatorOnWS05(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws05')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS05 = res.data
          console.log(res,this.listOperatorWS05)
        }
      },

      async fetchOperatorOnWS06(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws06')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS06 = res.data
          console.log(res,this.listOperatorWS06)
        }
      },

      async fetchOperatorOnWS07(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws07')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS07 = res.data
          console.log(res,this.listOperatorWS07)
        }
      },

      async fetchOperatorOnWS08(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws08')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS08 = res.data
          console.log(res,this.listOperatorWS08)
        }
      },

      async fetchOperatorOnWS09(){
        const axios = require('axios')
        const res = await axios.get('/operator/get_operator_on_ws09')
        if(res.data == null){
          console.log("Data kosong")
        }else{
          
          this.listOperatorWS09 = res.data
          console.log(res,this.listOperatorWS09)
        }
      },




      

    },
  }
</script>

<style>
  #judul{
    font-size: 5rem;
    margin-top: 5%;
    margin-bottom: 5%;
  }
</style>
