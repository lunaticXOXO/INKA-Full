<template>
<v-app>
    <h1 class="mx-auto text-center mt-15">Distribusi Perkakas</h1>
    <v-card class="mx-auto text-center mt-15 mb-10" width="750" height="400">
       <v-form
            class="pa-6"
          ref="form"
          @submit.prevent="submitHandler"
          v-model="valid"
          lazy-validation
       >
        <div class="d-flex">
            <v-menu     
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="dueDate" v-bind="attrs" v-on="on" label="Range Tanggal Awal" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            
            <v-date-picker full-width v-model="dueDate"></v-date-picker>
          </v-menu>
          
          <v-menu
            ref="menu"
            v-model="menu"
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
                label="Range Jam Awal"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>  
            </template>
            <v-time-picker
              v-if="menu"
              v-model="datetime"
              full-width
              format="24hr"
              @click:minute="$refs.menu.save(time)"
            ></v-time-picker>
          </v-menu>
        </div>
    
        <div class="d-flex">
            <v-menu     
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-10" :value="dueDate2" v-bind="attrs" v-on="on" label="Range Tanggal Akhir" prepend-icon="mdi-calendar"></v-text-field>
            </template>
            <v-date-picker full-width v-model="dueDate2"></v-date-picker>
          </v-menu>
          
          <v-menu
            ref="menu2"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time2"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="mx-10"
                v-model="datetime2"
                label="Range Jam Akhir"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>  
            </template>
            <v-time-picker
              v-if="menu2"
              v-model="datetime2"
              full-width
              format="24hr"
              @click:minute="$refs.menu2.save(time2)"
            ></v-time-picker>
          </v-menu>
        </div>

        <v-autocomplete 
        v-model="ws00"
        item-text="nama"
        item-value="id"
        :items ="items" 
        label="Stasiun Kerja">
        </v-autocomplete>

    <!-- <v-card class="mx-auto text-center" max-width="1250" elevation="0">
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
                                <v-radio-group v-model="workstation">
                                <v-radio  :value = "item.id" >
                                    
                                </v-radio>
                                </v-radio-group>
                                <p class="mt-5">{{ item.nama }}</p>  
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-card> -->
    <div class="d-flex" >
       
    
        <v-btn
        :disabled="!valid"
        color="success"
        class="mx-auto text-center"
        type="submit"
        @click="validate()"
        >
        Submit
        </v-btn>
   

    </div>
    </v-form>

    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>

    </v-card>

</v-app>

</template>

<script>
 export default{

    data(){
        return {
            
            tgl00 : undefined,
            tgl01 : undefined,
            dueDate : undefined,
            datetime : undefined,
            dueDate2 : undefined,
            datetime2 : '',
            time : null,
            time2 : null,
            menu2 : false,
            menu : false,
            valid : true,
            items : [],
            items2 : [],
            ws00 : undefined, 
            snackbar : {
                show : false,
                color : null,
                message : null,
            },

        }

       
    },


    mounted(){
        this.fetchData()
    },

    methods : {

    validate () {
        if(this.$refs.form.validate()){
          this.RequestKebutuhanTool()
        }
      },

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

        async RequestKebutuhanTool(){
            try{
                const axios = require('axios')
                this.tgl00 = this.dueDate + ' ' +  this.datetime
                this.tgl01 = this.dueDate2 + ' ' + this.datetime2
                const res = await axios.post('/tools/request_distribusi_perkakas',{
                    tgl00 : this.tgl00,
                    tgl01 : this.tgl01,
                    ws00 : this.ws00
                })
                console.log("id item : ", this.ws00)
                if (res.data.status == 'berhasil'){
                    setTimeout(() => {
                        location.replace('/listKebutuhanPerkakasByWorkstation/' + this.ws00 + '?rencanaMulai=' + this.dueDate) 
                    }, 1000)

                    console.log("request berhasil")
                    this.snackbar = {
                        show : true,
                        message : "Request Berhasil",
                        color : "green"
            }
                }else{
                    this.snackbar = {
                        show : true,
                        message : "Request Failed",
                        color : "red"
            }
                }
            }
            catch(error){
                console.log(error)
            }
           
            return this.dueDate

        }        
       


    }

 }
</script>
