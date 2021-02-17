<template>
    <v-container>
        <button id='back' style='border-style: solid; border-color: #000000; border-radius: 10px; text-align: center;'><v-icon>mdi-chevron-left</v-icon> Zurück</button>
        <p id='title'></p>
        <div class="container vertical flat" id="bar_chart" style="background-color: #EBEBEB; border-radius: 10px; max-width: 300px;">
            <!--<div id='pb' class="progress-bar" v-for="item in values" :key="item">
                <div class="progress-track">
                    <div class="progress-fill">
                        <span class='span'>{{item}}</span>
                    </div>
                </div>
            </div>-->
        </div>
    </v-container>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'RoomHistory',

    data: () => ({
        maxValue: 1000,
    }),

    mounted() {
        document.getElementById('back').onclick = function() {
            EventBus.$emit('LOADSITE', {'site': 'listview', 'data': null});
            document.getElementById("bar_chart").innerHTML = '';
        }
        EventBus.$on('ROOMDATA', (params) => {
            document.getElementById('title').innerHTML = params[0]['Raum'];
            var values = [];
            params.forEach(function(value) {
                values.push(value['score']);
            })
            this.refreshChart(values);
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

        refreshChart: (values) => {
            values.forEach(function(value) {
                var tag_progress_bar = document.createElement('div');
                tag_progress_bar.className = 'progress-bar';

                var tag_progress_track = document.createElement('div');
                tag_progress_track.className = 'progess-track';
                
                var tag_progress_fill = document.createElement('div');
                tag_progress_fill.className = 'progress-fill';
                
                var tag_span = document.createElement('span');
                tag_span.className = 'span';
                tag_span.innerHTML = value;
                
                tag_progress_fill.appendChild(tag_span);
                tag_progress_track.appendChild(tag_progress_fill);
                tag_progress_bar.appendChild(tag_progress_track);
                document.getElementById("bar_chart").appendChild(tag_progress_bar);
            })

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
            
            var position = 0;
            document.getElementsByClassName('progress-bar').forEach(function(elem) {
                var currentValue = values[position];
                var mV = 1000;
                var percent = (currentValue / mV * 100 * 5) + '%';
                //var pTop = (700 - percent.slice(0, percent.length - 1)) + "%"
                elem.style.width = percent;
                var f = fB(currentValue);
                elem.style.backgroundColor = 'rgb(' + f[0] + ',' + f[1] + ',' + f[2] + ')';
                position += 1;
            });
            document.getElementById('bar_chart').style.transform = 'rotate(270deg)';
            document.getElementById('bar_chart').style.width = '50%';
            document.getElementById('bar_chart').style.padding = '64px';
        }
    },
}
</script>