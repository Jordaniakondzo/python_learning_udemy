# Afficher les tables de multiplication de 1 à 10 
for i in range(1, 11):
    print(f"Table de {i}: ", end="\n")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Ligne vide entre les tables