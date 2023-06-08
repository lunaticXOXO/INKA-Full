<template>
<v-app>
    <h1 class="mx-auto text-center mt-15">Distribusi Perkakas</h1>
    <v-card class="mx-auto text-center mt-15 mb-10" width="700" height="400">
       
        <div class="d-flex">
            <v-menu 
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker full-width v-model="dueDate"></v-date-picker>
          </v-menu>
          
          <v-menu
            ref="menu"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="mx-10"
                v-model="datetime"
                label="Due Time"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menu2"
              v-model="datetime"
              full-width
              format="24hr"
              @click:minute="$refs.menu.save(time)"
            ></v-time-picker>
          </v-menu>



        </div>


    <v-card class="mx-auto text-center" max-width="1250" elevation="0">
            <v-container fluid>
                <v-row dense>
                    <v-col
                        v-for="item in items"
                        :key="item.nama"
                        :cols="item.flex"
                        :value="item.id"
                        >
                        <v-card class="mx-auto justify-center text-center" elevation="0" outlined>
                            <div class="d-flex ml-2 text-center">
                                <v-radio-group v-model="radios">
                                <v-radio  :value = "item.id" >
                                    
                                </v-radio>
                                </v-radio-group>
                                <p class="mt-5">{{ item.nama }}</p>  
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    <div class="d-flex" >
    <v-btn class="mx-auto text-center" color="primary">
        Submit
    </v-btn>


    </div>
    
    </v-card>

</v-app>

</template>

<script>
 export default{

    data(){
        return {
            items : [],
            workstation : undefined,
         

        }

       
    },


    mounted(){
            this.fetchData()
    },

    methods : {

        async fetchData(){
            try{
                const axios = require('axios')
                const res = await axios.get('/stasiun_kerja/show_stasiun_kerja')
                if (res == null){
                    alert("Stasiun Kerja Kosong")  
                }
                else{
                    this.items = res.data
                    console.log(res,this.items)
                }
            }
            catch(error){
                alert("Error")
                console.log(error)
            }
        },

       


    }

 }
</script>
