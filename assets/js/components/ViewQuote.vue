<template>
    <div class="columns">
        <div class="column is-12">
            <section class="section">
                <div class="has-text-left">
                    <a class="button has-background-grey-lighter" @click="returnDashboard">
                        <i class="fas fa-home"></i>
                    </a>
                </div>
                <div class="has-text-centered">
                    <h1 class="title is-1">Liste des devis</h1>
                </div>
            </section>

            <form class="login form">
                <div class="field is-grouped has-addons">
                    <span class="control is-expanded">
                        <input v-model="search" class="input" type="text" placeholder="Chercher un devis" @keydown.enter.prevent="filteredAndSortedQuotes">
                    </span>
                    <p class="control">
                        <a class="button button-search is-link">
                            <i class="fas fa-search"></i>
                        </a>
                    </p>
                </div>
            </form>

            <section class="section">
                <div class="has-text-centered">
                    <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                        <thead>
                        <tr class="table-quotes-head">
                            <th class="has-text-centered" @click="sort('ref')">Ref Devis <span><i class="fas" v-if="currentSort === 'ref'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('project')">Nom Projet <span><i class="fas" v-if="currentSort === 'project'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('salesperson')">Commercial <span><i class="fas" v-if="currentSort === 'salesperson'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('client')">Client <span><i class="fas" v-if="currentSort === 'client'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('phone')">N° Téléphone <span><i class="fas" v-if="currentSort === 'phone'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('email')">Adresse Mail <span><i class="fas" v-if="currentSort === 'email'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('price')">Prix <span><i class="fas" v-if="currentSort === 'price'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered">Devis</th>
                            <th class="has-text-centered" @click="sort('state')">Etat Devis <span><i class="fas" v-if="currentSort === 'state'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('created_at')">Date création <span><i class="fas" v-if="currentSort === 'created_at'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('updated_at')">Date modification <span><i class="fas" v-if="currentSort === 'updated_at'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered">Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="quote in filteredAndSortedQuotes" >

                            <td class="has-text-centered">{{quote.reference}}</td>
                            <td class="has-text-centered">{{quote.name}}</td>
                            <td class="has-text-centered" v-for="salesperson in salespersons" v-if="quote.salesperson === salesperson.id">{{salesperson.full_name}}</td>
                            <td class="has-text-centered" v-for="client in clients" v-if="quote.client === client.id">{{client.full_name}}</td>
                            <td class="has-text-centered" v-for="client in clients" v-if="quote.client === client.id">{{client.phone}}</td>
                            <td class="has-text-centered" v-for="client in clients" v-if="quote.client === client.id">{{client.email}}</td>
                            <td class="has-text-centered">{{quote.price}}€</td>
                            <td class="has-text-centered">
                                <div v-if="quote.attachment !== null">
                                    <a :href="'/static/pdf/' + quote.attachment" target="_blank">
                                        <i class="fas fa-file-pdf"></i>
                                    </a>
                                </div>
                            </td>
                            <td class="has-text-centered">{{quote.state}}</td>
                            <td class="has-text-centered">{{quote.created_at | formatDate}}</td>
                            <td class="has-text-centered">{{quote.updated_at | formatDate}}</td>
                            <td class="has-text-centered">
                                <i @click="setModalUpdateQuote(quote)" class="fas fa-edit"></i>
                                <i @click="setModalDeleteQuote(quote)" class="fas fa-trash"></i>
                            </td>
                        </tr>
                        </tbody>
                        <tfoot>
                        <tr>
                            <td colspan="12">
                                <nav class="pagination is-right" role="navigation" aria-label="pagination">
                                    <ul class="pagination-list">
                                        <li>
                                            <div class="select">
                                                <select v-model="pageSize">
                                                    <option :value="Math.ceil(totalQuotes / 4)">{{Math.ceil(totalQuotes / 4)}}</option>
                                                    <option :value="Math.ceil(totalQuotes / 2)">{{Math.ceil(totalQuotes / 2)}}</option>
                                                    <option :value="totalQuotes">all</option>
                                                </select>
                                            </div>
                                        </li>
                                        <li v-if="currentPage > initialPage+1"><a @click="firstPage" class="pagination-link">{{initialPage}}</a></li>
                                        <li v-if="currentPage > initialPage+1"><span class="pagination-ellipsis">&hellip;</span></li>
                                        <li v-if="currentPage > initialPage"><a @click="prevPage" class="pagination-link">{{currentPage-1}}</a></li>
                                        <li><a class="pagination-link is-current">{{currentPage}}</a></li>
                                        <li v-if="currentPage !== totalPage"><a @click="nextPage" class="pagination-link">{{currentPage+1}}</a></li>
                                        <li v-if="currentPage < totalPage-1"><span class="pagination-ellipsis">&hellip;</span></li>
                                        <li v-if="currentPage < totalPage-1"><a @click="lastPage" class="pagination-link">{{totalPage}}</a></li>
                                        <li><a @click="prevPage" class="pagination-previous" :disabled="currentPage === initialPage"><</a></li>
                                        <li><a @click="nextPage" class="pagination-next" :disabled="currentPage === totalPage">></a></li>
                                    </ul>
                                </nav>
                            </td>
                        </tr>
                        </tfoot>
                    </table>
                </div>

                <div class="modal" :class="{'is-active': (showModalUpdate === true)}" v-if="showModalUpdate === true">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head has-background-link">
                            <p class="modal-card-title has-text-centered has-text-white">Edition du devis Ref : {{this.reference}}</p>
                            <button @click="hideModalUpdate" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body">

                            <form action="#">
                                <div class="field">
                                    <label class="label">Projet</label>

                                    <input type="text" v-model="quotePrj" :placeholder="this.name" >
                                </div>


                                <div class="field">
                                    <label class="label">Reference</label>

                                    <input type="text" v-model="quoteRef" :placeholder="this.reference" >
                                </div>

                                <div class="field">
                                    <label class="label">Etat Devis</label>
                                    <p class="control has-icons-left">
                                        <span class="select">
                                          <select @focus="selectFocus = 'state'" @blur="selectFocus = ''" v-model="quoteState">
                                            <option value="" disabled>{{this.state}}</option>
                                            <option v-if="this.state !== 'Brouillon'">Brouillon</option>
                                            <option v-if="this.state !== 'En attente'">En attente</option>
                                            <option v-if="this.state !== 'Accepté'">Accepté</option>
                                            <option v-if="this.state !== 'Refusé'">Refusé</option>
                                            <option v-if="this.state !== 'En Commande'">En Commande</option>
                                            <option v-if="this.state !== 'Transfert en Facturation'">Transfert en Facturation</option>
                                            <option v-if="this.state !== 'Archivé'">Archivé</option>
                                          </select>
                                        </span>
                                        <span class="icon is-small is-left">
                                          <i class="fas fa-file-alt" :class="{'icon-focus': (selectFocus === 'state')}"></i>
                                        </span>
                                    </p>
                                </div>
                            </form>

                        </section>
                        <footer class="modal-card-foot justify-content-end">
                            <button @click="updateQuote" class="button is-link">Enregistrer</button>
                            <button @click="hideModalUpdate" class="button">Annuler</button>
                        </footer>
                    </div>
                </div>

                <div class="modal" :class="{'is-active': (showModalDelete === true)}" v-if="showModalDelete === true">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head has-background-danger">
                            <p class="modal-card-title has-text-centered has-text-white">Suppression du devis Ref : {{this.reference}}</p>
                            <button @click="hideModalDelete" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body d-flex justify-content-center">

                            <button @click="deleteQuote" class="button mr-1 is-danger">Supprimer</button>
                            <button @click="hideModalDelete" class="button">Annuler</button>

                        </section>
                        <footer class="modal-card-foot justify-content-center">
                            <p class="has-text-danger">La suppression du devis est définitive !</p>
                        </footer>
                    </div>
                </div>
            </section>
            <b-loading :is-full-page="isFullPage" :active.sync="isLoading" :can-cancel="true"></b-loading>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "ViewQuote",
        data() {
            return {
                quotes: [],
                clients: [],
                salespersons: [],
                errors: [],
                search: '',
                isLoading: false,
                isFullPage: true,
                currentSort: 'created_at',
                currentSortDir: 'desc',
                pageSize: null,
                currentPage: 1,
                initialPage: 1,
                showModalUpdate: false,
                showModalDelete: false,
                selectedQuote: null,
                quotePrj: '',
                quoteRef: '',
                quoteState: '',
                selectFocus: '',
            }
        },
        async created() {
            try {
                const response = await axios.get(this.$store.state.endpoints.baseUrl + 'api/quotes/')
                this.quotes = response.data
            } catch (e) {
                this.errors.push(e)
            }

            this.pageSize = this.quotes.length;
        },
        methods: {
            returnDashboard() {
                this.$router.push({name: 'Dashboard'})
            },
            sort: function (s) {
                if (s === this.currentSort) {
                    this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc'
                }
                this.currentSort = s
            },
            nextPage: function () {
                if ((this.currentPage * this.pageSize) < this.quotes.length) this.currentPage++
            },
            prevPage: function () {
                if (this.currentPage > 1) this.currentPage--
            },
            firstPage: function () {
                if (this.currentPage > 1) this.currentPage = this.initialPage
            },
            lastPage: function () {
                if (Math.floor(this.quotes.length / this.pageSize) > 1) this.currentPage = Math.floor(this.quotes.length / this.pageSize)
            },
            setModalUpdateQuote(quote) {
                this.showModalUpdate = true;
                this.selectedQuote = quote;
                this.name = quote.name;
                this.reference = quote.reference;
                this.state = quote.state;
            },
            setModalDeleteQuote(quote) {
                this.showModalDelete = true;
                this.selectedQuote = quote;
                this.id = quote.id;
            },
            hideModalUpdate: function () {
                this.showModalUpdate = false;
                this.customer = '';
                this.salesperson = '';
                this.quoteState = '';
            },
            hideModalDelete: function () {
                this.showModalDelete = false
            },
            getQuotes() {
                axios.get(this.$store.state.endpoints.baseUrl + 'api/quotes/')
                .then(response => {
                    this.quotes = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
            },
            updateQuote() {

                let date = new Date();
                let now = date.getFullYear() + '-' + (date.getMonth() +1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + (date.getMinutes()<10?'0':'') + date.getMinutes();

                if (this.quotePrj === '') {
                    this.quotePrj = this.selectedQuote.name
                }

                if (this.quoteRef === '') {
                    this.quoteRef = this.selectedQuote.reference
                }

                if (this.quoteState === '') {
                    this.quoteState = this.selectedQuote.state
                }

                let quoteUpdate = {
                    'name': this.quotePrj,
                    'reference': this.quoteRef,
                    'price': this.selectedQuote.price,
                    'attachment': this.selectedQuote.attachment,
                    'state': this.quoteState,
                    'client_id': this.selectedQuote.client,
                    'salesperson_id': this.selectedQuote.salesperson,
                    'created_at': this.selectedQuote.created_at,
                    'updated_at': now
                };

                axios.put(this.$store.state.endpoints.baseUrl + 'api/quotes/' + this.selectedQuote.id,
                    quoteUpdate, {
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    }).then((response) => {
                        this.name = '';
                        this.reference = '';
                        this.customer = '';
                        this.salesperson = '';
                        this.quoteState = '';
                        this.selectedQuote = null;
                        this.showModalUpdate = false;
                        this.getQuotes();

                    }).catch(e => {
                        this.errors.push(e);
                    });
            },
            deleteQuote() {
                let index = this.quotes.indexOf(this.selectedQuote);

                axios.delete(this.$store.state.endpoints.baseUrl + 'api/quotes/' + this.selectedQuote.id)
                    .then(response => {
                        this.quotes.splice(index, 1);
                        this.selectedQuote = null;
                        this.showModalDelete = false;
                    }).catch(e => {
                        this.errors.push(e);
                    });
            }
        },
        computed: {
            filteredAndSortedQuotes() {
                let self = this;

                let result = this.quotes.filter(function (quote) {
                    return  quote.reference.toLowerCase().indexOf(self.search) >= 0
                        || quote.name.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        // || salesperson.full_name.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        // || client.full_name.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        // || client.phone.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        // || client.email.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.price.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.state.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.created_at.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.updated_at.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                });

                return result.sort((a, b) => {
                    let modifier = 1;
                    if (this.currentSortDir === 'desc') modifier = -1;
                    if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                    if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                    return 0;
                }).filter((row, index) => {
                    let start = (this.currentPage - 1) * this.pageSize;
                    let end = this.currentPage * this.pageSize;
                    if (index >= start && index < end) return true;
                });
            },
            totalPage: function () {
                return Math.ceil(this.quotes.length / this.pageSize)
            },
            totalQuotes: function () {
                return this.quotes.length
            }
        },
        mounted() {
            this.isLoading = true;

            axios.get(this.$store.state.endpoints.baseUrl + `api/salespersons/`)
                .then(response => {
                    this.salespersons = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                });

            axios.get(this.$store.state.endpoints.baseUrl + `api/clients/`)
                .then(response => {
                    this.clients = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                });

            this.isLoading = false;
        }
    }
</script>

<style>
</style>
