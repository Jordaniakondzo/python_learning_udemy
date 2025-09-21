# Le de but de cet exercice est de pratiquer la compréhension de listes en Python.
# On va créer plusieurs listes en utilisant des compréhensions de listes.

# Liste 1 : Nombres pairs à partir d'une liste donnée
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [n for n in nombres if n % 2 == 0]
print(nombres_pairs)

# Liste 2 : Nombres positifs dans une plage donnée
nombres = range(-10, 10)
nombres_positifs = [n for n in nombres if n >= 0]
print(nombres_positifs)

# Liste 3 : Doubler les nombres dans une plage donnée
nombres = range(5)
nombres_doubles = [n * 2 for n in nombres]
print(nombres_doubles)

# Liste 4 : Inverser les nombres dans une plage donnée uniquement pour les nombres impairs
nombres = range(10)
nombres_inverses = [n if n % 2 == 0 else -n for n in nombres]
print(nombres_inverses)

# Liste 5 : Nombres impairs à partir d'une liste donnée
nombres = range(51)
nombres_impairs = [n for n in nombres if n % 2 != 0]
print(nombres_impairs)

# Liste 6 : Recupérer uniquement les villes ayant plus de 7 lettres
villes = ["Paris", "Londres", "New York", "Los Angeles", "Tokyo", "Berlin", "Madrid"]
villes_longues = [ville for ville in villes if len(ville) > 7]
print(villes_longues)