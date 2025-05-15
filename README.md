# <div align='center'>🇬🇧

# <div align='center'>ChessUp⬆︎<br> _Chess Tournament CLI_

> **Organize and manage an entire open chess tournament from start to finish, right in your terminal — no spreadsheets, no hassle, no distractions.**

---

## <div align='center'>✨ Key Features

| What you get                        | Details                                                                                                                                                                                              |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Fully featured CLI workflow**     | Set up new tournaments, register players, generate rounds, input match outcomes, track standings, and manage reports — all within an intuitive, interactive terminal interface.                      |
| **Swiss-style pairing algorithm**   | Automatically pairs players intelligently between rounds, avoiding repeat matchups and allocating byes when participant count is uneven. Ensures fair, efficient pairings throughout the tournament. |
| **Robust persistent storage**       | All tournament data and player details are stored as JSON files in the `data/` folder. You can exit the program anytime and resume exactly where you left off — no data lost.                        |
| **Enhanced CLI readability**        | Custom-built `ansify()` utility enhances the UI with ANSI color codes for better clarity and accessibility in both light and dark terminal environments.                                             |
| **Clean and maintainable codebase** | Fully PEP 8 compliant with flake8 support. Includes a ready-to-use HTML report generator to help you keep the code lint-free and maintainable over time.                                             |

These features are fully operational and included in the repository — no future promises, only working code.

---

## <div align='center'>🚀 Quick Start Guide

```bash
# Step 1 — Clone the repo
$ git clone https://github.com/dim-gggl/Chess_Up.git
$ cd Chess_Up

# Step 2 — Create and activate a virtual environment
$ python -m venv .venv                  # On Windows: python -m venv .venv && .venv\Scripts\activate
$ source .venv/bin/activate             # macOS/Linux

# Step 3 — Install dependencies
$ pip install -r requirements.txt

# Step 4 — Launch the app
$ python chess_up.py                    # Use python3 if needed
```

On first launch, you’ll land on a straightforward **Main menu** interface:

```
1 — TOURNAMENTS
2 — PLAYERS
3 — REPORTS
4 — SAVE ALL
q — QUIT
```

Use the numeric shortcuts to navigate — the interface is fully guided and beginner-friendly.

---

## <div align='center'>🛠 Typical Workflow

1. Navigate to **Players Menu** to add participants. You’ll input first and last names, date of birth, and optionally a FIDE ID for each.
2. Open the **Tournaments Menu**, create a new tournament, and fill in the details like name, location, date, and number of rounds.
3. Still within the **Tournaments Menu**, assign registered players to the newly created event.
4. Start the first round — the app will pair matches, you’ll input results, and close the round. Repeat the process until the final round.
5. Don’t forget: you can press **4 — SAVE ALL** anytime to save progress. Everything is stored safely and can be resumed later.

Pro tip: if your player list has an odd number, ChessUp automatically assigns a bye (worth 1 point) to a random unpaired player. 🤓

---

## <div align='center'>📂 Project Structure Overview

```
📦Chess_Up
 ┣ 📂controllers   # Core logic: menu flow, input handling, round mechanics
 ┣ 📂models        # Data models: Player, Tournament, Round, Match, Score
 ┣ 📂views         # Display logic: colored menus, text rendering, UI helpers
 ┣ 📂utils         # Reusable utilities: validation, JSON I/O, sorting, formatting
 ┣ 📂data          # Persistent storage: auto-generated JSON player/tournament files
 ┣ chess_up.py     # Entry point: boots MainMenu and starts the app
 ┗ requirements.txt
```

---

## <div align='center'>🧹 Code Quality & Linting

Keep your code neat with `flake8` and its HTML report plugin:

```bash
# Install linting tools (only once)
$ pip install flake8 flake8-html

# Generate HTML report from root directory
$ flake8 . --format=html --htmldir=flake8_report

# Open flake8_report/index.html in any browser to review warnings
```

There is also a sample `flake8_report/` directory included in the repository for reference.

---

## <div align='center'>📈 Roadmap / Contribution Ideas

ChessUp is already functional and stable as a terminal-based tournament manager, but future expansions are welcome:

* Add support for alternative pairing systems (e.g. FIDE-compliant Swiss pairing, round‑robin formats, Kö system…)
* Enhanced import/export support for PGN (game logs), CSV (spreadsheet editing), and PDF (printable reports)
* RESTful API back-end or full web interface (e.g. Flask, FastAPI + React frontend)
* Automated test coverage using `pytest` and `coverage`

Security disclosure policy is available in **SECURITY.md**.
Note: no license yet — open to suggestions or discussions.

---

Lovingly crafted with plenty of coffee ☕, strategic thinking ♟, and long nights of debugging by **Dimitri Gaggioli**, right from the heart of Paris in 2025. This project blends code, logic, and passion to make tournament management feel like a game well played — practical, empowering, and geeky in all the right ways.


# <div align="center"> 🇫🇷
# <div align="center">ChessUp⬆︎ <br> _**Gestionnaire de Tournois d’Échecs en Ligne de Commande**_

> **Organisez et administrez un open d’échecs complet, du premier coup jusqu’à la remise des prix, sans jamais quitter votre terminal : pas de tableur, pas de galère, juste le jeu.**

