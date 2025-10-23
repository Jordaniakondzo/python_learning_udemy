# Ecrire dans un fichier JSON
import json

# Chemin du fichier JSON
fichier_json = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Exercices\Partie 02\fichier.json"

# Données à écrire dans le fichier JSON
json_data = {
    "nom": "Dupont",
    "prénom": "Jean",
    "âge": 30,
    "ville": "Paris",
    "profession": "Développeur"
}
# Écriture des données dans le fichier JSON avec une indentation pour la lisibilité.
# L'argument indent=4 permet de formater le JSON avec une indentation de 4 espaces.
# L'argument ensure_ascii=False permet de conserver les caractères non-ASCII (comme les accents) dans le fichier.
# La fonction dump() est utilisée pour écrire les données dans le fichier JSON.
with open(fichier_json, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)
