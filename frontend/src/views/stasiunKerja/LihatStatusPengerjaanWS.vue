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
    
    <v-card class="mt-5 mx-10">
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
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

      
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p >ID Operasi : {{ selectedBar00 ? selectedBar00.idOperasi : '' }}</p>
                  <p>Proses : {{selectedBar00 ? selectedBar00.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar00 ? selectedBar00.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar00 ? selectedBar00.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar00 ? selectedBar00.rencanaSelesai : ''}}</p>
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
          label="WS01 Plan"
          :bars="itemsWS01"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
          color = "#2596be"
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <!-- <div v-for="bar in bars" v-bind:key="bar.idOperasi"> -->
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p >ID Operasi : {{ selectedBar01 ? selectedBar01.idOperasi : '' }}</p>
                  <p>Proses : {{selectedBar01 ? selectedBar01.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar01 ? selectedBar01.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar01 ? selectedBar01.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar01 ? selectedBar01.rencanaSelesai : ''}}</p>
                </v-card-text>
                <!-- </div> -->

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
          label="WS02 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart2(bar)"
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
                    <p>ID Operasi : {{selectedBar02 ? selectedBar02.idOperasi : ''}}</p>
                    <p>Proses : {{selectedBar02 ? selectedBar02.namaProses : ''}}</p>
                    <p>Lokasi Stasiun Kerja : {{selectedBar02 ? selectedBar02.namaStasiunKerja : ''}}</p>
                    <p>Operator : </p>
                    <br>
                    <p>Rencana Mulai : {{selectedBar02 ? selectedBar02.rencanaMulai : ''}}</p>
                    <p>Rencana Selesai : {{selectedBar02 ? selectedBar02.rencanaSelesai : ''}}</p>
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
          label="WS03 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart3(bar)"
                >
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>
                
                <!-- <div v-for="bar in bars" v-bind:key="bar.idOperasi"> -->
                  <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                    <br>
                    <p>ID Operasi : {{selectedBar03 ? selectedBar03.idOperasi : ''}}</p>
                    <p>Proses : {{selectedBar03 ? selectedBar03.namaProses : ''}}</p>
                    <p>Lokasi Stasiun Kerja : {{selectedBar03 ? selectedBar03.namaStasiunKerja : ''}}</p>
                    <p>Operator : </p>
                    <br>
                    <p>Rencana Mulai : {{selectedBar03 ? selectedBar03.rencanaMulai : ''}}</p>
                    <p>Rencana Selesai : {{selectedBar03 ? selectedBar03.rencanaSelesai : ''}}</p>
                  </v-card-text>
                <!-- </div> -->
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
          label="WS04 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = " selectedGantChart4(bar)"
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
                  <p>ID Operasi : {{selectedBar04 ? selectedBar04.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar04 ? selectedBar04.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar04 ? selectedBar04.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar04 ? selectedBar04.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar04 ? selectedBar04.rencanaSelesai : ''}}</p>
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
          label="WS05 Plan"
          :bars="itemsWS05"
          bar-start="rencanaMulai"
          bar-end="rencanaSelesai"
          :bar-style="getBarStyle"
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

      
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p >ID Operasi : {{ selectedBar05 ? selectedBar05.idOperasi : '' }}</p>
                  <p>Proses : {{selectedBar05 ? selectedBar05.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar05 ? selectedBar05.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar05 ? selectedBar05.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar05 ? selectedBar05.rencanaSelesai : ''}}</p>
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
          label="WS06 Plan"
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

            <template v-slot:[`bar.idOperasi`]="{ bar }">
              <span >{{bar.idOperasi}}</span>
            </template>

              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="font-weight-bold"
                  color="#2596be"
                  :id="bar.idOperasi"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart6(bar)"
                
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
                  <p>ID Operasi : {{selectedBar06 ? selectedBar06.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar06 ? selectedBar06.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar06 ? selectedBar06.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar06 ? selectedBar06.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar06 ? selectedBar06.rencanaSelesai : ''}}</p>
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
          label="WS07 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart7(bar)"
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
                  <p>ID Operasi : {{selectedBar07 ? selectedBar07.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar07 ? selectedBar07.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar07 ? selectedBar07.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar07 ? selectedBar07.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar07 ? selectedBar07.rencanaSelesai : ''}}</p>
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
          label="WS08 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart8(bar)"
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
                  <p>ID Operasi : {{selectedBar08 ? selectedBar08.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar08 ? selectedBar08.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar08 ? selectedBar08.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar08 ? selectedBar08.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar08 ? selectedBar08.rencanaSelesai : ''}}</p>
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
          label="WS09 Plan"
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
                  color="#2596be"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart9(bar)"
                  
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
                  <p>ID Operasi : {{selectedBar09 ? selectedBar09.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar09 ? selectedBar09.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar09 ? selectedBar09.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Rencana Mulai : {{selectedBar09 ? selectedBar09.rencanaMulai : ''}}</p>
                  <p>Rencana Selesai : {{selectedBar09 ? selectedBar09.rencanaSelesai : ''}}</p>
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

    <v-card  class="mb-5 mx-10">
    
      <v-card
          color="#6f6f6f"
          dark
          class="px-5 py-3"
          max-height ="200"
            >
        <v-card-title class="text-h5">
          TIMELINE ACTUAL PENGERJAAN OPERASI
        </v-card-title>
            
      </v-card> 
      <br><br>

       <g-gantt-chart
      :chart-start="myChartStartCustom2"
      :chart-end="myChartEndCustom2"
        :row-label-width="`${rowLabelWidth}%`"
        :row-height="rowHeight"
        :grid="grid"
        :theme="selectedTheme"
        class="mb-4"
      >
      
       <g-gantt-row
          label="WS00 Actual"
          :bars="itemsWS00Actual"
          bar-start="mulai"
          bar-end="selesai"
        >
          <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS00Actual"
              width="750"
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
                <div v-for="bar in bars" v-bind:key="bar.idOperasi">
            
                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                
                  <p>ID Operasi : {{selectedBar00Actual ? selectedBar00Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar00Actual ? selectedBar00Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar00Actual ? selectedBar00Actual.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar00Actual ? selectedBar00Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar00Actual ? selectedBar00Actual.selesai : ''}}</p>
                </v-card-text>
              </div>

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
          label="WS01 Actual"
          :bars="itemsWS01Actual"
          bar-start="mulai"
          bar-end="selesai"
        >
          <template #bar-label="{bar}">
            <v-dialog
              v-model="dialogWS01Actual"
              width="950"
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar01Actual ? selectedBar01Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar01Actual ? selectedBar01Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar01Actual ? selectedBar01Actual.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar01Actual ? selectedBar01Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar01Actual ? selectedBar01Actual.selesai : ''}}</p>
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar02Actual ? selectedBar02Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar02Actual ? selectedBar02Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar02Actual ? selectedBar02Actual.namaStasiunKerja : ''}}</p>
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
                  color="#222222"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart3Actual(bar)"
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
                  <p>ID Operasi : {{selectedBar03Actual ? selectedBar03Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar03Actual ? selectedBar03Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar03Actual ? selectedBar03Actual.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar03Actual ? selectedBar03Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar03Actual ? selectedBar03Actual.selesai : ''}}</p>
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar04Actual ? selectedBar04Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar04Actual ? selectedBar04Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar04Actual ? selectedBar04Actual.namaStasiunKerja : ''}}</p>
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
            {{bar.namaProses}}

            </v-btn>
          </template>

          <v-card>
            <v-card-title class="text-h4 grey lighten-2">
              Detail Operasi
            </v-card-title>

            <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
              <br>
                  <p>ID Operasi : {{selectedBar05Actual ? selectedBar05Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar05Actual ? selectedBar05Actual.namaProses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar05Actual ? selectedBar05Actual.namaStasiunKerja : ''}}</p>
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar06Actual ? selectedBar06Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar06Actual ? selectedBar06Actual.namaProses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar06Actual ? selectedBar06Actual.namaStasiunKerja : ''}}</p>
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
                  color="#28B463"
                  dark
                  v-bind="attrs"
                  v-on="on"
                  @click = "selectedGantChart7Actual(bar)"
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
                  <p>ID Operasi : {{selectedBar07Actual ? selectedBar07Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar07Actual ? selectedBar07Actual.namaProses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar07Actual ? selectedBar07Actual.namaStasiunKerja : ''}}</p>
                  <p>Operator : </p>
                  <br>
                  <p>Mulai : {{selectedBar07Actual ? selectedBar07Actual.mulai : ''}}</p>
                  <p>Selesai : {{selectedBar07Actual ? selectedBar07Actual.selesai : ''}}</p>
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar08Actual ? selectedBar08Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar08Actual ? selectedBar08Actual.namaProses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar08Actual ? selectedBar08Actual.namaStasiunKerja : ''}}</p>
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
                {{bar.namaProses}}
                </v-btn>
              </template>

              <v-card>
                <v-card-title class="text-h4 grey lighten-2">
                  Detail Operasi
                </v-card-title>

                <v-card-text class="text-h5 black--text darken-2 font-weight-bold">
                  <br>
                  <p>ID Operasi : {{selectedBar09Actual ? selectedBar09Actual.idOperasi : ''}}</p>
                  <p>Proses : {{selectedBar09Actual ? selectedBar09Actual.namaProses : ''}}</p>
                   <p>Lokasi Stasiun Kerja : {{selectedBar09Actual ? selectedBar09Actual.namaStasiunKerja : ''}}</p>
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