---

## <div align="center">✨ Fonctionnalités phares

| Ce que ça fait                  | Détails                                                                                                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Flux CLI complet**            | Créez un tournoi, enregistrez les joueurs, générez les rondes, saisissez les résultats, suivez le classement et éditez des rapports — le tout via une interface interactive ultra‑lisible. |
| **Appariement style Suisse**    | L’algorithme évite les re‑matchs et attribue automatiquement un bye si le nombre de joueurs est impair, garantissant des rencontres équitables à chaque ronde.                             |
| **Stockage persistant en JSON** | Toutes les données (tournois, joueurs, scores) sont enregistrées dans `data/`. Quittez l’appli quand vous voulez ; au redémarrage vous reprenez exactement où vous étiez.                  |
| **Lisibilité colorisée**        | L’utilitaire interne `ansify()` injecte des couleurs ANSI pour une interface claire, que votre terminal soit en thème clair ou sombre.                                                     |
| **Code propre & maintenable**   | Conforme PEP 8, avec `flake8` et génération de rapports HTML pour garder la base de code nickel chrome.                                                                                    |

Ces fonctionnalités sont déjà disponibles dans le dépôt — zéro vaporware, que du concret.

---

## <div align="center">🚀 Mise en route express

```bash
# Étape 1 — Cloner le dépôt
$ git clone https://github.com/dim-gggl/Chess_Up.git
$ cd Chess_Up

# Étape 2 — Créer et activer un environnement virtuel
$ python -m venv .venv                  # Sous Windows : python -m venv .venv && .venv\Scripts\activate
$ source .venv/bin/activate             # macOS/Linux

# Étape 3 — Installer les dépendances
$ pip install -r requirements.txt

# Étape 4 — Lancer l’application
$ python chess_up.py                    # Utilisez python3 si nécessaire
```

Au premier lancement, vous arrivez sur le **menu principal** :

```
1 — TOURNAMENTS
2 — PLAYERS
3 — REPORTS
4 — SAVE ALL
q — QUIT
```

Chaque option est auto‑documentée, impossible de se perdre.

---

## <div align="center">🛠 Flux de travail type

1. Rendez‑vous dans le **Players Menu** pour ajouter les participants : nom, prénom, date de naissance, et éventuellement l’ID FIDE.
2. Ouvrez le **Tournaments Menu**, créez un nouveau tournoi et renseignez le nom, le lieu, les dates et le nombre de rondes.
3. Toujours dans le **Tournaments Menu**, assignez les joueurs enregistrés à l’événement fraîchement créé.
4. Lancez la première ronde : l’appli effectue les appariements, vous saisissez les scores, puis vous clôturez la ronde. Répétez jusqu’à la fin du tournoi.
5. Besoin d’une pause ? Appuyez à tout moment sur **4 — SAVE ALL** pour sauvegarder. Votre progression est sécurisée.

Astuce : si le nombre de joueurs est impair, ChessUp attribue automatiquement un bye (valant 1 point) à un joueur non encore exempté. 🎲

---

## <div align="center">📂 Arborescence du projet

```
📦Chess_Up
 ┣ 📂controllers   # Logique métier : menus, gestion d’entrées, mécaniques de rondes
 ┣ 📂models        # Modèles de données : Player, Tournament, Round, Match, Score
 ┣ 📂views         # Rendu CLI : menus colorés, helpers d’affichage
 ┣ 📂utils         # Outils réutilisables : validation, I/O JSON, tri, formatage
 ┣ 📂data          # Stockage persistant : fichiers JSON générés pour joueurs et tournois
 ┣ chess_up.py     # Point d’entrée : lance MainMenu
 ┗ requirements.txt
```

---

## <div align="center">🧹 Qualité & linting

Préservez un code irréprochable grâce à `flake8` :

```bash
# Installer les outils (une seule fois)
$ pip install flake8 flake8-html

# Générer un rapport HTML depuis la racine du projet
$ flake8 . --format=html --htmldir=flake8_report

# Ouvrez flake8_report/index.html dans votre navigateur et corrigez ce qui pique 👀
```

Un exemple de dossier `flake8_report/` est déjà inclus pour vous montrer le rendu.

---

## <div align="center">📈 Feuille de route / idées de contribution

ChessUp est stable et pleinement opérationnel en mode terminal, mais de nombreuses évolutions restent possibles :

* Intégrer d’autres systèmes d’appariement (Suisse FIDE complet, round‑robin, système Kö, etc.)
* Ajouter des exports/imports en PGN (logs de parties), CSV (édition tableur) et PDF (rapports imprimables)
* Déployer une API REST ou une interface web complète (Flask/FastAPI + React)
* Couvrir le code avec des tests automatisés (`pytest` + `coverage`)

La politique de divulgation se trouve dans **SECURITY.md**. Licence non définie pour le moment — on est ouverts à la discussion.

---

Conçu avec beaucoup de café ☕, un sens aigu de la stratégie ♟ et d’innombrables nuits de débogage par **Dimitri Gaggioli**, directement depuis Paris en 2025. Ce projet fusionne code, logique et passion pour transformer la gestion de tournois en une partie gagnante — pratique, puissante et résolument geek.

---
