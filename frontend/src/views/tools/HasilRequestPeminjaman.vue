<template>
<v-app>

    <v-card 
        class="mt-6 ml-5"
        max-width = "800">
        <br>
        <h2 class="mx-auto text-center">Waktu dan Stasiun Kerja Pilihan</h2>
        <br>
        
        <v-data-table 
            :headers = "column2"
            :items = "requestpeminjaman"
            :items-per-page="5"
            >
        
        </v-data-table>
    
    </v-card>

    <v-card 
        class="mt-6 ml-5"
        max-width = "1250">
        <br>
        <h2 class="mx-auto text-center">Permintaan Peminjaman Perkakas Sesuai Kebutuhan</h2>
        <br>
        
        <v-data-table 
            :headers = "column"
            :items = "requestpeminjaman"
            :items-per-page="5"
            >
        
        <template v-slot:[`item.id`]="{ item }">
                <span>{{item.id}}</span>
        </template>

        <template v-slot:[`item.tanggal`]="{ item }">
                <span>{{item.tanggal}}</span>
        </template>

        </v-data-table>

        <div class="d-flex">
            <v-text-field
                    max-width="10"
                    dense
                    v-model="uuid"
                    @keyup.enter="parseBarcode"
                    autofocus
                    single-line 
                    class="shrink ml-4 mt-2"
                    label="ID Operator"
                    >
            </v-text-field>
        
        <v-btn 
        color="green" 
        class="mb-5 ml-4"
        @click ="peminjamanPerkakas()"
        >
            Submit
        </v-btn>
        </div>
        <v-snackbar :color="snackbar.color" v-model="snackbar.show" top>
        {{snackbar.message}}
      </v-snackbar>
    </v-card>
    </v-app>
</template>

<script>
  export default {

    data(){
      return {
        valid : true,
        column : [
            {text : 'ID Box',                       value : 'boxId'},
            {text : 'ID Tool Stock',                value : 'id'},
            {text : 'Nama Tools',                   value : 'nama'},
            {text : 'Jumlah',             value : 'quantity'},
           
        ],

        column2 : [
        {text : 'Workstation', value : 'onWs'},
        {text : 'Tanggal', value : 'tanggal'}

        ],
        requestpeminjaman : [],
        tanggal : '',
        uuid : '',
        snackbar : {
                    show : false,
                    color : null,
                    message : null,
        },
        
       
      }
    },

    mounted(){
        this.fetchHasilRequestPeminjaman()
       
    },

    methods: {
    

      async fetchHasilRequestPeminjaman(){
        try{
          const axios = require('axios');
          const res = await axios.get('/tools/show_requestbox_peminjaman/' + this.$route.params.id,{
                params : {
                    tanggal : this.$route.query.tanggal
                }
          });
          if (res.data == null){
            alert('Customer Kosong')
          }else{
            this.requestpeminjaman = res.data
            console.log(res,this.requestpeminjaman)
          }
        }
        catch(error){
          alert("Error")
          console.log(error)
        }
      },

      async peminjamanPerkakas(){
        try{
            const axios = require('axios')
            const res = await axios.post('/tools/peminjaman_tools/' + this.$route.params.id + '/' + this.$route.query.tanggal,{
              
                uuid : this.uuid
                
            })

            if(res.data.status == 'berhasil'){
                this.snackbar = {
                        show : true,
                        message : "Peminjaman Berhasil",
                        color : "green"
            }
            setTimeout(() => {
                        location.replace('/hasilRequestPeminjaman/' + this.$route.params.id + '?tanggal=' + this.$route.query.tanggal) 
                    }, 1000)
        }
            else{
                this.snackbar = {
                        show : true,
                        message : "Peminjaman Gagal",
                        color : "red"
            }}
         
        }
        catch(error){
            alert("error")
            console.log(error)
        }
      
    },
  }

}
</script>