<template>
    <v-card  
        class="mx-auto text-center mt-8"
        max-width="1000">
        <h1>List Jenis Proses</h1>
        <v-data-table
          :headers = "column"
          :items = "jenisproses">
        </v-data-table>
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