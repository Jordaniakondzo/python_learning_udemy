# Ajouter des données dans un fichier JSON
import json

# Chemin du fichier JSON
fichier_json = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Exercices\Partie_02\fichier.json"

# On ouvre d'abord le fichier en mode lecture pour charger les données existantes.
# fichier_json ici est le chemin vers le fichier JSON et f est l'objet du fichier contenu dans la variable data.
with open(fichier_json, "r", encoding="utf-8") as f:
    # Chargement des données JSON depuis le fichier existant.
    data = json.load(f)

# Ajout de nouvelles données au dictionnaire existant.
nouvelles_donnees = {
    "nom": "Dupont",
    "prénom": "Jean",
    "âge": 30,
    "status": "Marié",
    "ville": "Paris",
    "profession": "Développeur"
}

# On ajoute les nouvelles données au dictionnaire existant
data.update(nouvelles_donnees)

# On ouvre le fichier en mode écriture pour sauvegarder les modifications
with open(fichier_json, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
