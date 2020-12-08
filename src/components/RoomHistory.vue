<template>
    <v-container>
        Titel:
        <div class="container vertical flat" id="bar_chart">
            <div class="progress-bar" v-for="item in values" :key="item">
                <div class="progress-track">
                    <div class="progress-fill">
                        <span class='span'>{{item}}</span>
                    </div>
                </div>
            </div>
        </div>
    </v-container>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'RoomHistory',

    data: () => ({
        //bar_chart_element: '<div class="progress-bar"><div class="progress-track"><div class="progress-fill"><span>{0}</span></div></div></div>',
        values: [536, 241, 799, 901, 432, 756, 100, 0, 2, 999], //get data from server
        times: [],
        //width: '' + (this.values.length * 45 + 24),
        //position: 0,
        maxValue: 1000,
    }),

    mounted() {
        EventBus.$on('LOADSITE', (params) => {
            if (params['site'] == 'history') {
                //Unschön, da dieser Listener schon in App.vue existiert.
                //Die Daten vielleicht in den EventBus senden und hier empfangen?
                console.log('Test');
                console.warn(this.farbBerechnung(50));
                console.log('After');
                //
                fetch('https://co2.uber.space/statusNow/A102').then(response => {
                    if (response.status !== 200) {console.warn('Code !== 200:' + response); return}
                    response.clone();
                    response.json().then(data => {
                        //[{"DatumZeit":"Wed, 18 Nov 2020 12:33:33 GMT", "ID":1, "Raum":"A102", "Temp":18.0, "co2":700.0, "h2o":55.0, "score":55.0}]
                        this.values = [-1];
                        this.values[0] = data[0]['score'];
                        this.refreshChart();
                    }).catch(error => {
                        console.warn('Error while parsing json:' + error.message);
                    })
                })
            }
        });
    },

    methods: {
        farbBerechnung: (score) => {
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
        },

        refreshChart: () => {
            document.getElementsByClassName('progress-bar').forEach(function(elem) {
                var currentValue = elem.textContent;
                var mV = 1000;
                var percent = (currentValue / mV * 100) + '%';
                var pTop = 100 - ( percent.slice(0, percent.length - 1) ) + "%"
                elem.style.width = percent;
                elem.style.right = pTop;
                var f = this.farbBerechnung(currentValue / mV * 100);
                elem.style.backgroundColor = 'rgb(' + f[0] + ',' + f[1] + ',' + f[2] + ')';
            });
            document.getElementById('bar_chart').style.transform = 'rotate(270deg)';
            document.getElementById('bar_chart').style.width = '45%';
            document.getElementById('bar_chart').style.padding = '64px';
        }
    },
}
</script>