<template>
  <v-app>
    <v-card class="mx-auto text-center" max-width="1000" elevation="0">
      <p id="judul" class="font-weight-thin">SmartWorks 4.0</p>
    </v-card>
    <v-carousel
      cycle
      height="100"
      hide-delimiters
      :show-arrows="false"
      :interval="15000"
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-sheet
          :color="colors[i]"
          height="100%"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div class="text-h3">
              {{ slide }}
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-carousel cycle :show-arrows="false" delimiter-icon="mdi-minus" height="700" :interval="15000">
      <v-carousel-item>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-col
          v-for=" index in listOperator"
          :key="index"
          cols="8"
          sm="auto"
          >
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>
      
      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
            <v-img
                height="200"
                width="150" 
                :src="require(`@/views/operator/foto/${index.link}`)" 
            >
            </v-img>
              <span class="mx-auto"><b>{{index.uuid}}</b></span>
            <br>
            <span class="mx-auto"><b>{{index.nama}}</b></span> 
          </v-col> 
        </v-row>
      </v-carousel-item>

      <v-carousel-item>
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
              label="WS00"
              :bars="itemsWS00"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS01"
              :bars="itemsWS01"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS02"
              :bars="itemsWS02"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS03"
              :bars="itemsWS03"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS04"
              :bars="itemsWS04"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS05"
              :bars="itemsWS05"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS06"
              :bars="itemsWS06"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS07"
              :bars="itemsWS07"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS08"
              :bars="itemsWS08"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

            <g-gantt-row
              label="WS09"
              :bars="itemsWS09"
              bar-start="rencanaMulai"
              bar-end="rencanaSelesai"
            >
            </g-gantt-row>

          </g-gantt-chart>
        </v-card>
      </v-carousel-item>

      <v-carousel-item>
        Material pada Gudang
        <v-data-table>

        </v-data-table>
      </v-carousel-item>

      <v-carousel-item>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <v-card
            class="mx-auto my-auto text-center"
            width="1000">
            <v-data-table
              :headers = "headers"
              :items = "proyek"> 
              <template v-slot:[`item.id`]="{ item }">
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
              </template>
            </v-data-table>
          </v-card>
        </v-row>
      </v-carousel-item>
    </v-carousel>
  </v-app>
</template>

<script>
  import {GGanttChart, GGanttRow} from 'vue-ganttastic'

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
      GGanttRow
    },

    data(){
      return {
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
        rowHeight: 50,
        rowLabelWidth: 5,
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
      this.fetchOperatorOnWS()
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
