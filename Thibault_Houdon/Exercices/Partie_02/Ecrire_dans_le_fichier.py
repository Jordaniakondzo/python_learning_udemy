# Ecrire dans un fichier texte
# Ce programme écrit plusieurs lignes de texte dans un fichier.
chemin = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Exercices\Partie 02\Texte.txt"
# Ouvrir le fichier en mode écriture avec encodage UTF-8 pour gérer les caractères spéciaux.
# Ici avec "w", le fichier sera créé s'il n'existe pas ou écrasé s'il existe déjà.
with open(chemin, "w", encoding="utf-8") as fichier:
    fichier.write("Ceci est une ligne écrite dans le fichier.\n")
    fichier.write("Voici une autre ligne avec des caractères spéciaux : é, è, à, ü, ñ.\n")
    fichier.write("Fin du fichier.")
# Pour remplir sans écraser le contenu existant, on peut utiliser le mode "a" (append) à la place de "w".
with open(chemin, "a", encoding="utf-8") as fichier:
    fichier.write("\nCette ligne a été ajoutée à la fin du fichier.\n")