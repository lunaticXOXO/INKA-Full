<!--
<template>
  <v-app>
    <div>
      <div id="ganttastic-wrapper">
        <v-card class="mt-10 mx-10">
          <g-gantt-chart
            :chart-start="chartStart"
            :chart-end="chartEnd"
            :grid="grid"
            :hide-timeaxis="hideTimeaxis"
            :push-on-overlap="pushOnOverlap"
            :highlighted-hours="highlightedHours"
            :row-label-width="`${rowLabelWidth}%`"
            :row-height="rowHeight"
            :theme="selectedTheme"
            @contextmenu-bar="onContextmenuBar($event)"
            @dragend-bar="stoppedDraggingBar($event)"
          >
            <g-gantt-row 
              v-for="item in items"
              :key="item.idOperasi"
              :label="item.namaStasiunKerja"
              :bars="item.bars"
              :bar-start="item.bars.rencanaMulai"
              :bar-end="item.bars.rencanaSelesai"
            >
              <template #bar-label="{bar}">
                <img
                  v-if="bar.image"
                  :src="require(`@/assets/${bar.image}`)"
                  height="20"
                  width="20"
                  class="mr-1"
                >
                <span>{{bar.label}}</span>
              </template>
            </g-gantt-row>
          </g-gantt-chart>
        </v-card>
      </div>
      <v-menu 
        v-model="showContextmenu"
        :position-x="contextmenuX"
        :position-y="contextmenuY"
      >
        <v-list>
          <v-list-item>
            It's a context menu!
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </v-app>
</template>

<script>
import {GGanttChart, GGanttRow} from 'vue-ganttastic'

export default {
  components: {
    GGanttChart,
    GGanttRow
  },

  data(){
    return {
      chartStart: "2022-08-02 00:00",
      chartEnd: "2022-08-03 00:00",
      pushOnOverlap: false,
      grid: true,
      rowHeight: 40,
      rowLabelWidth: 10,
      hideTimeaxis: false,
      highlightOnHover: true,
      hours: [...Array(24).keys()],
      highlightedHours: [10,12],
      showContextmenu: false,
      contextmenuTimeout: null,
      contextmenuX: 0,
      contextmenuY: 0,
      selectedTheme: "vue",
      items : [
      {bars : [
              {
                myStart : 'rencanaMulai',
                myEnd : 'rencanaSelesai',
                label : 'namaProses'
              }

          ]}
      ],
      rowList: [
          /*{barList : [
              {
                myStart : 'rencanaMulai',
                myEnd : 'rencanaSelesai',
                label : 'namaProses'
              }

          ]}*/
        /*{
          label: "WS1",
          barList: [
            {
              myStart: "2022-08-01 16:00",
              myEnd: "2022-08-01 24:00",
              label: "Assy. Smartpoint",
              ganttBarConfig: {color:"white", backgroundColor: "#404040", opacity: 0.5, immobile: true}
            },
            {
              myStart: "2022-08-02 06:00",
              myEnd: "2022-08-02 14:00",
              label: "Ins. Smartpoint",
              ganttBarConfig: {color:"white", backgroundColor: "#2e74a3", bundle: "blueBundle"}
            }
          ]
        },

        {
          label: "WS2",
          barList: [
            {
              myStart: "2022-08-01 02:00",
              myEnd: "2022-08-01 07:00",
              label: "Assy. Frame",
              ganttBarConfig: {color:"white", backgroundColor: "#de3b26", bundle:"redBundle"}
            },
            {
              myStart: "2022-08-01 12:00",
              myEnd: "2022-08-01 18:00",
              label: "Assy. Scanner",
              ganttBarConfig: {color:"white", backgroundColor: "#2e74a3", bundle:"blueBundle"}
            },
            {
              myStart: "2022-08-01 19:00",
              myEnd: "2022-08-01 00:00",
              label: "Assy. Motherboard",
              ganttBarConfig: {color:"white", backgroundColor: "#aa34a3"}
            }
          ]
        },

        {
          label: "WS3",
          barList: [
            {
              myStart: "2022-08-01 17:00",
              myEnd: "2022-08-01 21:00",
              label: "Cut. Box",
              ganttBarConfig: {color:"white", backgroundColor: "#de3b26", bundle: "redBundle"}
            },
            {
              myStart: "2022-08-01 21:30",
              myEnd: "2022-08-02 02:00",
              label: "Wel. Box",
              ganttBarConfig: {color:"white", backgroundColor: "#a23def"}
            },
            {
              myStart: "2022-08-02 03:00",
              myEnd: "2022-08-02 07:00",
              label: "Cut. Body",
              ganttBarConfig: {color:"white", backgroundColor: "#5effad"}
            },
            {
              myStart: "2022-08-02 08:00",
              myEnd: "2022-08-02 12:00",
              label: "Wel. Body",
              ganttBarConfig: {color:"white", background: "repeating-linear-gradient(45deg,#de7359,#de7359 10px,#ffc803 10px,#ffc803 20px)"}
            }, 
          ]
        },

        {
          label: "WS4",
          barList: [
            {
              myStart: "2022-08-01 07:00",
              myEnd: "2022-08-01 15:00",
              label: "Assy. Elektronik",
              ganttBarConfig:{color:"white", backgroundColor: "#d18aaf", handles: true}
            },
            {
              myStart: "2022-08-01 16:00",
              myEnd: "2022-08-01 23:00",
              label: "Ins. Elektronik",
              ganttBarConfig: {color:"white", backgroundColor: "#f2840f", borderRadius: 0}
            }, 
          ]
        }*/

      ]
    }
  },

  mounted(){
    this.fetchDataStatusWS()
  },

  methods: {
    stoppedDraggingBar(){

    },

    onContextmenuBar(e){
      e.event.preventDefault()
      this.contextmenuY = e.event.clientY
      this.contextmenuX = e.event.clientX
      this.showContextmenu = true
      if(this.contextmenuTimeout){
        clearTimeout(this.contextmenuTimeout)
      }
      this.contextmenuTimeout = setTimeout(() => this.showContextmenu = false, 3000)
    },

    async fetchDataStatusWS(){
      const axios = require('axios')
      const res = await axios.get('/stasiun_kerja/status_pengerjaan_stasiunkerja')
      if(res.data == null){
         console.log("Data Pengerjaan Kosong")
      }else{
        this.items = res.data
        console.log(res,this.items)
      }

    }
  }
}
</script>

