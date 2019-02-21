<template>
    <div style="padding: 2rem 3rem; text-align: left;">

        <div class="control mb-1">
            <label class="radio">
                <input type="radio" name="client" value="new" v-model="client" checked>
                Nouveau client
            </label>

            <label class="radio">
                <input type="radio" name="client" value="madera" v-model="client">
                Client Madera
            </label>
        </div>

        <div v-if="client === 'new'">
            <!--<div class="field is-horizontal">-->
                <!--<div class="control">-->
                    <!--<input :class="['input', ($v.form.username.$error) ? 'is-danger' : '']" type="text"-->
                           <!--placeholder="Nom"-->
                           <!--v-model="form.username">-->
                <!--</div>-->
                <!--<div class="control">-->
                    <!--<input :class="['input', ($v.form.username.$error) ? 'is-danger' : '']" type="text"-->
                           <!--placeholder="Prénom"-->
                           <!--v-model="form.username">-->
                <!--</div>-->
            <!--</div>-->

            <div class="field is-horizontal">
              <div class="field-body">
                <div class="field">
                  <p class="control is-expanded has-icons-left">
                    <input class="input" type="text" placeholder="Nom">
                    <span class="icon is-small is-left">
                      <i class="fas fa-user"></i>
                    </span>
                  </p>
                </div>
                <div class="field">
                  <p class="control is-expanded has-icons-left">
                    <input class="input" type="text" placeholder="Prénom">
                    <span class="icon is-small is-left">
                      <i class="fas fa-user"></i>
                    </span>
                  </p>
                </div>
              </div>
            </div>

            <div class="field">
              <p class="control is-expanded has-icons-left">
                <input class="input" type="email" placeholder="Email">
                <span class="icon is-small is-left">
                  <i class="fas fa-envelope"></i>
                </span>
              </p>
            </div>

            <div align="center" class="is-centered">
                <button class="button is-success" type="submit">Créer nouveau client</button>
            </div>





            <!--<div class="field">-->
                <!--<label class="label">Email</label>-->
                <!--<div class="control">-->
                    <!--<input :class="['input', ($v.form.email.$error) ? 'is-danger' : '']" type="text"-->
                           <!--placeholder="Email" v-model="form.email">-->
                <!--</div>-->
                <!--<p v-if="$v.form.email.$error" class="help is-danger">This email is invalid</p>-->
            <!--</div>-->
        </div>

        <div v-if="client === 'madera'">
            <div class="field">
                <div class="control">
                    <div class="select is-primary">
                        <select>
                            <option>Select 2 à mettre en place</option>
                            <option>Liste client API</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
    import {validationMixin} from 'vuelidate'
    import {required, email} from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                client: 'new',
                form: {
                    username: '',
                    email: '',
                }
            }
        },
        validations: {
            form: {
                username: {
                    required
                },
                email: {
                    required,
                    email
                }
            }
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