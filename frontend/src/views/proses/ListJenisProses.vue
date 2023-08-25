<template>
    <v-card  
        class="mx-auto text-center mt-8"
        max-width="1700">
        <v-card
                color="#6f6f6f"
                dark
                class="px-5 py-3"
                max-height ="200"
            >
            <v-card-title class="text-h5">
             DAFTAR JENIS PROSES
            </v-card-title>
        </v-card>
         <br><br>
        <v-data-table
          :headers = "column"
          :items = "jenisproses">
        </v-data-table>
        <br>
        <v-card
            color="#6f6f6f"
            dark
            class="px-5 py-3"
            max-height ="50"
        >
        </v-card>

    </v-card>
</template>

<script>

export default{
    data(){
        return{
            column : [
                {text : 'ID',value : 'id'},
                {text : 'Nama Jenis Proses',value : 'namaJenisProses'},
            ],
            jenisproses : []
        }
    },
    mounted(){
        this.fetchJenisProses()
    },
    methods : {
        async fetchJenisProses(){
            try{
                const axios = require('axios')
                const res = await axios.get('/jenis_proses/get_jenisproses')
                if(res.data == null){
                    console.log('Data kosong')
                }else{
                    this.jenisproses = res.data
                    console.log(res,this.jenisproses)
                   
                }

            }catch(error){
                alert("Error")
            }
        }
    },
}


</script>