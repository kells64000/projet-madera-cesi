<template>
    <div style="padding: 2rem 3rem; text-align: left;">

        <div class="control mb-1 has-text-centered">
            <label class="radio">
                <input type="radio" name="client" value="new" v-model="clientType" @focus="clientSelected = ''" @click="resetFormNewClient" checked>
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
                            <input class="input" type="text" placeholder="Code Postal" v-model="form.zipCode">
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
                    <input :class="['input', (form_email_error !== '') ? 'is-danger' : '']" type="email" placeholder="Email" v-model="form.email" @keydown="form_email_error = ''">
                    <span class="icon is-small is-left">
                      <i class="fas fa-envelope"></i>
                    </span>
                </p>
                <p v-if="form_email_error !== ''" class="help is-danger">{{form_email_error}}</p>
            </div>

            <div class="has-text-centered">
                <button class="button is-link" type="button" @click="createClient" :disabled="canCreateClient ? false : true">Créer nouveau client</button>
            </div>
        </div>

        <div v-if="clientType === 'madera'">

            <div class="field has-text-centered">
                <v-select v-model="clientSelected" :options="clients" label="full_name" @focus="this.clientSelected = ''">
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
                        <input class="input" type="text" placeholder="Adresse" :value="clientSelected.address.street" readonly>
                        <span class="icon is-small is-left">
                          <i class="fas fa-address-card"></i>
                        </span>
                    </p>
                </div>

                <div class="field is-horizontal">
                    <div class="field-body">
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="number" placeholder="Code Postal" :value="clientSelected.address.zipcode" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-map-marker-alt"></i>
                                </span>
                            </p>
                        </div>
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Ville" :value="clientSelected.address.city" readonly>
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
    import {required, minLength, email, requiredIf} from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                clients: [],
                clientType: 'new',
                clientSelected: '',
                errors: [],
                form: {
                    firstName: '',
                    lastName: '',
                    address: '',
                    zipCode: '',
                    city: '',
                    email: '',
                    phone: '',
                    is_pro: 'Particulier',
                    company: '',
                },
                form_email_error: '',
                canCreateClient: false
            }
        },
        validations: {
            form: {
                firstName: {
                    required
                },
                lastName: {
                    required
                },
                address: {
                    required
                },
                zipCode: {
                    required,
                    min: minLength(5)
                },
                city: {
                    required
                },
                email: {
                    required,
                    email
                },
                phone: {
                    required,
                    min: minLength(10),
                },
                company: {
                    requiredIf: requiredIf((vueInstance) => {
                        return vueInstance.is_pro === 'Professionnel'
                    })
                }
            }
        },
        watch: {
            $v: {
                handler: function (val) {
                    if (this.form_email_error === '') {
                        if (!val.$invalid) {
                            this.canCreateClient = true
                        } else {
                            this.canCreateClient = false
                        }

                    } else {
                        this.canCreateClient = false
                    }
                },
                deep: true
            },
            clientSelected: {
                handler: function () {
                    if (this.clientSelected !== '') {
                        this.$store.commit("setQuoteClient", this.clientSelected);
                        this.$store.commit("setQuoteProjectRef", this.createRefProject(this.quoteProject, this.clientSelected.last_name));
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
            },

        },
        async created() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/clients`)
                this.clients = response.data
            } catch (e) {
                this.errors.push(e)
            }
        },
        computed: {
            quoteProject() {
                return this.$store.getters.getQuoteProject;
            },
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
                    'address': {
                        'street': this.form.address,
                        'zipcode': this.form.zipCode,
                        'city': this.form.city,
                    },
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
                        this.clientSelected = response.data;
                        this.getClients()

                    }).catch(e => {
                        if(this.form.is_pro === true) {
                            this.form.is_pro = 'Professionnel'
                        } else {
                            this.form.is_pro = 'Particulier'
                        }

                        if(e.response.data['email'] !== "") {
                            this.form_email_error = e.response.data['email'];
                        }

                        this.errors.push(e);
                    });
            },
            resetFormNewClient() {
                this.form.is_pro = 'Particulier';
                this.form.firstName = '';
                this.form.lastName = '';
                this.form.address = '';
                this.form.zipCode = '';
                this.form.city = '';
                this.form.email = '';
                this.form.phone = '';
                this.form.company = '';
            },
            createRefProject(project, customer) {
              let prj = project.toString().substr(0, 3);
              let client = customer.toString().substr(0, 3);
              let num = (Math.floor(Math.random() * 10000) + 10000).toString().substring(1);

              prj = prj.toUpperCase();
              client = client.toUpperCase();

              return prj + client + num
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
