<template>
    <v-card 
        class="mx-auto text-center mt-10"
        max-width="1000">
        <br>
        <h1>List Barcode Material</h1>
        <br>
        <v-data-table 
            :headers = "column"
            :items = "statusbarcode">
        </v-data-table>
    </v-card>
</template>

<script>
    export default {
        data(){
            return{
                column : [
                    {text : 'ID Stock Material',    value : 'id'},
                    {text : 'Workstation',          value : 'workstation'},
                    {text : 'Status',               value : 'status'}
                ],
                statusbarcode : [],
                editedIndex: -1,
                editedItem: {
                    code: '',
                    descriptions: '',
                },
                defaultItem: {
                    code: '',
                    descriptions: '',
                }
            }
        },

        mounted(){
            this.fetchStatusBarcode()
        },

        methods : {
            close () {
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem);
                    this.editedIndex = -1;
                }, 300)
            },

            editKlasifikasi(classification){
                console.log('ID : ' + classification.code)
                this.editedIndex = this.classification.indexOf(classification);
                this.editedItem = Object.assign({},classification);
            },

            async fetchStatusBarcode(){
                try{
                    const axios = require('axios')
                    const res = await axios.get('/status_barcode/get_status_barcode')
                    if(res.data == null){
                        console.log('Data kosong')
                    }else{
                        this.statusbarcode = res.data
                        console.log(res,this.classification)
                    }
                }catch(error){
                    alert("Error")
                }
            },

         
        },
    }
</script>