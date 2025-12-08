"""
Exemples de fonctions simples en Python avec des annotations de type.
Les fonctions incluent l'addition, la multiplication, la salutation et la vérification de la parité.
"""

def add(a: int, b: int) -> int:
    """Retourne la somme de deux entiers."""
    return a + b
def multiply(a: int, b: int) -> int:
    """Retourne le produit de deux entiers."""
    return a * b
def greet(name: str) -> str:
    """Retourne un message de salutation pour le nom donné."""
    return f"Bonjour, {name}!"
def is_even(n: int) -> bool:
    """Retourne True si l'entier est pair, sinon False."""
    return n % 2 == 0

add_result = add(a=3, b=5)
multiply_result = multiply(a=4, b=2)
greeting = greet(name="Alice")
even_check = is_even(n=10)
print(f"Addition: {add_result}")
print(f"Multiplication: {multiply_result}")
print(f"Bonjour: {greeting}")
print(f"Is 10 even? {even_check}")