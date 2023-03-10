### `Repository name : OC_Project_09_Repository`
### 📖 Vue d'ensemble
Développer une application web `LITREview` en utilisant Django et une base de données `sqlite3`, 
qui permet aux utilisateurs de :
- S'inscrire, se connecter, se déconnecter
- Créer et publier des tickets (livres ou articles) en demandant des critiques
- Créer et publier des critiques de livres ou d’articles publiés
- Ajouter ou désabonner un utilisateur à suivre
- Visualiser les utilisateurs à suivre et les abonnés
- Consulter les publications des utilisateurs qu'ils suivent
- Modifier ou supprimer ses propres publications
### 💿 Installer Python
### 💿 Créer et activer un nouvel environnement virtuel `ENV` & Choisir l'interpréteur Python
```bash
python -m venv ENV
```
```bash
ENV/Scripts/activate
```
### ⚙️ Cloner depuis GitHub le projet Django
```bash
git clone https://github.com/RochdiGZ/OC_Project_09_Repository.git
```
### ⚙️ Modifier les propriétés du dossier OC_Project_09_Repository comme source de données
-  A l'aide de PyCharm, il suffit de sélectionner le dossier et d'utiliser le bouton droit de la souris pour choisir 
`Mark Directory as > Sources Root`
### 💿 Installer tous les modules du projet Django
```bash
cd OC_Project_09_Repository
```
```bash
python.exe -m pip install --upgrade pip
``` 
```bash
pip install -r requirements.txt
```
### ⚙️ Créer le dossier flake8_report
```bash
flake8 --format=html --htmldir=flake8_report --max-line-length=119
```
### ⚙️ Créer un super utilisateur
```bash
python manage.py createsuperuser
``` 
Dans l'étape suivante, il suffit de rester dans le terminal pour taper un nom d'utilisateur et un mot de passe 
avec confirmation du mot de passe. Par exemple,
- nom d'utilisateur : `Rochdi`
- Mot de passe : `secret@django`
### ⚙️ Lancer le serveur de développement
```bash
python manage.py runserver
``` 
Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page de connexion à 
l'application `LiTReview` via l'adresse `http://127.0.0.1:8000` .
### ⚙️ Se connecter avec l'interface de l'administration Django via `http://127.0.0.1:8000/admin`
- Une fois le serveur de développement lancé, vous pouvez voir, dans un navigateur web, la page de l'administration 
Django via `http://127.0.0.1:8000/admin`. Pour se connecter, il suffit de taper le nom d'utilisateur `Rochdi` et 
le mot de passe `secret@django` du super utilisateur ayant été créé précédemment, et de cliquer sur le bouton 
`Connexion`.
- `Une fois connecté, vous pouvez accéder à notre base de données et savoir les noms de tous les utilisateurs inscrits`
- Vous pouvez utiliser un nom d'utilisateur inscrit et le mot de passe `secret@django` 
pour se connecter à notre application.
### ⚙️ Se connecter avec l'interface de l'application LITReview via `http://127.0.0.1:8000`
- Dans le cas où vous ne disposez pas d'un compte, il suffit de cliquer sur le bouton `S'inscrire` 
et de taper un nom d'utilisateur et un mot de passe avec confirmation du mot de passe.
- Dans le cas où vous disposez d'un compte, il suffit de taper le nom d'utilisateur et le mot de passe de votre compte 
ayant été créé précédemment, et de cliquer sur le bouton `Se Connecter`.
`http://127.0.0.1:8000/home` où vous pouvez utiliser les services de notre application.
- vous pouvez accéder à notre base de données et savoir les noms de tous les utilisateurs inscrits`
### ⚙️ Accéder à la page de flux de l'application LITReview via `http://127.0.0.1:8000/feed`
- Visualiser le flux de tickets et critiques publiés, par ordre chronologique, les plus récents en premier 
- Créer un propre ticket en demandant une critique et l'afficher dans le flux via le bouton 
`Demander une critique` affiché en haut de la page de flux
- Créer une critique `à partir de zéro`, c'est-à-dire `pas en réponse à un ticket d'un autre utilisateur` : 
Créer un ticket et une critique pour les afficher dans le flux via le bouton `Créer une critique`,
affiché en haut de la page de flux
- Créer une critique en réponse à un ticket et l'afficher dans le flux via le bouton `Créer une critique` 
affiché dans une publication du ticket
- Accéder à la page d'abonnements via le lien `Abonnments` pour 
ajouter ou désabonner des utilisateurs à suivre et visualiser les abonnés
- Visualiser mes posts via le lien `Posts` et pouvoir modifier ou supprimer un ticket ou une critique
- Se déconnecter via le lien `Se déconnecter`
### 📖 Visiter les pages d'un utilisateur connecté