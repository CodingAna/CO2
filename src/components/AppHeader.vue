<template>
    <v-app-bar>
        <v-toolbar-title>
            CO2-Messwert
        </v-toolbar-title>
        <v-btn @click="logoutclick" style="margin-left: auto;" color="#791014" dark>
            Abmelden
        </v-btn>
    </v-app-bar>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'AppHeader',

    data: () => ({    
    }),
    
    methods:  {
        logoutclick() {
            EventBus.$emit('LOGOUTEVENT');
        },
    },
}
</script>