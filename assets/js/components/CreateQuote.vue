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
            <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
        </div>
   </div>
</template>

<script>
     import axios from 'axios'
     import HorizontalStepper from 'vue-stepper';
     import Projet from './stepCreateQuote/Projet.vue';
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
                        icon: 'assignment',
                        name: 'Projet',
                        title: 'Projet',
                        subtitle: 'Nom du projet',
                        component: Projet,
                        completed: false
                    },
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
                        title: 'Récapitulatif',
                        subtitle: 'Liste des modules',
                        component: Recapitulatif,
                        completed: false
                    }
                ],
                isLoading: false,
                isFullPage: true,
                pathPdf: ''
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
            createPDF() {

                let PDFcontext = {
                    'date': this.quoteDate,
                    'name': this.quoteProject,
                    'ref': this.quoteProjectRef,
                    'price': this.quotePrice,
                    'client': this.quoteClient,
                    'salesperson': this.quoteSalesperson,
                    'modules': this.quoteModules
                };

                axios.post(this.$store.state.endpoints.baseUrl + 'api/quotes/pdf/',
                    PDFcontext, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then((response) => {
                        this.pathPdf = response.data.filename

                    }).catch(e => {

                        console.log(e.response);

                        this.errors.push(e);
                    });
            },
            createQuote() {

                let QuoteCreate = {
                    'name': this.quoteProject,
                    'reference': this.quoteProjectRef,
                    'price': this.quotePrice,
                    'state': 'Brouillon',
                    'attachment': this.pathPdf,
                    'client': {
                        'id': this.quoteClient.id,
                        'full_name': this.quoteClient.full_name,
                        'phone': this.quoteClient.phone,
                        'email': this.quoteClient.email,
                        'street': this.quoteClient.street,
                        'city': this.quoteClient.city,
                        'zipcode': this.quoteClient.zipcode,
                    },
                    'salesperson': {
                        'id': this.quoteSalesperson.id,
                        'full_name': this.quoteSalesperson.full_name,
                    },
                };

                axios.post(this.$store.state.endpoints.baseUrl + 'api/quotes/',
                    QuoteCreate, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then((response) => {
                        this.$router.push({name: 'ViewQuote'});

                    }).catch(e => {

                        console.log(e.response);

                        this.errors.push(e);
                    });
            },
            // Executed when @stepper-finished event is triggered
            alert() {
                this.isLoading = true;
                this.createPDF();
                this.createQuote();
                this.isLoading = false;
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
            quoteSalesperson(){
                return this.$store.getters.getUser;
            },
            quoteModules() {
                return this.$store.getters.getQuoteModules;
            },
            quotePrice() {
                return this.$store.getters.getQuotePrice;
            },
            quoteGamme() {
                return this.$store.getters.getQuoteGamme;
            },
        }
    }
</script>

<style>
</style>
