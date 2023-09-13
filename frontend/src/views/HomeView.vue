<template>
  <v-app>
    <v-card class="mx-auto text-center" max-width="1000" elevation="0">
      <p id="judul" class="font-weight-thin">SmartWorks 4.0</p>
    </v-card>
   

    <v-carousel cycle :show-arrows="false" delimiter-icon="mdi-minus" height="850">
      
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
              width="750"
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
                  <p>Proses : {{selectedBar001 ? selectedBar01.proses : ''}}</p>
                  <p>Lokasi Stasiun Kerja : {{selectedBar01 ? selectedBar01.namaWS : ''}}</p>
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
                  <p>Lokasi Stasiun Kerja : {{selectedBar01Actual ? selectedBar01Actual.namaWS : ''}}</p>
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
              width="750"
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
              width="750"
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
            <div class="app">
          <apexchart ref="realtimeChart" type="line" height="550" :options="chartOptions" :series="chartSeries"></apexchart>
        </div>
        <v-card-text>
          <div class="text-h4">
            Kurva S
          </div>
        </v-card-text>
            <!-- <v-data-table
              :headers = "headers"
              :items = "proyek"> 

            </v-data-table> -->
          </v-card>
        </v-row>
      </v-carousel-item>

      <!-- <v-carousel-item>
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
      </v-carousel-item> -->

    </v-carousel>
  </v-app>
</template>

<script>
  import {GGanttChart, GGanttRow} from 'vue-ganttastic'
  import VueApexCharts from 'vue-apexcharts'

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
      apexchart: VueApexCharts,
     
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

      this.fetchDataStatusWS00Actual(),
      this.fetchDataStatusWS01Actual(),
      this.fetchDataStatusWS02Actual(),
      this.fetchDataStatusWS03Actual(),
      this.fetchDataStatusWS04Actual(),
      this.fetchDataStatusWS05Actual(),
      this.fetchDataStatusWS06Actual(),
      this.fetchDataStatusWS07Actual(),
      this.fetchDataStatusWS08Actual(),
      this.fetchDataStatusWS09Actual(),
      


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
      this.fetchOperatorOnWS09(),

      this.fetchProgressProyek()
    },

    methods : {

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
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws00')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS00 = res.data
          console.log(res,this.itemsWS00)
        }
      },

      async fetchDataStatusWS00Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws00')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS00Actual = res.data
          console.log(res,this.itemsWS00Actual)
        }
      },

      async fetchDataStatusWS01(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws01')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS01 = res.data
          console.log(res,this.itemsWS01)
        }
      },

      async fetchDataStatusWS01Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws01')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS01Actual = res.data
          console.log(res,this.itemsWS01Actual)
        }
      },


      async fetchDataStatusWS02(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws02')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS02 = res.data
          console.log(res,this.itemsWS02)
        }
      },

      async fetchDataStatusWS02Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws02')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS02Actual = res.data
          console.log(res,this.itemsWS02Actual)
        }
      },


      async fetchDataStatusWS03(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws03')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS03 = res.data
          console.log("Plan03 :",res,this.itemsWS03)
        }
      },

      async fetchDataStatusWS03Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws03')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS03Actual = res.data
          console.log("Actual03 : ",res,this.itemsWS03Actual)
        }
      },

      async fetchDataStatusWS04(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws04')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS04 = res.data
          console.log(res,this.itemsWS04)
        }
      },

      async fetchDataStatusWS04Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws04')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS04Actual = res.data
          console.log(res,this.itemsWS04Actual)
        }
      },


      async fetchDataStatusWS05(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws05')
      
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS05 = res.data
          console.log(res,this.itemsWS05)
        }
      },

      async fetchDataStatusWS05Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws05')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS05Actual = res.data
          console.log(res,this.itemsWS05Actual)
        }
      },


      async fetchDataStatusWS06(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws06')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS06 = res.data
          console.log(res,this.itemsWS06)
        }
      },

      async fetchDataStatusWS06Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws06')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS06Actual = res.data
          console.log(res,this.itemsWS06Actual)
        }
      },


      async fetchDataStatusWS07(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws07')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS07 = res.data
          console.log(res,this.itemsWS07)
        }
      },

       async fetchDataStatusWS07Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws07')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS07Actual = res.data
          console.log(res,this.itemsWS07Actual)
        }
      },


      async fetchDataStatusWS08(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws08')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS08 = res.data
          console.log(res,this.itemsWS08)
        }
      },

      async fetchDataStatusWS08Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws08')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS08Actual = res.data
          console.log(res,this.itemsWS08Actual)
        }
      },


      async fetchDataStatusWS09(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_plantoday/ws09')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS09 = res.data
          console.log(res,this.itemsWS09)
        }
      },

      async fetchDataStatusWS09Actual(){
        const axios = require('axios')
        const res = await axios.get('/operasi/get_gantchart_actualtoday/ws09')
        if(res.data == null){
          console.log("Data Pengerjaan Kosong")
        }else{
          this.itemsWS09Actual = res.data
          console.log(res,this.itemsWS09Actual)
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
