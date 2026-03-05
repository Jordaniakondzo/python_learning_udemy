# 🧠 Notes de formation Python  

_Formation : Python – La Formation Complète 2025 (Thibault Houdon, Udemy)_  

---

## 📑 Table des matières

- [📝 Introduction](#-introduction)
- [Section 12 : Les types natifs](#section-12--les-types-natifs)
- [Section 13 : Les variables](#section-13--les-variables)
- [Section 14 : Le type des objets et la conversion](#section-14--le-type-des-objets-et-la-conversion)
- [Section 15 : Interagir avec l’utilisateur](#section-15--interagir-avec-lutilisateur)
- [Section 16 : Apprendre à résoudre des problèmes](#section-16--apprendre-à-résoudre-des-problèmes)
- [Section 17 : Manipuler les chaînes de caractères](#section-17--manipuler-les-chaînes-de-caractères)
- [Section 18 : Les opérateurs](#section-18--les-opérateurs)
- [Section 19 : Le formatage des chaînes de caractères](#section-19--le-formatage-des-chaînes-de-caractères)
- [Section 20 : Projet #1 — La calculatrice](#section-20--projet-1--la-calculatrice)
- [Section 21 : Les structures conditionnelles](#section-21--les-structures-conditionnelles)
- [Section 22 : Les erreurs que vous allez rencontrer](#section-22--les-erreurs-que-vous-allez-rencontrer)
- [Section 23 : Quelques modules et fonctions utiles](#section-23--quelques-modules-et-fonctions-utiles)
- [Section 24 : Les listes](#section-24--les-listes)
- [Section 25 : Fonctions intégrées et méthodes supplémentaires](#section-25--fonctions-intégrées-et-méthodes-supplémentaires)
- [Section 26 : Les boucles](#section-26--les-boucles)
- [Section 27 : Exercices sur les boucles](#section-27--exercices-sur-les-boucles)
- [Section 28 : Projet #2 — La calculatrice (avec gestion des erreurs)](#section-28--projet-2--la-calculatrice-avec-gestion-des-erreurs)
- [Section 29 : Projet #3 — La liste de courses](#section-29--projet-3--la-liste-de-courses)
- [Section 30 : Projet #4 — Le nombre mystère](#section-30--projet-4--le-nombre-mystère)

- [Section 31 : Projet #5 — Créer un jeu de rôle](#section-31--projet-5--créer-un-jeu-de-rôle)
- [Section 32 : Fin de la première partie](#section-32--fin-de-la-première-partie)

---

## 📝 Introduction  

Les sections **1 à 11** de la formation sont principalement consacrées aux **instructions générales, conseils méthodologiques et organisation de l’apprentissage**.  
Elles posent les bases théoriques et pratiques (installation de Python, configuration de l’environnement, présentation de l’interface, etc.).  

👉 Dans ce fichier de notes, je commence à documenter **à partir de la section 12**, là où débute le contenu technique (types natifs, variables, conversions, etc.), afin de garder mes notes centrées sur la partie **programmation effective**.  

👉 Cette première partie correspond donc au **socle fondamental** de mon apprentissage Python : elle introduit les types de données, les variables, les conversions, les structures de contrôle et les premières boucles — étant de briques indispensables pour comprendre et construire les projets suivants. 

---

## Section 12 : Les types natifs

### 📌 Objectif de la section

Comprendre les types de données fondamentaux en Python, leur utilisation, leurs constructeurs, et comment les manipuler efficacement.

---

### 🔹 Types natifs abordés

### Chaînes de caractères (`str`)

- Définition avec guillemets simples ou doubles : `'texte'` ou `"texte"`
- Fonctions utiles : `len()`, `.upper()`, `.lower()`, `.capitalize()`
- Accès par index : `mot[0]`
- Slicing : `mot[1:4]`

### Nombres (`int`, `float`)

- Entiers (`int`) : `5`, `-3`, `0`
- Décimaux (`float`) : `3.14`, `-0.5`
- Opérations : `+`, `-`, `*`, `/`, `//`, `%`, `**`

### Booléens (`bool`)

- Deux valeurs possibles : `True`, `False`
- Utilisés dans les conditions et les tests logiques
- Résultat de comparaisons : `5 > 3 → True`

---

### 🔸 Constructeurs de types

Les fonctions suivantes permettent de convertir une valeur vers un type donné :

```python
str(123)      # '123'
int("42")     # 42
float("3.14") # 3.14
bool("")      # False
```

---

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur les chaînes de caractères  
- ✅ Quiz sur les booléens  
- ✅ Quiz sur les types natifs  
- ✅ Exercice : Créer des objets natifs  
- ✅ Exercice : Corriger les erreurs de chaînes  
- ✅ Exercice : Corriger les variables  

---

### 🧾 Résumé

- Les types natifs sont les **briques de base** du langage Python.  
- Ils sont simples à manipuler mais essentiels pour comprendre les structures plus complexes.  
- Savoir les **convertir** et les **tester** est fondamental pour la suite de la formation.

---

## Section 13 : Les variables

### 📌 Objectif de la section

Comprendre ce qu’est une variable, comment la créer, la nommer correctement, et comment elle interagit avec les objets en mémoire.

---

### 🔹 Définition et création

Une variable est un nom qui référence un objet en mémoire.  

Elle se crée simplement par affectation :

```python
nom = "Jordani"
age = 25
```

---

### 🔸 Règles de nommage

- Doit commencer par une lettre ou un underscore `_`  
- Ne doit pas contenir d’espace ni de caractères spéciaux  
- Sensible à la casse (`Nom ≠ nom`)  

**Bonnes pratiques :**

- Utiliser des noms explicites (`compteur`, `mot_de_passe`)  
- Éviter les noms trop courts ou ambigus (`x`, `data`, `temp`)  

---

### 🧠 Concepts clés

Une variable peut changer de type au cours du programme :

```python
x = 5       # int
x = "cinq"  # str
```

---
Les variables sont des références, pas des conteneurs :

- Deux variables peuvent pointer vers le même objet

- Utiliser `id()` pour voir l’identifiant mémoire

---

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur les variables

- ✅ Exercice : Créer et nommer des variables

- ✅ Exercice : Corriger des erreurs de nommage

- ✅ Exercice : Comprendre les références en mémoire

### 🧾 Résumé

- Les variables sont les fondations de tout programme.
- Bien les nommer améliore la **lisibilité** et la **maintenance** du code.
- Comprendre leur comportement en mémoire est essentiel pour éviter les erreurs subtiles.

---

## Section 14 : Le type des objets et la conversion

### 📌 Objectif de la section

Comprendre comment identifier le type d’un objet, effectuer des conversions entre types, et anticiper les erreurs liées aux incompatibilités.

---

### 🔹 Identifier le type d’un objet

Utiliser la fonction `type()` pour connaître le type d’une variable :  

```python
x = "Python"
print(type(x))  # <class 'str'>
```

Tous les objets en Python ont un type : `int`, `float`, `str`, `bool`, `list`, etc.

---

### 🔸 Conversion entre types

Utiliser les constructeurs pour convertir :

```python
int("abc")     # ❌ ValueError
```

La conversion `bool()` est utile pour tester la **vérité** d’un objet :

- `bool("")` → False
- `bool("abc")` → True
- `bool(0)` → False
- `bool(1)` → True

---

### 🧠 Concepts clés

- Le type d’un objet détermine son comportement et les méthodes disponibles.
- La conversion est souvent nécessaire pour manipuler des données utilisateur (input() retourne toujours une chaîne).
- Il est important de tester les conversions avec try/except pour éviter les erreurs.

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur le type des objets

- ✅ Exercice : Identifier le type d’une variable

- ✅ Exercice : Convertir des objets

- ✅ Exercice : Corriger des erreurs de conversion

---

### 🧾 Résumé

- `type()` est essentiel pour comprendre ce que contient une variable.
- Les conversions permettent de rendre les données compatibles avec les opérations souhaitées.
- Il faut toujours anticiper les erreurs de conversion, surtout avec des données externes.

---

## Section 15 : Interagir avec l’utilisateur

### 📌 Objectif de la section

Apprendre à récupérer des données saisies par l’utilisateur et à les utiliser dans un programme Python.  
Comprendre comment gérer les entrées et les convertir au bon format.

---

### 🔹 La fonction `input()`

Permet de demander une saisie à l’utilisateur :

```python
nom = input("Quel est ton prénom ? ")
print("Bonjour", nom)
```

Par défaut, input() retourne une chaîne de caractères `(str)`, même si l’utilisateur entre un nombre :

```python
age = input("Quel est ton âge ? ")  # '25'
```

---

### 🔸 Conversion des entrées

Il faut convertir les entrées si on veut les utiliser comme des nombres.
Exemple :

```python
age = int(input("Quel est ton âge ? "))
taille = float(input("Quelle est ta taille en mètres ? "))
```

Attention aux erreurs si l’utilisateur entre une valeur non convertible :

```python
int("abc")  # ❌ ValueError
```

---

### 🧠 Concepts clés

- L’interaction avec l’utilisateur rend le programme dynamique.
- Toujours anticiper le type de données attendu.
- Il est possible de combiner `input()` avec des conditions :

```python
mot_de_passe = input("Entrez votre mot de passe : ")
if len(mot_de_passe) < 8:
    print("Mot de passe trop court.")
```

---

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur `input()` et les conversions
- ✅ Exercice : Créer un script interactif
- ✅ Exercice : Vérifier la validité d’un mot de passe
- ✅ Exercice : Créer une calculatrice simple avec `input()` et `int()`

### 🧾 Résumé

- `input()` est la porte d’entrée des données utilisateur.
- Toujours convertir les données au bon type avant de les utiliser.
- Anticiper les erreurs de saisie est une bonne pratique pour des programmes robustes.

---

## Section 16 : Apprendre à résoudre des problèmes

### 📌 Objectif de la section
Développer une méthode de réflexion pour aborder les problèmes en programmation, structurer ses idées, et créer des solutions efficaces avec Python.

---

### 🔹 Étapes de résolution d’un problème

1. **Comprendre le problème**  
   - Lire attentivement l’énoncé  
   - Identifier les données d’entrée et de sortie  
   - Reformuler avec ses propres mots  

2. **Découper le problème**  
   - Diviser en sous-problèmes plus simples  
   - Identifier les étapes logiques  

3. **Écrire un algorithme**  
   - Décrire les étapes en pseudo-code  
   - Penser en termes de conditions, boucles, fonctions  

4. **Coder la solution**  
   - Traduire l’algorithme en Python  
   - Tester avec des cas simples  

5. **Corriger et améliorer**  
   - Identifier les erreurs  
   - Optimiser le code  
   - Ajouter des commentaires  

---

### 🧠 Concepts clés

- La programmation est avant tout une **manière de penser**.  
- Il faut apprendre à traduire une idée en **instructions claires**.  
- La rigueur et la patience sont essentielles pour progresser.  

---

### 🧾 Résumé

- Résoudre un problème, c’est avant tout **bien le comprendre**.  
- Il faut **structurer sa pensée** avant de coder.  
- Les erreurs font partie du processus d’apprentissage.  
- Plus tu pratiques, plus ta logique devient fluide.

---

## Section 17 : Manipuler les chaînes de caractères

### 📌 Objectif de la section

Maîtriser les opérations courantes sur les chaînes de caractères (str) : extraction, modification, recherche, nettoyage, et transformation.

---

### 🔹 Accès aux caractères

- Par index : `mot[0]` → premier caractère  
- Par slicing : `mot[1:4]` → sous-chaîne d’un intervalle donné  
- Inversion de chaîne : `mot[::-1]` 

---

### 🔸 Méthodes utiles

Python fournit de nombreuses méthodes intégrées pour travailler avec les chaînes.  
Ces méthodes permettent de transformer, nettoyer et analyser du texte facilement :

| Méthode        | Description                               |
|----------------|-------------------------------------------|
| `.upper()`     | Convertit en majuscules                   |
| `.lower()`     | Convertit en minuscules                   |
| `.capitalize()`| Met la première lettre en majuscule       |
| `.strip()`     | Supprime les espaces en début et fin       |
| `.replace(a,b)`| Remplace `a` par `b`                      |
| `.find()`      | Retourne l’index de la première occurrence |
| `.count()`     | Compte le nombre d’occurrences             |
| `.startswith()`| Vérifie si la chaîne commence par un motif |
| `.endswith()`  | Vérifie si la chaîne se termine par un motif |

---

### 🔹 Concaténation et répétition

- Concaténer deux chaînes : `mot1 + mot2`
- Répéter une chaîne plusieurs fois :  `"ha" * 3 → "hahaha"`

---

### 🔸 Vérifications

- `in` / `is` pour tester la présence ou l’identité : `"py" in "python" → True`
  
- `.isdigit()` / `.isalpha()` / `.isalnum()` / `.isspace()` pour tester le contenu  

---

### 🧠 Concepts clés

- Les chaînes sont **immuables** : on ne peut pas modifier un caractère directement.  
- Les méthodes retournent toujours une **nouvelle chaîne**.  
- Bien connaître ces méthodes permet de **nettoyer et transformer** des données textuelles efficacement.  

---

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur les méthodes de chaînes  
- ✅ Exercice : Nettoyer une chaîne  
- ✅ Exercice : Vérifier le format d’un mot de passe  
- ✅ Exercice : Créer une phrase à partir de plusieurs mots  

---

### 🧾 Résumé

- Les chaînes sont **omniprésentes** en Python (saisie utilisateur, fichiers, API…).  
- Savoir les manipuler est essentiel pour le **traitement de texte et de données**.  
- Les méthodes sont nombreuses mais **intuitives** une fois maîtrisées.

---

## Section 18 : Les opérateurs

### 📌 Objectif de la section

Comprendre les différents types d’opérateurs en Python et leur rôle dans les expressions, les calculs, les comparaisons et les conditions.

---

### 🔹 Les opérateurs arithmétiques

Les opérateurs arithmétiques permettent de réaliser des **calculs mathématiques de base** sur les nombres.  

| Opérateur | Description          | Exemple | Résultat |
|-----------|----------------------|---------|----------|
| `+`       | Addition             | 2 + 3   | 5        |
| `-`       | Soustraction         | 5 - 2   | 3        |
| `*`       | Multiplication       | 4 * 2   | 8        |
| `/`       | Division (float)     | 5 / 2   | 2.5      |
| `//`      | Division entière     | 5 // 2  | 2        |
| `%`       | Modulo (reste)       | 5 % 2   | 1        |
| `**`      | Puissance            | 2 ** 3  | 8        |

---

### 🔸 Les opérateurs de comparaison

Les opérateurs de comparaison servent à **tester l’égalité ou l’ordre entre deux valeurs**.  

| Opérateur | Signification       | Exemple | Résultat |
|-----------|---------------------|---------|----------|
| `==`      | Égal à              | 5 == 5  | True     |
| `!=`      | Différent de        | 5 != 3  | True     |
| `<`       | Inférieur à         | 3 < 5   | True     |
| `>`       | Supérieur à         | 5 > 3   | True     |
| `<=`      | Inférieur ou égal   | 5 <= 5  | True     |
| `>=`      | Supérieur ou égal   | 5 >= 3  | True     |

---

### 🔹 Les opérateurs logiques

Les opérateurs logiques permettent de **combiner plusieurs conditions** pour construire des expressions plus complexes.  

| Opérateur | Fonction                          | Exemple        | Résultat |
|-----------|-----------------------------------|----------------|----------|
| `and`     | Tous les tests doivent être vrais | True and False | False    |
| `or`      | Au moins un test doit être vrai   | True or False  | True     |
| `not`     | Inverse la valeur logique         | not True       | False    |

---

### Concepts clés

- Les opérateurs sont essentiels pour écrire des **conditions** et des **expressions**.  
- Ils peuvent être combinés dans des **structures complexes :**

```python
if age >= 18 and pays == "France":
    print("Accès autorisé")
```

- L’ordre des opérations suit les règles classiques de priorité :  
  1. Parenthèses  
  2. Puissances  
  3. Multiplication / Division  
  4. Addition / Soustraction  

---

### Quiz et exercices réalisés

- ✅ Quiz sur les opérateurs arithmétiques  
- ✅ Quiz sur les opérateurs logiques  
- ✅ Exercice : Créer des expressions conditionnelles  
- ✅ Exercice : Simuler des calculs avec des entrées utilisateur  

---

### Résumé

- Les opérateurs permettent de **manipuler les données** et de **prendre des décisions**.  
- Bien les comprendre est indispensable pour écrire des conditions **claires et efficaces**.  
- Ils sont omniprésents dans les **boucles, fonctions, tests et calculs**.

---

## Section 19 : Le formatage des chaînes de caractères

### 📌 Objectif de la section

Apprendre à insérer dynamiquement des valeurs dans des chaînes de caractères, en utilisant les différentes méthodes de formatage disponibles en Python.

---

### 1. 🔤 Concaténation classique

La concaténation consiste à **assembler plusieurs chaînes de caractères** en une seule.  
C’est simple mais peu flexible, car elle nécessite souvent des conversions manuelles `(str())`.

- Exemple :

```python
nom = "Jordani"
print("Bonjour " + nom)
```

---

### 2. 🧩 Méthode `.format()`

La méthode `.format()` permet d’**insérer des valeurs à l’intérieur d’une chaîne** grâce à des emplacements `{}`.  
Elle est plus puissante que la concaténation, notamment pour réorganiser les valeurs `{1}, {0}` comme dans cet exemple de code:

```python
prenom = "Jordani"
age = 25
print("Je m'appelle {} et j'ai {} ans.".format(prenom, age))
```

---

### 3. ⚡ F-strings (recommandé depuis Python 3.6)

Les f-strings offrent une manière **moderne et lisible** d’insérer directement des variables ou des expressions dans une chaîne.  
Elles sont à la fois **claires, rapides et performantes**, et représentent aujourd’hui la méthode la plus recommandée.

Exemple :

```python
prenom = "Jordani"
age = 25
print(f"Je m'appelle {prenom} et j'ai {age} ans.")

```

Elle permet d’insérer des expressions directement : `f"{2 + 3}"`

---

### 🧠 Concepts clés

- Le formatage est essentiel pour afficher des données de manière **propre et lisible**.  
- Les f-strings sont aujourd’hui la méthode la plus **pratique et moderne**.  
- Bien formater les chaînes est utile pour les **interfaces, rapports, journaux et affichages dynamiques**.  

---

### 🧪 Quiz et exercices réalisés

- ✅ Quiz sur les f-strings  
- ✅ Quiz sur `.format()` et les emplacements  
- ✅ Exercice : Créer une fiche utilisateur formatée  
- ✅ Exercice : Afficher des données alignées dans un tableau  

---

### 🧾 Résumé

- Utilise les **f-strings** pour un code plus clair et moderne.  
- Le formatage permet de **structurer l’affichage** des données.  
- Tu peux combiner formatage et logique pour créer des **interfaces dynamiques**.

---

## Section 20 : Projet #1 — La calculatrice

### 🎯 Objectif du projet

Ce premier projet marque le début de la mise en pratique concrète des connaissances.  
L’objectif est simple mais fondamental : créer une calculatrice en ligne de commande qui demande à l’utilisateur deux nombres et affiche le résultat de leur addition.

---

### 🛠️ Compétences mobilisées

- Utilisation de `input()` pour récupérer des données utilisateur  
- Conversion des chaînes en nombres (`int()` ou `float()`)  
- Affichage du résultat avec `print()` et formatage (f-string)  
- Structuration du code en étapes claires  

---

### 💡 Pourquoi ce projet est important

- Il permet de **consolider les bases** : types natifs, variables, conversion, affichage.  
- Il initie à la logique de projet : **entrée → traitement → sortie**.  
- Il sert de point de départ pour des versions plus avancées (ajout d’opérations, gestion des erreurs, interface graphique…).  

---

### 🧪 Étapes du projet

1. Demander deux nombres à l’utilisateur  
2. Convertir les entrées en entiers  
3. Calculer la somme  
4. Afficher le résultat avec un message clair  

---

### 📂 Exemple du projet

Le code complet de la calculatrice se trouve dans le fichier :  
[`Projet #1 — Calculatrice`](../Projets/Calculatrice.py).

---

### 🧾 Résumé

- Ce projet est une **première pierre** vers des applications plus complexes.  
- Même avec peu de lignes, on peut créer un **outil utile et fonctionnel**.  
- Il encourage à réfléchir en termes de **flux de données** et d’**interaction utilisateur**.

---

## Section 21 : Les structures conditionnelles

## 📌 Objectif de la section

Apprendre à contrôler le flux d’un programme en fonction de conditions.  
Savoir utiliser les blocs `if`, `elif`, `else` pour prendre des décisions dynamiques.

---

## 🔹 Syntaxe de base

Les structures conditionnelles permettent d’exécuter différents blocs d’instructions selon que des conditions soient vraies ou fausses.  
Elles reposent sur une indentation stricte (souvent 4 espaces) pour définir les blocs.

```python
if condition:
    # instructions si la condition est vraie
elif autre_condition:
    # instructions si la première est fausse mais celle-ci est vraie
else:
    # instructions si aucune condition n’est vraie
```  

---

## 🔸 Opérateurs utilisés dans les conditions

Pour écrire des conditions, on utilise différents opérateurs :

- **Comparaison** : `==`, `!=`, `<`, `>`, `<=`, `>=`  
- **Logique** : `and`, `or`, `not`  
- **Appartenance** : `in`, `not in`  
- **Booléens** : `True`, `False`  

---

## 🧠 Concepts clés

- L’ordre des conditions est important : le programme s’arrête dès qu’une condition est vraie.  
- `elif` permet d’éviter des imbrications trop profondes.  
- `else` est facultatif mais pratique pour gérer les cas par défaut.  
- Les conditions peuvent être combinées pour plus de précision.  

---

## 🧪 Quiz et exercices réalisés

- ✅ Quiz sur les blocs `if/elif/else`  
- ✅ Quiz sur les opérateurs logiques  
- ✅ Exercice : Vérification de mot de passe  
- ✅ Exercice : Calculateur d’âge  
- ✅ Exercice : Détection de mot vide ou numérique  

---

## 🧾 Résumé

- Les structures conditionnelles sont le **cœur de la logique décisionnelle**.  
- Elles permettent de rendre le programme **intelligent et interactif**.  
- Bien les maîtriser est essentiel pour tous les projets à venir.

---

## Section 22 : Les erreurs que vous allez rencontrer

## 📌 Objectif de la section
Identifier les erreurs les plus fréquentes en Python, comprendre leur origine, et apprendre à les corriger pour progresser plus sereinement dans ton apprentissage.

---

## 🔹 Types d’erreurs courantes

### 1. 🧱 Erreurs de syntaxe (*SyntaxError*) 

Elles apparaissent lorsque la structure du code est incorrecte.  
Exemples typiques :  

- Oubli du `:` après une condition ou une boucle  
- Mauvaise indentation  
- Parenthèses ou guillemets non fermés  

Exemple:

```python
if x == 5  # ❌ SyntaxError : missing ':'
```

---

### 2. 🧠 Erreurs de type (*TypeError*) 

Elles surviennent lorsqu’on tente une opération entre deux types incompatibles.  
Exemple : concaténer une chaîne avec un entier sans conversion.

```python
print("âge : " + 25)  # ❌ TypeError : str + int
```

---

### 3. 🔍 Erreurs de nom (*NameError*)

Elles se produisent lorsqu’on utilise une variable qui n’a pas été définie.  
Exemple : appel d’un identifiant inexistant.

```python
print(nom)  # ❌ NameError : 'nom' n’est pas défini
```  

---

### 4. 📦 Erreurs de conversion (_ValueError_)

Elles apparaissent lorsqu’une conversion de type est impossible.  
Exemple : transformer un mot en nombre.

```python
int("abc")  # ❌ ValueError
```

---

### 5. 📭 Erreurs d’index (*IndexError*)

Elles surviennent lorsqu’on tente d’accéder à une position inexistante dans une liste.  
Exemple : demander l’élément à l’index 5 alors que la liste n’en contient que 3. 

```python
liste = [1, 2, 3]
print(liste[5])  # ❌ IndexError
``` 

---

## 🔸 Bonnes pratiques pour éviter les erreurs

- Lire attentivement les messages d’erreur (ils indiquent la cause et la ligne du problème).  
- Utiliser des noms de variables explicites.  
- Tester le code étape par étape.  
- Ajouter des commentaires pour clarifier la logique.  
- Employer `try/except` pour gérer les exceptions de manière contrôlée.  

---

## 🧠 Concepts clés

- Les erreurs font partie intégrante de l’apprentissage.  
- Savoir les lire et les comprendre est une compétence essentielle.  
- Corriger une erreur permet de **mieux comprendre le langage**.  

---

## 🧾 Résumé

- Les erreurs ne sont pas des échecs, mais des **opportunités d’apprentissage**.  
- Chaque message d’erreur contient des indices précieux.  
- Plus on pratique, plus on apprend à les anticiper et à les corriger rapidement.

---

## Section 23 : Quelques modules et fonctions utiles

## 📌 Objectif de la section

Découvrir les modules standards les plus pratiques en Python, apprendre à les importer et à utiliser leurs fonctions pour enrichir ses programmes.

---

## 🔹 Qu’est-ce qu’un module ?

Un module est un fichier Python contenant du code réutilisable.  
Il peut être importé dans un autre script avec la commande `import`.  
La bibliothèque standard de Python est très riche et permet de gagner du temps en évitant de réinventer la roue.

---

## 🔸 Modules abordés dans cette section

### 🎲 1. Le module `random`

Le module `random` permet de générer des **valeurs aléatoires**, utiles pour les jeux, les simulations ou encore les tests.  
Il propose plusieurs fonctions pour obtenir des entiers, des flottants, choisir un élément ou mélanger une liste.

**Quelques fonctions clés :**

- `random.random()` → nombre flottant entre 0 et 1

- `random.randint(a, b)` → entier entre a et b inclus

- `random.choice(liste)` → sélectionne un élément aléatoire

- `random.shuffle(liste)` → mélange une liste

---

### 🗂️ 2. Le module `os`

Le module `os` sert à interagir avec le **système d’exploitation :** *manipuler les fichiers, les dossiers, les chemins, etc.*  
On peut par exemple récupérer le répertoire courant, lister les fichiers d’un dossier ou vérifier l’existence d’un chemin.  
Il est parfois comparé à des alternatives modernes comme `pathlib`.

Exemples :

- `os.getcwd()` → récupère le répertoire courant

- `os.listdir()` → liste les fichiers d’un dossier

- `os.path.exists()` → vérifie si un chemin existe

---

### 🧭 3. Explorer un module avec `dir()` et `help()`

Les fonctions intégrées `dir()` et `help()` permettent d’**explorer les capacités d’un module ou d’un objet**.  

- `dir()` liste les attributs et fonctions disponibles.  
- `help()` affiche la documentation détaillée d’une fonction ou d’un module.  

Ces outils sont très utiles pour découvrir de nouvelles bibliothèques.

Exemple :

- `dir(random)` → liste tous les attributs et fonctions disponibles dans le module

- `help(random.randint)` → affiche la documentation de la fonction randint

On peut les utiliser sur n’importe quel objet, module ou fonction pour en découvrir les capacités. 

---

### 🔍 4. Vérifier si un objet est *callable*

Un objet est dit *callable* s’il peut être **appelé comme une fonction** (c’est-à-dire si on peut utiliser `()` après son nom).  
Exemple : les fonctions sont *callable*, mais les nombres ne le sont pas.  

Exemple :

```python
callable(print)  # True
callable(42)     # False
```

Cela nous permet de savoir si on peut utiliser les parenthèses `()` sur un objet.

---

### 🧠 Concepts clés

- Les modules permettent d’**étendre les capacités de Python** sans tout réécrire soi-même.  
- Connaître les modules les plus courants fait gagner du temps et améliore l’efficacité.  
- Importer un module, c’est accéder à tout un ensemble d’outils déjà prêts.  

---

### 🧾 Résumé

- Les modules sont comme des **boîtes à outils** prêtes à l’emploi.  
- On peut les combiner pour créer des programmes plus puissants.  
- Bien les connaître facilite la mise en place de **projets plus ambitieux**.

---

## Section 24 : Les listes

### 📌Objectif de la section

Découvrir et maîtriser les listes en Python, qui sont des structures de données fondamentales permettant de stocker des collections d’éléments modifiables.

---

### 🔹Définition et création

Une liste est une **séquence ordonnée et modifiable**.  
Elle peut contenir différents types de données (entiers, chaînes, booléens, flottants…).  
Les listes peuvent aussi être imbriquées pour représenter des structures plus complexes (comme des matrices).  

Exemple :

```python
fruits = ["pomme", "banane", "cerise"]

# Elle peut contenir des types variés :
mixte = [1, "deux", True, 3.14]

# Les listes peuvent être imbriquées :
matrice = [[1, 2], [3, 4]]
```

---

### 🔸 Accès et modification

- Accès par index (le premier élément commence à l’index 0) : `fruits[0] → "pomme"`.  
- Modification d’un élément à une position donnée : `fruits[1] = "kiwi"`.  
- Découpage (*slicing*) pour récupérer une partie de la liste : `fruits[1:], fruits[::-1]`.  

---

### 🔹 Méthodes utiles

Les listes possèdent de nombreuses méthodes pour faciliter leur manipulation :  

| Méthode       | Description                           |
|---------------|---------------------------------------|
| `.append(x)`  | Ajoute `x` à la fin                   |
| `.insert(i,x)`| Insère `x` à l’index `i`              |
| `.remove(x)`  | Supprime la première occurrence de `x`|
| `.pop(i)`     | Supprime et retourne l’élément à `i`  |
| `.clear()`    | Vide la liste                         |
| `.copy()`     | Crée une copie superficielle          |
| `.extend(l)`  | Ajoute tous les éléments de `l`       |
| `.index(x)`   | Retourne l’index de `x`               |
| `.count(x)`   | Compte les occurrences de `x`         |
| `.sort()`     | Trie la liste en place                |
| `.reverse()`  | Inverse l’ordre des éléments          |

---

### 🔸 Fonctions utiles

Certaines fonctions intégrées sont très pratiques avec les listes :

- `len()` → donne la longueur de la liste  
- `list()` → crée une liste à partir d’une autre séquence. Exemple :

```python
list("abc") → ['a', 'b', 'c'] 
```

- `in` / `not in` → testent l’appartenance d’un élément.

---

### 🧠 Concepts clés

- Les listes sont **mutables**, donc leur contenu peut être modifié.  
- Elles sont très utilisées pour gérer des données dynamiques.  
- Bien connaître leurs méthodes permet de manipuler efficacement des **collections d’éléments**.  

---

### 🧾 Résumé

- Les listes sont des **outils puissants** pour organiser et stocker des données.  
- Elles sont omniprésentes dans les projets Python.  
- Les maîtriser est essentiel pour la suite du cours (boucles, fonctions, projets). 

---

## Section 25 : Fonctions intégrées et méthodes supplémentaires

### 📌 Objectif de la section

Découvrir et maîtriser les fonctions intégrées et méthodes les plus utilisées en Python, afin d’optimiser l’écriture et la lecture du code.

---

### 🔹 Rappel : Méthodes vs Fonctions

- **Méthode** : attachée à un objet, s’utilise avec un point.  
  Exemple : `"Python".upper()` ou `[1, 2, 3].append(4)`  
- **Fonction** : indépendante, s’utilise directement avec des parenthèses.  
  Exemple : `len("Python")` ou `type(42)`  

---

### 🔸 Fonctions intégrées utiles

Voici quelques fonctions intégrées incontournables :  

| Fonction             | Description                                   |
|----------------------|-----------------------------------------------|
| `len()`              | Longueur d’un objet (liste, chaîne, etc.)     |
| `type()`             | Type d’un objet                               |
| `str()`, `int()`, `float()` | Conversions de types                   |
| `print()`            | Affiche une valeur                           |
| `input()`            | Récupère une saisie utilisateur               |
| `help()`             | Affiche l’aide sur un objet ou une fonction   |
| `dir()`              | Liste les attributs et méthodes d’un objet    |
| `id()`               | Identifiant mémoire de l’objet                |

---

## 🔹 Méthodes supplémentaires vues

- **Sur les chaînes** : `.startswith()`, `.endswith()`, `.find()`, `.count()`  
- **Sur les listes** : `.sort()`, `.reverse()`, `.copy()`, `.extend()`  
- **Sur les booléens** : `any()`, `all()` → testent des conditions sur une séquence  

---

## 🧠 Concepts clés

- Les **fonctions intégrées** sont des outils puissants pour inspecter, transformer et interagir avec les objets.  
- Les **méthodes** permettent de manipuler directement les objets.  
- Bien les connaître rend le code plus **concise, lisible et efficace**.  

---

## 🧾 Résumé

- Python offre une grande richesse de **fonctions et méthodes prêtes à l’emploi**.  
- Les combiner permet de résoudre des problèmes plus rapidement.  
- Ces outils sont les **fondations de l’efficacité** d’un développeur Python.  

---

# Section 26 : Les boucles

## 📌 Objectif de la section

Apprendre à répéter des instructions en Python grâce aux boucles `for` et `while`, et comprendre comment contrôler leur exécution avec `break`, `continue`, et `else`.

---

## 🔹 La boucle `for`

La boucle `for` est utilisée pour **parcourir une séquence** (liste, chaîne, intervalle, etc.).  
Elle est idéale lorsque le nombre d’itérations est connu à l’avance.

Syntaxe :

```python
for i in range(5):
    print(i)
```

Peut être combinée avec `if, break, continue,` et `else`

---

## 🔸 La boucle `while`

La boucle `while` répète un bloc d’instructions **tant qu’une condition est vraie**.  
Elle est utile lorsque la durée de la boucle dépend d’un état qui peut évoluer. 

Syntaxe :

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

⚠️ Attention : un mauvais contrôle de la condition peut entraîner des **boucles infinies**.  

---

## 🔹 Contrôle de boucle

Les instructions spéciales permettent de modifier le comportement des boucles :  

| Instruction | Rôle                                                                 |
|-------------|---------------------------------------------------------------------|
| `break`     | Interrompt immédiatement la boucle                                  |
| `continue`  | Ignore le reste du bloc et passe à l’itération suivante             |
| `else`      | S’exécute si la boucle se termine sans `break`                      |
| `pass`      | Ne fait rien (instruction vide, utilisée comme **placeholder**)     |

**📝 Quand utiliser pass ?**

- Lorsque tu écris la structure d’une boucle mais que tu n’as pas encore décidé du contenu.
- Pour éviter une erreur de syntaxe quand un bloc ne peut pas rester vide.

Exemple typique :

```python
for i in range(5):
    pass  # À compléter plus tard
```

---

## 🔸 Fonctions utiles avec les boucles

- `range(start, stop, step)` → génère une séquence de nombres  
- `enumerate()` → permet d’obtenir à la fois l’index et la valeur  
- `zip()` → combine plusieurs séquences ensemble  

---

## 🧠Concepts clés

- Les boucles permettent d’**automatiser des tâches répétitives**.  
- `for` convient lorsque le nombre d’itérations est déterminé.  
- `while` est adapté aux conditions dynamiques.  
- Bien utiliser `break` et `continue` permet de **contrôler finement le flux d’exécution**.  

---

## 🧾Résumé

- Les boucles sont **indispensables** pour parcourir des données et automatiser des actions.  
- Leur contrôle permet d’écrire un code **plus intelligent et plus fluide**.  
- Elles constituent une étape clé avant de développer des projets plus interactifs. 

---

## Section 27 : Exercices sur les boucles

## 📌 Objectif de la section
Mettre en pratique les boucles `for` et `while`, ainsi que les instructions `break`, `continue`, `else` et `pass`, à travers une série d’exercices progressifs.

---

## 🧪 Exercices réalisés

- ✅ Exercice 6 : Afficher dix utilisateurs  
  📂 [Afficher_dix_utilisateurs.py](../Exercices/Exercices_boucles/Afficher_dix_utilisateurs.py)  

- ✅ Exercice 7 : Afficher un mot à l’envers  
  📂 [Inverse_de_mot.py](../Exercices/Exercices_boucles/Inverse_de_mot.py)

- ✅ Exercice de codage 24 : Afficher la table de multiplication d’un nombre  
  📂 [Table_de_multiplication.py](../Exercices/Exercices_boucles/Table_de_multiplication.py)  

- ✅ Exercice de codage 25 : Sortir d’une boucle infinie  
  📂 [While_input.py](../Exercices/Exercices_boucles/While_input.py)  

- ✅ Exercice 8 : Sortir d’une boucle `while` avec `input`  
  📂 [While_input.py](../Exercices/Exercices_boucles/While_input.py)  

- ✅ Exercice 9 : Remplacer des boucles par des compréhensions de listes  
  📂 [Comprehension_listes.py](../Exercices/Exercices_boucles/Comprehension_listes.py)  

---

## 🧠 Concepts clés

- La pratique est essentielle pour **maîtriser les boucles** et anticiper les erreurs classiques.  
- Chaque exercice illustre une **situation courante** (affichage, saisie utilisateur, contrôle de flux).  
- Les compréhensions de listes permettent de simplifier et **rendre plus lisible** du code basé sur des boucles.  

---

## 🧾 Résumé

- Les exercices permettent de consolider la compréhension des boucles.  
- Ils montrent la diversité des cas pratiques : de la simple répétition à l’optimisation avec les compréhensions.  
- Ces bases sont indispensables pour passer à des projets plus complexes.

---

# Section 28 : Projet #2 — La calculatrice (avec gestion des erreurs)

## 🎯 Objectif du projet

Améliorer la première version de la calculatrice en ligne de commande en ajoutant une **gestion des erreurs**.  
Comparer deux approches : une simple avec validation par conditions, et une plus avancée avec gestion des exceptions.

---

## 🛠️ Compétences mobilisées

- Utilisation de `input()` pour récupérer des données utilisateur  
- Validation d’entrées avec `all()` et `.isdigit()` (version simple)  
- Gestion des erreurs avec `try/except` (version avancée)  
- Prévention des divisions par zéro  
- Amélioration de l’expérience utilisateur avec des messages clairs  

---

## 💡 Pourquoi ce projet est important

- Il illustre deux manières différentes de rendre un programme plus sûr.  
- Il permet de comprendre la différence entre **validation préventive** et **gestion d’erreurs**.  
- C’est une étape clé avant d’aller vers des applications interactives plus complexes.  

---

## 🧪 Étapes du projet

1. Demander deux nombres à l’utilisateur.  
2. **Version 1** : Vérifier que les entrées sont bien des chiffres (`all()` et `.isdigit()`).  
3. **Version 2** : Utiliser `try/except` pour intercepter les erreurs.  
4. Ajouter plusieurs opérations (addition, soustraction, multiplication, division).  
5. Empêcher les divisions par zéro.  
6. Afficher des messages clairs pour guider l’utilisateur.  

---

## 📂 Exemple du projet

- Version 1 (validation par conditions) : [Calculatrice_gestionErreur.py](../Projets/Caculatrice_gestionErreur.py)  
- Version 2 (améliorée avec la gestion des exceptions et le choix des opérations à éffectuér) : [Calculatrice_gestionErreur2.py](../Projets/Calculatrice_gestionErreur2.py)  

---

## 🧠 Concepts clés

- `.isdigit()` et `all()` permettent une **validation simple et rapide**, mais limitée.  
- `try/except` offre une **solution plus robuste et évolutive**.  
- Choisir la bonne approche dépend du **niveau de fiabilité attendu** pour le programme.  

---

## 🗒️ Résumé

- La validation par conditions permet de filtrer les erreurs simples.  
- La gestion des exceptions avec `try/except` rend le programme **plus professionnel**.  
- Ce projet montre l’importance de toujours prévoir l’imprévu.  

---

## Section 29 : Projet #3 — La liste de courses

## 🎯 Objectif du projet

Créer une application simple en ligne de commande permettant à l’utilisateur de **gérer une liste de courses**.  
Ce projet introduit la manipulation des listes, l’interaction utilisateur et la structuration du code en plusieurs fonctions.

---

## 🛠️ Compétences mobilisées

- Création et modification de listes  
- Utilisation de boucles `while` pour créer un menu interactif  
- Conditions `if/elif/else` pour gérer les choix  
- Organisation du code en fonctions réutilisables  
- Gestion des erreurs simples (entrée invalide, doublons, suppression d’un élément absent…)  

---

## 🧪 Fonctionnalités à implémenter

- Ajouter un élément à la liste  
- Afficher la liste actuelle  
- Supprimer un élément  
- Vider la liste  
- Quitter le programme  

📂 [Liste_de_courses.py](../Projets/Liste_de_courses.py)

---

## 💡 Pourquoi ce projet est important

- C’est une **mini-application interactive** complète.  
- On pratique la **modularité** avec des fonctions bien nommées.  
- On commence à penser en termes d’**expérience utilisateur**.  
- On pose les bases pour des projets plus avancés :  
  - sauvegarde des données  
  - interface graphique  
  - programmation orientée objet (POO)  

---

## 🗒️ Résumé

- Ce projet synthétise les acquis : **listes, boucles, conditions, fonctions, input() et print()**.  
- Il aide à **structurer ton code** pour le rendre lisible et maintenable.  
- Il peut facilement être enrichi dans les prochaines étapes.  

---

## Section 30 : Projet #4 — Le nombre mystère

 🎯 **Objectif du projet**

Créer un jeu interactif dans lequel l’ordinateur choisit un nombre aléatoire entre 1 et 100, et l’utilisateur doit le deviner en un nombre limité d’essais.  
Ce projet est à la fois ludique et formateur, car il combine plusieurs notions clés du langage Python.

---

🛠️ **Compétences mobilisées**

- Utilisation du module `random` pour générer un nombre aléatoire  
- Boucle `while` pour répéter les tentatives  
- Conditions `if/elif/else` pour guider l’utilisateur  
- Instruction `break` pour interrompre la boucle en cas de victoire  
- Gestion des entrées utilisateur avec `input()` et conversion en `int`  
- Affichage dynamique avec `print()` et f-strings  

---

🧪 **Fonctionnalités à implémenter**

- Générer un nombre mystère entre 1 et 100  
- Demander à l’utilisateur de deviner le nombre  
- Comparer la réponse avec le nombre mystère  
- Afficher un message d’aide : _trop grand_ / _trop petit_  
- Limiter le nombre d’essais (par exemple à 10)  
- Afficher un message de victoire ou de défaite  
- **Bonus** : proposer de rejouer. Dans ma version, j’ai ajouté une touche personnelle permettant à l’utilisateur de continuer à jouer lorsque le nombre de tentatives est à 0 ou après une victoire, rendant ainsi le jeu plus intéressant 💡🔎😅  

📂 [Nombre_mystere.py](../Projets/Nombre_mystere.py)

---
💡 **Points forts de mon implémentation**

- L’utilisation de `time.sleep()` rend le jeu plus fluide et engageant.  
- La validation d’entrée est bien pensée (`isdigit()`, bornes 1–100).  
- La rejouabilité intégrée rend le jeu plus intéressant que la simple version classique.  
- Les messages sont variés et adaptés (victoire, défaite, erreurs).  

---

### 🔍 Améliorations possibles

Les évolutions ou améliorations possibles (difficultés, score, factorisation du code) viendront naturellement au rythme de ma progression : elles deviendront des exercices supplémentaires pour approfondir des notions comme la POO, les fichiers, ou les interfaces graphiques.

- **Paramétrage des tentatives** : permettre à l’utilisateur de choisir le nombre de vies au début du jeu.  
- **Compteur de scores** : garder en mémoire le nombre de victoires et de défaites sur plusieurs parties.  
- **Difficulté progressive** : proposer différents niveaux (plage plus large, moins de tentatives).  
- **Factorisation du code** : isoler la logique du jeu dans une fonction `jouer()` pour éviter la duplication des blocs de rejouabilité.  
- **Expérience utilisateur** : ajouter un message plus détaillé (par exemple “Il vous reste X tentatives sur 5”).  

---

💡 **Pourquoi ce projet est important**

- Il permet de **combiner plusieurs notions** dans un seul programme concret.  
- Il entraîne à la **logique conditionnelle** et à la **gestion des états** d’un jeu.  
- Il introduit la notion d’**expérience utilisateur** avec feedback, délais et rejouabilité.  
- C’est une excellente base pour créer des jeux plus complexes (scores, niveaux, interface graphique).  

---

🧾 **Fiche récapitulative**

- Ce projet est un excellent exercice de logique et de structuration.  
- Il pousse à penser en termes de flux de jeu et de retours utilisateur.  
- Il est facilement extensible : ajout de niveaux, score, rejouabilité…

---

## Section 31 : Projet #5 — Créer un jeu de rôle

## 🎯 Objectif du projet

Créer un jeu de rôle textuel dans le terminal, où le joueur affronte un ennemi dans un **combat au tour par tour**.  
Ce projet introduit la **gestion d’état**, les **interactions complexes** et la **logique de jeu dynamique**.

---

## 🛠️ Règles du jeu

- Le joueur et l’ennemi commencent avec **50 points de vie**.  
- Le joueur dispose de **3 potions de soin** :  
  - Chaque potion rend entre **15 et 50 PV** (valeur aléatoire).  
  - L’ennemi n’a pas de potion.  
  - Utiliser une potion **fait passer le tour** du joueur.  
- Les attaques infligent :  
  - **5 à 10 PV de dégâts** pour le joueur,  
  - **5 à 15 PV** pour l’ennemi.  
- À chaque tour :  
  - Le joueur choisit entre **attaquer (1)**, **utiliser une potion (2)** ou **quitter (3)**.  
  - Si l’ennemi est encore en vie après l’action du joueur, il attaque.  
  - Si le joueur n’a plus de potions, il doit attaquer.  
- Le jeu se termine :  
  - Si l’ennemi tombe à 0 PV → **victoire du joueur 🎉**  
  - Si le joueur tombe à 0 PV → **défaite ☠️**

📂 [Jeu_de_role.py](../Projets/Jeu_de_role.py)

---

## 🔸 Étapes d’implémentation

1. Initialiser les points de vie et le nombre de potions.  
2. Créer une boucle principale qui tourne **tant que les deux personnages sont en vie**.  
3. Afficher un menu à chaque tour et récupérer le choix du joueur.  
4. Gérer les effets de l’attaque ou de la potion.  
5. Faire attaquer l’ennemi si celui-ci est encore en vie.  
6. Afficher les PV restants après chaque action.  
7. Terminer le jeu avec un message adapté selon le résultat.  

---

## 💡 Points forts de mon implémentation

- **Fluidité et immersion** grâce à l’utilisation de `time.sleep()` entre les actions.  
- **Bonne gestion des conditions** (attaques, potions, choix invalides, etc.).  
- **Détails logiques soignés** :  
  - Le joueur ne peut pas dépasser 50 PV.  
  - L’ennemi inflige **le double des dégâts** si le joueur boit une potion.  
- **Structure claire et intuitive**, idéale pour un premier moteur de jeu textuel.

---

## 🔍 Améliorations possibles (selon progression)

Les évolutions viendront naturellement au fil de mon apprentissage. Elles pourront servir de base pour explorer de nouvelles notions comme la **POO**, les **fichiers** ou la **gestion d’événements**.

- **Refactorisation avec des fonctions** : séparer les actions (`attaquer()`, `utiliser_potion()`, `tour_ennemi()`) pour plus de lisibilité.  
- **Ajout de niveaux de difficulté** : plus de dégâts ennemis ou moins de potions.  
- **Système de score** : nombre de tours pour vaincre l’ennemi, meilleur score sauvegardé.  
- **Interface graphique** : adapter le jeu avec Tkinter ou une interface console enrichie (ex : `rich`).  
- **Gestion des exceptions** : renforcer la robustesse du jeu (erreurs d’entrée, saisies invalides).  
- **Tests unitaires** : tester les fonctions (par ex. génération de dégâts, consommation de potion).  

---

## 💡 Concepts clés

- Utilisation du module `random` pour générer les **dégâts et soins**.  
- **Boucle `while`** avec plusieurs conditions et interactions utilisateur.  
- Gestion d’état par des **variables persistantes**.  
- **Affichage dynamique et immersif** avec `print()` et `time.sleep()`.  
- Structure logique de jeu et **contrôle du flux d’exécution**.  

---

## 🧾 Résumé

Ce projet constitue une étape clé dans mon apprentissage : il synthétise les boucles, conditions, entrées utilisateur et gestion aléatoire.  
Il m’a permis de **penser en termes de gameplay**, de structure logique, et d’**expérience utilisateur**.  
Ce type de projet est une excellente base pour passer vers des jeux plus complexes et mieux structurés.

---

## Section 32 : Fin de la première partie

## 🎯 Objectif de la section

Clore la première partie de la formation en réalisant un **bilan de compétences**, un **résumé des acquis**, et un **examen pratique** permettant de valider la compréhension globale des bases du langage Python.  

---

## 🧾 Résumé de la première partie

Cette première partie a permis d’acquérir les fondations solides du langage Python à travers des notions essentielles :  

- Les **types natifs** (`int`, `str`, `float`, `bool`)  
- La **manipulation de chaînes de caractères** et le **formatage dynamique** (`f-string`, `format()`)  
- La **gestion des variables** et des **conversions de type**  
- Les **structures conditionnelles** (`if`, `elif`, `else`)  
- Les **opérateurs mathématiques, logiques et de comparaison**  
- Les **boucles** (`for`, `while`) et leur rôle dans l’automatisation  
- Les **listes** et leurs méthodes fondamentales (`append`, `remove`, `extend`, etc.)  
- L’**interaction utilisateur** avec la fonction `input()`  
- La **gestion des erreurs** simples et la logique de débogage  

👉 Ces connaissances forment le **socle du développement Python**, sur lequel reposent les projets réalisés (calculatrice, liste de courses, jeu du nombre mystère, jeu de rôle, etc.).

---

## 📊 Bilan de compétence

> D’après le document “Bilan_de_competences_partie_01.pdf”, toutes les compétences principales de cette première partie sont validées.  
> Chaque notion peut être cochée comme acquise après la pratique et les projets.  

**Domaines validés :**  

- [x] Types natifs et conversions  
- [x] Manipulation des chaînes  
- [x] Variables et conventions de nommage  
- [x] Opérateurs et formatage  
- [x] Structures conditionnelles  
- [x] Listes et boucles  
- [x] Interaction avec l’utilisateur  
- [x] Gestion des erreurs simples  

---

## 🧪 Examen pratique — Mode entraînement

L’examen pratique de la première partie (80 questions, durée : 1 h 30) a permis de mettre en application l’ensemble des concepts étudiés.  

**Résultats du mode entraînement :**

- ✅ Score : **96 % (77/80)**  
- 📅 Date : 16 octobre 2025  
- 🎯 Taux minimal requis : 75 %  
- 🌟 Tous les domaines (variables, fonctions, listes, boucles, structures, erreurs, etc.) ont été validés à plus de 90 %.

👉 L’examen en **mode officiel (examen)** reste à effectuer prochainement pour finaliser cette partie.

---

## 💭 Réflexions et motivation

La section inclut également un rappel important sur la **motivation à coder** et l’**effet Dunning-Kruger**, ce moment où l’on croit tout savoir avant de réaliser la profondeur réelle du domaine.  
> Le message essentiel : **la persévérance prime sur le découragement.**  
> Le codage est un apprentissage continu ; reconnaître ses limites est une étape vers la maîtrise.

---

## 🧠 Bilan personnel

> “Apprendre Python, ce n’est pas juste apprendre à écrire du code, mais à raisonner, à structurer et à résoudre des problèmes.”  

Cette première partie m’a permis de :

- Poser les **bases solides** du raisonnement algorithmique,  
- Développer mes premiers **réflexes de programmation**,  
- Créer mes premiers **projets complets et fonctionnels**,  
- Renforcer ma motivation à poursuivre vers des thématiques plus avancées (fonctions, fichiers, POO…).  

---

## 🏁 Conclusion

Cette première partie se clôt avec succès :

- [x] **Compétences acquises**  
- [x] **Projets terminés**  
- [x] **Examen d’entraînement validé**  

La suite de la formation portera sur des concepts plus avancés et une structuration plus modulaire du code.  
> 💪 _“Les fondations sont posées, le reste n’est plus qu’une question de pratique et de persévérance.”_
