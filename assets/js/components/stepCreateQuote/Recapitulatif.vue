<template>
    <div class="card" style="margin: 3rem">
        <header class="card-header">
            <div class="card-header-title d-flex flex-column align-start">
                <div>Devis MADERA</div>
                <div>Projet : {{quoteProject}}</div>
                <div>Ref : {{quoteProjectRef}}</div>
                <div>Date : {{quoteDate | formatDate}}</div>
            </div>
            <div class="card-header-title d-flex flex-column align-end">
                    <div>{{quoteClient.full_name}}</div>
                    <div>{{quoteClient.address['street']}}</div>
                    <div>{{quoteClient.address['zipcode']}} {{quoteClient.address['city']}}</div>
                    <div>{{quoteClient.email}}</div>
                    <div>{{quoteClient.phone}}</div>
            </div>
        </header>
        <div class="card-content">
            <div class="content">

                <div class="subtitle is-size-6 d-flex justify-content-space-beetween" v-for="module in quoteModules">
                    {{module.name}}
                    <span>
                        {{module.price}}€
                    </span>
                </div>
            </div>
        </div>
        <footer class="card-footer justify-content-end pr-1-5">
            €
        </footer>
    </div>
</template>

<script>
    export default {
        props: ['clickedNext', 'currentStep'],
        data() {
            return {
                nom: 1
            }
        },
        computed: {
            quoteDate() {
                return this.$store.getters.getQuoteDate;
            },
            quoteProject() {
                return this.$store.getters.getQuoteProject;
            },
            quoteProjectRef() {
                return this.$store.getters.getQuoteProjectRef;
            },
            quoteClient() {
                return this.$store.getters.getQuoteClient;
            },
            quoteModules() {
                return this.$store.getters.getQuoteModules;
            },
        },
        watch: {
            nom: {
                handler: function () {
                    if (this.nom !== 0) {
                        this.$emit('can-continue', {value: true});
                    } else {
                        this.$emit('can-continue', {value: true});
                        setTimeout(() => {
                            this.$emit('change-next', {nextBtnValue: true});
                        }, 3000)
                    }
                },
                deep: true
            },

            clickedNext() {
                if (this.nom !== 0) {
                    this.$emit('can-continue', {value: true});
                }
            }
        },
        mounted() {
            if (this.nom === 0) {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>
