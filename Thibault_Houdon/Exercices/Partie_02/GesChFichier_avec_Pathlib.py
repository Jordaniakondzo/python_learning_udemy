from pathlib import Path
import shutil

# Obtenir le chemin du dossier courant
p = Path.cwd()
print(f"Current working directory: {p}")

# Lire le contenu du dossier courant avec la methode iterdir() qui permet de lister les fichiers et dossiers présents dans un répertoire.
for child in p.iterdir():
    print(child.name, child.is_file(), child.is_dir())

# Créer un nouveau dossier dans le dossier courant à l'aide de la méthode mkdir() qui permet de créer un nouveau répertoire.
nouveau_dossier = p / "Nouveau_Dossier"
nouveau_dossier.mkdir()
print(f"Dossier créé: {nouveau_dossier}")

# Supprimer le dossier créé dans le dossier courant à l'aide de la bibliothèque shutil qui permet de supprimer un dossier non vide.
shutil.rmtree(nouveau_dossier)

# Créer un fichier texte dans le dossier courant à l'aide de la méthode touch() qui permet de créer un fichier vide.
fichier = p / "Nouveau_Fichier.txt"
fichier.touch()
print(f"Fichier créé: {fichier}")

# Ecrire du texte dans le fichier créé à l'aide de la méthode write_text() qui permet d'écrire du texte dans un fichier.
fichier.write_text("Ceci est un nouveau fichier texte.")

# Lire le contenu du fichier créé à l'aide de la méthode read_text() qui permet de lire le contenu d'un fichier.
contenu = fichier.read_text()
print(contenu)

# Supprimer le fichier créé à l'aide de la méthode unlink() qui permet de supprimer un fichier.
fichier.unlink()

# Note : Le module glob peut également être utilisé pour rechercher des fichiers et des dossiers en fonction de motifs spécifiques.
# Par exemple, pour trouver tous les fichiers texte dans le dossier courant :
import glob

# Utilisation de glob pour trouver tous les fichiers texte dans un dossier spécifique et les afficher.
P = Path.cwd() / 'Exercices' / 'Partie_02'
print(P.glob('*.txt'))  # Affichage du générateur de fichiers texte.
# Itérateur sur tous les fichiers texte dans le dossier courant
for file in P.glob('*.txt'):
    print(file)

# Le module rglob permet de faire des recherches récursives dans le dossier courant et les sous-dossiers.
# Par exemple, pour trouver tous les fichiers texte dans le dossier courant et ses sous-dossiers :
P = Path.cwd() / 'Exercices' / 'Partie_02'
print(P.rglob('*.txt'))  # Itérateur sur tous les fichiers texte dans le dossier courant et ses sous-dossiers
for file in P.rglob('*.txt'):
    print(file)