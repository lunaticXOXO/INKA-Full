<template>
    <v-app>
        <v-card class="mx-auto text-center mt-6 mb-6" max-width="1000" elevation="0">
            <h1>Operator Hadir</h1>
        </v-card>
        <v-card class="mx-auto" max-width="1250" elevation="0">
            <v-container fluid>
                <v-row dense>
                    <v-col>
                        <div class="d-flex">
                            <v-container class="white">
                        <v-row>
                            <v-col
                            v-for=" index in listOperator"
                            :key="index"
                            cols="8"
                            sm="auto"
                            >
                            <span class="mx-auto"><b>{{index.nama}}</b></span>
                            
                                <v-img
                                    height="200"
                                    width="150" 
                                    :src="require(`@/views/operator/foto/${index.link}`)" 
                                >
                                </v-img>
                                <span class="mx-auto"><b>{{index.uuid}}</b></span>
                            </v-col>
                        </v-row>
                    </v-container>
                            <!--
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/saepudin.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651100028</p>
                                <p>SAEPUDIN</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/puryadi.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>999900105</p>
                                <p>PURYADI</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/budicahyono.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651400111</p>
                                <p>WAHYUDI</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/aziz.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651100023</p>
                                <p>MUHAMMAD AZIZ K</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/jemyherdian.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651600506</p>
                                <p>JEMY HERDIAN NUR</p>  
                            </v-card>
                        </div>
                        <div class="d-flex mt-10">
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/kusantok.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651400110</p>
                                <p>KUSANTOK</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651600010.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651600010</p>
                                <p>ERWIN DWI ANDRIYANTO</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651600437.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651600437</p>
                                <p>DANY WAHYU S</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651600475.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651600475</p>
                                <p>BAGAS LIDAKDHO</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651500190.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651500190</p>
                                <p>PUPUT ABDUL SAPUTRA</p>  
                            </v-card>
                            -->
                        </div>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </v-app>
</template>

<script>
export default {
    data() {
        return {
            items: [
                { title: '651100028', name: 'SAEPUDIN', flex: 2 },
                { title: '999900105', name: 'PURYADI', flex: 2 },
                { title: '651400111', name: 'WAHYUDI', flex: 2 },
                { title: '651100023', name: 'MUHAMMAD AZIZ K', flex: 2 },
                { title: '651600506', name: 'JEMY HERDIAN NUR', flex: 2 },
                { title: '651400110', name: 'KUSANTOK', flex: 2},
                { title: '651600010', name: 'ERWIN DWI ANDRIYANTO', flex: 2},
                { title: '651600437', name: 'DANY WAHYU S', flex: 2},
                { title: '651600475', name: 'BAGAS LIDAKDHO', flex: 2},
                { title: '651500190', name: 'PUPUT ABDUL SAPUTRA', flex: 2},
            ],
            listOperator : undefined
        }
    },

    mounted(){
        this.getLinkOperator()
    },
    methods : {
        async getLinkOperator(){
            try{
                const axios = require('axios')
                const res = await axios.get('/operator/get_operator_hadir')
                if (res.data == null){
                    console.log("data kosong")
                }else{
                    this.listOperator = res.data
                    console.log("data terisi")
                    console.log(res,this.listOperator)
                }

            }catch(error){
                console.log(error)
            }
        }
    },
}
</script>