var today = new Date();
var newDate = new Date(Date.now()+1*24*60*60*1000);
var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
var date2 = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+ newDate.getDate();
//var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

var dateTime = date
var dateTime2 = date2 


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

    

      myChartStartCustom2: dateTime,
      myChartEndCustom2: dateTime2,

    

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

  mounted(){
    this.fetchStartFinishOperation(this.tanggalPencarian, this.tanggalPencarian2)
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
      const res = await axios.get('/operasi/get_operasi_gantt/ws00')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS00 = res.data
        console.log("ws00",this.itemsWS00)
      }
    },

    
    async fetchDataStatusWS00Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws00')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS00Actual = res.data
        console.log("ws00 Actual" ,this.itemsWS00Actual)
      }
    },
    
   
    async fetchDataStatusWS01(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws01')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS01 = res.data
        console.log("ws01",this.itemsWS01)
      }
    },

    async fetchDataStatusWS01Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws01')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS01Actual = res.data
        console.log("ws01 Actual",this.itemsWS01Actual)
      }
    },

    
    async fetchDataStatusWS02(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws02')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS02 = res.data
        console.log("ws02",this.itemsWS02)
      }
    },

    async fetchDataStatusWS02Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws02')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS01Actual = res.data
        console.log("ws02 Actual",this.itemsWS01Actual)
      }
    },
    

    async fetchDataStatusWS03(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws03')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS03 = res.data
        console.log("ws03",this.itemsWS03)
      }
    },

    async fetchDataStatusWS03Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws03')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS03Actual = res.data
        console.log("ws03 Actual",this.itemsWS03Actual)
      }
    },


    async fetchDataStatusWS04(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws04')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS04 = res.data
        console.log("ws04 Actual",this.itemsWS04)
      }
    },

    async fetchDataStatusWS04Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws04')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS04Actual = res.data
        console.log("ws04",this.itemsWS04Actual)
      }
    },

  
    async fetchDataStatusWS05(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws05')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS05 = res.data
        console.log("ws05:",this.itemsWS05)
      }
    },


    async fetchDataStatusWS05Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws05')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS05Actual = res.data
        console.log("ws05:",this.itemsWS05Actual)
      }
    },

    
    async fetchDataStatusWS06(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws06')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS06 = res.data
        console.log("ws06:",this.itemsWS06)
      }
    },

    async fetchDataStatusWS06Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws06')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS06Actual = res.data
        console.log("ws06 Actual:",this.itemsWS06Actual)
      }
    },

    
    async fetchDataStatusWS07(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws07')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS07 = res.data
        console.log("ws07:",this.itemsWS07)
      }
    },

    async fetchDataStatusWS07Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws07')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS07Actual = res.data
        console.log("ws07 Actual:",this.itemsWS07Actual)
      }
    },

  
    async fetchDataStatusWS08(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws08')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS08 = res.data
        console.log("ws08",this.itemsWS08)
      }
    },

    async fetchDataStatusWS08Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws08')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS08Actual = res.data
        console.log("ws08 Actual",this.itemsWS08Actual)
      }
    },


    async fetchDataStatusWS09(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt/ws09')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS09 = res.data
        console.log("ws09",this.itemsWS09)
      }
    },

    async fetchDataStatusWS09Actual(){
      const axios = require('axios')
      const res = await axios.get('/operasi/get_operasi_gantt2/ws09')
      if(res.data == null){
        console.log("Data Pengerjaan Kosong")
      }else{
        this.itemsWS09Actual = res.data
        console.log("ws09",this.itemsWS09Actual)
      }
    },

   async fetchStartFinishOperation(tanggalPencarian, tanggalPencarian2){
    try{

        const axios = require('axios')
        const res = await axios.get('/operasi/get_operasi_start_finish/' + tanggalPencarian + '/'  + tanggalPencarian2)
        //console.log("pilih mulai : ",this.tanggalPencarian )
        //console.log("pilih selesai : ",this.tanggalPencarian2 )

        if (res.data == null){
          console.log("kosong")
        }else{
          this.listdate = res.data
          console.log("fetch tanggal",res,this.listdate)
          this.mulai_str = this.listdate[0].mulai
          this.selesai_str = this.listdate[0].selesai
          this.myChartStartCustom2 = this.mulai_str
          this.myChartEndCustom2 = this.selesai_str

          console.log("mulai",this.myChartStartCustom2)
          console.log("selesai",this.myChartEndCustom2)
        }
    }
    catch(error){
        console.log(error)
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

  
     this.fetchStartFinishOperation(this.tanggalPencarian,this.tanggalPencarian2)
     
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

      


      //console.log(this.pilihan)
    },
  }
}

</script>