<style scoped>
  #ganttastic-wrapper{
    height: 50vh;
    overflow-y: auto;
  }
</style>


<template>
  <div>
    <div id="ganttastic-wrapper">
      <g-gantt-chart
        :chart-start="chartStart"
        :chart-end="chartEnd"
        :grid="grid"
        :hide-timeaxis="hideTimeaxis"
        :push-on-overlap="pushOnOverlap"
        :highlighted-hours="highlightedHours"
        :row-label-width="`${rowLabelWidth}%`"
        :row-height="rowHeight"
        :theme="selectedTheme"
        @contextmenu-bar="onContextmenuBar($event)"
        @dragend-bar="stoppedDraggingBar($event)"
      >
        <g-gantt-row 
          v-for="row in rowList"
          :key="row.title"
          :label="row.label"
          :bars="row.barList"
          :highlight-on-hover="highlightOnHover"
          bar-start="myStart"
          bar-end="myEnd"
        >
          <template #bar-label="{bar}">
            <img
              v-if="bar.image"
              :src="require(`@/assets/${bar.image}`)"
              height="20"
              width="20"
              class="mr-1"
            >
            <span>{{bar.label}}</span>
          </template>
        </g-gantt-row>
      </g-gantt-chart>
    </div>

    <v-card class="pa-2" flat>
      <v-row justify="end">
        <v-btn
          dark
          color="primary"
          small 
          class="mr-4"
          href="https://github.com/InfectoOne/vue-ganttastic-homepage/blob/master/src/views/Example.vue"
          target="blank"
        >
          <span>View code</span>
          <v-icon right>mdi-code-tags</v-icon>
        </v-btn>
      </v-row>
    </v-card>

    <v-card 
      width="100%"
      height="28vh"
      color ="#dff2ea"
      class="d-none d-md-flex"
    >
      <v-row class="pa-2">
        <v-col cols="3">
          <v-checkbox
            v-model="hideTimeaxis"
            label="Hide timeaxis"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-checkbox 
            v-model="pushOnOverlap"
            label="Push on overlap"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-checkbox 
            v-model="grid"
            label="Grid"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-checkbox 
            v-model="highlightOnHover"
            label="Highlight on hover"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-select 
            v-model="selectedTheme"
            label="Theme"
            :items="themes"
            outlined
            dense
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-slider
            v-model="rowHeight"
            label="Row height"
            :min="20"
            :max="100"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-slider 
            v-model="rowLabelWidth"
            label="Row label width"
            :min="10"
            :max="50"
            hide-details
          />
        </v-col>

        <v-col cols="3">
          <v-select 
            v-model="highlightedHours"
            label="Highlighted hours"
            :items="hours"
            multiple
            outlined
            dense
            hide-details
          />
        </v-col>
      </v-row>
    </v-card>

    <v-menu 
      v-model="showContextmenu"
      :position-x="contextmenuX"
      :position-y="contextmenuY"
    >
      <v-list>
        <v-list-item>
          It's a context menu!
        </v-list-item>
      </v-list>
    </v-menu>

  </div>
