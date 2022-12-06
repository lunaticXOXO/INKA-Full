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
    <!--
    <h3 class="ml-10 mt-6">Pilih Stasiun Kerja</h3>
    <v-card class="mx-auto" max-width="1250" elevation="0">
          <v-container fluid>
              <v-row dense>
                  <v-col
                      v-for="item in itemsWS"
                      :key="item.name"
                      :cols="item.flex">
                      <v-card class="mx-auto justify-center text-center" elevation="0" outlined>
                          <div class="d-flex ml-2 text-center">
                              <v-checkbox v-model="pilihan"></v-checkbox>
                              <p class="mt-5">{{ item.name }}</p>  
                          </div>
                      </v-card>
                  </v-col>
              </v-row>
          </v-container>
      </v-card>
    -->
    <h3 class="ml-10 mt-6">Pencarian Tanggal</h3>
    <v-card class="ml-2" max-width="400" elevation="0">
      <v-menu class="ml-10 mt-6">
        <template v-slot:activator="{ on, attrs }">
          <v-text-field class="ml-10" :value="tanggalPencarian" v-bind="attrs" v-on="on" label="Tanggal Mulai" prepend-icon="mdi-calendar"></v-text-field>
        </template>
        <v-date-picker width="1000" v-model="tanggalPencarian"></v-date-picker>
      </v-menu>
      <v-menu class="ml-10 mt-6">
        <template v-slot:activator="{ on, attrs }">
          <v-text-field class="ml-10" :value="tanggalPencarian2" v-bind="attrs" v-on="on" label="Tanggal Selesai" prepend-icon="mdi-calendar"></v-text-field>
        </template>
        <v-date-picker width="1000" v-model="tanggalPencarian2"></v-date-picker>
      </v-menu>
    </v-card>
    <v-btn
      color="success"
      class="mx-auto text-center" 
      max-width="1200"
      width="200"
      type="submit"
      @click="validate()">
      Submit
    </v-btn>

    <br>
    
    <v-card class="mt-10 mx-10">
      <h2>Jadwal Kerja WS</h2>
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
          <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS00"
              width="750"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS00 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS01"
          :bars="itemsWS01"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS01"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS01 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS02"
          :bars="itemsWS02"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS02"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS02 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS03"
          :bars="itemsWS03"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS03"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS03 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS04"
          :bars="itemsWS04"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS04"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS04 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS05"
          :bars="itemsWS05"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS05"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS05 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS06"
          :bars="itemsWS06"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS06"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS06 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

        <g-gantt-row
          label="WS07"
          :bars="itemsWS07"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS07"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS07 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>
        <g-gantt-row
          label="WS08"
          :bars="itemsWS08"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS08"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  block
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS08 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>
        <g-gantt-row
          label="WS09"
          :bars="itemsWS09"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
        >
        <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS09"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{bar.idOperasi}}</p>
                  <p>Proses : {{bar.namaProses}}</p>
                  <p>Lokasi Stasiun Kerja : {{bar.namaStasiunKerja}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{bar.rencanaMulai}}</p>
                  <p>Rencana Selesai : {{bar.rencanaSelesai}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS09 = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>
        </g-gantt-row>

      </g-gantt-chart>
    </v-card>
   
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
      //pilihan: undefined,
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
      tanggalPencarian: '',
      tanggalPencarian2: '',
      //myChartStart: "2020-03-01 00:00",
      //myChartEnd: "2020-03-01 23:00",
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

  methods:{
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

    validate(){
      const date = new Date(this.tanggalPencarian)
      date.setDate(date.getDate() + 1);
      this.myChartStartCustom = this.tanggalPencarian

      const date2 = new Date(this.tanggalPencarian2)
      date2.setDate(date2.getDate() + 1);
      this.myChartEndCustom = this.tanggalPencarian2
      
      console.log(this.myChartStartCustom)
      console.log(this.myChartEndCustom)

      this.fetchDataStatusWS00()
      this.fetchDataStatusWS01()
      this.fetchDataStatusWS02()
      this.fetchDataStatusWS03()
      this.fetchDataStatusWS04()
      this.fetchDataStatusWS05()
      this.fetchDataStatusWS06()
      this.fetchDataStatusWS07()
      this.fetchDataStatusWS08()
      this.fetchDataStatusWS09()
      //console.log(this.pilihan)
    },
  }
}
</script>