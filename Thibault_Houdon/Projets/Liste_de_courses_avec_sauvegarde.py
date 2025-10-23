# Le but de ce projet est de créer un programme qui permet de gérer une liste de courses avec sauvegarde dans un fichier.
"""On va réaliser une version améliorée du programme précédent de la liste de courses avec la possibilité de sauvegarder les données dans un fichier JSON. Ainsi, la liste de courses persistera entre les différentes exécutions du programme.
On va utiliser le module json pour gérer la sérialisation et la désérialisation des données.
"""
import json
import sys
import os

# Définir le chemin du fichier de sauvegarde
chemin_fichier = r"C:\Users\User\Documents\GitHub\python_learning_udemy\Thibault_Houdon\Projets\liste_de_courses.json"

# Charger la liste de courses depuis le fichier JSON s'il existe
if os.path.exists(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        liste_de_courses = json.load(f)
# Sinon, initialiser une liste vide        
else:
    liste_de_courses = []

# Boucle principale
while True:
    # Choix de l'action à effectuer
    print("Choisissez par les 5 options suivantes:")
    print("1. Ajouter un élément à la liste")
    print("2. Supprimer un élément de la liste")
    print("3. Afficher la liste")
    print("4. Vider la liste")
    print("5. Quitter")
    choix = input("👉 Votre choix : ")
    if choix == "1":
        element = input("Entrez le nom de l'élément à ajouter : ")
        liste_de_courses.append(element)
        print(f"L'élément '{element}' a été ajouté à la liste.")
    elif choix == "2":
        element = input("Entrez le nom de l'élément à supprimer : ")
        if element in liste_de_courses:
            liste_de_courses.remove(element)
            print(f"L'élément '{element}' a été supprimé de la liste.")
        if not liste_de_courses:
            print("La liste est vide, il n'y a rien à supprimer.")    
        else:
            print(f"L'élément '{element}' n'est pas dans la liste.")
            print("Voici la liste actuelle :")
            # Affichage de la liste de courses avec les indices
            for index, item in enumerate(liste_de_courses):
                print(f"{index + 1}. {item}")
            print("Veuillez choisir un élément présent dans la liste pour le supprimer.")
    elif choix == "3":
        print("Liste de courses :")
        if not liste_de_courses:
            print("La liste est vide, il n'y a rien à afficher.")
        else:
            print("Voici le contenu de la liste :")
            for index, element in enumerate(liste_de_courses):
                print(f"{index + 1}. {element}")
    elif choix == "4":
        liste_de_courses.clear()
        print("La liste a été vidée de tous les éléments.")
    elif choix == "5":
        print("Au revoir!")
        # Sauvegarder la liste de courses dans le fichier JSON avant de quitter
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(liste_de_courses, f, indent=4, ensure_ascii=False)
        sys.exit()
    else:
        print("Choix invalide, veuillez réessayer.")
    print("_" * 50, "\n")  # Juste pour séparer les différentes itérations de la boucle
# Fin du programme