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
                <div class="field" v-if="gammeSelected !== ''">
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
                        <label for="selectModuleWallExtSquare">Murs Extérieur :</label>
                    </div>
                    <v-select id="selectModuleWallExtSquare" v-model="modulesWallExtSquareSelected" multiple :options="modules.ext.carre" label="name" :disabled="modulesWallExtSquareSelected === '' ? false : true">
                        <template slot="option" slot-scope="option">
                            {{option.name}}
                        </template>
                    </v-select>
                </div>

                <div class="box" v-if="modulesWallExtSquareSelected !== ''">
                    <div class="tags">
                        <span class="tag is-link is-small" :class="currentModuleSelected === module ? 'tag-selected': ''"
                              @click="currentModuleSelected = module, currentGammeSelected = ''" v-for="module in modulesWallExtSquareSelected">
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
                <div class="field" v-if="formeSelected === 'Personnaliser'">
                    <div>
                        <label for="selectModuleWallExt">Murs Extérieur :</label>
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
                
                <div v-if="formeSelected !== ''">
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
                                        <input v-if="formeSelected === 'Carré'" class="input" type="text" v-model="currentModuleSelected.height" :placeholder="currentModuleSelected.height" @change="carreHauteur(currentModuleSelected.height)">
                                        <input v-if="formeSelected === 'Rectangle'" class="input" type="text" v-model="currentModuleSelected.height" :placeholder="currentModuleSelected.height" @change="rectangleHauteur(currentModuleSelected.height)">
                                        <input v-if="formeSelected === 'Personnaliser'" class="input" type="text" v-model="currentModuleSelected.height" :placeholder="currentModuleSelected.height" @change="extHauteur(currentModuleSelected.height)">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-vertical"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Longueur</label>
                                    <p class="control has-icons-left">
                                        <input v-if="formeSelected === 'Carré'" class="input" type="text" :value="currentModuleSelected.length" :placeholder="currentModuleSelected.length" @change="prixModuleCarre(currentModuleSelected, currentModuleSelected.length, $event); carreLongueur($event)">
                                        <input v-if="formeSelected === 'Rectangle'" class="input" type="text" :value="currentModuleSelected.length" :placeholder="currentModuleSelected.length" @change="prixModuleRect(currentModuleSelected, currentModuleSelected.length, $event); rectangleLongueur(currentModuleSelected.length, $event)">
                                        <input v-if="formeSelected === 'Personnaliser'" class="input" type="text" :value="currentModuleSelected.length" :placeholder="currentModuleSelected.length" @change="prixModule(currentModuleSelected, currentModuleSelected.length, $event)">
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-ruler-horizontal"></i>
                                    </span>
                                    </p>
                                </div>
                                <div class="field">
                                    <label class="label">Unite d'usage</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="text"
                                               :placeholder="currentModuleSelected.unit" readonly>
                                        <span class="icon is-small is-left">
                                      <i class="fas fa-balance-scale"></i>
                                    </span>
                                    </p>
                                </div>

                                <div v-if="currentModuleSelected.family === 'ext' || currentModuleSelected.family === 'int'">

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
                formes: [
                    {name: 'Carré', img: '/static/img/house/forms/Maison_carree.jpg'},
                    {name: 'Rectangle', img: '/static/img/house/forms/Maison_rectangle.jpg'},
                    {name: 'Personnaliser', img: '/static/img/house/forms/Maison_perso.jpg'},
                ],
                modules: {
                    ext: {
                        carre: [
                            {name: 'Mur-nord', family: "ext", height: '2.5', length: '1.0', unit: 'm²', angle: '', angle_type: '', length2: '', price: 1000},
                            {name: 'Mur_sud', family: "ext", height: '2.5', length: '1.0', unit: 'm linéaire', angle: '', angle_type: '', length2: '', price: 1000},
                            {name: 'Mur_ouest', family: "ext", height: '2.5', length: '1.0', unit: 'unite', angle: '', angle_type: '', length2: '', price: 1000},
                            {name: 'Mur_est', family: "ext", height: '2.5', length: '1.0', unit: 'unite', angle: '', angle_type: '', length2: '', price: 1000},
                        ],
                        rectangle: [
                            {name: 'Mur-nord', family: "ext", height: '2.0', length: '1.5', unit: 'm²', angle: '', angle_type: '', length2: '', price: 1500},
                            {name: 'Mur_sud', family: "ext", height: '2.0', length: '1.5', unit: 'm linéaire', angle: '', angle_type: '', length2: '', price: 1500},
                            {name: 'Mur_ouest', family: "ext", height: '2.0', length: '1.0', unit: 'unite', angle: '', angle_type: '', length2: '', price: 1000},
                            {name: 'Mur_est', family: "ext", height: '2.0', length: '1.0', unit: 'unite', angle: '', angle_type: '', length2: '', price: 1000},
                        ],
                        perso: [],
                    },
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
                gammeSelected: '',
                formeSelected: '',
                modulesWallExtSquareSelected: '',
                modulesWallExtRectSelected: '',
                modulesWallExtSelected: '',
                modulesWallIntSelected: '',
                modulesFloorSlabSelected: '',
                modulesFloorStructuralSelected: '',
                modulesRoofCarpentersSelected: '',
                modulesRoofCoverSelected: '',
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

                if(this.modulesWallExtSquareSelected === '' && this.modulesWallExtRectSelected === '' && this.modulesWallExtSelected === '' && this.modulesWallIntSelected === '' && this.modulesFloorSlabSelected === '' && this.modulesFloorStructuralSelected === '' && this.modulesRoofCarpentersSelected === '' && this.modulesRoofCoverSelected === ''){
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
            carreLongueur(length) {
                this.modulesWallExtSquareSelected.forEach(function (module) {
                    module.length = length.target.value;
                });
            },
            rectangleLongueur(oldLength, length) {

                this.modulesWallExtRectSelected.forEach(function (module) {
                    if(module.length === oldLength) {
                        module.length = length.target.value;
                    }
                });
            },
            carreHauteur(height) {
                this.modulesWallExtSquareSelected.forEach(function (module) {
                    module.height = height;
                });
            },
            rectangleHauteur(height) {
                this.modulesWallExtRectSelected.forEach(function (module) {
                    module.height = height;
                });
            },
            extHauteur(height) {
                this.modulesWallExtSelected.forEach(function (module) {
                    module.height = height;
                });
            },
            prixModuleCarre(module, oldLength, length) {
                let lenghtDiff = length.target.value - oldLength;
                let newPrice = lenghtDiff * module.price + module.price;
                this.modulesWallExtSquareSelected.forEach(function (module) {
                    module.price = newPrice;
                });
            },
            prixModuleRect(module, oldLength, length) {
                let lenghtDiff = length.target.value - oldLength;
                let newPrice = module.price = lenghtDiff * module.price + module.price;
                this.modulesWallExtRectSelected.forEach(function (module) {
                    if(module.length === oldLength) {
                        module.price = newPrice;
                    }
                });
            },
            prixModule(module, oldLength, length) {
                let lenghtDiff = length.target.value - oldLength;
                module.price = lenghtDiff * module.price + module.price;
            }
        },
        watch: {
            formeSelected: {
                handler: function () {
                    if(this.formeSelected === 'Carré') {
                        this.currentModuleSelected = '';
                        this.modulesWallExtRectSelected = '';
                        this.modulesWallExtSelected = '';

                        let modulesCarre = [];
                        this.modules.ext.carre.forEach( function (module) {
                            modulesCarre.push(module)
                        });
                        this.modulesWallExtSquareSelected = modulesCarre;

                    }

                    if(this.formeSelected === 'Rectangle') {
                        this.currentModuleSelected = '';
                        this.modulesWallExtSquareSelected = '';
                        this.modulesWallExtSelected = '';

                        let modulesRect = [];
                        this.modules.ext.rectangle.forEach( function (module) {
                            modulesRect.push(module)
                        });
                        this.modulesWallExtRectSelected = modulesRect;
                    }

                    if(this.formeSelected === 'Personnaliser') {
                        this.currentModuleSelected = '';
                        this.modulesWallExtSquareSelected = '';
                        this.modulesWallExtRectSelected = '';
                    }
                },
            },
            modulesWallExtSquareSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
            modulesWallExtRectSelected: {
               handler: function () {
                    this.modulesSelected = this.modulesSelected + 1
                }
            },
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
            if (this.modulesSelected === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }

            axios.get(`http://127.0.0.1:8000/api/gammes`)
                .then(response => {
                    this.modules.ext.perso = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                });

            // axios.get(`http://127.0.0.1:8000/api/modules/family/ext`)
            //     .then(response => {
            //         this.modules.ext.perso = response.data
            //     })
            //     .catch(e => {
            //         this.errors.push(e)
            //     });

            // axios.get(`http://127.0.0.1:8000/api/modules/family/int`)
            //     .then(response => {
            //         this.modules.int = response.data
            //     })
            //     .catch(e => {
            //         this.errors.push(e)
            //     })


        }
    }
</script>