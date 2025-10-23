"""Lire le contenu d'un fichier texte et l'afficher à l'écran.
Sans oublier de gérer le chemin du fichier correctement.
On utilise une chaîne brute (raw string) pour éviter les problèmes avec les backslashes dans le chemin du fichier sous Windows.
"""
chemin = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Exercices\Partie_02\Texte.txt"
# Ouvrir le fichier en mode lecture avec encodage UTF-8 pour éviter les problèmes d'accents et afficher le contenu.
with open(chemin, "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)