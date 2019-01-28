<template>
    <div class="columns">
        <div class="column is-12">
            <section class="section">
                <div class="has-text-centered">
                    <h1>Liste des devis</h1>
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
                            <th @click="sort('id')">N° Devis</th>
                            <th @click="sort('name')">Nom Client</th>
                            <th @click="sort('phone')">N° Téléphone</th>
                            <th @click="sort('email')">Adresse Mail</th>
                            <th @click="sort('price')">Prix (€)</th>
                            <th @click="sort('state')">Etat Devis</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="quote in sortedQuotes">
                            <td>{{quote.id}}</td>
                            <td>{{quote.name}}</td>
                            <td>{{quote.phone}}</td>
                            <td>{{quote.email}}</td>
                            <td>{{quote.price}}</td>
                            <td>{{quote.state}}</td>
                        </tr>
                        </tbody>
                        <tfoot>
                        <tr>
                            <td colspan="6">
                                <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                                    <a v-if="currentPage !== initialPage" @click="prevPage" class="pagination-previous">Précedent</a>
                                    <a v-if="currentPage !== totalPage" @click="nextPage" class="pagination-next">Suivant</a>
                                    <ul class="pagination-list">
                                        <li v-if="currentPage > initialPage+1"><a @click="firstPage" class="pagination-link">{{initialPage}}</a></li>
                                        <li v-if="currentPage > initialPage+1"><span class="pagination-ellipsis">&hellip;</span></li>
                                        <li v-if="currentPage > initialPage"><a @click="prevPage" class="pagination-link">{{currentPage-1}}</a></li>
                                        <li><a class="pagination-link is-current">{{currentPage}}</a></li>
                                        <li v-if="currentPage !== totalPage"><a @click="nextPage" class="pagination-link">{{currentPage+1}}</a></li>
                                        <li v-if="currentPage < totalPage-1"><span class="pagination-ellipsis">&hellip;</span></li>
                                        <li v-if="currentPage < totalPage-1"><a @click="lastPage" class="pagination-link">{{totalPage}}</a></li>
                                    </ul>
                                </nav>
                            </td>
                        </tr>
                        </tfoot>
                    </table>
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
                currentSort: 'id',
                currentSortDir: 'asc',
                pageSize: 2,
                currentPage: 1,
                initialPage: 1,
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
        }
    }
</script>

<style>

</style>