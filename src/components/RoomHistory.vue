<template>
    <v-container>
        <v-row v-for='value in values' :key='value'>
            <!--<div style='margin: 0px; padding: 0px; height: {{100 - (value * 100 / values.length)}};'>-->
            {{value}}
            <!--</div>-->
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'RoomHistory',
    
    data: () => ({
        values: [25, 50, 75, 100, 40, 120],
    }),
}
</script>
