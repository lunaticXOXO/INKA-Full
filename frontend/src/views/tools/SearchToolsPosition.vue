<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width = "1200">
        <br>
        <h1>Pencarian Perkakas</h1>
        <br>
     

        <div class="d-flex">
          
          
            <v-autocomplete
            class="custom-v-select mx-auto text-center"
          
            item-text="nama"
            item-value="nama"
            v-model="type"
            :items="tooltype"

            label="Nama Tools"
        ></v-autocomplete>
        </div>
        <v-btn
          :loading="loading"
          color="primary"
          class="d-flex mx-auto mt-10"
          @click="RequestSearch()"
          >
          Search
        </v-btn>

        <v-data-table 
          
          :headers="headers"
          :items="listsearch"
          :items-per-page="5"
          class="elevation-1 mt-15"
         >
        
        </v-data-table>
        
      
 
   
    <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
            {{snackbar.message}}
        </v-snackbar>
    </v-card>
</template>

<script>
  export default {
   data(){
    return {

       
      snackbar : {
        show : false,
        color : null,
        message : null,
      },
        headers: [
    
        {text : 'Code', value : 'toolTypeCode'},
        {text: 'Nama Perkakas' , value : 'nama'},
        {text : 'Tool Stock', value : 'idToolStock'},
        {text : 'Jumlah',value : 'quantity'},
        {text : 'Posisi Workstation', value : 'onWs'},
     
        
        
      ],
  
        listtool : [],
        listsearch : [],
        tooltype : [],
        type : '',
      
   
     
   }    
},

mounted(){
    this.fetchToolType(),
    this.ListSearch(),
    this.RequestSearch()
  
  
},
  
  methods : {

    async RequestSearch(){

        console.log("name : ", this.type)

        try{
            //setTimeout(() => {
            const axios = require('axios')
            const res = await axios.get('/tools/show_posisi_tools_byname/' + this.type)
            if(res.data.length == 0){
                this.snackbar = {
                show : true,
                message : "Perkakas Tidak Ditemukan",
                color : "red"
            }
                 
                 console.log("tools kosong")
            }else{
                let counter = 0
                window.setTimeout(() => {
                           
                            this.listsearch = res.data 
                            console.log(res,this.listsearch)
                    
                        counter++
                        //console.log("counter : ",counter)
                        if(counter >= 0){
                            console.log("counter : ", counter)
                            window.clearInterval(() => {},1500)
                        }
                        

                }, 1500)

                      


              this.snackbar = {
                show : true,
                message : "Perkakas Ditemukan",
                color : "green"
            }

            window.clearInterval(1500)
            //this.listsearch = null
                
            }
        //}, 1000)
        }
    
        catch(error){
            console.log(error)
        }
    },

    async ListSearch(){
        try{
            const axios = require('axios')
            const res = await axios.get('/tools/show_posisi_tools')
            if(res.data == null){
                 console.log("tools kosong")
            }else{
                
                    this.listsearch = res.data 
                    //console.log(res,this.listtool)
         
                
            }

        }
        catch(error){
            console.log(error)
        }

    },

    async fetchToolType(){
        try{
          const axios = require('axios');
          const res = await axios.get('/tools/show_tooltype');
          if (res.data == null){
            console.log('tools Kosong')
          }else{
            this.tooltype = res.data
            console.log(res,this.tooltype)
           
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

<style>

.custom-v-select {
  max-width: 500px; 
}

</style>