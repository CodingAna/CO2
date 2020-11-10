<template>
    <v-container>
        <ListHeader/>
        <ListRow/>
    </v-container>
</template>

<script>
import ListHeader from './ListHeader';
import ListRow from './ListRow';

export default {
    name: 'ListView',
    
    components: {
        ListHeader,
        ListRow,
    },
    
    data: () => ({
    }),
}
</script>