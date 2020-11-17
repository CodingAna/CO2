<template>
    <v-container>
        <v-row v-for='value in values' :key='value'>
            <!--<div style='margin: 0px; padding: 0px; height: {{100 - (value * 100 / values.length)}};'>-->
            {{value}}
            <!--</div>-->
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: 'RoomHistory',

    data: () => ({
        bar_chart_element = '<div class="progress-bar"><div class="progress-track"><div class="progress-fill"><span>%s</span></div></div></div>',
        values = [536, 241, 799, 901, 432, 756, 100, 0, 2, 999], //get data from server
        times = [],
        maxValue = 1000,
        width = '' + (values.length * 45 + 24),
        position = 0,
    }),

    mounted() {

        $('#bar_chart').css({
            'width': width,
            'height': '320px'
        })

        values.forEach(function(value) {
            $('#bar_chart').append(bar_chart_element.replace("%s", [times[position]])); //not working
            position += 1;
        });

        position = 0;
        $('.vertical .progress-fill span').each(function() {
            var percent = (values[position] / maxValue * 100) + '%';
            var pTop = 100 - ( percent.slice(0, percent.length - 1) ) + "%"
            $(this).parent().css({
                'height' : percent,
                'top' : pTop,
                'background-color' : 'rgb(' + farbBerechnung(50) + ')'
            });
        position += 1;
      });
    },

    methods: {
        farbBerechnung(score) {
            r = 0;
            g = 0;
            b = 0;
            if (score > 100) {
                r = 50 * 2.55;
                b = 100 * 2.55;
            } else {
                r = (-0.01 * (score * score) + (2 * score)) * 2.55;
                g = (-0.01 * (score * score) + 100) * 2.55;
            }
            return [r, g, b];
      }
    },
}
</script>