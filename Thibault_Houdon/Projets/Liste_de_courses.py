# Le but de ce projet est de créer un programme qui permet de gérer une liste de courses.
"""On va réaliser une version simple de la liste de courses avec la création d'une liste en mémoire à laquelle on ajoute, on enlève des éléments, on affiche la liste et on vide la liste par l'utilisateur.
On va utiliser une boucle while pour permettre à l'utilisateur de faire plusieurs actions jusqu'à ce qu'il décide de quitter le programme.
"""
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
        break
    else:
        print("Choix invalide, veuillez réessayer.")
    print("_" * 50, "\n")  # Juste pour séparer les différentes itérations de la boucle
# Fin du programme