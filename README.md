## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

Le déploiement s'opère à travers l'utilisation des technologies :

- CircleCI
- Docker / DockerHub
- Heroku
- Sentry

Vous devez posséder un compte pour chaqune de ses applications.

Le cheminement du pipeline: 
- Fait d'abord passer les tests et vérifie la conformité à la PEP8;
- Si les vérifications sont correctement passées, une image docker est créée puis poussée sur DockerHub;
- Si la poussée est validée, l'application est déployée sur Heroku.

### CircleCI
https://app.circleci.com/pipelines/github/Kern84/Python-OC-Lettings-FR

A cette adresse vous pouvez voir tous les pipelines qui ont été lancé.
Pour que le code fonctionne dans une autre configuration vous devez enregistrer dans l'onglet "Environment Variables" les clés suivantes:
- DOCKER_LOGIN : Nom du User Docker
- DOCKER_PASSWORD : Mot de passe généré dans Docker
- HEROKU_API_KEY : Nom de la clé API de Heroku
- HEROKU_APP_NAME : Nom de l'application Heroku

### Heroku
https://oc-lettings-application.herokuapp.com/

Vous pouvez consulter l'application à cette adresse.

### DockerHub
https://hub.docker.com/repository/docker/adrienlr/oc_lettings

Vous pouvez consulter les images Docker qui ont été poussées.

Pour lancer une image Docker en local en la récupérant depuis DockerHub:
- Vous devez avoir installer Docker préalablement sur votre machine.
- Entrer la ligne de commande dans votre terminal:
`docker run -it -p 8000:8000 nom_du_compte_docker/nom_du_dépot_dockerhub:tag_dockerhub`

Par exemple :
`docker run -it -p 8000:8000 adrienlr/oc_lettings:0.0.69`

Le site sera disponible localement à l'adresse http://127.0.0.1:8000/

### Sentry
https://sentry.io/organizations/alr84/issues/?project=6593803

Vous pouvez consulter le monitoring Sentry de l'application à cette adresse.