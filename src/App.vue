<template>
    <v-app>
        <v-main>
            <AppHeader v-show="loggedIn"/>
            <Login v-show="page == 'login'"/>
            <ListView v-show="page == 'listview'"/>
            <RoomHistory v-show="page == 'history'"/>
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
            const path = 'https://co2.uber.space/login';
			fetch(path, {
				credentials: "omit",
				mode: "cors",
				method: "post",
				headers: { "Content-Type": "application/json"},
				body: payload
			})
			.then(resp => {
				if (resp.status === 200) {
					return resp.json()
				} else {
					console.log("Status: " + resp.login)
					return Promise.reject("server")
				}
			})
			.then(dataJson => {
				if(!dataJson.success) {
					console.log(dataJson); //Rückantwortobjekt ausgeben
				}
				else {
					console.log(dataJson); //Rückantwortobjekt ausgeben
				}				
			})
			.catch(err => {
				if (err === "server") return
				console.log(err);
			})
            if (payload['email'] == 'l.b@gew.de' && payload['password'] == 'Test1234') {
                this.loggedIn = true;
                this.page = 'listview';
            }
        },
    },
};
</script>
