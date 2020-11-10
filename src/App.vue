<template>
    <v-app>
        <v-main>
            <Appheader v-show="loggedIn"/>
            <Login v-show="page == 'login'"/>
            <Listview v-show="page == 'listview'"/>
        </v-main>
        <Appfooter/>
    </v-app>
</template>

<script>
import EventBus from './EventBus';
import Login from './components/Login';
import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import ListView from './components/ListView';

export default {
    name: 'App',
  
    components: {
        Appheader,
        Appfooter,
        Login,
        Listview,
    },
    
    data:() => ({
        loggedIn: false,
        page: 'login',
    }),
    
    mounted() {
        EventBus.$on('LOGINEVENT', (payload) => {
            this.login(payload);
        });
        EventBus.$on('LOGOUTEVENT',() => {
            this.loggedIn = false;
            this.page = 'login';
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
        
        logout() {
            this.loggedIn = false;
            this.page = 'login';
        }
    },
};
</script>
