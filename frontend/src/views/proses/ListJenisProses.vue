<template>
    <v-card  
        class="mx-auto text-center"
        max-width="1000">

        <h2>List Jenis Proses</h2>
        <v-data-table
          :headers = "column"
          :items = "jenisproses"
        >
        </v-data-table>
    </v-card>
</template>

<script>

export default{
    data(){
        return{
            column : [
                {text : 'Id',value : 'id'},
                {text : 'Nama Jenis Proses',value : 'namajenisproses'},
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