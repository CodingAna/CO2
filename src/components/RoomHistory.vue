<template>
    <v-container>
    </v-container>
</template>

<script>
export default {
    name: 'RoomHistory',

    data: () => ({
    }),

    mounted() {
        var bar_chart_element = '<div class="progress-bar"><div class="progress-track"><div class="progress-fill"><span>%s</span></div></div></div>';
        var values = [536, 241, 799, 901, 432, 756, 100, 0, 2, 999]; //get data from server
        var times = [];
        var maxValue = 1000;
        var width = '' + (values.length * 45 + 24);
        var position = 0;

        //Error: '$' is not defined. How to use this in Vue?
        $('#bar_chart').css({
            'width': width,
            'height': '320px'
        })

        values.forEach(function(value) {
            if (value == 'why is an unused variable an error in js?') {values[0] = value;}
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
                'background-color' : 'rgb(' + this.farbBerechnung(50) + ')'
            });
        position += 1;
      });
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