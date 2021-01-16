<template>
    <v-container id='vcontainer'>
        <!--<v-row id='vrow' v-for="satz in messwerte" :key="satz" style="border-top-style: none; border-right-style: none; border-bottom-style: solid; border-left-style: none;">
            <v-col v-for="wert in satz" :key="wert" cols="2" align="center">
                <v-btn block color="#791014" dark v-if="wert == satz[0]" @click="emitData('history', wert)">
                    {{wert}}
                </v-btn>
                <div v-else justify="center">
                    {{wert}}
                </div>
            </v-col>
        </v-row>-->
    </v-container>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'ListRow',
    
    data: () => ({
    }),

    mounted() {
        EventBus.$on('LOADROOMS', (rooms) => {
            console.log('rooms: ' + rooms);
            var fetchedRoomData = []; //TODO: Add roomdata into this array and sort it after the last call of fetch (End of for-loop). Then add the (sorted) data in the "v-container"
            document.getElementById('vcontainer').innerHTML = '';
            for (var i=0; i<rooms.length; i++) {
                var room = rooms[i];
                if (room == null) continue
                var path = 'https://co2.uber.space/statusNow/' + room;
                console.log('fetching data for room ' + room);
                fetch(path).then(response => {
                    if (response.status !== 200) {console.error('Code !== 200:' + response); return}
                    response.clone();
                    response.json().then(data => {
                        var roomData = data[data.length-1];
                        var roomString = '';
                        Object.keys(roomData).forEach(function(key) {
                            if (key != 'ID' && key != 'Raum' && key != 'DatumZeit') {
                                var changed = roomData[key];
                                //if (key == 'Temp') changed += '°C'; //Or change this in ListHeader to show it only once?
                                //if (key == 'co2') changed = roomData[key] + 'ppcm³';
                                if (key == 'h2o') changed = (0 + roomData[key] * 100);
                                roomString += '<div justify="center" class="col col-2">' + changed + '</div>';
                            }
                        });
                        //{"DatumZeit":"Tue, 29 Dec 2020 11:37:55 GMT","ID":102,"Raum":"A102","Temp":23.0,"co2":900.0,"h2o":70.0,"score":60.0}
                        var roomTest = "window.emitData(\'" + room + "\');";
                        document.getElementById('vcontainer').innerHTML += '<div id="vrow" class="row" style="border-top-style: none; border-right-style: none; border-bottom-style: solid; border-left-style: none;"><div align="center" class="col col-2"><button onclick="' + roomTest + '" id="room' + roomData["Raum"] + '" type="button" class="v-btn v-btn--block v-btn--contained theme--dark v-size--default" style="background-color: rgb(121, 16, 20); border-color: rgb(121, 16, 20);"><span class="v-btn__content">' + roomData["Raum"] + '</span></button></div>' + roomString + '</div>';
                        //onclick wird entweder direkt ausgeführt (beim laden) oder gar nicht, wenn statt test() eine function() {} angegeben wird
                        //document.getElementById('room' + room).onclick = test(room);
                    }).catch(error => {
                        console.error('An error occured while parsing the string:' + error);
                    });
                });
            }
        });
    },

    methods: {
    },
}

window.emitData = function(data) {
    EventBus.$emit('LOADSITE', {'site': 'history', 'data': data});
}
</script>