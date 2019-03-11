<template>
    <div id="content-modules" style="padding-left: 3rem; padding-right: 3rem; text-align: left; height: 100%; position: relative">

        <div class="columns">
            <div class="column">

                <div class="columns align-center">

                    <div class="column-is-6 h-200 d-flex align-center">
                        <!-- Gamme -->
                        <div class="field">
                            <div class="control">
                                <div>
                                    <label for="selectGamme">Gamme :</label>
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

                <div v-if="gammeSelected !== ''">
                    <figure class="mt-2 mb-1">
                        <img :src="'/static/img/house/forms/Maison_perso.jpg'">
                    </figure>
                    <!-- Mur ext -->
                    <div class="field">
                        <div>
                            <label for="selectModuleWallExt">Murs Extérieurs :</label>
                        </div>
                        <v-select id="selectModuleWallExt" v-model="modulesWallExtSelected" multiple :options="modules.ext.perso" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>

                    <div class="box" v-if="modulesWallExtSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesWallExtSelected">
                                {{module.name}}
                            </span>
                        </div>
                    </div>
                    <!-- mur int -->
                    <div class="field">
                        <div>
                            <label for="selectModuleWallInt">Cloisons intérieures :</label>
                        </div>
                        <v-select id="selectModuleWallInt" v-model="modulesWallIntSelected" multiple :options="modules.int" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>
    
                    <div class="box" v-if="modulesWallIntSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesWallIntSelected">
                              {{module.name}}
                            </span>
                        </div>
                    </div>
                    <!-- plaancher dalle -->
                    <div class="field">
                        <div>
                            <label for="selectModuleFloorSlab">Plancher sur dalle :</label>
                        </div>
                        <v-select id="selectModuleFloorSlab" v-model="modulesFloorSlabSelected" multiple :options="modules.plancher.dalle" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>

                    <div class="box" v-if="modulesFloorSlabSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesFloorSlabSelected">
                              {{module.name}}
                            </span>
                        </div>
                    </div>
                    <!-- plancher porteur -->
                    <div class="field">
                        <div>
                            <label for="selectModuleFloorStructural">Plancher porteur :</label>
                        </div>
                        <v-select id="selectModuleFloorStructural" v-model="modulesFloorStructuralSelected" multiple :options="modules.plancher.porteur" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>

                    <div class="box" v-if="modulesFloorStructuralSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesFloorStructuralSelected">
                              {{module.name}}
                            </span>
                        </div>
                    </div>
                    <!-- charpente -->
                    <div class="field">
                        <div>
                            <label for="selectModuleRoofCarpenters">Fermes de charpente :</label>
                        </div>
                        <v-select id="selectModuleRoofCarpenters" v-model="modulesRoofCarpentersSelected" multiple :options="modules.toit.charpente" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>

                    <div class="box" v-if="modulesRoofCarpentersSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesRoofCarpentersSelected">
                              {{module.name}}
                            </span>
                        </div>
                    </div>
                    <!-- couverture -->
                    <div class="field">
                        <div>
                            <label for="selectModuleRoofCover">Couverture :</label>
                        </div>
                        <v-select id="selectModuleRoofCover" v-model="modulesRoofCoverSelected" multiple :options="modules.toit.couverture" label="name">
                            <template slot="option" slot-scope="option">
                                {{option.name}}
                            </template>
                        </v-select>
                    </div>

                    <div class="box" v-if="modulesRoofCoverSelected !== ''">
                        <div class="tags">
                            <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                                  @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesRoofCoverSelected">
                              {{module.name}}
                            </span>
                        </div>
                    </div>
                    
                </div>

            </div>

            <div class="column">
                <affix class="sidebar-menu" relative-element-selector="#content-modules">
                    <div class="card" v-if="checkModuleSelected === true || checkGammeSelected === true">
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
                                        <input class="input" type="text"
                                               :value="currentGammeSelected.finitionExterieure" readonly>
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
                                        <input class="input" type="text" v-model="currentModuleSelected.name"
                                               :placeholder="currentModuleSelected.name">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-user-edit"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field" v-if="currentGammeSelected.family !== 'CHA'" >
                                    <label class="label">Hauteur</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" v-model="currentModuleSelected.height" :placeholder="currentModuleSelected.height" @change="extHauteur(currentModuleSelected.height)">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field" v-if="currentGammeSelected.family === 'CHA'" >
                                    <label class="label">Hauteur</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" v-model="currentModuleSelected.unit" :placeholder="currentModuleSelected.unit" @change="extHauteur(currentModuleSelected.unit)">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Longueur</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" :value="currentModuleSelected.length" :placeholder="currentModuleSelected.length" @change="prixModule(currentModuleSelected, currentModuleSelected.length, $event)">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-horizontal"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Unite d'usage</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" :placeholder="currentModuleSelected.unit" readonly>
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-balance-scale"></i>
                                    </span>
                                    </p>
                                </div>

                                <div v-if="currentModuleSelected.family === 'EXT' || currentModuleSelected.family === 'INT'">

                                    <div class="field">
                                        <div class="control">
                                            <div>
                                                <label for="selectAngle" class="label">Angle</label>
                                            </div>

                                            <div id="selectAngle" class="select">
                                                <select v-model="currentModuleSelected.angle">
                                                    <option value="">Aucun</option>
                                                    <option>Entrant</option>
                                                    <option>Sortant</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="field"
                                         v-if="currentModuleSelected.angle !== '' && currentModuleSelected.angle !== 'Aucun'">
                                        <label class="label">Degré de l'angle</label>
                                        <p class="control has-icons-left">
                                            <input class="input" type="text" v-model="currentModuleSelected.angle_type"
                                                   :placeholder="currentModuleSelected.angle_type">
                                            <span class="icon is-small is-left">
                                              <i class="fas fa-drafting-compass"></i>
                                            </span>
                                        </p>

                                        <label class="label">Longueur 2</label>
                                        <p class="control has-icons-left">
                                            <input class="input" type="text" v-model="currentModuleSelected.length2"
                                                   :placeholder="currentModuleSelected.length2">
                                            <span class="icon is-small is-left">
                                              <i class="fas fa-ruler-horizontal"></i>
                                            </span>
                                        </p>
                                    </div>

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
                </affix>
            </div>
        </div>
        <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        props: ['clickedNext', 'currentStep'],
        data() {
            return {
                gammes: [
                    {name: 'Excellence', finitionExterieure: 'Crépi', isolation: 'Laine de verre', couverture: 'Ardoise', img: '/static/img/house/gammes/excellence.jpeg'},
                    {name: 'Luxe', finitionExterieure: 'Crépi', isolation: 'Laine de roche', couverture: 'Zinc', img: '/static/img/house/gammes/luxe.jpeg'},
                    {name: 'Naturelle', finitionExterieure: 'Bois', isolation: 'Ouate de cellulose', couverture: 'Brande', img: '/static/img/house/gammes/naturelle.jpeg'},
                ],
                modules: {
                    ext: [],
                    int: [],
                    plancher: {
                        dalle: [],
                        porteur: [],
                    },
                    toit: {
                        charpente: [],
                        couverture: [],
                    },
                },
                modulesWallExtSelected: '',
                modulesWallIntSelected: '',
                modulesFloorSlabSelected: '',
                modulesFloorStructuralSelected: '',
                modulesRoofCarpentersSelected: '',
                modulesRoofCoverSelected: '',
                gammeSelected: '',
                currentGammeSelected: '',
                modulesSelected : [],
                currentModuleSelected: '',
                isLoading: false,
                isFullPage: true
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

                if(this.modulesWallExtSelected === '' && this.modulesWallIntSelected === '' && this.modulesFloorSlabSelected === '' && this.modulesFloorStructuralSelected === '' && this.modulesRoofCarpentersSelected === '' && this.modulesRoofCoverSelected === ''){
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
            extHauteur(height) {
                this.modulesWallExtSelected.forEach(function (module) {
                    module.height = height;
                });
            },
            prixModule(module, oldLength, length) {
                let lenghtDiff = length.target.value - oldLength;
                module.price = lenghtDiff * module.price + module.price;
            }
        },
        watch: {
            modulesWallExtSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesWallIntSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesFloorSlabSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesFloorStructuralSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesRoofCarpentersSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesRoofCoverSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesSelected: {
                handler: function () {
                    if (this.modulesSelected !== '') {
                        // console.log(this.modulesSelected);
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
            this.isLoading = true;

            if (this.modulesSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }

            // axios.get(this.$store.state.endpoints.baseUrl + `api/gammes`)
            //     .then(response => {
            //         this.modules.ext.perso = response.data
            //     })
            //     .catch(e => {
            //         this.errors.push(e)
            //     });

            // axios.get(this.$store.state.endpoints.baseUrl + `api/modules/family/ext`)
            //     .then(response => {
            //         this.modules.ext.perso = response.data
            //     })
            //     .catch(e => {
            //         this.errors.push(e)
            //     });

            // axios.get(this.$store.state.endpoints.baseUrl + `api/modules/family/int`)
            //     .then(response => {
            //         this.modules.int = response.data
            //     })
            //     .catch(e => {
            //         this.errors.push(e)
            //     });

            this.isLoading = false;
        }
    }
</script>