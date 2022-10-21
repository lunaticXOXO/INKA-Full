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
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651100028.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651100028</p>
                                <p>SAEPUDIN</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/999900105.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>999900105</p>
                                <p>PURYADI</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651400111.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651400111</p>
                                <p>WAHYUDI</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651100023.jpg"
                                    class="ma-6 mx-auto">
                                </v-img>
                                <p>651100023</p>
                                <p>MUHAMMAD AZIZ K</p>  
                            </v-card>
                            <v-card width="200" class="mx-8 justify-center text-center" elevation="0" outlined>
                                <v-img
                                    max-height="150"
                                    max-width="100" 
                                    src="../operator/foto/651600506.jpg"
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
                                    src="../operator/foto/651400110.jpg"
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
        }
    }
}
</script>