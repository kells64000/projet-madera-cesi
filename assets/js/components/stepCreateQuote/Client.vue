<template>
    <div style="padding: 2rem 3rem; text-align: left;">

        <div class="control mb-1 has-text-centered">
            <label class="radio">
                <input type="radio" name="client" value="new" v-model="clientType" @focus="clientSelected = ''" checked>
                Nouveau client
            </label>

            <label class="radio">
                <input type="radio" name="client" value="madera" v-model="clientType">
                Client Madera
            </label>
        </div>

        <div v-if="clientType === 'new'">

            <div class="control has-text-centered mb-1">
                <div class="select">
                    <select  v-model="form.is_pro">
                        <option disabled>{{this.form.is_pro}}</option>
                        <option v-if="this.form.is_pro !== 'Particulier'">Particulier</option>
                        <option v-if="this.form.is_pro !== 'Professionnel'">Professionnel</option>
                    </select>
                </div>
            </div>

            <div class="field is-horizontal">
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input class="input" type="text" placeholder="Prénom" v-model="form.firstName">
                            <span class="icon is-small is-left">
                              <i class="fas fa-user"></i>
                            </span>
                        </p>
                    </div>
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input class="input" type="text" placeholder="Nom" v-model="form.lastName">
                            <span class="icon is-small is-left">
                              <i class="fas fa-user"></i>
                            </span>
                        </p>
                    </div>
                </div>
            </div>

            <div v-if="form.is_pro === 'Professionnel'" class="field">
                <p class="control is-expanded has-icons-left">
                    <input class="input" type="text" placeholder="Nom de l'entreprise" v-model="form.company">
                    <span class="icon is-small is-left">
                      <i class="fas fa-building"></i>
                    </span>
                </p>
            </div>

            <div class="field">
                <p class="control is-expanded has-icons-left">
                    <input class="input" type="text" placeholder="Adresse" v-model="form.address">
                    <span class="icon is-small is-left">
                      <i class="fas fa-address-card"></i>
                    </span>
                </p>
            </div>

            <div class="field is-horizontal">
                <div class="field-body">
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input class="input" type="number" placeholder="Code Postal" v-model="form.zipCode">
                            <span class="icon is-small is-left">
                              <i class="fas fa-map-marker-alt"></i>
                            </span>
                        </p>
                    </div>
                    <div class="field">
                        <p class="control is-expanded has-icons-left">
                            <input class="input" type="text" placeholder="Ville" v-model="form.city">
                            <span class="icon is-small is-left">
                              <i class="fas fa-city"></i>
                            </span>
                        </p>
                    </div>
                </div>
            </div>

            <div class="field">
              <p class="control is-expanded has-icons-left">
                <input class="input" type="text" placeholder="Téléphone" v-model="form.phone">
                <span class="icon is-small is-left">
                  <i class="fas fa-phone"></i>
                </span>
              </p>
            </div>

            <div class="field">
                <p class="control is-expanded has-icons-left">
                    <input class="input" type="email" placeholder="Email" v-model="form.email">
                    <span class="icon is-small is-left">
                      <i class="fas fa-envelope"></i>
                    </span>
                </p>
            </div>

            <div class="has-text-centered">
                <button class="button is-link" type="button" @click="createClient">Créer nouveau client</button>
            </div>
        </div>

        <div v-if="clientType === 'madera'">

            <div class="field has-text-centered">
                <v-select v-model="clientSelected" :options="clients" label="first_name" @focus="this.clientSelected = ''">
                    <template slot="option" slot-scope="option">
                        {{option.first_name}} {{option.last_name}}
                    </template>
                </v-select>
            </div>

            <div v-if="clientSelected === ''" style="height: 50%"></div>

            <div v-if="clientSelected !== ''">
                <div class="field is-horizontal">
                    <div class="field-body">
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Prénom" :value="clientSelected.first_name" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-user"></i>
                                </span>
                            </p>
                        </div>
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Nom" :value="clientSelected.last_name" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-user"></i>
                                </span>
                            </p>
                        </div>
                    </div>
                </div>

                <div v-if="clientSelected.is_pro === true" class="field">
                    <p class="control is-expanded has-icons-left">
                        <input class="input" type="text" placeholder="Nom de l'entreprise" :value="clientSelected.company" readonly>
                        <span class="icon is-small is-left">
                      <i class="fas fa-building"></i>
                    </span>
                    </p>
                </div>

                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input class="input" type="text" placeholder="Adresse" :value="clientSelected.address" readonly>
                        <span class="icon is-small is-left">
                          <i class="fas fa-address-card"></i>
                        </span>
                    </p>
                </div>

                <div class="field is-horizontal">
                    <div class="field-body">
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="number" placeholder="Code Postal" :value="clientSelected.zipCode" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-map-marker-alt"></i>
                                </span>
                            </p>
                        </div>
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Ville" :value="clientSelected.city" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-city"></i>
                                </span>
                            </p>
                        </div>
                    </div>
                </div>

                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input class="input" type="text" placeholder="Téléphone" :value="clientSelected.phone" readonly>
                        <span class="icon is-small is-left">
                          <i class="fas fa-phone"></i>
                        </span>
                    </p>
                </div>

                <div class="field">
                    <p class="control is-expanded has-icons-left">
                        <input class="input" type="email" placeholder="Email" :value="clientSelected.email" readonly>
                        <span class="icon is-small is-left">
                          <i class="fas fa-envelope"></i>
                        </span>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {validationMixin} from 'vuelidate'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                clients: [],
                clientType: 'new',
                clientSelected: '',
                form: {
                    firstName: '',
                    lastName: '',
                    address: '',
                    postalCode: '',
                    city: '',
                    email: '',
                    phone: '',
                    is_pro: 'Particulier',
                    company: '',
                }
            }
        },
        watch: {
            clientSelected: {
                handler: function () {
                    if (this.clientSelected !== '') {
                        this.$store.commit("setQuoteClient", this.clientSelected);
                        this.$emit('can-continue', {value: true});
                    } else {
                        this.$emit('can-continue', {value: false});
                        setTimeout(() => {
                            this.$emit('change-next', {nextBtnValue: true});
                        }, 3000)
                    }
                },
                deep: true
            },

            clickedNext() {
                if (this.clientSelected !== '') {
                    this.$emit('can-continue', {value: true});
                }
            }
        },
        async created() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/clients`)
                this.clients = response.data
            } catch (e) {
                this.errors.push(e)
            }
        },
        methods: {
            getClients() {
                axios.get(`http://127.0.0.1:8000/api/clients`)
                .then(response => {
                    this.clients = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
            },
            createClient() {

                if(this.form.is_pro === 'Professionnel') {
                    this.form.is_pro = true
                } else {
                    this.form.is_pro = false
                }

                let clientCreate = {
                    'first_name': this.form.firstName,
                    'last_name': this.form.lastName,
                    'street': this.form.address,
                    'zipCode': this.form.postalCode,
                    'city': this.form.city,
                    'email': this.form.email,
                    'phone': this.form.phone,
                    'is_pro': this.form.is_pro,
                    'company': this.form.company
                };

                axios.post('http://127.0.0.1:8000/api/clients/',
                    clientCreate, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then((response) => {
                        this.clientType = 'madera';
                        this.clientSelected = response.data.first_name + response.data.last_name;
                        //this.is_pro = response.data.is_pro;
                        this.getClients()

                    }).catch(e => {
                        this.errors.push(e);
                    });
            },
        },
        mounted() {
            if (this.clientSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>