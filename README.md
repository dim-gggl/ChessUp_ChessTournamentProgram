# <div align="center">README ChessUp⬆︎</div>    
  
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
source .venv/bin/activate
pip install -r requirements.txt
```  
  

### Sous Windows :  
  

```bash
python -m venv .venv
.venv\Scripts\activate
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

Un dossier `flake8_report`, déjà dans le dossier racine du projet, accueillera le rapport détaillé.  
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
