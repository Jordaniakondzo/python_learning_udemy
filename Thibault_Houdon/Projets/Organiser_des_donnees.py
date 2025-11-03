"""
Le but de projet est d'organiser éfficacement les données contenues dans le fichier texte 'prenoms.txt'.
Ainsi, nous allons tous les noms contenus dans ce fichier, les trier par ordre alphabétique, et les écrire dans un nouveau fichier 'prenoms_organises.txt'.
Etapes:
1. Ouvrir le fichier 'prenoms.txt' en mode lecture.
2. Récuper chaque prénom séparément et les stocker dans une liste.
3. Nettoyer les données en supprimant les espaces inutiles, les virgules et les lignes vides.
4. Ecrire la liste ordonnées et nettoyée dans un nouveau fichier 'prenoms_organises.txt'.

"""
from pathlib import Path

# Chemin du fichier 'prenoms.txt'
chemin_fichier = Path.cwd() / "Projets" / "prenoms.txt"

# Créer le fichier 'prenoms_organises.txt'
chemin_nouveau_fichier = Path.cwd() / "Projets" / "prenoms_organises.txt"
chemin_nouveau_fichier.touch(exist_ok=True)

# Étape 1: Ouvrir le fichier 'prenoms.txt' en mode lecture
contenu_fichier = chemin_fichier.read_text(encoding='utf-8')

# Étape 2: Récuper chaque prénom séparément et les stocker dans une liste.
# Diviser le contenu du fichier en lignes
lignes = contenu_fichier.splitlines()
# Initialiser une liste pour stocker les prénoms
prenoms = []
# Parcourir chaque ligne et extraire les prénoms
for ligne in lignes:
    prenoms_dans_ligne = ligne.split() # Diviser la ligne en prénoms basés sur les espaces et les virgules.
    # Ajouter chaque prénom à la liste principale
    for prenom in prenoms_dans_ligne:
        prenoms.append(prenom)

# Étape 3: Nettoyer les données en supprimant les espaces inutiles et les lignes vides.
# Initialiser une liste pour stocker les prénoms nettoyés
prenoms_nettoyes = []
# Parcourir chaque prénom contenu dans la liste 'prenoms' et le nettoyer
for prenom in prenoms:
    prenom_nettoye = prenom.strip(",. ").strip()  # Supprimer les espaces et les virgules
    if prenom_nettoye:  # Vérifier que le prénom n'est pas une chaîne vide
        prenoms_nettoyes.append(prenom_nettoye)

# Étape 4.1: Trier la liste des prénoms par ordre alphabétique.
# Ici nous utilisons la méthode sort() pour trier directement la liste en place.
# Alternativement, on pourrait utiliser la fonction sorted() pour créer une nouvelle liste triée.
prenoms_nettoyes.sort()

# Étape 4.2: Écrire la liste triée dans le fichier 'prenoms_organises.txt'.
chemin_nouveau_fichier.write_text('\n'.join(prenoms_nettoyes), encoding='utf-8')
