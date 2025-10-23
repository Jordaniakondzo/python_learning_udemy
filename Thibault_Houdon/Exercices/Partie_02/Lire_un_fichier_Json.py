# Lire un fichier JSON
import json

# Chemin du fichier JSON
fichier_json = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Exercices\Partie_02\fichier.json"

# Ouverture du fichier en mode lecture avec encodage UTF-8 pour gérer correctement les caractères spéciaux.
with open(fichier_json, "r", encoding="utf-8") as f:
    # Chargement des données JSON depuis le fichier
    # Les données sont stockées dans la variable "data"
    # La fonction load() est utilisée pour lire les données à partir du fichier JSON.
    data = json.load(f)
    # Affichage des données lues
    print(data)