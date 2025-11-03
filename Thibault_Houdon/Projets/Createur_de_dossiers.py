"""
Le but de ce projet est de créer une structure de dossiers contenue dans un dictionnaire à l'interieur
du dossier contenu dans le chemin à spécifier.
On utilise les modules pathlib pour manipuler les chemins de fichiers.
"""
import pathlib
import shutil

# Définir le chemin du dossier parent où les dossiers principaux et sous-dossiers seront créés
chemin_parent = pathlib.Path.cwd() / "Projets" / "Dossier_test"

# Créer le dossier parent s'il n'existe pas déjà
chemin_parent.mkdir(exist_ok=True)

# Définir les dossiers principaux et leurs sous-dossiers dans un dictionnaire
dossiers_principaux = {
    "Films": ["Le seigneur des anneaux", "Harry Potter", "Moon", "Forrest Gump"],
    "Series": ["Breaking Bad", "Game of Thrones", "Stranger Things", "The Crown"],
    "Documentaires": ["Planet Earth", "The Last Dance", "Making a Movie", "The Secret Life of Pets"],
    "Animes": ["Naruto", "One Piece", "Attack on Titan", "My Hero Academia"],
    "Mangas": ["Death Note", "Fullmetal Alchemist", "Demon Slayer", "Jujutsu Kaisen"]
}

# Parcourir le dictionnaire et créer les dossiers principaux et leurs sous-dossiers
for dossier_principal, sous_dossiers in dossiers_principaux.items():
    for sous_dossier in sous_dossiers:
        # Créer le chemin complet du sous-dossier
        chemin_dossier = chemin_parent / dossier_principal / sous_dossier
        # Créer le sous-dossier s'il n'existe pas déjà
        chemin_dossier.mkdir(parents=True, exist_ok=True)

# Suppression du dossier de test et de tout son contenu (dossiers et sous-dossiers) après la création pour éviter l'encombrement du dossier de travail ou formation.
# shutil.rmtree(chemin_parent)