</template>

<script>
import {GGanttChart, GGanttRow} from 'vue-ganttastic'

export default {
  components: {
    GGanttChart,
    GGanttRow
  },

  data(){
    return {
      chartStart: "2020-03-02 00:00",
      chartEnd: "2020-03-04 00:00",
      pushOnOverlap: true,
      grid: true,
      rowHeight: 40,
      rowLabelWidth: 15,
      hideTimeaxis: false,
      highlightOnHover: false,
      hours: [...Array(24).keys()],
      highlightedHours: [10,12],
      showContextmenu: false,
      contextmenuTimeout: null,
      contextmenuX: 0,
      contextmenuY: 0,
      selectedTheme: "default",
      themes: [
        "default",
        "vue",
        "dark",
        "material-blue",
        "creamy",
        "slumber",
        "sky",
        "crimson",
        "grove",
        "fuchsia",
        "flare"
      ],
      rowList: [
        {
          label: "Row #1",
          barList: [
            {
              myStart: "2020-03-03 18:00",
              myEnd: "2020-03-03 23:00",
              label: "Immobile",
              ganttBarConfig: {color:"white", backgroundColor: "#404040", opacity: 0.5, immobile: true}
            },
            {
              myStart: "2020-03-03 04:00",
              myEnd: "2020-03-03 15:00",
              label: "Bar",
              ganttBarConfig: {color:"white", backgroundColor: "#2e74a3", bundle: "blueBundle"}
            }
          ]
        },

        {
          label: "Row #2",
          barList: [
            {
              myStart: "2020-03-02 09:00",
              myEnd: "2020-03-02 18:00",
              image: "vue_ganttastic_logo_no_text.png",
              label: "I have an image",
              ganttBarConfig: {color:"white", backgroundColor: "#de3b26", bundle:"redBundle"}
            },
            {
              myStart: "2020-03-03 04:00",
              myEnd: "2020-03-03 15:00",
              label: "We belong together ^",
              ganttBarConfig: {color:"white", backgroundColor: "#2e74a3", bundle:"blueBundle"}
            },
            {
              myStart: "2020-03-03 18:00",
              myEnd: "2020-03-03 22:00",
              label: "Bar",
              ganttBarConfig: {color:"white", backgroundColor: "#aa34a3"}
            }
          ]
        },

        {
          label: "Row #3",
          barList: [
            {
              myStart: "2020-03-02 09:00",
              myEnd: "2020-03-02 18:00",
              label: "I am with stupid ^",
              ganttBarConfig: {color:"white", backgroundColor: "#de3b26", bundle: "redBundle"}
            },
            {
              myStart: "2020-03-02 22:30",
              myEnd: "2020-03-03 05:00",
              label: "With handles!",
              ganttBarConfig: {color:"white", backgroundColor: "#a23def", handles: true}
            },
            {
              myStart: "2020-03-02 01:00",
              myEnd: "2020-03-02 07:00",
              label: "Bar",
              ganttBarConfig: {color:"white", backgroundColor: "#5effad"}
            },
            {
              myStart: "2020-03-03 14:00",
              myEnd: "2020-03-03 20:00",
              label: "Woooow!",
              ganttBarConfig: {color:"white", background: "repeating-linear-gradient(45deg,#de7359,#de7359 10px,#ffc803 10px,#ffc803 20px)"}
            }, 
          ]
        },

        {
          label: "Row #4",
          barList: [
            {
              myStart: "2020-03-03 06:30",
              myEnd: "2020-03-03 20:00",
              label: "Bar",
              ganttBarConfig:{color:"white", backgroundColor: "#d18aaf", handles: true}
            },
            {
              myStart: "2020-03-02 00:30",
              myEnd: "2020-03-03 01:00",
              label: "Rectangular",
              ganttBarConfig: {color:"white", backgroundColor: "#f2840f", borderRadius: 0}
            }, 
          ]
        }

      ]
    }
  },


  methods: {

    stoppedDraggingBar(){
    },

    onContextmenuBar(e){
      e.event.preventDefault()
      this.contextmenuY = e.event.clientY
      this.contextmenuX = e.event.clientX
      this.showContextmenu = true
      if(this.contextmenuTimeout){
        clearTimeout(this.contextmenuTimeout)
      }
      this.contextmenuTimeout = setTimeout(() => this.showContextmenu = false, 3000)
    }

  }
}
</script>

