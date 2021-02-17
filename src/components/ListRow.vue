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
        function fB(score) {
            var r = 0;
            var g = 0;
            var b = 0;
            if (score > 100) {
                r = 50 * 2.55;
                b = 100 * 2.55;
            } else {
                r = (-0.01 * (score * score) + (2 * score)) * 2.55;
                g = (-0.01 * (score * score) + 100) * 2.55;
            }
            return [r, g, b];
        }

        EventBus.$on('LOADROOMS', (roomNames) => {
            document.getElementById('vcontainer').innerHTML = '';
            var fetchedRoomData = [];
            for (var i=0; i<roomNames.length; i++) {
                var path = 'https://co2.uber.space/statusNow/' + roomNames[i];
                fetch(path).then(response => {
                    if (response.status !== 200) {console.error('Code !== 200:' + response); return}
                    response.clone();
                    response.json().then(data => {
                        fetchedRoomData.push(data[data.length-1]);
                        EventBus.$emit('SORTFETCHED', fetchedRoomData, roomNames);
                    }).catch(error => {
                        console.error('An error occured while parsing the string:' + error);
                    });
                });
            }
        });
        EventBus.$on('SORTFETCHED', (fetchedRoomData, roomNames) => {
            if (fetchedRoomData.length < roomNames.length) return;
            for (var i=fetchedRoomData.length; i>1; i--) {
                for (var j=0; j<i-1; j++) {
                    var splitted = fetchedRoomData[j]['Raum'].replace(/^(A)/, '') + 0;
                    var nextSplitted = fetchedRoomData[j+1]['Raum'].replace(/^(A)/, '') + 0;
                    if (splitted > nextSplitted) {
                        var save = fetchedRoomData[j];
                        fetchedRoomData[j] = fetchedRoomData[j+1];
                        fetchedRoomData[j+1] = save;
                    }
                }
            }
            //Array is sorted by rooms ascending
            for (var k=0; k<fetchedRoomData.length; k++) {
                var roomString = '';
                Object.keys(fetchedRoomData[k]).forEach(function(key) {
                    if (key != 'ID' && key != 'Raum' && key != 'DatumZeit') {
                        var changed = fetchedRoomData[k][key];
                        //if (key == 'Temp') changed += '°C'; //Or change this in ListHeader to show it only once?
                        //if (key == 'co2') changed = fetchedRoomData[k][key] + 'ppcm³';
                        if (key == 'h2o') changed = (0 + fetchedRoomData[k][key] * 100);
                        roomString += '<div justify="center" class="col col-2">' + changed + '</div>';
                    }
                });
                var f = fB(fetchedRoomData[k]['score']);
                roomString += '<div justify="center" class="col col-2">' + '<div style="background-color: rgb(' + f[0] + ',' + f[1] + ',' + f[2] + '); width: 90px; height: 45px; border-radius: 10px;"></div>' + '</div>';
                //Example data object: {"DatumZeit":"Tue, 29 Dec 2020 11:37:55 GMT","ID":102,"Raum":"A102","Temp":23.0,"co2":900.0,"h2o":70.0,"score":60.0}
                var roomTest = "window.emitData(\'" + roomNames[k] + "\');";
                document.getElementById('vcontainer').innerHTML += '<div id="vrow" class="row" style="border-top-style: none; border-right-style: none; border-bottom-style: solid; border-left-style: none;"><div align="center" class="col col-2"><button onclick="' + roomTest + '" id="room' + fetchedRoomData[k]["Raum"] + '" type="button" class="v-btn v-btn--block v-btn--contained theme--dark v-size--default" style="background-color: rgb(121, 16, 20); border-color: rgb(121, 16, 20);"><span class="v-btn__content">' + fetchedRoomData[k]["Raum"] + '</span></button></div>' + roomString + '</div>';
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