# Générer une base de données aléatoire dans un fichier JSON avec Faker
# Caractéristiques de la base de données :
# - 1000 utilisateurs ayant des noms uniques.
# - Chaque utilisateur a un nom unique, un prénom, une adresse e-mail, une adresse postale, une date de naissance et un numéro de téléphone.
# - Les années sont comprises entre 1950 et 2008.

import json
from faker import Faker
from pathlib import Path

# Créer une instance de Faker 
fake = Faker('fr_FR')  # Utiliser la locale française pour générer des données adaptées à la France

# Créer une liste vide pour stocker les données
data = []

# Créer 1000 utilisateurs et les ajouter à la liste
for _ in range(1000):
    user = {
        "name": fake.unique.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),  # Remplacer les sauts de ligne par des virgules pour une meilleure lisibilité
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=76).strftime("%Y-%m-%d"),
        "phone_number": fake.phone_number()
    }
    data.append(user)

# Enregistrer les données dans un fichier JSON
chemin_fichier = Path.cwd() / "Exercices" / "Partie_02" / "db_aleatoire.json"
with open(chemin_fichier, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)