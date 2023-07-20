<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
        <br>
        <h1>Material Perlu Pesan</h1>
        <br>
        <!-- <router-link to="/jenisMaterial">
            <v-btn color="primary" class="d-flex ml-4 mb-6">
                Add Material Type
            </v-btn>
        </router-link> -->

        <!-- <v-data-table 
            v-model="selected"
            :headers = "column"
            :items = "types"
            item-value = "code"
            show-select
            class="elevation-1">
           
        </v-data-table> -->

        <div class="d-flex">
            <v-menu 
              class="mt-6"
              transition="scale-transition"
              offset-y
              max-width="280px"
              min-width="280px"
            >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field class="mx-6" :value="dueDate" v-bind="attrs" v-on="on" label="Tanggal" prepend-icon="mdi-calendar"></v-text-field>
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
            max-width="280px"
            min-width="280px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="mx-6"
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
        <v-btn
          :loading="loading"
          color="primary"
          class="d-flex mx-auto mt-10"
          @click="RequestPurchaseTime()"
          >
          Search
        </v-btn>

        <v-data-table 
          id="mytable"
          show-select = "true"
          v-model="selected"
          :headers="headers"
          :items="types"
          :items-per-page="5"
          class="elevation-1 mt-15"
          item-key="id">
    
        
          <template v-slot:[`item.id`]="{ item }">
            <div>
                <span >{{item.id}}</span>
            </div>
          </template>

          <template v-slot:[`item.code`]="{ item }">
            <span>{{item.code}}</span>
          </template>

          <template v-slot:[`item.nama`]="{ item }">
            <span>{{item.nama}}</span>
          </template>

      
        
 
   

      </v-data-table>
      
      <v-btn 
    color="primary" 
    class="mt-10 mb-5"
    v-bind="attrs"
    v-on="on"
    @click = "insertPesan()">
        Purchase
    </v-btn>

    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
   data(){
    return {

        time: null,
        menu2: false,
        valid: true,
        selected: [],
        dueDate : '',
      datetime : '',
      fullDate : '',
      loading : false,
      snackbar : {
        show : false,
        color : null,
        message : null,
      },
        headers: [
        // {
        //   text: 'ID',
        //   align: 'left',
        //   sortable: false,
        //   value: 'id',
        // },
        {text : 'Code', value : 'code'},
        {text: 'Name' , value : 'nama'},
        {text : 'Jumlah', value : 'jumlah'},
        {text : 'Pemasok',value : 'pemasok'},
        {text : 'Peringkat', value : 'peringkat'},
        {text : 'Rencana Kedatangan',value : 'RencanaKedatangan'},
        {text : 'Harga',value : 'Harga'},
        {text : 'Lead Time',value : 'LeadTime'},
        {text : 'Minimal Order',value : 'MinimalOrder'}
        
      ],
  
       types : [],
       requirmentMaterial : [],
        index : 0,
      
        mytable : false,

        id : '',
        code : '',
        nama : '',
        jumlah : '',
        pemasok : '',
        peringkat : '',
        RencanaKedatangan : undefined,
        LeadTime : '',
        Harga : '',
        MinimalOrder : '',
        originalDate : '',

        year : undefined,
        month : undefined,
        day : undefined,

        convertedDate : ''
   }    
},

mounted(){
  window.setInterval(() => {
    this.fetchMaterial()
     }, 1500)
  
},
  
  methods : {

    async fetchMaterial(){
        try{
          const axios = require('axios');
          const res = await axios.get('/material/show_material_haruspesan');
          if (res.data == null){
            alert('Material Kosong')
          }else{
            this.types = res.data
            
            console.log(res,this.types)
            if(this.mytable == true){
              console.log("test")
            }
            console.log("pilih : ",this.selected)
           
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      
      async RequestPurchaseTime(){
        this.loading = true
        try{
           
            this.fullDate = this.dueDate + " " + this.datetime
            const axios = require('axios');
            const res = await axios.post('/material/add_time_purchase',{fullDate : this.fullDate})
            setTimeout(() => {
              if (res.data.status == "berhasil"){
                this.snackbar = {
                  show : true,
                  message : "Pencarian Kebutuhan Material Berhasil",
                  color : "green" 
                }
                const res2 = axios.get('/material/show_material_haruspesan')
                if(res2.data == null){
                  console.log("")
                }
                else{
                  this.types = res2.data
                  console.log(res2,this.types)
                }
                this.loading = false
              }else if(res.data.status == "gagal"){
                this.snackbar = {
                  show : true,
                  message : "Pencarian Kebutuhan Material Gagal",
                  color : "red"
                }
                console.log("Gagal")
                this.loading = false
              }
            }, 1000)

        }
        catch(error){
          console.log(error)
        }
        
      },

      async convertDate(){
        for(this.index in this.selected){
            this.originalDate = new Date(this.selected[this.index].RencanaKedatangan)
            this.year = this.originalDate.getFullYear()
            this.month  = String(this.originalDate.getMonth() + 1).padStart(2, '0');
            this.day = String(this.originalDate.getDate()).padStart(2, '0');


            this.convertDate = `${this.year}-${this.month}-${this.day}`
            console.log("id : ",this.selected[this.index].id,"convert date : ",this.convertDate)
        }
      },

      async insertPesan(){
      try{
        const axios = require('axios')
        for(this.index in this.selected){
         
          this.originalDate = new Date(this.selected[this.index].RencanaKedatangan)
          this.year = this.originalDate.getFullYear()
          this.month  = String(this.originalDate.getMonth() + 1).padStart(2, '0');
          this.day = String(this.originalDate.getDate()).padStart(2, '0');


          this.convertDate = `${this.year}-${this.month}-${this.day}`
          const res = await axios.post('/material/insert_material_haruspesan',{
              id                : this.selected[this.index].id,
              code              : this.selected[this.index].code,
              nama              : this.selected[this.index].nama,
              jumlah            : this.selected[this.index].jumlah,
              pemasok           : this.selected[this.index].pemasok,
              peringkat         : this.selected[this.index].peringkat,
              RencanaKedatangan : this.convertDate,
              
              LeadTime          : this.selected[this.index].LeadTime,
              Harga             : this.selected[this.index].Harga,
              MinimalOrder      : this.selected[this.index].MinimalOrder

          })
          if(res.data.status == 'berhasil'){
              console.log("success")
              this.snackbar = {
                  show : true,
                  message : "Pemesanan Kebutuhan Material Berhasil",
                  color : "green" 
                }
                setTimeout(() => { 
                  location.replace('/listHasilPesanMaterial/' +  this.selected[this.index].pemasok)

                }, 1000)
          }
          else if(res.data.status == 'gagal'){
            this.snackbar = {
                  show : true,
                  message : "Pemesanan Kebutuhan Material Gagal",
                  color : "red" 
                }
          }
          //console.log("ID : ", this.selected[this.index].id)
        }
      }
      catch(error){
        console.log(error)
      }
       
      }

  }


  }
</script>