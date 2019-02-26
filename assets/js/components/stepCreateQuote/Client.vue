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
                            <input class="input" type="number" placeholder="Code Postal" v-model="form.postalCode">
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
                <button class="button is-link" type="submit">Créer nouveau client</button>
            </div>
        </div>

        <div v-if="clientType === 'madera'">

            <div class="field has-text-centered">
                <v-select v-model="clientSelected" :options="clients" label="fullName" @focus="this.clientSelected = ''">
                    <template slot="option" slot-scope="option">
                        {{option.firstName}} {{option.lastName}}
                    </template>
                </v-select>
            </div>

            <div v-if="clientSelected === ''" style="height: 50%"></div>

            <div v-if="clientSelected !== ''">
                <div class="field is-horizontal">
                    <div class="field-body">
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Prénom" :value="clientSelected.firstName" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-user"></i>
                                </span>
                            </p>
                        </div>
                        <div class="field">
                            <p class="control is-expanded has-icons-left">
                                <input class="input" type="text" placeholder="Nom" :value="clientSelected.lastName" readonly>
                                <span class="icon is-small is-left">
                                  <i class="fas fa-user"></i>
                                </span>
                            </p>
                        </div>
                    </div>
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
                                <input class="input" type="number" placeholder="Code Postal" :value="clientSelected.postalCode" readonly>
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
    import {validationMixin} from 'vuelidate'
    import {required, email} from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                clients: [
                    {firstName: 'Client1', lastName: 'Test1', fullName: 'Client_1', address: '11 rue du bois', postalCode: 33000, city: 'Bordeaux', phone: '0102030405', email: 'client1@madera.com'},
                    {firstName: 'Client2', lastName: 'Test2', fullName: 'Client_2', address: '12 rue du platane', postalCode: 64000, city: 'Pau', phone: '0504030201', email: 'client2@madera.com'},
                    {firstName: 'Client3', lastName: 'Test3', fullName: 'Client_3', address: '13 rue du chêne', postalCode: 75000, city: 'Paris', phone: '0405060201', email: 'client3@madera.com'},
                    {firstName: 'Client4', lastName: 'Test4', fullName: 'Client_4', address: '14 rue du pastaga', postalCode: 13013, city: 'Marseille', phone: '0301020304', email: 'client4@madera.com'},
                    {firstName: 'Client5', lastName: 'Test5', fullName: 'Client_5', address: '15 rue du sentier', postalCode: 64510, city: 'Bordes', phone: '0908070605', email: 'client5@madera.com'},
                ],
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
                }
            }
        },
        validations: {
            form: {
                email: {
                    required,
                    email
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
        mounted() {
            if (this.clientSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>