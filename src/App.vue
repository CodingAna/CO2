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
            if (this.page == 'history') {
                //Use params['data'] to get the selected room.
                console.log(params['data']);
                var path = 'https://co2.uber.space/statusNow/A102' //+ params['data']
                console.log('Path:' + path);
                //Change the following room to a var    ____    to get the selected room.
                fetch(path).then(response => {
                    if (response.status !== 200) {console.error('Code !== 200:' + response); return}
                    response.clone();
                    response.json().then(data => {
                        console.log('Data before emit:' + data);
                        EventBus.$emit('ROOMDATA', data);
                    }).catch(error => {
                        console.error('An error occured while parsing the string:' + error);
                    })
                })
            }
        });
    },
    
    methods: {
        login(payload){
            console.log(JSON.stringify(payload));
            console.log(payload);
            const path = 'https://co2.uber.space/login';
			fetch(path, {
				credentials: "omit",
				mode: "cors",
				method: "post",
				headers: { "Content-Type": "application/json"},
				body: JSON.stringify(payload)
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
				
				if (dataJson.login) {
                    console.log(dataJson.login); //Rückantwortobjekt ausgeben
                    this.loggedIn = true;
                    this.page = 'listview';
                    console.log('side load');
                }			
                else {
                    console.log('fehler')
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
