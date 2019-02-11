<template>
    <div class="columns is-vcentered">
        <div class="login column is-4">
            <section class="section">
                <div class="has-text-centered">
                    <img class="login-logo" src="assets/img/logo.png">
                </div>

                <form class="login form">

                    <div class="field">
                        <label class="label">Email</label>
                        <div class="control has-icons-right">
                            <input v-model="email" @focus="is_focus = 'email'" class="input" :class="is_focus === 'email' ? 'is-primary' : ''" id="id_email" type="text" autofocus>
                            <span class="icon is-small is-right">
                                <i class="fa fa-envelope"></i>
                            </span>
                        </div>
                    </div>

                    <div class="field">
                        <label class="label">Mot de passe</label>
                        <div class="control has-icons-right">
                            <input v-model="password" @focus="is_focus = 'pwd'" class="input" :class="is_focus === 'pwd' ? 'is-primary' : ''" id="id_password" type="password">
                            <span class="icon is-small is-right">
                                <i class="fa fa-key"></i>
                            </span>
                        </div>
                    </div>
                    <div class="has-text-centered">
                        <button @click.prevent="authenticate" class="button is-vcentered is-primary is-outlined" type="submit">
                            Connexion
                        </button>
                    </div>

                </form>
            </section>
        </div>

        <vue-particles class="interactive-bg column is-8"
                       color="#ffffff"
                       :particleOpacity="0.7"
                       :particlesNumber="200"
                       shapeType="circle"
                       :particleSize="5"
                       linesColor="#00acd6"
                       :linesWidth="1"
                       :lineLinked="true"
                       :lineOpacity="0.4"
                       :linesDistance="50"
                       :moveSpeed="5"
                       :hoverEffect="true"
                       hoverMode="repulse"
                       :clickEffect="true"
                       clickMode="grab">
        </vue-particles>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Login',
        data() {
            return {
                email: '',
                password: '',
                is_focus: '',
            }
        },
        methods: {
            authenticate() {
                const payload = {
                    email: this.email,
                    password: this.password
                }
                axios.post(this.$store.state.endpoints.obtainJWT, payload)
                    .then((response) => {
                        this.$store.commit('updateToken', response.data.token)
                        // get and set auth user
                        const base = {
                            baseURL: this.$store.state.endpoints.baseUrl,
                            headers: {
                                // Set your Authorization to 'JWT', not Bearer!!!
                                Authorization: `JWT ${this.$store.state.jwt}`,
                                'Content-Type': 'application/json'
                            },
                            xhrFields: {
                                withCredentials: true
                            }
                        }
                        // Even though the authentication returned a user object that can be
                        // decoded, we fetch it again. This way we aren't super dependant on
                        // JWT and can plug in something else.
                        const axiosInstance = axios.create(base)
                        axiosInstance({
                            url: "api/users/",
                            method: "get",
                            params: {}
                        })
                            .then((response) => {
                                this.$store.commit("setAuthUser",
                                    {authUser: response.data, isAuthenticated: true}
                                )
                                this.$router.push({name: 'Dashboard'})
                            })

                    })
                    .catch((error) => {
                        console.log(error);
                        console.debug(error);
                        console.dir(error);
                    })
            }
        }
    }
</script>

<style>
</style>
