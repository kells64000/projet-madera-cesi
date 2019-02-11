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
                        <input v-model="search" class="input" type="text" placeholder="Chercher un devis">
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
                            <th class="has-text-centered" @click="sort('id')">N° Devis <span><i class="fas" v-if="currentSort === 'id'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('name')">Nom Client <span><i class="fas" v-if="currentSort === 'name'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('phone')">N° Téléphone <span><i class="fas" v-if="currentSort === 'phone'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('email')">Adresse Mail <span><i class="fas" v-if="currentSort === 'email'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('price')">Prix <span><i class="fas" v-if="currentSort === 'price'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('state')">Etat Devis <span><i class="fas" v-if="currentSort === 'state'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('created_at')">Date création <span><i class="fas" v-if="currentSort === 'created_at'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered" @click="sort('updated_at')">Date modification <span><i class="fas" v-if="currentSort === 'updated_at'" :class="currentSortDir === 'asc' ? 'fa-caret-up' : 'fa-caret-down'"></i></span></th>
                            <th class="has-text-centered">Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="quote in filteredAndSortedQuotes /*sortedQuotes*/" >

                            <td class="has-text-centered">{{quote.id}}</td>
                            <td class="has-text-centered">{{quote.name}}</td>
                            <td class="has-text-centered">{{quote.phone}}</td>
                            <td class="has-text-centered">{{quote.email}}</td>
                            <td class="has-text-centered">{{quote.price}}€</td>
                            <td class="has-text-centered">{{quote.state}}</td>
                            <td class="has-text-centered">{{quote.created_at | formatDate}}</td>
                            <td class="has-text-centered">{{quote.updated_at | formatDate}}</td>
                            <td class="has-text-centered">
                                <i @click="showModalEdit = true, setModalUpdateQuote(quote.id, quote.name, quote.phone, quote.email, quote.price, quote.state)" class="fas fa-edit"></i>
                                <i @click="showModalDelete = true, setModalDeleteQuote(quote.id)" class="fas fa-trash"></i>
                            </td>
                        </tr>
                        </tbody>
                        <tfoot>
                        <tr>
                            <td colspan="9">
                                <nav class="pagination is-right" role="navigation" aria-label="pagination">
                                    <ul class="pagination-list">
                                        <li>
                                            <div class="select">
                                                <select v-model="pageSize">
                                                    <option :value="pageSize">{{pageSize}}</option>
                                                    <option v-if="pageSize !== 2" :value="2">2</option>
                                                    <option v-if="pageSize !== 5" :value="5">5</option>
                                                    <option v-if="pageSize !== 10" :value="10">10</option>
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
                <div class="modal" :class="{'is-active': (showModalEdit === true)}">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head has-background-link">
                            <p class="modal-card-title has-text-centered has-text-white">Edition du devis N° {{this.id}}</p>
                            <button @click="hideModalUpdate" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body">

                            <form action="#">
                                <div class="field">
                                    <label class="label">Nom Client</label>
                                    <div class="control">
                                        <input class="input" type="text" :value="this.name">
                                    </div>
                                </div>

                                <div class="field">
                                    <label class="label">Téléphone</label>
                                    <div class="control">
                                        <input class="input" type="text" :value="this.phone">
                                    </div>
                                </div>

                                <div class="field">
                                    <label class="label">Adresse Mail</label>
                                    <p class="control has-icons-left">
                                        <input class="input" type="email" :value="this.email">
                                        <span class="icon is-small is-left">
                                          <i class="fas fa-envelope"></i>
                                        </span>
                                    </p>
                                </div>

                                <div class="field">
                                    <label class="label">Prix</label>
                                    <p class="control has-icons-right">
                                        <input class="input" type="text" :value="this.price">
                                        <span class="icon is-small is-right">
                                          <i class="fas fa-euro-sign"></i>
                                        </span>
                                    </p>
                                </div>

                                <div class="field">
                                    <label class="label">Etat Devis</label>
                                    <p class="control has-icons-left">
                                        <span class="select">
                                          <select>
                                            <option selected>{{this.state}}</option>
                                            <option>brouillon</option>
                                            <option>archivé</option>
                                          </select>
                                        </span>
                                        <span class="icon is-small is-left">
                                          <i class="fas fa-file-alt"></i>
                                        </span>
                                    </p>
                                </div>
                            </form>

                        </section>
                        <footer class="modal-card-foot justify-content-end">
                            <button @click="updateQuote()" class="button is-link">Enregistrer</button>
                            <button @click="hideModalUpdate" class="button">Annuler</button>
                        </footer>
                    </div>
                </div>
                <div class="modal" :class="{'is-active': (showModalDelete === true)}">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head has-background-danger">
                            <p class="modal-card-title has-text-centered has-text-white">Suppression du devis N° {{this.id}}</p>
                            <button @click="hideModalDelete" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body d-flex justify-content-center">

                            <button @click="deleteQuote()" class="button mr-1 is-danger">Supprimer</button>
                            <button @click="hideModalDelete" class="button">Annuler</button>

                        </section>
                        <footer class="modal-card-foot justify-content-center">
                            <p class="has-text-danger">La suppression du devis est définitive !</p>
                        </footer>
                    </div>
                </div>
            </section>
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
                errors: [],
                loading: true,
                currentSort: 'id',
                currentSortDir: 'asc',
                pageSize: 3,
                currentPage: 1,
                initialPage: 1,
                showModalEdit: false,
                showModalDelete: false,
                search: '',
            }
        },
        async created() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/quotes`)
                this.quotes = response.data
            } catch (e) {
                this.errors.push(e)
            } finally {
                this.loading = false
            }
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
            setModalUpdateQuote(id, name, phone, email, price, state) {
                this.id = id;
                this.name = name;
                this.phone = phone;
                this.email = email;
                this.price = price;
                this.state = state;
            },
            setModalDeleteQuote(id) {
                this.id = id;
            },
            hideModalUpdate: function () {
                this.showModalEdit = false
            },
            hideModalDelete: function () {
                this.showModalDelete = false
            },
            updateQuote(id, name, phone, email, price, state) {
                const quote = axios.put('http://127.0.0.1:8000/api/quotes/' + id);


            },
            deleteQuote(id) {

                id = 1;

                const quote = axios.delete('http://127.0.0.1:8000/api/quotes/' + id);
                return axios.delete(quote);
            }
        },
        computed: {
            filteredAndSortedQuotes() {
                let self = this;

                let result = this.quotes.filter(function (quote) {
                    return  quote.id.toString().indexOf(self.search) >= 0
                        || quote.name.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.phone.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
                        || quote.email.toLowerCase().indexOf(self.search.toLowerCase()) >= 0
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
        }
    }
</script>



<style>

</style>