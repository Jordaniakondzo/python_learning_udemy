# Le but de cet exercice est de créer une calculatrice simple qui gère les erreurs d'entrée de l'utilisateur.
premier_nombre = input("Entrez le premier nombre: ")
deuxieme_nombre = input("Entrez le deuxieme nombre: ")
if all(n.isdigit() for n in [premier_nombre, deuxieme_nombre]):
    premier_nombre = int(premier_nombre)
    deuxieme_nombre = int(deuxieme_nombre)
    resultat = premier_nombre + deuxieme_nombre
    # L'application de la méthode f-string pour afficher le résultat de l'addition de deux nombres
    print(f"Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est: {resultat}")
else:
    print("Erreur: Veuillez entrer des nombres valides.")