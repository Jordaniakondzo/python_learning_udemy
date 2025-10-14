# Calculatrice avec gestion d'erreurs pour les entrées non numériques et la division par zéro
# L'utilisateur peut entrer des nombres entiers ou décimaux, positifs ou négatifs
premier_nombre = deuxieme_nombre = ""
operation = input("Choisissez une opération (+, -, *, /) : ")

# Boucle pour obtenir deux nombres valides (entiers ou décimaux, positifs ou négatifs)
while True:
    premier_nombre = input("Entrez le premier nombre: ")
    deuxieme_nombre = input("Entrez le deuxieme nombre: ")
    # Vérifie si les deux entrées sont des nombres valides (entiers ou décimaux)
    try:
        premier_nombre_float = float(premier_nombre)
        deuxieme_nombre_float = float(deuxieme_nombre)
        break
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides (entiers ou décimaux).")

# Calcul selon l'opération choisie par l'utilisateur
if operation == '+':
    resultat = premier_nombre_float + deuxieme_nombre_float
elif operation == '-':
    resultat = premier_nombre_float - deuxieme_nombre_float
elif operation == '*':
    resultat = premier_nombre_float * deuxieme_nombre_float
elif operation == '/':
    if deuxieme_nombre_float == 0:
        print("Erreur: Division par zéro n'est pas permise.")
        exit()
    resultat = round(premier_nombre_float / deuxieme_nombre_float, 2)
else:
    print("Erreur: Opération non reconnue.")
    exit()

print(f"Le résultat de l'opération {operation} entre {premier_nombre_float} et {deuxieme_nombre_float} est: {resultat}")
# ...existing code...