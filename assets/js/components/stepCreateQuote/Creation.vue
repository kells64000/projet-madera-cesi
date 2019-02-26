<template>
    <div style="padding: 2rem 3rem; text-align: left;">

        <div class="columns" style="height: 50%">
            <div class="column">
                <div class="field has-text-centered">
                    <v-select v-model="modulesSelected" multiple :options="modules" label="name">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentSelected === module ? 'tag-selected': ''" @click="currentSelected = module" v-for="module in modulesSelected">
                          {{module.name}}
                        </span>
                    </div>
                </div>

            </div>

            <div class="column">

                <div class="card" v-if="checkCurrentSelected === true">
                    <header class="card-header">
                        <p class="card-header-title">
                            {{currentSelected.name}}
                        </p>
                    </header>
                    <div class="card-content">
                        <div class="content">
                            <div class="field">
                                <label class="label">Hauteur</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentSelected.hauteur">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Largeur</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentSelected.largeur">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-horizontal"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Profondeur</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentSelected.profondeur">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-road"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Prix</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentSelected.price" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-euro-sign"></i>
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>

    </div>
</template>

<script>
    import {validationMixin} from 'vuelidate'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                modules: [
                    {name: 'ModuleTest', hauteur: '1.8', largeur: '2.6', profondeur: '0.8', price: 1500},
                    {name: 'ModuleTest2', hauteur: '1.4', largeur: '2.7', profondeur: '1.4', price: 500.50},
                    {name: 'ModuleTest3', hauteur: '1.1', largeur: '1.7', profondeur: '2.5', price: 200.25},
                ],
                modulesSelected: '',
                currentSelected: '',
            }
        },
        computed: {
            checkCurrentSelected() {
                if(this.modulesSelected === ''){
                    this.currentSelected = ''
                }

                if(this.currentSelected !== ''){
                    return true;
                } else {
                    return false;
                }
            }
        },
        watch: {
            modulesSelected: {
                handler: function () {
                    if (this.modulesSelected !== '') {
                        this.$store.commit("setQuoteModules", this.modulesSelected);
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
                if (this.modulesSelected !== '') {
                    this.$emit('can-continue', {value: true});
                }
            }
        },
        mounted() {
            if (this.modulesSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>