<template>
<div>
    <vue-draggable-resizable :parent="true" :grid=[20,20] :x="x" :y="y" :h="h" :w="w" @dragging="onDrag" @resizing="onResize">
        <p>You cannot move me or resize me outside my parent.</p>
    </vue-draggable-resizable>

</div>
                <!--<vue-draggable-resizable :parent="true" :max-width="290" :max-height="290" :grid="[10,20]">-->
                    <!--<p>Component costrained in parent with <b>maxWidth</b> and <b>maxHeight</b> equal to 290.</p>-->
                <!--</vue-draggable-resizable>-->

</template>

<script>

    export default {
        name: "CreateQuote",
        data: function () {
            return {
                width: 0,
                height: 0,
                x: 0,
                y: 0
            }
        },
        methods: {
            onResize: function (x, y, width, height) {
                this.x = x
                this.y = y
                this.width = width
                this.height = height
            },
            onDrag: function (x, y) {
                this.x = x
                this.y = y
            }
        }
    }
</script>

<style>

</style>