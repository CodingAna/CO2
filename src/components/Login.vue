<template>
    <v-container>
        <v-card class="mx-auto" max-width="600" outlined>
            <v-list-item three-line>
                <v-list-item-content>
                    <div class="overline mb-4">
                        Schulprojekt CO2
                    </div>
                    <v-list-item-title class="headline mb-1">
                        Anmeldung
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        <v-form v-model="valid">
                            <v-container>
                                <v-row>
                                    <v-col cols="12" md="12">
                                        <v-text-field v-model="email" :rules="emailRules" label="E-Mail" required/>
                                    </v-col>
                                    <v-col cols="12" md="12">
                                        <!--:rules="[passwordRules.required, passwordRules.min]"-->
                                        <v-text-field v-model="password" :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'" :type="show3 ? 'text' : 'password'" label="Passwort" class="input-group--focused" @click:append="show3 = !show3" :rules="[passwordRules.required, passwordRules.min]"/>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-form>
                    </v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-avatar
                  size="180"
                  >
                  <img 
                  src="../assets/gew.svg" 
                  style="margin: auto;">
                  </v-list-item-avatar>

            </v-list-item>
            <v-card-actions>
                <v-row>
                    <v-col>
                        <v-checkbox style="margin-right:20%;" color="green">
                            <template v-slot:label>
                                <div @click.stop="">
                                    Do you accept the
                                    <a href="#" @click.prevent="terms = true">
                                        terms
                                    </a>
                                    and
                                    <a href="#" @click.prevent="conditions = true">
                                        conditions
                                    </a>
                                    ?
                                </div>
                            </template>
                        </v-checkbox>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col style="margin-left:35%">
                        <v-btn dark color="#791014" @click="loginclick()">
                            Login
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card-actions>
        </v-card>
        <v-dialog v-model="terms" width="70%">
            <v-card>
                <v-card-title class="title">
                    Terms
                </v-card-title>
                <v-card-text v-for="n in 5" :key="n"> <!-- The content gets displayed 5 times. Remove this XD -->
                    {{content}}
                </v-card-text>
                <v-card-actions>
                    <v-spacer/>
                    <v-btn text color="purple" @click="terms = false">
                        Ok
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="conditions" width="70%">
            <v-card>
                <v-card-title class="title">
                    Conditions
                </v-card-title>
                <v-card-text v-for="n in 5" :key="n">
                    {{content}}
                </v-card-text>
                <v-card-actions>
                    <v-spacer/>
                    <v-btn text color="purple" @click="conditions = false">
                        Ok
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
import EventBus from '../EventBus';

export default {
    name: 'Login',
    
    data: () => ({
        valid: false,
        email: '',
        password: '',
        emailRules: [
            v => !!v || 'Bitte E-Mail eingeben',
            v => /.+@.+/.test(v) || 'Bitte gültige E-Mail eingeben',
        ],

        show3: false,
        passwordRules: {
            required: value => !!value || 'Es muss ein Passwort eingegeben werden',
            min: v => v.length >= 8 || 'Passwort muss mindestens 8 Zeichen lang sein',
        },

        terms: false,
        conditions: false,
        content: 'Der Friedrich bat mich, dass ich doch, zum Wohle unseres Projektes und der Einhaltung der DSGVO eine Sammlung an Datenschutzzusicherungen ersönne, die sich auf einer bestimmten Seite wiederfänden. So setze ich mich also an den Computer und ersann mit größter Freude und scharfem Verstand, folgendes Verzeichnis an Zusicherungen, die ich dem interessierten Leser und jedem Benutzer der Seite gerne machen würde. So lesen Sie diese Worte und seien Sie versichert, dass Sie ohne Hintergedanken und rein zum Schutze einer besonders schützenswerten Gruppe geschrieben und aufgenommen worden. Wir, der Informatik-LK des Werdener Gymnasiums entwickelte nach reinstem Wissen und Gewissen und unter der Anstrengung siebener, in seltenen Fällen, leistungsstarkter Prozessoren eine Seite, um die Daten der uns zugetragenen und ebenfalls von uns geprüften, eingestellten und platzierten Kleinstcomputer zu sammeln. Diese Daten suchten wir auszuwerten und entwarfen zu diesem Zwecke ein Portal, in das Sie, werter und geschätzer Leser, nun Zugriff erhalten haben. Die einzigen Daten, die wir benutzen sind die derer, die nichts davon wissen.',
    }),
    
    methods: {
        loginclick() {
            const payload = {
                email: this.email,
                password: this.password
            };
            EventBus.$emit('LOGINEVENT', payload);
        },
    },
}
</script>