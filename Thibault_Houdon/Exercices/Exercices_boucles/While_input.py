# Demander à l'utilisateur s'il veut continuer, et continuer tant qu'il répond "o"
# Ainsi la boucle s'arrête quand il répond "n" ou autre chose que "o", si non elle sera infinie
continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")