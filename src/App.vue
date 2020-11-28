<template>
    <v-app>
        <v-main>
            <AppHeader v-show="loggedIn"/>
            <Login v-show="page == 'loginy'"/>
            <ListView v-show="page == 'listviewy'"/>
            <RoomHistory v-show="true"/>
        </v-main>
        <AppFooter/>
    </v-app>
</template>

<script>
import EventBus from './EventBus';
import Login from './components/Login';
import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import ListView from './components/ListView';
import RoomHistory from './components/RoomHistory';

export default {
    name: 'App',
    components: {
        AppHeader,
        AppFooter,
        Login,
        ListView,
        RoomHistory,
    },
    
    data:() => ({
        loggedIn: false,
        page: 'login',
    }),
    //Test
    
    mounted() {
        EventBus.$on('LOGINEVENT', (payload) => {
            this.login(payload);
        });
        EventBus.$on('LOGOUTEVENT',() => {
            this.loggedIn = false;
            this.page = 'login';
        });
        EventBus.$on('LOADSITE', (params) => {
            this.page = params['site'];
        });
    },
    
    methods: {
        login(payload){
            console.log(payload);
            if (payload['email'] == 'l.b@gew.de' && payload['password'] == 'Test1234') {
                this.loggedIn = true;
                this.page = 'listview';
            }
        },
    },
};
</script>
