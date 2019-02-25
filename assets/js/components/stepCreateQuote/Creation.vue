<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <div class="field">
            <div class="control">
                <div class="select is-primary">
                    <select>
                        <option>Select modules</option>
                        <option>Liste modules API</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="field">
            <div class="control">
                <div class="select is-primary">
                    <select>
                        <option>Select composants</option>
                        <option>Liste composants API</option>
                    </select>
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
                form: {}
            }
        },
        validations: {
            form: {}
        },
        watch: {
            $v: {
                handler: function (val) {
                    if (!val.$invalid) {
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

            clickedNext(val) {
                console.log(val);
                if (val === true) {
                    this.$v.form.$touch();
                }
            }
        },
        mounted() {
            if (!this.$v.$invalid) {
                this.$emit('can-continue', {value: false});
            } else {
                this.$emit('can-continue', {value: true});
            }
        }
    }
</script>