<template>
<v-app>

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
      color="blue"
      class="mx-auto text-center" 
      max-width="1200"
      width="200"
      type="submit"
      @click="validate()">
      Submit
    </v-btn>
    <br>

  
    <v-card class="mt-10 mx-10">

        <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
            >
      <v-card-title class="text-h5">
        TIMELINE RENCANA PENGERJAAN OPERASI
      </v-card-title>
            
      </v-card> 
      <br><br>

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
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS00"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart0(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

      
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p >ID Operasi : {{ selectedBar00 ? selectedBar00.id : '' }}</p>
                  <p>Proses : {{selectedBar00 ? selectedBar00.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar00 ? selectedBar00.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar00 ? selectedBar00.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar00 ? selectedBar00.selesai : ''}}</p>
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
              label="WS00 Actual"
              :bars="itemsWS00Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS00Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart0Actual(bar)"
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
                
                  <p>ID Operasi : {{selectedBar00Actual ? selectedBar00Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar00Actual ? selectedBar00Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar00Actual ? selectedBar00Actual.namaWS : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar00Actual ? selectedBar00Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar00Actual ? selectedBar00Actual.selesai : ''}}</p>
                </v-card-text>
      
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS00Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>

            </g-gantt-row>

            <g-gantt-row
              label="WS01 Plan"
              :bars="itemsWS01"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart1(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar01 ? selectedBar01.id : ''}}</p>
                  <p>Proses : {{selectedBar01 ? selectedBar01.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar01 ? selectedBar01.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar01 ? selectedBar01.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar01 ? selectedBar01.selesai : ''}}</p>
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
              label="WS01 Actual"
              :bars="itemsWS01Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS01Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart1Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               
            
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar01Actual ? selectedBar01Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar01Actual ? selectedBar01Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar01Actual ? selectedBar01Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar01Actual ? selectedBar01Actual.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar01Actual ? selectedBar01Actual.selesai : ''}}</p>
                </v-card-text>
           
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS01Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>


            </g-gantt-row>

            <g-gantt-row
              label="WS02 Plan"
              :bars="itemsWS02"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart2(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               
                
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar02 ? selectedBar02.id : ''}}</p>
                  <p>Proses : {{selectedBar02 ? selectedBar02.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar02 ? selectedBar02.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar02 ? selectedBar02.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar02 ? selectedBar02.selesai : ''}}</p>
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
              label="WS02 Actual"
              :bars="itemsWS02Actual"
              bar-start="mulai"
              bar-end="selesai"

            >
            
            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS02Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart2Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               
            
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar02Actual ? selectedBar02Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar02Actual ? selectedBar02Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar02Actual ? selectedBar02Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar02Actual ? selectedBar02Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar02Actual ? selectedBar02Actual.selesai : ''}}</p>
                </v-card-text>
           
                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS02Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>


            </g-gantt-row>

            <g-gantt-row
              label="WS03 Plan"
              :bars="itemsWS03"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart3(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               
                
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar03 ? selectedBar03.id : ''}}</p>
                  <p>Proses : {{selectedBar03 ? selectedBar03.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar03 ? selectedBar03.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar03 ? selectedBar03.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar03 ? selectedBar03.selesai : ''}}</p>
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
              label="WS03 Actual"
              :bars="itemsWS03Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS03Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart3Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
               
                
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar03Actual ? selectedBar03Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar03Actual ? selectedBar03Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar03Actual ? selectedBar03Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar03Actual ? selectedBar03Actual.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar03Actual ? selectedBar03Actual.selesai : ''}}</p>
                </v-card-text>
           

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS03Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>


            </g-gantt-row>

            <g-gantt-row
              label="WS04 Plan"
              :bars="itemsWS04"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = " selectedGantChart4(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar04 ? selectedBar04.id : ''}}</p>
                  <p>Proses : {{selectedBar04 ? selectedBar04.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar04 ? selectedBar04.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar04 ? selectedBar04.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar04 ? selectedBar04.selesai : ''}}</p>
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
              label="WS04 Actual"
              :bars="itemsWS04Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS04Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart4Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar04Actual ? selectedBar04Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar04Actual ? selectedBar04Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar04Actual ? selectedBar04Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar04Actual ? selectedBar04Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar04Actual ? selectedBar04Actual.selesai : ''}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS04Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>

            </g-gantt-row>

            <g-gantt-row
              label="WS05 Plan"
              :bars="itemsWS05"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart5(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

      
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p >ID Operasi : {{ selectedBar05 ? selectedBar05.id : '' }}</p>
                  <p>Proses : {{selectedBar05 ? selectedBar05.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar05 ? selectedBar05.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar05 ? selectedBar05.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar05 ? selectedBar05.selesai : ''}}</p>
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
              label="WS05 Actual"
              :bars="itemsWS05Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
        <v-dialog
          v-model="dialogWS05Actual"
          width="500"
          :retain-focus="false"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="font-weight-bold"
              color="#28B463"
              dark
              v-bind="attrs"
              v-on="on"
              @click = "selectedGantChart5Actual(bar)"
            >
            {{bar.proses}}

            </v-btn>
          </template>

          <v-card>
            <v-card-title class="text-h4 grey lighten-2">
              Detail Operasi
            </v-card-title>

            <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
              <br>
                  <p>ID Operasi : {{selectedBar05Actual ? selectedBar05Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar05Actual ? selectedBar05Actual.proses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar05Actual ? selectedBar05Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar05Actual ? selectedBar05Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar05Actual ? selectedBar05Actual.selesai : ''}}</p>
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
              label="WS06 Plan"
              :bars="itemsWS06"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart6(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar06 ? selectedBar06.id : ''}}</p>
                  <p>Proses : {{selectedBar06Actual ? selectedBar06Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar06 ? selectedBar06.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar06 ? selectedBar06.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar06 ? selectedBar06.selesai : ''}}</p>
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
              label="WS06 Actual"
              :bars="itemsWS06Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS06Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart6Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar06Actual ? selectedBar06Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar06Actual ? selectedBar06Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar06Actual ? selectedBar06Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar06Actual ? selectedBar06Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar06Actual ? selectedBar06Actual.selesai : ''}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS06Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>

            </g-gantt-row>

            <g-gantt-row
              label="WS07 Plan"
              :bars="itemsWS07"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart7(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar07 ? selectedBar07.id : ''}}</p>
                  <p>Proses : {{selectedBar07 ? selectedBar07.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar07 ? selectedBar07.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar07 ? selectedBar07.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar07 ? selectedBar07.selesai : ''}}</p>
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
              label="WS07 Actual"
              :bars="itemsWS07Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS07Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart7Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar07Actual ? selectedBar07Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar07Actual ? selectedBar07Actual.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar07Actual ? selectedBar07Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar07Actual ? selectedBar07Actual.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar07Actual ? selectedBar07Actual.selesai : ''}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS07Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>

            </g-gantt-row>

            <g-gantt-row
              label="WS08 Plan"
              :bars="itemsWS08"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart8(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar08 ? selectedBar08.id : ''}}</p>
                  <p>Proses : {{selectedBar08 ? selectedBar08.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar08 ? selectedBar08.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar08 ? selectedBar08.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar08 ? selectedBar08.selesai : ''}}</p>
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
              label="WS08 Actual"
              :bars="itemsWS08Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS08Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  block
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart8Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar08Actual ? selectedBar08Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar08Actual ? selectedBar08Actual.proses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar08Actual ? selectedBar08Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar08Actual ? selectedBar08Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar08Actual ? selectedBar08Actual.selesai : ''}}</p>
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    text
                    @click="dialogWS08Actual = false"
                  >
                    Back
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </template>

            </g-gantt-row>

            <g-gantt-row
              label="WS09 Plan"
              :bars="itemsWS09"
              bar-start="mulai"
              bar-end="selesai"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart9(bar)"
                  
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar09 ? selectedBar09.id : ''}}</p>
                  <p>Proses : {{selectedBar09 ? selectedBar09.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar09 ? selectedBar09.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar09 ? selectedBar09.mulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar09 ? selectedBar09.selesai : ''}}</p>
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

              <g-gantt-row
              label="WS09 Actual"
              :bars="itemsWS09Actual"
              bar-start="mulai"
              bar-end="selesai"
            >

            <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS09Actual"
              width="500"
              :retain-focus="false"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart9Actual(bar)"
                >
                {{bar.proses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar09Actual ? selectedBar09Actual.id : ''}}</p>
                  <p>Proses : {{selectedBar09Actual ? selectedBar09Actual.proses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar09Actual ? selectedBar09Actual.namaWs : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar09Actual ? selectedBar09Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar09Actual ? selectedBar09Actual.selesai : ''}}</p>
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

      itemsWS00Actual: undefined,
      itemsWS01Actual: undefined,
      itemsWS02Actual: undefined,
      itemsWS03Actual: undefined,
      itemsWS04Actual: undefined,
      itemsWS05Actual: undefined,
      itemsWS06Actual: undefined,
      itemsWS07Actual: undefined,
      itemsWS08Actual: undefined,
      itemsWS09Actual: undefined,

      //pilihan: undefined,

      listdate : [],
      idOperation : '',

      rowHeight: 30,
      rowLabelWidth: 10,
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

      dialogWS00Actual: undefined,
      dialogWS01Actual: undefined,
      dialogWS02Actual: undefined,
      dialogWS03Actual: undefined,
      dialogWS04Actual: undefined,
      dialogWS05Actual: undefined,
      dialogWS06Actual: undefined,
      dialogWS07Actual: undefined,
      dialogWS08Actual: undefined,
      dialogWS09Actual: undefined,

      tanggalPencarian: '',
      tanggalPencarian2 : '',
  
      mulai_str : '',
      selesai_str : '',

      index : undefined,

      myChartStartCustom: dateTime,
      myChartEndCustom: dateTime2,



      selectedBar00 : [],
      selectedBar01 : [],
      selectedBar02 : [],
      selectedBar03 : [],
      selectedBar04 : [],
      selectedBar05 : [],
      selectedBar06 : [],
      selectedBar07 : [],
      selectedBar08 : [],
      selectedBar09 : [],

      selectedBar00Actual : [],
      selectedBar01Actual : [],
      selectedBar02Actual : [],
      selectedBar03Actual : [],
      selectedBar04Actual : [],
      selectedBar05Actual : [],
      selectedBar06Actual : [],
      selectedBar07Actual : [],
      selectedBar08Actual : [],
      selectedBar09Actual : [],
      

    }
  },



  methods:{

    getBarStyle(){
      return {background : 'blue'}
    },

    selectedGantChart0(itemsWS00){
       this.selectedBar00 = itemsWS00
    },

    selectedGantChart0Actual(itemsWS00Actual){
      this.selectedBar00Actual = itemsWS00Actual
      
    },

    selectedGantChart1(itemsWS01){
        this.selectedBar01 = itemsWS01
        console.log("gant1 :",this.selectedBar01)
    },

    selectedGantChart1Actual(itemsWS01Actual){
       this.selectedBar01Actual = itemsWS01Actual

    },

    selectedGantChart2(itemsWS02){
      this.selectedBar02 = itemsWS02
    },

    selectedGantChart2Actual(itemsWS02Actual){
      this.selectedBar02Actual = itemsWS02Actual
    },

    selectedGantChart3(itemsWS03){
      this.selectedBar03 = itemsWS03
    },


    selectedGantChart3Actual(itemsWS03Actual){
      this.selectedBar03Actual = itemsWS03Actual
    },

    selectedGantChart4(itemsWS04){
       this.selectedBar04 = itemsWS04
    },


    selectedGantChart4Actual(itemsWS04Actual){
      this.selectedBar04Actual = itemsWS04Actual
    },

    selectedGantChart5(itemsWS05){
      this.selectedBar05 = itemsWS05
    
    },

    selectedGantChart5Actual(itemsWS05Actual){
       this.selectedBar05Actual = itemsWS05Actual
       console.log("actual05",this.selectedBar05Actual)
    },

    selectedGantChart6(itemsWS06){
      this.selectedBar06 = itemsWS06
    },


    selectedGantChart6Actual(itemsWS06Actual){
      this.selectedBar06Actual = itemsWS06Actual
    },

    selectedGantChart7(itemsWS07){
       this.selectedBar07 = itemsWS07
    },

    selectedGantChart7Actual(itemsWS07Actual){
      this.selectedBar07Actual = itemsWS07Actual
    },

    selectedGantChart8(itemsWS08){
      this.selectedBar08 = itemsWS08
    },

    selectedGantChart8Actual(itemsWS08Actual){
       this.selectedBar08Actual = itemsWS08Actual
    },

    
    selectedGantChart9(itemsWS09){
      this.selectedBar09 = itemsWS09
    },

    selectedGantChart9Actual(itemsWS09Actual){
      this.selectedBar09Actual = itemsWS09Actual
    },

   
    async fetchDataStatusWS00(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws00')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS00 = res.data
          console.log(res,this.itemsWS00)
        }
      },

      async fetchDataStatusWS00Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws00')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS00Actual = res.data
          console.log(res,this.itemsWS00Actual)
        }
      },

      async fetchDataStatusWS01(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws01')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS01 = res.data
          console.log(res,this.itemsWS01)
        }
      },

      async fetchDataStatusWS01Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws01')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS01Actual = res.data
          console.log(res,this.itemsWS01Actual)
        }
      },


      async fetchDataStatusWS02(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws02')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS02 = res.data
          console.log(res,this.itemsWS02)
        }
      },

      async fetchDataStatusWS02Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws02')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS02Actual = res.data
          console.log(res,this.itemsWS02Actual)
        }
      },


      async fetchDataStatusWS03(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws03')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS03 = res.data
          console.log("Plan03 :",res,this.itemsWS03)
        }
      },

      async fetchDataStatusWS03Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws03')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS03Actual = res.data
          console.log("Actual03 : ",res,this.itemsWS03Actual)
        }
      },

      async fetchDataStatusWS04(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws04')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS04 = res.data
          console.log(res,this.itemsWS04)
        }
      },

      async fetchDataStatusWS04Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws04')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS04Actual = res.data
          console.log(res,this.itemsWS04Actual)
        }
      },


      async fetchDataStatusWS05(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws05')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS05 = res.data
          console.log(res,this.itemsWS05)
        }
      },

      async fetchDataStatusWS05Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws05')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS05Actual = res.data
          console.log(res,this.itemsWS05Actual)
        }
      },


      async fetchDataStatusWS06(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws06')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS06 = res.data
          console.log(res,this.itemsWS06)
        }
      },

      async fetchDataStatusWS06Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws06')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS06Actual = res.data
          console.log(res,this.itemsWS06Actual)
        }
      },


      async fetchDataStatusWS07(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws07')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS07 = res.data
          console.log(res,this.itemsWS07)
        }
      },

       async fetchDataStatusWS07Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws07')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS07Actual = res.data
          console.log(res,this.itemsWS07Actual)
        }
      },


      async fetchDataStatusWS08(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws08')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS08 = res.data
          console.log(res,this.itemsWS08)
        }
      },

      async fetchDataStatusWS08Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws08')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS08Actual = res.data
          console.log(res,this.itemsWS08Actual)
        }
      },


      async fetchDataStatusWS09(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plan/ws09')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS09 = res.data
          console.log(res,this.itemsWS09)
        }
      },

      async fetchDataStatusWS09Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actual/ws09')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS09Actual = res.data
          console.log(res,this.itemsWS09Actual)
        }
      },
   
   

    validate(){
      const date = new Date(this.tanggalPencarian)
      date.setDate(date.getDate() + 1);
      this.myChartStartCustom = this.tanggalPencarian

      const date2 = new Date(this.tanggalPencarian2)
      date2.setDate(date2.getDate() + 1);
      this.myChartEndCustom = this.tanggalPencarian2

      
      console.log("pencarian1 :",this.tanggalPencarian)
      console.log("pencarian2 :",this.tanggalPencarian2)
      console.log("renmul",this.myChartStartCustom)
      console.log("rensel",this.myChartEndCustom)

  
     
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

      this.fetchDataStatusWS00Actual()
      this.fetchDataStatusWS01Actual()
      this.fetchDataStatusWS02Actual()
      this.fetchDataStatusWS03Actual()
      this.fetchDataStatusWS04Actual()
      this.fetchDataStatusWS05Actual()
      this.fetchDataStatusWS06Actual()
      this.fetchDataStatusWS07Actual()
      this.fetchDataStatusWS08Actual()
      this.fetchDataStatusWS09Actual()

      
    },
  }
}



</script>