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
user :    root
passwd :  root
</pre>

La base de donnée en local pour les commerciaux est : **mysqli**

La base mysqli permet de stocker les devis sur le device si aucune connexion à la base principale n'est possible
Lorsque une connexion internet est de nouveau disponible les données de la base mysqli sont intégrées à la base postgre

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

**NPM => VueJs**

**Templates**
