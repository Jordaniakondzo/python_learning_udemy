# Dans ce programme, l'utilisateur doit deviner un nombre mystère entre 1 et 100 choisi aléatoirement par l'ordinateur.
# L'utilisateur a un nombre limité de tentatives pour deviner le nombre.
# Le programme donne des indices si le nombre proposé est plus grand ou plus petit que le nombre mystère.
# On utilise la bibliothèque random pour générer le nombre mystère et la bibliothèque time pour ajouter des pauses dans le jeu.
import random
import time

print("Bienvenue dans le jeu du nombre mystère !")
time.sleep(2)
print("Je pense à un nombre entre 1 et 100.")
time.sleep(2)
print("Essayez de le deviner !")
time.sleep(2)

nombre_mystere = random.randint(1, 100)
tentatives = 5
print(f"Vous avez {tentatives} tentatives pour deviner le nombre.")

while True:
    if tentatives == 0:
        print(f"Désolé, vous avez épuisé toutes vos tentatives. Le nombre mystère était {nombre_mystere}.")
        print("Fin du jeu.")
        # Option pour rejouer le jeu si l'utilisateur n'a pas réussi à deviner le nombre
        print("Voulez-vous réessayer ? (o/n)")
        # La fonction lower() permet de convertir la saisie de l'utilisateur en minuscules
        reessayer = input().lower()
        # Si l'utilisateur veut rejouer, on réinitialise le jeu avec un nouveau nombre mystère et le nombre de tentatives, si non on quitte le jeu
        if reessayer == 'o':
            nombre_mystere = random.randint(1, 100)
            tentatives = 5
            print("Nouveau jeu !")
            print(f"Vous avez {tentatives} tentatives pour deviner le nombre.")
            continue
        else:
            break
    print(f"\nIl vous reste {tentatives} tentative{tentatives > 1 and 's' or ''}.")
    essai = input("Entrez votre proposition : ")
    if not essai.isdigit():
        print("Erreur: Veuillez entrer un nombre valide entre 1 et 100.")
        continue
    essai = int(essai)
    if essai < 1 or essai > 100:
        print("Erreur: Le nombre doit être entre 1 et 100.")
        continue
    if essai == nombre_mystere:
        print("Félicitations ! Vous avez deviné le nombre mystère !")
        print(f"Vous avez trouvé le nombre en {6 - tentatives} tentatives.")
        print("Fin du jeu.")
        # Option pour rejouer le jeu si l'utilisateur a réussi à deviner le nombre
        print("Voulez-vous jouer à nouveau ? (o/n)")
        reessayer = input().lower()
        if reessayer == 'o':
            nombre_mystere = random.randint(1, 100)
            tentatives = 5
            print("Nouveau jeu !")
            print(f"Vous avez {tentatives} tentatives pour deviner le nombre.")
            continue
        else:
            break
    elif essai < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    else:
        print("Le nombre mystère est plus petit.")
    tentatives -= 1
    
print("Merci d'avoir joué 😊!")
# Fin du programme