<style scoped>
  #ganttastic-wrapper{
    height: 50vh;
    overflow-y: auto;
  }
</style>
-->

<template>
  <v-app>
    <h3 class="ml-10 mt-6">Tanggal Mulai Pencarian</h3>
    <v-menu class="ml-10 mt-6">
      <template v-slot:activator="{ on, attrs }">
        <v-text-field class="ml-10" :value="tanggalPencarian" v-bind="attrs" v-on="on" label="Tanggal Pencarian" prepend-icon="mdi-calendar"></v-text-field>
      </template>
      <v-date-picker width="1000" v-model="tanggalPencarian"></v-date-picker>
    </v-menu>
    <v-btn
      color="success"
      class="ml-10"
      width="200"
      type="submit"
      @click="validate()">
      Submit
    </v-btn>

    <!--
    <v-card class="mt-10 mx-10">
      <h2>Default</h2>
      <g-gantt-chart
        :chart-start="myChartStart"
        :chart-end="myChartEnd"
      >
        <g-gantt-row
          v-for="row in rows"
          :key="row.label"
          :label="row.label"
          :bars="row.bars"
          bar-start="myStart"
          bar-end="myEnd"
          >
          <template #bar-label="{bar}">
            <span>{{bar.label}}</span>
          </template>
        </g-gantt-row>
      </g-gantt-chart>
    </v-card>

    <v-card class="mt-10 mx-10">
      <h2>JSON Auto</h2>
      <g-gantt-chart
        :chart-start="myChartStartCustom"
        :chart-end="myChartEndCustom"
      >
        <g-gantt-row
          v-for="row in items"
          :key="row.namaStasiunKerja"
          :label="row.namaStasiunKerja"
          :bars="items"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        />
      </g-gantt-chart>
    </v-card>
    -->
    
    <v-card class="mt-10 mx-10">
      <h2>JSON Manual</h2>
      <g-gantt-chart
        :chart-start="myChartStartCustom"
        :chart-end="myChartEndCustom"
      >
        <g-gantt-row
          v-for="row in items2"
          :key="row.namaStasiunKerja"
          :label="row.namaStasiunKerja"
          :bars="items2"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
          <template #bar-label="{bar}">
            <span>{{bar.namaProses}}</span>
          </template>
        </g-gantt-row>
      </g-gantt-chart>
    </v-card>

    <v-card class="mt-10 mx-10">
      <h2>JSON Adjust</h2>
      <g-gantt-chart
        :chart-start="myChartStartCustom"
        :chart-end="myChartEndCustom"
      >
        <g-gantt-row
          v-for="row in items3"
          :key="row.label"
          :label="row.label"
          :bars="row.bars"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
          <template #bar-label="{bar}">
            <span>{{bar.namaProses}}</span>
          </template>
        </g-gantt-row>
      </g-gantt-chart>
    </v-card>
  </v-app>
