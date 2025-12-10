"""
Exemples de fonctions simples en Python avec des annotations de type.
Les fonctions incluent l'addition, la multiplication, la salutation et la vérification de la parité.
"""

def add(a: int, b: int) -> int:
    """Description de la fonction add

    Args:
        a (int): Le premier nombre entier
        b (int): Le deuxième nombre entier

    Returns:
        int: La somme des deux entiers
    """
    return a + b

def multiply(a: int, b: int) -> int:
    """Description de la fonction multiply

    Args:
        a (int): Le premier nombre entier
        b (int): Le deuxième nombre entier

    Returns:
        int: Le produit des deux entiers
    """
    return a * b

def greet(name: str) -> str:
    """Description de la fonction greet

    Args:
        name (str): Le nom de la personne à saluer

    Returns:
        str: Un message de salutation
    """
    return f"Bonjour, {name}!"

def is_even(n: int) -> bool:
    """Description de la fonction is_even

    Args:
        n (int): Le nombre à vérifier

    Returns:
        bool: True si le nombre est pair, False sinon
    """
    return n % 2 == 0

add_result = add(a=3, b=5)
multiply_result = multiply(a=4, b=2)
greeting = greet(name="Alice")
even_check = is_even(n=10)
print(f"Addition: {add_result}")
print(f"Multiplication: {multiply_result}")
print(f"Bonjour: {greeting}")
print(f"Is 10 even? {even_check}")