# Vérification de la validité d'un mot de passe
# Le mot de passe doit contenir au moins 8 caractères et ne pas être composé uniquement de chiffres ou de lettres.
mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
elif len(mdp) >= 8 and mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
elif len(mdp) >= 8 and mdp.isalpha():
    print("Votre mot de passe ne contient que des lettres.")
elif len(mdp) >= 8 and not any(c.isalpha() for c in mdp):
    print("Votre mot de passe ne contient pas de lettres.")
elif len(mdp) >= 8 and not any(c.isdigit() for c in mdp):
    print("Votre mot de passe ne contient pas de nombres.")
else:
    print("Inscription terminée.")
