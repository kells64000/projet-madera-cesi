<template>
    <div class="card" style="margin: 3rem">
        <header class="card-header">
            <p class="card-header-title">
                Devis
            </p>
        </header>
        <div class="card-content">
            <div class="content">
                Liste des modules et composant prix par ligne
            </div>
        </div>
        <footer class="card-footer justify-content-end">
            prix du devis en €
        </footer>
    </div>
</template>

<script>
    export default {
        props: ['currentStep'],

        methods: {
          canContinue() {
              this.$emit('can-continue', {value: true});
          }
        },

        mounted() {
           this.$emit('can-continue', {value: true})
        }
    }
</script>