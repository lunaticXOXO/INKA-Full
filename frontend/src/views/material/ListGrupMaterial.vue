<template>
    <v-card  
        class="mx-auto text-center mt-10"
        max-width="1000">
        <h2>List Grup Material</h2>
        <v-data-table
          :headers = "column"
          :items = "grup"
        >
        </v-data-table>
    </v-card>
</template>

<script>

export default{
    data(){
        return{
            column : [
                {text : 'Code',value : 'code'},
                {text : 'Description',value : 'descriptions'},
                {text : 'Remark',value : 'remark'}
            ],
            grup : []
        }
    },
    mounted(){
        this.fetchGrup()
    },
    methods : {
        async fetchGrup(){
            try{
                const axios = require('axios')
                const res = await axios.get('/material/show_groups')
                if(res.data == null){
                    console.log('Data kosong')
                }else{
                    this.grup = res.data
                    console.log(res,this.classification)
                }

            }catch(error){
                alert("Error")
            }
        }
    },
}


</script>