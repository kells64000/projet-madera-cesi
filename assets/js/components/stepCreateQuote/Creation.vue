<template>
    <div style="padding-left: 3rem; padding-right: 3rem; text-align: left; height: 100%">

        <div class="columns" style="height: 50%">
            <div class="column">

                <div class="columns align-center">

                    <div class="column-is-6 h-200 d-flex align-center">

                        <div class="field">
                            <div class="control">
                                <div>
                                    <label for="selectGamme">Gammes :</label>
                                </div>

                                <div id="selectGamme" class="select">
                                    <select v-model="gammeSelected">
                                        <option :value="gamme.name" v-for="gamme in gammes">{{gamme.name}}</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                    </div>

                    <div class="column-is-6 h-200">

                         <figure class="image is-128x128 mt-2" v-show="gammeSelected === gamme.name" @click="currentGammeSelected = gamme, currentModuleSelected = ''" v-for="gamme in gammes">
                            <img :src="gamme.img" >
                        </figure>

                    </div>

                </div>

                <div class="columns align-center">

                    <div class="column-is-6 h-200 d-flex align-center">

                        <div class="field">
                            <div class="control">
                                <div>
                                    <label for="selectForme">Formes :</label>
                                </div>

                                <div id="selectForme" class="select">
                                    <select v-model="formeSelected">
                                        <option :value="forme.name" v-for="forme in formes">{{forme.name}}</option>
                                    </select>
                                </div>
                            </div>
                        </div>

                    </div>

                    <div class="column-is-6 h-200">

                        <figure class="image is-256x256 mt-2" v-show="formeSelected === forme.name"
                                v-for="forme in formes">
                            <img :src="forme.img">
                        </figure>

                    </div>

                </div>

                <div class="field">
                    <div>
                        <label for="selectModuleWallExternal">Murs Extérieur :</label>
                    </div>
                    <v-select id="selectModuleWallExternal" v-model="modulesExternalWallSelected" multiple :options="modules" label="name">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesExternalWallSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesExternalWallSelected">
                          {{module.name}}
                        </span>
                    </div>
                </div>

                <div class="field">
                    <div>
                        <label for="selectModuleWallInternal">Murs Intérieur :</label>
                    </div>
                    <v-select id="selectModuleWallInternal" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesInternalWallSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">
                          {{module.name}}
                        </span>
                    </div>
                </div>

                <div class="field">
                    <div>
                        <label for="selectModuleWallAngle">Murs Angle :</label>
                    </div>
                    <v-select id="selectModuleWallAngle" v-model="modulesAngleWallSelected" multiple :options="modules" label="name">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesAngleWallSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesAngleWallSelected">
                          {{module.name}}
                        </span>
                    </div>
                </div>

            </div>


            <div class="column">

                <div class="card" style="position: fixed;" v-if="checkModuleSelected === true || checkGammeSelected === true">
                    <header class="card-header">
                        <p class="card-header-title" v-if="currentGammeSelected !== ''">
                            Gamme : {{currentGammeSelected.name}}
                        </p>
                        <p class="card-header-title" v-if="currentModuleSelected !== ''">
                            Module : {{currentModuleSelected.name}}
                        </p>
                    </header>
                    <div class="card-content">
                        <div class="content" v-if="currentGammeSelected !== ''">

                            <div class="field">
                                <label class="label">Finition Exterieure</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :value="currentGammeSelected.finitionExterieure" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-brush"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Isolation</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :value="currentGammeSelected.isolation" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-igloo"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Couverture</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :value="currentGammeSelected.couverture" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-home"></i>
                                    </span>
                                </p>
                            </div>
                        </div>

                        <div class="content" v-if="currentModuleSelected !== ''">

                            <div class="field">
                                <label class="label">Nom</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" v-model="currentModuleSelected.name" :placeholder="currentModuleSelected.name">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-user-edit"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Hauteur</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentModuleSelected.hauteur">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Longueur</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentModuleSelected.longueur">
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-horizontal"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Unite d'usage</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentModuleSelected.unite_usage" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-balance-scale"></i>
                                    </span>
                                </p>
                            </div>
                            <div class="field">
                                <label class="label">Prix</label>
                                <p class="control has-icons-left">
                                    <input class="input" type="text" :placeholder="currentModuleSelected.price" readonly>
                                    <span class="icon is-small is-left">
                                      <i class="fas fa-euro-sign"></i>
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="clear:both;"></div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['clickedNext', 'currentStep'],
        data() {
            return {
                gammes: [
                    {name: 'Execellence', finitionExterieure: 'Crépi', isolation: 'Laine de verre', couverture: 'Ardoise', img: 'https://picsum.photos/128/128?341'},
                    {name: 'Luxe', finitionExterieure: 'Crépi', isolation: 'Laine de roche', couverture: 'Zinc', img: 'https://picsum.photos/128/128?147'},
                    {name: 'Naturelle', finitionExterieure: 'Bois', isolation: 'Ouate de cellulose', couverture: 'Brande', img: 'https://picsum.photos/128/128?417'},
                ],
                formes: [
                    {name: 'Carré', img: '/assets/img/house/forms/Maison_carree.jpg'},
                    {name: 'Rectangle', img: '/assets/img/house/forms/Maison_Rectangle.jpg'},
                    {name: 'U', img: '/assets/img/house/forms/Maison_U.jpg'},
                    {name: 'L', img: '/assets/img/house/forms/Maison_L.jpg'},
                ],
                modules: [
                    {name: 'Mur-nord', hauteur: '1.8', longueur: '2.6', unite_usage: 'm²', price: 1500},
                    {name: 'Mur_sud', hauteur: '1.4', longueur: '2.7', unite_usage: 'm linéaire', price: 500.50},
                    {name: 'Mur_ouest', hauteur: '1.1', longueur: '1.7', unite_usage: 'unite', price: 200.25},
                    {name: 'Mur_est', hauteur: '1.1', longueur: '1.7', unite_usage: 'unite', price: 200.25},
                ],
                gammeSelected: '',
                formeSelected: '',
                modulesExternalWallSelected: '',
                modulesInternalWallSelected: '',
                modulesAngleWallSelected: '',
                modulesSelected : [],
                currentGammeSelected: '',
                currentModuleSelected: '',
            }
        },
        computed: {
            checkGammeSelected() {

                if(this.gammeSelected === ''){
                    this.currentGammeSelected = ''
                }

                if(this.currentGammeSelected !== ''){
                    return true;
                } else {
                    return false;
                }
            },
            checkModuleSelected() {

                if(this.modulesExternalWallSelected === '' && this.modulesInternalWallSelected === '' && this.modulesAngleWallSelected === ''){
                    this.currentModuleSelected = ''
                }

                if(this.currentModuleSelected !== ''){
                    return true;
                } else {
                    return false;
                }
            },
        },
        methods: {

        },
        watch: {
            modulesExternalWallSelected: {
                handler: function () {
                    if(!this.modulesSelected.includes(this.modulesExternalWallSelected)) {
                        this.modulesSelected = this.modulesExternalWallSelected;
                    }
                }
            },
            modulesInternalWallSelected: {
                handler: function () {
                     if(!this.modulesSelected.includes(this.modulesInternalWallSelected)) {
                        this.modulesSelected = this.modulesInternalWallSelected;
                    }
                }
            },
            modulesAngleWallSelected: {
                handler: function () {
                    if (!this.modulesSelected.includes(this.modulesAngleWallSelected)) {
                        this.modulesSelected = this.modulesAngleWallSelected;
                    }
                }
            },
            modulesSelected: {
                handler: function () {
                    if (this.modulesSelected !== '') {
                        console.log(this.modulesSelected);
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