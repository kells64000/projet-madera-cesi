# Projet-madera-cesi

## Prérequis
- Création du virtual env

Unix
<pre>virtualenv -p python3 .</pre>
Windows
<pre>pip install virtualenv</pre>
- installation des dépendances 

<pre>pip install -r requirements.txt</pre>

## Virtual Env
Lancement du virtual env (windows) :
<pre>Scripts\activate</pre>

## VCS => Git

Pour le déroulement du projet nous utilisons [Git Flow](https://danielkummer.github.io/git-flow-cheatsheet/)

Master = Prod

Develop = pre-Prod

## Base de donnée

La base de donnée de l'application est : **Postgresql** 

<pre>
DB-name : madera
user :    postgres
passwd :  postgres
</pre>

La base de donnée en local pour les commerciaux est : **mysqli**

La base mysqli permet de stocker les devis sur le device si aucune connexion à la base principale n'est possible
Lorsque une connexion internet est de nouveau disponible les données de la base mysqli sont intégrées à la base postgre

Le dossier **db** contient un dump récent de postgresql

Pour l'importer dans le client postgresql, exécuter :

`pg_restore -U postgres -j 2 -Fc -v -d madera madera.dump.bin`

>Créer la base si elle n'existe pas encore
`createdb -U postgres -E UTF-8 madera`.
>Puis lancer `pg_restore` pour importer

## Donnée de l'application

L'utilisateur pour la démo est :

<pre>
email : staff@madera.com
password : madera
</pre>

## Environnement de dév

### Back

**Virtualenv**

**Créer une application**

Pour créer une nouvelle application, se rendre dans le dossier `apps` puis lancer commande de génération d'application.

```bash
cd projet-madera-cesi/apps
django-admin startapp <name>
```

### Front

**NPM**

Installer les packages de NPM

```bash
npm i
```

Ne pas oublier de compiler les fichiers quand une modification est faite en saas ou en js via

```bash
npm run dev
```

Pour faire des modifications sur les fichiers *scss* || *vue* || *js* sans relancer tout le temps <code>npm run dev</code>

```bash
npm start
```
Cette commande est un alias de <code>npm run watch</code> et permet de compiler les assets dès qu'une modification est apportée

**Bulma**

Les fichiers *saas* ce trouvent dans <code>assets/saas</code>

Créer un fichier pour chaque template avec la syntaxe suivante : <code>_page.scss</code>

et l'importer dans le fichier app.scss 

Exemple :

```scss
@import 'page';
```

Le fichier <code>_variables.scss</code> permet d'écraser les valeurs des variables de Bulma

**VueJs**

Les composants vue sont dans <code>assets/js/components</code>

La déclaration des components ce fait dans <code>assets/js/index.js</code>

```javascript
import Demo from Login.vue;

const app = new Vue({
    el: '#app',
    components: {
        Demo
    }
});
```
