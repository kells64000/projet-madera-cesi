<template>
        <div class="columns">
            <div class="column is-2">

            </div>
            <div class="column is-8">
                <VueDragResize :isActive="true"
                               :parentLimitation="true"
                               :w="200" :h="200"
                               v-on:resizing="resize" v-on:dragging="resize">
                    <h3>Hello World!</h3>
                    <p>{{ top }} х {{ left }} </p>
                    <p>{{ width }} х {{ height }}</p>
                </VueDragResize>

            </div>
            <div class="column is-2">

            </div>
        </div>
</template>

<script>
    import VueDragResize from 'vue-drag-resize';

    export default {
        name: "CreateQuote",
        components: {
            VueDragResize
        },

        data() {
            return {
                width: 0,
                height: 0,
                top: 0,
                left: 0
            }
        },

        methods: {
            resize(newRect) {
                this.width = newRect.width;
                this.height = newRect.height;
                this.top = newRect.top;
                this.left = newRect.left;
            }
        }
    }
</script>

<style>

</style>