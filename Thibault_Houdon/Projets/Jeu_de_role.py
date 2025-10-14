# Le but de ce projet est de créer un jeu de rôle simple en Python comportant deux joueurs qui sont le personnage principal et l'ennemi.
# Les deux joueurs auront au départ 50 points de vie, mais le personnage principal aura 3 potions de soin qui lui permettront de regagner les points de vie dans un intervalle aléatoire de 15 à 50 points.
# Le personnage principal pourra attaquer l'ennemi en infligeant des dégâts dans un intervalle aléatoire de 5 à 10 points, tandis que l'ennemi pourra attaquer le personnage principal en infligeant des dégâts dans un intervalle aléatoire de 5 à 15 points.
# Le jeu commencera par l'attaque du personnage principal, puis l'ennemi attaquera à son tour, et ainsi de suite jusqu'à ce que l'un des deux joueurs ait 0 point de vie.
import random
import time

print("Bienvenue dans le jeu de rôle !")
time.sleep(2)
print("Le jeu commence !")
time.sleep(2)
player_health = 50
enemy_health = 50
player_potions = 3

print("Vous avez 50 points de vie et 3 potions de soin.")
time.sleep(2)
print("L'ennemi a aussi 50 points de vie.")
time.sleep(2)

while player_health > 0 and enemy_health > 0:
    print("\n" + "-"*40)  # Séparateur visuel
    print("1. Souhaitez-vous attaquer l'ennemi ⚔️?")
    print("2. Souhaitez-vous utiliser une potion de soin 🧪?")
    print("3. Souhaitez-vous quitter le jeu ?")
    choix = input("👉 Votre choix : ")

    if choix == "1":
        player_damage = random.randint(5, 10)
        enemy_health -= player_damage
        print(f"Vous avez infligé {player_damage} points de dégâts à l'ennemi.")
        time.sleep(2)

        if enemy_health <= 0:
            print("Félicitations 🎉🎊! Vous avez vaincu l'ennemi !")
            time.sleep(2)
            break

        enemy_damage = random.randint(5, 15)
        player_health -= enemy_damage
        print(f"L'ennemi vous a infligé {enemy_damage} points de dégâts.")
        time.sleep(2)

        if player_health <= 0:
            print("Vous avez été vaincu par l'ennemi. Game over ☠️!")
            time.sleep(2)
            break

        print(f"Il vous reste {player_health} points de vie.")
        print(f"Il reste {enemy_health} points de vie à l'ennemi.")
        time.sleep(2)

    elif choix == "2":
        if player_potions > 0:
            potion_heal = random.randint(15, 50)
            player_health += potion_heal
            player_health = min(player_health, 50)  # Assure que la santé ne dépasse pas 50
            player_potions -= 1
            print(f"Vous avez utilisé une potion de soin et regagné {potion_heal} ❤️  points de vie.")
            print(f"Il vous reste {player_potions} potions de soin 🧪.")
            time.sleep(2)
            # L'ennemi attaque après l'utilisation de la potion de soin infligeant le double des dégâts.
            print("L'ennemi profite de votre moment de faiblesse en vous infligeant le double des dégâts 😱!")
            time.sleep(2)
            enemy_damage = 2 * random.randint(5, 15)
            player_health -= enemy_damage
            print(f"L'ennemi vous a infligé {enemy_damage} points de dégâts.")
            time.sleep(2)

            if player_health <= 0:
                print("Vous avez été vaincu par l'ennemi. Game over !")
                break
            print(f"Il vous reste {player_health} points de vie.")
            print(f"Il reste {enemy_health} points de vie à l'ennemi.")
            time.sleep(2)
        else:
            print("Vous n'avez plus de potions de soin !")
            print("Veuillez choisir une autre action.")
            time.sleep(2)
            pass
    elif choix == "3":
        print("Merci d'avoir joué ! À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
        time.sleep(2)

print("Fin du jeu.")