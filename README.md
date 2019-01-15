# Projet-madera-cesi

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

### Front

*NPM*

Installer les packages de NPM

<pre>
npm i
</pre>

**Bulma**


**VueJs**