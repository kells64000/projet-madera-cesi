<template>
    <div class="d-flex justify-content-center" style="padding: 2rem 3rem; text-align: left;">

        <div class="field">
            <p class="control is-expanded has-icons-left">
                <input class="input" type="text" v-model="project">
                <span class="icon is-small is-left">
                      <i class="fas fa-marker"></i>
                </span>
            </p>
        </div>

    </div>
</template>

<script>

    export default {
        props: ['clickedNext', 'currentStep'],
        data() {
            return {
                project: '',
            }
        },
        watch: {
            project: {
                handler: function () {
                    if (this.project !== '') {
                        this.$store.commit("setQuoteProject", this.project);
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
                if (this.project !== '') {
                    this.$emit('can-continue', {value: true});
                }
            }
        },
        mounted() {
            if (this.project === '') {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>
