# <div align="center"> 🇫🇷 README ChessUp⬆︎  ♟</div>    
  
Bienvenue sur **ChessUp⬆︎**, l'appli pour gérer des tournois d'échecs en toute sérénité.  


Dans ce doc, tu trouveras comment l’installer, vérifier la qualité du style du code, et comment la lancer en local.

  

---  


> **Recommandations** :
>
> Pour profiter pleinement de l'app, active l’affichage des couleurs dans ton terminal (voir l’option `Preferences/Profiles/Colors` sous macOS, par exemple) et choisis un thème à fond sombre. L’expérience sera plus sympa !  

---  
  

## <div align="center"> 1. Clôner le repo Github</div>  
  

Ouvre ton terminal et rends-toi dans le dossier qui contiendra le repo github de **ChessUp⬆︎**.

```bash
cd le/chemin/de/mon_dossier
```

Et là effectue la commande git clone :

```bash
git clone https://github.com/dim-gggl/ChessUp_ChessTournamentProgram.git 
```

Et voilà, normalement, tu as reçu le code.

---

## <div align="center">2. Installer un environnement virtuel</div>  
  

Place-toi dans le dossier du repo **ChessUp⬆︎** avec la commande :

```bash
cd ChessUp_ChessTournamentProgram
```

Avant de lancer le programme, on installe un environnement virtuel :  
  

### Sous macOS / Linux :  
  

```bash
python -m venv .venv
```

puis

```bash
source .venv/bin/activate
```

et installe les dépendances :

```bash
pip install -r requirements.txt
```


#### Sous Windows :

```bash
python -m venv .venv
```

Ensuite :

```bash
.venv\Scripts\activate
```

et enfin, installe les dépendances avec 

```bash
pip install -r requirements.txt
```

> **Note** : Sur certaines versions de Python 3, il faut préciser `python3` au lieu de `python`.  
  
  
---  
  

## <div align="center"> 3. Générer un rapport flake8</div>  
  

Pour vérifier que le code est aux normes PEP8, on va utiliser **flake8** + **flake8-html** :

1. **Installer** les deux outils :
  

```bash
pip install flake8 flake8-html
```

2. **Configurer** flake8 :  
  

Pour enregistrer une configuration spécifique, crée un fichier ".flake8" dans le dossier racine du projet.
Dans ce fichier, commence par coller ceci :

```ini
[flake8]
max-line-length = 119
exclude =
    .venv,
    .git,
    __pycache__
```

Ajoute les dossiers que tu veux que flake8 ignore à cette liste.

3. **Lancer** flake8 en mode HTML :  
  

```bash
flake8 . --format=html --htmldir=flake8_report
```

Un dossier `flake8_report` sera créé dans le dossier racine du projet, contenant le rapport détaillé.  
Tu n'auras qu'à ouvrir le fichier "index.html" et tout y sera très clair.

---

## <div align="center"> 4. Lancer **ChessUp⬆︎**</div>  
  

Toujours depuis le dossier du repo "ChessUp_ChessTournamentProgram", exécute :

```bash
python chess_up.py
```

Et la page d'accueil de ChessUp devrait s'afficher.  
Après quoi tu arrives au Menu Principal.

---

## <div align="center"> Conseils d’utilisation</div>  
  

- **Ajouter de nouveaux joueurs** se fait via le Menu **JOUEURS** : on te demandera prénom, nom, date de naissance, etc.
- **Inscrire des joueurs à un tournoi** se fait via le Menu **TOURNOIS**, une fois que tu as créé ou sélectionné un tournoi.
- **Gérer les rounds et entrer les scores** : tu peux lancer chaque round depuis le menu Tournoi, puis saisir les résultats match par match.  
  
---  
  
## <div align="center"> Le fonctionnement global</div> 
  
1. Crée un tournoi (Menu **Tournois**).  
  
2. Ajoute des joueurs (Menu **Joueurs**) puis inscris-les à ton tournoi (toujours dans le Menu **Tournois**).  
  
3. Lance les rounds, saisis les résultats, et poursuis jusqu’à la fin.  
  
  
N’hésite pas à explorer les Menus **Rapports** pour générer des stats ou exporter des listes. 

---
---


# <div align="center"> 🇬🇧 README ChessUp⬆︎ ♟</div>

(At least, documentation is available in english ! ) 
  
Welcome to **ChessUp⬆︎**, the app for managing chess tournaments with complete peace of mind.  


In this doc, you'll find out how to install it, check the quality of the code style, and how to run it locally.

  

---


> **Recommendations** :
>
> To get the most out of the app, activate the colour display in your terminal (see the `Preferences/Profiles/Colors` option on macOS, for example) and choose a theme with a dark background. It'll be a much more pleasant experience!  

---
  

## <div align="center">1. Clone the Github repo</div>
  

Open your terminal and go to the folder that will contain the **ChessUp⬆︎** github repo.

```bash
cd the/path/to/my_folder
```

Then run the git clone command:

```bash
git clone https://github.com/dim-gggl/ChessUp_ChessTournamentProgram.git
```

And that's it, you should have received the code.

---

## <div align="center">2. Installing a virtual environment</div>
  

Go to the repo folder **ChessUp⬆︎** with the command :

```bash
cd ChessUp_ChessTournamentProgram
```

Before running the program, we install a virtual environment:
  

### Under macOS / Linux :
  

```bash
python -m venv .venv
```

then

```bash
source .venv/bin/activate
```

and install the dependencies:

```bash
pip install -r requirements.txt
```


#### On Windows :

```bash
python -m venv .venv
```

Then :

```bash
.venv\Scripts\activate
```

and finally, install the dependencies with

```bash
pip install -r requirements.txt
```

> **Note** : On some versions of Python 3, you must specify `python3` instead of `python`.  
  
  
---
  

## <div align="center">3. Generate a flake8 report</div>
  

To check that the code is PEP8 compliant, we'll use **flake8** + **flake8-html** :

1. **Install** both tools:
  

```bash
pip install flake8 flake8-html
```

2. **Configure** flake8 :
  

To save a specific configuration, create a ".flake8" file in the project's root folder.
In this file, start by pasting the following:

```ini
[flake8]
max-line-length = 119
exclude =
    .venv,
    .git,
    __pycache__
```

Add the folders you want flake8 to ignore to this list.

3. **Launch** flake8 in HTML mode:  
  

```bash
flake8 . --format=html --htmldir=flake8_report
```

A `flake8_report` folder will be created in the project root folder, containing the detailed report.  
All you have to do is open the "index.html" file and everything will be very clear.

---

## <div align="center"> 4. Run **ChessUp⬆︎**</div>
  

Still from the "ChessUp_ChessTournamentProgram" repo folder, run :

```bash
python chess_up.py
```
> Or `python3 chess_up.py`

And the ChessUp home page should appear.  
Then you arrive at the Main Menu.

---

## <div align="center"> Advice on use</div>
  

- Adding **new players** is done via the **PLAYERS** Menu: you will be asked for first name, surname, date of birth, etc.
- Registering players for a **tournament** is done via the **TOURNAMENTS** Menu, once you have created or selected a tournament.
- Manage **rounds** and enter **scores**: you can launch each round from the Tournament menu, then enter the results match by match.  
  
---
  
## <div align="center"> Overall operation</div>
  
1. Create a tournament (Menu **Tournaments**).  
  
2. Add players (**Player Menu**) then register them in your tournament (still in the **Tournaments Menu**).  
  
3. Start the rounds, enter the results and continue to the end.  
  
  
Feel free to explore the **Reports** Menus to generate stats or export lists.






