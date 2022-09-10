<template>
    <v-app>
      <h3 class="ml-10 mt-6">Pilih Stasiun Kerja</h3>
      <v-card class="mx-auto" max-width="1250" elevation="0">
            <v-container fluid>
                <v-row dense>
                    <v-col
                        v-for="item in items"
                        :key="item.name"
                        :cols="item.flex">
                        <v-card class="mx-auto justify-center text-center" elevation="0" outlined>
                            <div class="d-flex ml-2 text-center">
                                <v-checkbox></v-checkbox>
                                <p class="mt-5">{{ item.name }}</p>  
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
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

      <h3 class="ml-10 mt-6">Hasil Pencarian</h3>
      <v-card class="ml-10 mt-8" max-width="1000" elevation="0">
        <v-data-table 
            :headers = "column"
            :items = "items3"
            hide-default-footer>
            <template v-slot:[`item.h`]="{ item }">
                <v-chip
                    :color="getColor()"
                    dark>
                    {{ item.h }}
                </v-chip>
            </template>
            <template v-slot:[`item.aksi`]="{ item }">
                <v-btn class="mx-1" x-small color="green" @click="selectOperasi(item)">
                    <v-icon small dark>mdi-check</v-icon>
                </v-btn>
            </template>
        </v-data-table>
      </v-card>
      <br><br>
    </v-app>
  </template>
  
  <script>
    export default{
        data(){
        return {
            items: [
                { name: 'MINOR BUSHING',                flex: 2 },
                { name: 'MINOR AXLE BOX & WHEEL ASSY',  flex: 3 },
                { name: 'MINOR ASSY BOLSTER',           flex: 3 },
                { name: 'ASSY BRAKE RIGING',            flex: 2 },
                { name: 'BOGIE FITTING 1',              flex: 2 },
                { name: 'BOGIE FITTING 2',              flex: 2 },
                { name: 'FITTING ACCESORIES BOGIE 1',   flex: 3 },
                { name: 'FITTING ACCESORIES BOGIE 2',   flex: 3 },
                { name: 'LOAD TEST',                    flex: 2 },
            ],
            column : [
                {text : '',    value : 'aksi'},
                {text : 'ID Operasi',    value : 'idOperasi'},
                {text : 'Stasiun Kerja', value : 'ws'},
                {text : 'Keterangan',    value : 'keterangan'},
                {text : 'H-2',           value : 'h-2'},
                {text : 'H-1',           value : 'h-1'},
                {text : 'H',             value : 'h'},
                {text : 'H+1',           value : 'h+1'},
                {text : 'H+2',           value : 'h+2'},
                {text : 'H+3',           value : 'h+3'},
                {text : 'H+4',           value : 'h+4'},
            ],
            items2:[
                {
                    "idOperasi":"0322090600003",
                    "ws":"FITTING ACCESORIES BOGIE 2",
                    "keterangan":"Jadwal",
                    "h-2":"",
                    "h-1":"",
                    "h":"",
                    "h+1":"",
                    "h+2":"180",
                    "h+3":"",
                    "h+4":"",
                },
                {
                    "idOperasi":"0322090600002",
                    "ws":"FITTING ACCESORIES BOGIE 2",
                    "keterangan":"Jadwal",
                    "h-2":"",
                    "h-1":"",
                    "h":"",
                    "h+1":"",
                    "h+2":"240",
                    "h+3":"",
                    "h+4":"",
                },
                {
                    "idOperasi":"0322090600001",
                    "ws":"FITTING ACCESORIES BOGIE 2",
                    "keterangan":"Jadwal",
                    "h-2":"",
                    "h-1":"",
                    "h":"",
                    "h+1":"",
                    "h+2":"90",
                    "h+3":"",
                    "h+4":"",
                },
                {
                    "idOperasi":"0322090600011",
                    "ws":"FITTING ACCESORIES BOGIE 2",
                    "keterangan":"Jadwal",
                    "h-2":"",
                    "h-1":"",
                    "h":"",
                    "h+1":"",
                    "h+2":"",
                    "h+3":"240",
                    "h+4":"",
                },
                {
                    "idOperasi":"0322090600010",
                    "ws":"FITTING ACCESORIES BOGIE 2",
                    "keterangan":"Jadwal",
                    "h-2":"",
                    "h-1":"",
                    "h":"",
                    "h+1":"",
                    "h+2":"",
                    "h+3":"180",
                    "h+4":"",
                },
            ],
            items3: undefined,
            checkbox: false,
        }
        },
    
        mounted(){
        
        },
    
        methods:{
            getColor() {
                return 'blue'
            },
            
            validate(){
                this.items3 = this.items2
            },
        },
    }
</script>