</template>

<script>

import {GGanttChart, GGanttRow} from 'vue-ganttastic'
//var today = new Date();
//var newDate = new Date(Date.now()+1*24*60*60*1000);
//var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
//var date2 = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+ newDate.getDate();
//var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
//var dateTime = date+' '+time;
//var dateTime2 = date2+' '+time;

export default {
  components:{
    GGanttChart,
    GGanttRow
  },

  data(){
    return {
      items: undefined,
      tanggalPencarian: '',
      myChartStart: "2020-03-01 00:00",
      myChartEnd: "2020-03-03 00:00",
      //myChartStartCustom: dateTime,
      //myChartEndCustom: dateTime2,
      myChartStartCustom:'',
      myChartEndCustom:'',
      items2:[
        {
          "idOperasi":"23NGWLRG3",
          "namaProses":"Setting brake boogie",
          "namaStasiunKerja":"WS8",
          "rencanaMulai":"2022-09-04 07:00",
          "rencanaSelesai":"2022-09-04 10:00"
        },
        {
          "idOperasi":"NABNJ4PL4",
          "namaProses":"Bogie Installation",
          "namaStasiunKerja":"WS8",
          "rencanaMulai":"2022-09-04 12:00",
          "rencanaSelesai":"2022-09-04 15:00"
        },
        {
          "idOperasi":"RKKXZTTQP",
          "namaProses":"Test beban",
          "namaStasiunKerja":"WS9",
          "rencanaMulai":"2022-09-04 17:00",
          "rencanaSelesai":"2022-09-04 19:00"
        },
        {
          "idOperasi":"SX7RQUVPP",
          "namaProses":"Bogie Assy NON Handbrake",
          "namaStasiunKerja":"WS8",
          "rencanaMulai":"2022-09-04 20:00",
          "rencanaSelesai":"2022-09-04 23:00"
        }
      ],

      rows: [
        {
          label: "My row #1",
          bars: [
            {
              myStart: "2020-03-01 12:10",
              myEnd: "2020-03-01 16:35"
            }
          ]
        },
        {
          label: "My row #2",
          bars: [
            {
              myStart: "2020-03-02 01:00",
              myEnd: "2020-03-02 12:00"
            },
            {
              myStart: "2020-03-02 13:00",
              myEnd: "2020-03-02 22:00"
            }
          ]
        }
      ],
      
      items3:[
        {
          label: "",
          bars: [
            {
              rencanaMulai: "",
              rencanaSelesai: ""
            }
          ]
        }
      ],
    }
  },

  mounted(){
    this.fetchDataStatusWS()
  },

  methods:{
    async fetchDataStatusWS(){
      const axios = require('axios')
      const res = await axios.get('/stasiun_kerja/status_pengerjaan_stasiunkerja')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.items = res.data
        //var stringify = JSON.stringify(res.data[0].rencanaMulai)
        //var hasil = JSON.parse(stringify)
        //console.log(hasil)
        //this.items3.label = res.data[0].namaStasiunKerja
        //this.items3.bars.rencanaMulai = res.data[0].rencanaMulai
        //this.items3.bars.rencanaSelesai = res.data[0].rencanaSelesai
        //console.log(this.items3.label)
        //console.log(this.items3.bars[0].rencanaMulai)
        //console.log(this.items3.bars[0].rencanaSelesai)
        //console.log(res.data[0].rencanaMulai)
        console.log(res,this.items)
      }
    },

    validate(){
      const date = new Date(this.tanggalPencarian)
      date.setDate(date.getDate() + 2);
      this.myChartStartCustom = this.tanggalPencarian
      this.myChartEndCustom = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+date.getDate();
      console.log(this.myChartStartCustom)
      console.log(this.myChartEndCustom)
    },
  }
}
</script>