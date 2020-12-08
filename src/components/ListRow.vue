<template>
    <v-container>
        <v-row v-for="satz in messwerte" :key="satz" style="border-top-style: none; border-right-style: none; border-bottom-style: solid; border-left-style: none;">
            <v-col v-for="wert in satz" :key="wert" cols="2" align="center">
                <v-btn block color="#791014" dark v-if="wert == satz[0]" @click="emitData('history', '{{wert}}')"><!-- Das funktioniert so nicht, der String ist dann "{{wert}}" und nicht der Wert der Variable -->
                    {{wert}}
                </v-btn>
                <div v-else justify="center">
                    {{wert}}
                </div>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'ListRow',
    
    data: () => ({
        messwerte: [
            ["A100", "89,99", "54", "16°C", "100", "Rot"],
            ["A101", "14","54", "16°C", "12", "Grün"],
            ["A100", "89,98", "54", "16°C", "100", "Rot"],
            ["A101", "20","54", "16°C", "12", "Grün"],
            ["A100", "89,97", "54", "16°C", "100", "Rot"],
            ["A101", "16","54", "16°C", "12", "Grün"],
            ["A100", "86,99", "54", "16°C", "100", "Rot"],
            ["A101", "17","54", "16°C", "12", "Grün"],
            ["A100", "85,99", "54", "16°C", "100", "Rot"],
            ["A101", "18","54", "16°C", "12", "Grün"],
        ]
    }),

    methods: {
        emitData(page, data) {
            EventBus.$emit('LOADSITE', {'site': page, 'data': data});
        },
    },
}
</script>