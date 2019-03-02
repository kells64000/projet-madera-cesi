<template>
   <div class="columns">
        <div class="column is-12">
            <section class="section">
                <div class="has-text-left">
                    <a class="button has-background-grey-lighter" @click="returnDashboard">
                        <i class="fas fa-home"></i>
                    </a>
                </div>
                <div class="has-text-centered">
                    <h1 class="title is-1">Création de devis</h1>
                </div>
            </section>

            <section class="section">
                <div class="container">
                    <div class="columns">
                        <div class="column is-8 is-offset-2">
                            <horizontal-stepper :steps="quoteSteps" @completed-step="completeStep"
                                                @active-step="isStepActive" @stepper-finished="alert"
                            >
                            </horizontal-stepper>
                        </div>
                    </div>
                </div>
            </section>
        </div>
   </div>
</template>

<script>
     import HorizontalStepper from 'vue-stepper';
     import Client from './stepCreateQuote/Client.vue';
     import Creation from './stepCreateQuote/Creation.vue';
     import Recapitulatif from './stepCreateQuote/Recapitulatif.vue';

    export default {
        name: "CreateQuote",
        components: {
            HorizontalStepper
        },
        data: function () {
            return {
                quoteSteps: [
                    {
                        icon: 'person',
                        name: 'client',
                        title: 'Client',
                        subtitle: 'Affectation du client',
                        component: Client,
                        completed: false
                    },
                    {
                        icon: 'view_quilt',
                        name: 'création',
                        title: 'Création',
                        subtitle: 'Choix des modules',
                        component: Creation,
                        completed: false

                    },
                    {
                        icon: 'shopping_cart',
                        name: 'récapitulatif',
                        title: 'Récapitulitif',
                        subtitle: 'Liste des modules',
                        component: Recapitulatif,
                        completed: false
                    }
                ]
            }
        },
        methods: {
            returnDashboard() {
                this.$router.push({name: 'Dashboard'})
            },
            // Executed when @completed-step event is triggered
            completeStep(payload) {
                this.quoteSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        step.completed = true;
                    }
                })
            },
            // Executed when @active-step event is triggered
            isStepActive(payload) {
                this.quoteSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        if(step.completed === true) {
                            step.completed = false;
                        }
                    }
                })
            },
            // Executed when @stepper-finished event is triggered
            alert(payload) {
                alert('Création du devis en bdd et génération du PDF =)')
            }
        }
    }
</script>

<style>
</style>