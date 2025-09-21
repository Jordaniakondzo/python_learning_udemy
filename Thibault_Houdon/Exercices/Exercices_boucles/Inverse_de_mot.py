# Methode 1 : Utiliser la fonction reversed()
# La fonction reversed() retourne un itérateur qui parcourt la séquence en sens inverse.
mot = input("Entrez un mot : ")
reversed(mot)  # Ceci retourne un itérateur et n'affiche rien
# Pour afficher les lettres dans l'ordre inverse, on peut utiliser une boucle for
for lettre in reversed(mot):
    print(lettre, end=' ')

print("\n")  # Juste pour ajouter une ligne vide entre les deux méthodes
# Methode 2 : Utiliser une boucle for avec un index négatif
# On peut parcourir la chaîne de caractères en utilisant des indices négatifs
mot_1 = input("Entrez un mot : ")
for lettre in mot_1[::-1]:
    print(lettre, end=' ')