<template>
    <v-container>
        Titel:
        <div class="container vertical flat" id="bar_chart" v-for="item in values" :key="item">
            <div class="progress-bar">
                <div class="progress-track">
                    <div class="progress-fill">
                        <span>{{item}}</span>
                    </div>
                </div>
            </div>
        </div>
    </v-container>
</template>

<script>
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
        /*var bar_chart_element = '<div class="progress-bar"><div class="progress-track"><div class="progress-fill"><span>%s</span></div></div></div>';
        var values = [536, 241, 799, 901, 432, 756, 100, 0, 2, 999]; //get data from server
        var times = [];
        var maxValue = 1000;
        var width = '' + (this.values.length * 45 + 24);
        var position = 0;*/

        //Die Historie konnte nicht beendet werden, da dieser Bereich (mounted() {}) nie ausgeführt wurde.
        //Prinzipiell sollte das Programm laufen (Code wurde aus History.html kopiert)

        /*
        document.getElementById('bar_chart').css({
            'width': this.width,
            'height': '320px'
        })

        console.log('Ich war hier');
        console.log(this.values);

        this.values.forEach(function(value) {
            console.log("Value:" + value);
            if (value == 'why is an unused variable an error in js?') {this.values[0] = value;}
            document.getElementById('bar_chart').append(this.bar_chart_element.replace("%s", [this.times[this.position]])); //not working
            this.position += 1;
        });

        */

       //This isnt working
        var position = 0;
        document.getElementsByClassName('.vertical .progress-fill span').each(function(elem) {
            var percent = (this.values[position] / this.maxValue * 100) + '%';
            var pTop = 100 - ( percent.slice(0, percent.length - 1) ) + "%"
            elem.parent().css({
                'height' : percent,
                'top' : pTop,
                'background-color' : 'rgb(' + this.farbBerechnung(50) + ')'
            });
            position += 1;
        });
        //
    },

    methods: {
        farbBerechnung(score) {
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
    },
}
</script>