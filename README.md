# Repository name : OC_Project_09_Repository
```
Développer une application web en utilisant Django
```
# 💿 Installer Python
Pour installer Python, il suffit d'utiliser l'une des urls :
```
https://www.python.org/downloads/windows/
https://www.python.org/downloads/macos/
https://www.python.org/downloads/source/
```
# 💿 Installer PyCharm Community
Pour installer PyCharm Community, il suffit d'utiliser l'une des urls :
```
https://www.jetbrains.com/fr-fr/pycharm/download/download-thanks.html?platform=windows&code=PCC
https://www.jetbrains.com/fr-fr/pycharm/download/download-thanks.html?platform=mac&code=PCC
https://www.jetbrains.com/fr-fr/pycharm/download/download-thanks.html?platform=linux&code=PCC
```
# 📖 Créer un nouveau dossier qui va contenir un repository GitHub
Pour créer un nouveau dossier, il suffit de choisir l'endroit et le nom du dossier. Par exemple, OC_P09.
# 📖 Lancer PyCharm Community et Ouvrir ce nouveau dossier sans choisir l'environnement virtuel existant
Lors de l'ouverture du nouveau dossier, par exemple OC_P09, un nouveau dossier nommé .idea sera créé
Pour savoir le contenu de votre dossier, il suffit de taper, dans le terminal, la commande :
```
OC_P09>ls
```
# 📖 Créer un nouvel environnement virtuel
Pour créer un nouvel environnement virtuel, nommé ENV, il suffit de taper, dans le terminal, la commande :
```
OC_P09>python -m venv ENV
``` 
# 📖 Activer le nouvel environnement virtuel
Pour activer le nouvel environnement virtuel, nommé ENV, il suffit de taper, dans le terminal, la commande :
```
OC_P09>ENV/Scripts/activate
``` 
# 📖 Configurer le nouvel environnement virtuel et choisir l'interpréteur Python
Pour configurer le nouvel environnement virtuel, nommé ENV, il suffit de :
```
Accéder au menu File et choisir Settings ou Utiliser le raccourci clavier Ctrl+Alt+S
Selectionner Project:OC_P09
Choisir Python Interpreter
Sélectionner ./ENV/Scripts/python.exe
``` 
# 📖 Mettre à jour le module pip
Pour mettre à jour le module pip, il suffit de taper, dans le terminal, la commande :
```
(ENV) OC_P09>python -m pip install --upgrade pip
``` 
# 📖 Cloner depuis GitHub le projet Django
Pour cloner depuis GitHub le projet Django, il suffit d'utiliser la commande :
```
(ENV) OC_P09>git clone https://github.com/RochdiGZ/OC_Project_09_Repository.git
```
Après le clonage du projet Django, un dossier OC_Project_09_Repository sera ajouté dans le dossier OC_P09.
# 📖 Modifier les propriétés du dossier OC_Project_09_Repository comme source de données
Pour Modifier les propriétés du dossier OC_Project_09_Repository comme source de données, il suffit de :
```
Sélectionner le dossier
Utiliser le bouton droit de la souris et choisir Mark Directory as > Sources Root
```
# 💿 Installer tous les modules du projet Django à partir du dossier OC_Project_09_Repository
Pour accéder au dossier OC_Project_09_Repository, il suffit de taper, dans le terminal, la commande :
```
(ENV) OC_P09>cd OC_Project_09_Repository
```
Pour installer tous les modules du projet Django, il suffit de taper, dans le terminal, la commande :
```
(ENV) OC_P09\OC_Project_09_Repository>pip install -r requirements.txt
```
# ⚙️ Créer le dossier flake_8_report
Pour créer le dossier flake8_report, il suffit de taper, dans le terminal, la commande :
```
(ENV) OC_P09\OC_Project_09_Repository>flake8 --format=html --htmldir=flake8_report --max-line-length=119
```
# ⚙️ Lancer le serveur de développement
Pour lancer le serveur de développement en local, il suffit de taper, dans le terminal, la commande :
```
python manage.py runserver
``` 
Vous devez bien sûr au préalable vous assurer d'avoir activé votre environnement virtuel et de vous trouver
dans le dossier qui contient le fichier `manage.py`.
Pour notre cas, on tape taper, dans le terminal, la commande :
```
(ENV) OC_P09\OC_Project_09_Repository>python manage.py runserver
``` 
Une fois le serveur de développement lancé, vous pouvez voir la page d'accueil par défaut de votre projet Django
à l'adresse `http://127.0.0.1:8000` dans un navigateur web.
```
[image](./media/serveur.png)
```
# ⚙️ Lancer la page de connexion à notre site web
Pour lancer la page de connexion à notre site web, il suffit d'utiliser un navigateur web et utiliser l'url :
`http://127.0.0.1:8000`
# ⚙️ Lancer l'interface de l'administration Django
Pour lancer l'interface de l'administration Django, il suffit d'utiliser un navigateur web et utiliser l'url :
`http://127.0.0.1:8000/admin`
# ⚙️ Se connecter avec l'interface de l'administration Django
Pour se connecter avec l'interface de l'administration Django,
il faut créer un super utilistaeur en tapant, dans le terminal, la commande :
```
(ENV) OC_P09\OC_Project_09_Repository>python manage.py createsuperuser
``` 
Dans l'étape suivante, il suffit de rester dans le terminal pour 
taper un nom d'utlisateur et un mot de passe avec confirmation du mot de passe