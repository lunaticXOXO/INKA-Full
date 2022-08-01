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
      chartStart: "2022-08-01 00:00",
      chartEnd: "2022-08-04 00:00",
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
      rowList: [
        {
          label: "WS1",
          barList: [
            {
              myStart: "2022-08-01 18:00",
              myEnd: "2022-08-01 23:00",
              label: "Assy. Smartpoint",
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
          label: "WS2",
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
              label: "Testing",
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
          label: "WS3",
          barList: [
            {
              myStart: "2020-03-02 09:00",
              myEnd: "2020-03-02 18:00",
              label: "Testing",
              ganttBarConfig: {color:"white", backgroundColor: "#de3b26", bundle: "redBundle"}
            },
            {
              myStart: "2020-03-02 22:30",
              myEnd: "2020-03-03 05:00",
              label: "Testing",
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
              label: "Testing",
              ganttBarConfig: {color:"white", background: "repeating-linear-gradient(45deg,#de7359,#de7359 10px,#ffc803 10px,#ffc803 20px)"}
            }, 
          ]
        },

        {
          label: "WS4",
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