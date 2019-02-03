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
                        <input class="input" type="text" placeholder="Chercher un devis">
                    </span>
                    <p class="control">
                        <a class="button button-search is-info">
                            <i class="fas fa-search"></i>
                        </a>
                    </p>
                </div>
            </form>

            <section class="section">
                <div class="has-text-centered">
                    <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
                        <thead>
                        <tr>
                            <th class="has-text-centered" @click="sort('id')">N° Devis</th>
                            <th class="has-text-centered" @click="sort('name')">Nom Client</th>
                            <th class="has-text-centered" @click="sort('phone')">N° Téléphone</th>
                            <th class="has-text-centered" @click="sort('email')">Adresse Mail</th>
                            <th class="has-text-centered" @click="sort('price')">Prix (€)</th>
                            <th class="has-text-centered" @click="sort('state')">Etat Devis</th>
                            <th class="has-text-centered">Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="quote in sortedQuotes">
                            <td class="has-text-centered">{{quote.id}}</td>
                            <td class="has-text-centered">{{quote.name}}</td>
                            <td class="has-text-centered">{{quote.phone}}</td>
                            <td class="has-text-centered">{{quote.email}}</td>
                            <td class="has-text-centered">{{quote.price}}</td>
                            <td class="has-text-centered">{{quote.state}}</td>
                            <td class="has-text-centered">
                                <i @click="editQuote" class="fas fa-edit"></i>
                            </td>
                        </tr>
                        </tbody>
                        <tfoot>
                        <tr>
                            <td colspan="7">
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
                <div class="modal" :class="{'is-active': (showModal == true)}">
                    <div class="modal-background"></div>
                    <div class="modal-card">
                        <header class="modal-card-head">
                            <p class="modal-card-title has-text-centered">Edition du Devis n° quote.id</p>
                            <button @click="hideModal" class="delete" aria-label="close"></button>
                        </header>
                        <section class="modal-card-body">

                        </section>
                        <footer class="modal-card-foot">
                            <button class="button is-success">Save changes</button>
                            <button class="button">Cancel</button>
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
                loading: false,
                currentSort: 'id',
                currentSortDir: 'asc',
                pageSize: 2,
                currentPage: 1,
                initialPage: 1,
                showModal: false,
                search: '',
            }
        },
        created() {
            axios.get(`http://jsonplaceholder.typicode.com/users`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.quotes = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })

            // async / await version (created() becomes async created())
            //
            // try {
            //   const response = await axios.get(`http://jsonplaceholder.typicode.com/posts`)
            //   this.posts = response.data
            // } catch (e) {
            //   this.errors.push(e)
            // }
        },
        methods: {
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
            editQuote: function () {
                this.showModal = true
            },
            hideModal: function () {
                this.showModal = false
            },
            returnDashboard() {
                this.$router.push({name: 'Dashboard'})
            }

        },
        computed: {
            sortedQuotes: function () {
                return this.quotes.sort((a, b) => {
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
            }
        },
        mounted: function() {

            // this.getQuotes();
        }
    }
</script>

<style>

</style>
