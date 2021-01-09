<template>
    <v-container>
        <v-row>
            <v-col background-color="light-blue" v-for="n in header" :key="n" cols="2">
                <v-card class="pa-2" bold>
                    {{n}}
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'ListHeader',
    
    data: () => ({
        header: ["Raum", "Temperatur (°C)", "CO2 (ppcm³)", "Luftfeuchtigkeit (%)", "Score"],
    }),
}
</script>