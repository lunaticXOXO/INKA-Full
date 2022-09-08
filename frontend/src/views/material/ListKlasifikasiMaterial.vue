<template>
    <v-card  
        class="mx-auto text-center mt-10"
        max-width="1000">

        <h2>List Klasifikasi</h2>
        <v-data-table
          :headers = "column"
          :items = "classification"
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
                {text : 'Description',value : 'descriptions'}
            ],
            classification : []
        }
    },
    mounted(){
        this.fetchClassification()
    },
    methods : {
        async fetchClassification(){
            try{
                const axios = require('axios')
                const res = await axios.get('/material/show_classification')
                if(res.data == null){
                    console.log('Data kosong')
                }else{
                    this.classification = res.data
                    console.log(res,this.classification)
                }

            }catch(error){
                alert("Error")
            }
        }
    },
}


</script>