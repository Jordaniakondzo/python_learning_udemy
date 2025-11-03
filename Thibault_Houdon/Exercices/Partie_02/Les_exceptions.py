# Le but de cet exercice est de gérer les erreurs lors de l'ouverture d'un fichier.
"""
Etapes à suivre :
1. Demander à l'utilisateur de saisir le nom d'un fichier à ouvrir.
2. Ouvrir le fichier en mode lecture avec encodage UTF-8.
3. Gérer les erreurs d'ouverture du fichier et afficher un message approprié.
4. Si le fichier est ouvert avec succès, lire et afficher son contenu.
Types d'erreurs à gérer :
- FileNotFoundError : si le fichier n'existe pas.
- PermissionError : si l'utilisateur n'a pas la permission d'ouvrir le fichier.
- UnicodeDecodeError : si le fichier ne peut pas être décodé en UTF-8. 
- OSError : pour toute autre erreur liée au système d'exploitation.
"""

# Demander à l'utilisateur de saisir le chemin ou le nom du fichier à ouvrir
fichier = input("Entrez le chemin ou le nom du fichier à ouvrir : ")
try:
    with open(fichier, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError:
    print("Le fichier n'existe pas.")
except PermissionError:
    print("L'utilisateur n'a pas la permission d'ouvrir le fichier.")
except UnicodeDecodeError:
    print("Le fichier ne peut pas être décodé en UTF-8.")
except OSError as e:
    print("Erreur liée au système d'exploitation :", e)
finally:
    print("Fin de l'opération d'ouverture du fichier.")

# Fin de l'exercice
