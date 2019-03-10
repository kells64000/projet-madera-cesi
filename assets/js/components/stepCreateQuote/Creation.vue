<template>
    <div id="content-modules" style="padding-left: 3rem; padding-right: 3rem; text-align: left; height: 90%; position: relative">

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

                <!-- Forme -->
                <div class="field">
                    <div class="control">
                        <div>
                            <label for="selectForme">Forme :</label>
                        </div>

                        <div id="selectForme" class="select">
                            <select v-model="formeSelected">
                                <option :value="forme.name" v-for="forme in formes">{{forme.name}}</option>
                            </select>
                        </div>
                    </div>
                </div>

                <figure class="mt-2" v-show="formeSelected === forme.name"
                        v-for="forme in formes">
                    <img :src="forme.img">
                </figure>


                <!-- Mur ext carré -->
                <div class="field" v-if="formeSelected === 'Carré'">
                    <div>
                        <label for="selectModuleWallExtCarre">Murs Extérieur :</label>
                    </div>
                    <v-select id="selectModuleWallExtCarre" v-model="modulesWallExtCarreSelected" multiple :options="modules.ext.carre" label="name" :disabled="modulesWallExtCarreSelected === '' ? false : true">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesWallExtCarreSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesWallExtCarreSelected">
                            {{module.name}}
                        </span>
                    </div>
                </div>
                
                <!-- Mur ext rectangle -->
                <div class="field" v-if="formeSelected === 'Rectangle'">
                    <div>
                        <label for="selectModuleWallExtRect">Murs Extérieur :</label>
                    </div>
                    <v-select id="selectModuleWallExtRect" v-model="modulesWallExtRectSelected" multiple :options="modules.ext.rectangle" label="name" :disabled="modulesWallExtRectSelected === '' ? false : true">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesWallExtRectSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesWallExtRectSelected">
                            {{module.name}}
                        </span>
                    </div>
                </div>

                <!-- Mur ext perso -->
                <div class="field" v-if="formeSelected === 'Personaliser'">
                    <div>
                        <label for="selectModuleWallExt">Murs Extérieur :</label>
                    </div>
                    <v-select id="selectModuleWallExt" v-model="modulesWallExtSelected" multiple :options="modules.ext.rectangle" label="name" :disabled="modulesWallExtSelected === '' ? false : true">
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

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleWallAngle">Murs Angle :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleWallAngle" v-model="modulesAngleWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesAngleWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesAngleWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleWallInternal">Cloisons intérieures :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleWallInternal" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesInternalWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleFloorSlab">Plancher sur dalle :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleFloorSlab" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesInternalWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleFloorCarrier">Plancher porteur :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleFloorCarrier" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesInternalWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleStructuralFarms">Fermes de charpente :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleStructuralFarms" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesInternalWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

                <!--<div class="field">-->
                    <!--<div>-->
                        <!--<label for="selectModuleRoofCover">Couverture :</label>-->
                    <!--</div>-->
                    <!--<v-select id="selectModuleRoofCover" v-model="modulesInternalWallSelected" multiple :options="modules" label="name">-->
                        <!--<template slot="option" slot-scope="option">-->
                            <!--{{option.name}}-->
                        <!--</template>-->
                    <!--</v-select>-->
                <!--</div>-->

                <!--<div class="box" v-if="modulesInternalWallSelected !== ''">-->
                    <!--<div class="tags">-->
                        <!--<span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"-->
                              <!--@click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesInternalWallSelected">-->
                          <!--{{module.name}}-->
                        <!--</span>-->
                    <!--</div>-->
                <!--</div>-->

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
                                        <input class="input" type="text" :value="currentGammeSelected.isolation"
                                               readonly>
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-igloo"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Couverture</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" :value="currentGammeSelected.couverture"
                                               readonly>
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
                                <div class="field">
                                    <label class="label">Hauteur</label>
                                    <p class="control has-icons-left">
                                        <input v-if="formeSelected === 'Carré'" class="input" type="text" v-model="currentModuleSelected.hauteur" :placeholder="currentModuleSelected.hauteur" @change="carreHauteur(currentModuleSelected.hauteur)">
                                        <input v-if="formeSelected === 'Rectangle'" class="input" type="text" v-model="currentModuleSelected.hauteur" :placeholder="currentModuleSelected.hauteur" @change="rectangleHauteur(currentModuleSelected.hauteur)">
                                        <input v-if="formeSelected === 'Personaliser'" class="input" type="text" v-model="currentModuleSelected.hauteur" :placeholder="currentModuleSelected.hauteur">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Longueur</label>
                                    <p class="control has-icons-left">
                                        <input v-if="formeSelected === 'Carré'" class="input" type="text" v-model="currentModuleSelected.longueur" :placeholder="currentModuleSelected.longueur" @change="carreLongueur(currentModuleSelected.longueur)">
                                        <input v-if="formeSelected === 'Rectangle'" class="input" type="text" :value="currentModuleSelected.longueur" :placeholder="currentModuleSelected.longueur"  @change="rectangleLongueur(currentModuleSelected.longueur, $event)">
                                        <input v-if="formeSelected === 'Personaliser'" class="input" type="text" :value="currentModuleSelected.longueur" :placeholder="currentModuleSelected.longueur">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-horizontal"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Unite d'usage</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text"
                                               :placeholder="currentModuleSelected.unite_usage" readonly>
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-balance-scale"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Prix</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text" :placeholder="currentModuleSelected.price"
                                               readonly>
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
        </div>
    </div>
