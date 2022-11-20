<template>
    <v-card  
        class="mx-auto text-center mt-10"
        max-width="1000">

        <h2>Material Login</h2>
        <v-data-table
          :headers = "column"
          :items = "matlogin"
        >
        </v-data-table>
    </v-card>
</template>

<script>

export default{
    data(){
        return{
            column : [
                {text : 'ID Material',value : 'idMat'},
                {text : 'Stasiun Kerja',value : 'stasiunKerja'},
                {text : 'Keterangan', value : 'keterangan'},
                {text : 'Waktu',value : 'waktu'},
                {text : 'Status',value : 'status01'}
            ],
            matlogin : []
        }
    },
    mounted(){
        this.fetchMatLogin()
    },
    methods : {
        async fetchMatLogin(){
            try{
                const axios = require('axios')
                const res = await axios.get('/material/get_material_login')
                if(res.data == null){
                    console.log('Data kosong')
                }else{
                    this.matlogin = res.data
                    console.log(res,this.classification)
                }

            }catch(error){
                alert("Error")
            }
        }
    },
}


</script>