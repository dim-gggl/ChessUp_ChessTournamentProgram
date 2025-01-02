import json
import os

def save_to_json(file_path, new_data, overwrite=False):
    """
    Sauvegarde les données dans un fichier JSON.
    - Si overwrite est False, on ajoute new_data aux données existantes.
    - Sinon, on écrase tout (overwrite = True).
    """
    try:
        if not overwrite:
            with open(file_path, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = []
    except FileNotFoundError:
        existing_data = []

    if isinstance(new_data, list):
        existing_data.extend(new_data)
    else:
        existing_data.append(new_data)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=4)

def load_from_json(file_path):
    """
    Charge les données depuis un fichier JSON et renvoie un tableau de dicts.
    Retourne une liste vide si le fichier n'existe pas ou est vide.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = f.read().strip()
            if not data:  # fichier vide
                return []
            return json.loads(data)
        except json.JSONDecodeError as e:
            print(f"[ERREUR] Problème de format JSON dans {file_path}: {e}")
            return []