</template>

<script>
    export default {
        props: ['clickedNext', 'currentStep'],
        data() {
            return {
                gammes: [
                    {name: 'Excellence', finitionExterieure: 'Crépi', isolation: 'Laine de verre', couverture: 'Ardoise', img: '/static/img/house/gammes/excellence.jpeg'},
                    {name: 'Luxe', finitionExterieure: 'Crépi', isolation: 'Laine de roche', couverture: 'Zinc', img: '/static/img/house/gammes/luxe.jpeg'},
                    {name: 'Naturelle', finitionExterieure: 'Bois', isolation: 'Ouate de cellulose', couverture: 'Brande', img: '/static/img/house/gammes/naturelle.jpeg'},
                ],
                formes: [
                    {name: 'Carré', img: '/static/img/house/forms/Maison_carree.jpg'},
                    {name: 'Rectangle', img: '/static/img/house/forms/Maison_Rectangle.jpg'},
                    {name: 'Personaliser', img: ''},

                ],
                modules: {
                    ext: {
                        carre: [
                            {name: 'Mur-nord', hauteur: '2.5', longueur: '2.0', unite_usage: 'm²', price: 1500},
                            {name: 'Mur_sud', hauteur: '2.5', longueur: '2.0', unite_usage: 'm linéaire', price: 500.50},
                            {name: 'Mur_ouest', hauteur: '2.5', longueur: '2.0', unite_usage: 'unite', price: 200.25},
                            {name: 'Mur_est', hauteur: '2.5', longueur: '2.0', unite_usage: 'unite', price: 200.25},
                        ],
                        rectangle: [
                            {name: 'Mur-nord', hauteur: '2.0', longueur: '1.5', unite_usage: 'm²', price: 1500},
                            {name: 'Mur_sud', hauteur: '2.0', longueur: '1.5', unite_usage: 'm linéaire', price: 500.50},
                            {name: 'Mur_ouest', hauteur: '2.0', longueur: '1.0', unite_usage: 'unite', price: 200.25},
                            {name: 'Mur_est', hauteur: '2.0', longueur: '1.0', unite_usage: 'unite', price: 200.25},
                        ],
                        perso: [
                            {name: 'Mur-nord', hauteur: '2.0', longueur: '1.5', unite_usage: 'm²', price: 1500},
                            {name: 'Mur_sud', hauteur: '2.0', longueur: '1.5', unite_usage: 'm linéaire', price: 500.50},
                            {name: 'Mur_ouest', hauteur: '2.0', longueur: '1.0', unite_usage: 'unite', price: 200.25},
                            {name: 'Mur_est', hauteur: '2.0', longueur: '1.0', unite_usage: 'unite', price: 200.25},
                        ],
                    },
                },
                gammeSelected: '',
                formeSelected: '',
                modulesWallExtCarreSelected: '',
                modulesWallExtRectSelected: '',
                modulesWallExtSelected: '',

                // modulesInternalWallSelected: '',
                // modulesAngleWallSelected: '',
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

                if(this.modulesWallExtCarreSelected === '' && this.modulesWallExtRectSelected === '' && this.modulesWallExtSelected === ''){
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
            carreLongueur(longueur) {
                this.modulesWallExtCarreSelected.forEach(function (module) {
                    module.longueur = longueur;
                });
            },
            carreHauteur(hauteur) {
                this.modulesWallExtCarreSelected.forEach(function (module) {
                    module.hauteur = hauteur;
                });
            },

            rectangleLongueur(oldLongueur, longueur) {

                this.modulesWallExtRectSelected.forEach(function (module) {
                    if(module.longueur === oldLongueur) {
                        module.longueur = longueur.target.value;
                    }
                });
            },
            rectangleHauteur(hauteur) {
                this.modulesWallExtRectSelected.forEach(function (module) {
                    module.hauteur = hauteur;
                });
            },

        },
        watch: {
            formeSelected: {
                handler: function () {
                    if(this.formeSelected === 'Carré') {
                        let modulesCarre = [];
                        this.modules.ext.carre.forEach( function (module) {
                            modulesCarre.push(module)
                        });
                        this.currentModuleSelected = '';
                        this.modulesWallExtRectSelected = '';
                        this.modulesWallExtSelected = '';
                        this.modulesWallExtCarreSelected = modulesCarre;
                    }

                    if(this.formeSelected === 'Rectangle') {
                        let modulesRect = [];
                        this.modules.ext.rectangle.forEach( function (module) {
                            modulesRect.push(module)
                        });
                        this.currentModuleSelected = '';
                        this.modulesWallExtCarreSelected = '';
                        this.modulesWallExtSelected = '';
                        this.modulesWallExtRectSelected = modulesRect;
                    }

                    if(this.formeSelected === 'Personaliser') {
                        let modulesExt = [];
                        this.modules.ext.perso.forEach( function (module) {
                            modulesExt.push(module)
                        });
                        this.currentModuleSelected = '';
                        this.modulesWallExtCarreSelected = '';
                        this.modulesWallExtRectSelected = '';
                        this.modulesWallExtSelected = modulesExt;
                    }
                },
            },

            modulesWallExtCarreSelected: {
               handler: function () {
                    if(!this.modulesSelected.includes(this.modulesWallExtCarreSelected)) {
                        this.modulesSelected = this.modulesWallExtCarreSelected;
                    }
                }
            },
            modulesWallExtRectSelected: {
               handler: function () {
                    if(!this.modulesSelected.includes(this.modulesWallExtRectSelected)) {
                        this.modulesSelected = this.modulesWallExtRectSelected;
                    }
                }
            },

            // modulesInternalWallSelected: {
            //     handler: function () {
            //          if(!this.modulesSelected.includes(this.modulesInternalWallSelected)) {
            //             this.modulesSelected = this.modulesInternalWallSelected;
            //         }
            //     }
            // },
            // modulesAngleWallSelected: {
            //     handler: function () {
            //         if (!this.modulesSelected.includes(this.modulesAngleWallSelected)) {
            //             this.modulesSelected = this.modulesAngleWallSelected;
            //         }
            //     }
            // },
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
            if (this.modulesSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>