<template>
    <div class="container">
        <div class="columns is-vcentered vh-50">
            <div class="column is-12">
                <section class="section">
                    <div class="has-text-right">
                        <button class="button has-background-grey-lighter" @click.prevent="logout()">
                            <i class="fas fa-sign-out-alt"></i>
                        </button>
                    </div>
                </section>
                <section class="section">
                    <div class="has-text-centered">
                        <img class="login-logo" src="assets/img/logo.png">
                    </div>
                    <div class="has-text-centered subtitle">
                        Bonjour {{userAuth.first_name}} {{userAuth.last_name}}
                    </div>
                </section>
            </div>
        </div>
        <div class="columns is-vcentered">
            <div class="column is-3 is-offset-2">
                <div class="has-text-centered">
                    <div class="card card-dashboard" @click.prevent="create()">
                        <div class="card-content has-background-grey-light">
                            <i class="far fa-plus-square fa-5x"></i>
                        </div>
                        <footer class="card-footer">
                            <p class="card-footer-item">
                                Créer devis
                            </p>
                        </footer>
                    </div>
                </div>
            </div>
            <div class="column is-3 is-offset-2">
                <div class="has-text-centered">
                    <div class="card card-dashboard" @click.prevent="consult()">
                        <div class="card-content has-background-grey-light">
                            <i class="fas fa-search fa-5x"></i>
                        </div>
                        <footer class="card-footer">
                            <p class="card-footer-item">
                                Consulter devis
                            </p>
                        </footer>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Dashboard",
        computed : {
            userAuth(){
                return this.$store.getters.getUser;
            }
        },
        methods: {
            logout() {
                this.$router.push({name: 'Home'})
            },
            create() {
                this.$router.push({name: 'CreateQuote'})
            },
            consult() {
                this.$router.push({name: 'ViewQuote'})
            }
        },
        created: function () {
            this.$store.commit('setAuthUser');
        }
    }
</script>

<style>
</style>