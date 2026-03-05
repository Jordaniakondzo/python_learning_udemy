# Partie 02 — Suite : Structuration et outils avancés en Python

⬅️ Retour : [Partie 02](Partie_02_01.md)

## 📚 Contenu de cette partie

Cette suite de la Partie 02 couvre notamment :

- [📝 Introduction](#-introduction)
- [🎯 Objectif de cette suite](#-objectif-de-cette-suite)
- [Section 44 : Les annotations de type](#section-44--les-annotations-de-type)
- [Section 45 : Les modules](#section-45--les-modules)
- [Section 46 : Les packages](#section-46--les-packages)
- [Section 47 : Documenter son code](#section-47--documenter-son-code)

---

## 📝 Introduction

Ce fichier constitue la **suite de la deuxième partie de l’apprentissage Python**.  
Après avoir exploré la manipulation de fichiers, la persistance des données, les fonctions et plusieurs projets pratiques d’automatisation, nous abordons désormais des notions essentielles pour écrire un code **plus structuré, plus lisible et plus professionnel**.

Dans cette continuité, nous allons introduire des outils et concepts qui permettent de mieux organiser un programme Python et d’améliorer sa fiabilité.

Cette étape marque également le début de la **programmation orientée objet (POO)**, une approche fondamentale pour organiser le code dans des applications plus complexes.

---

## 🎯 Objectif de cette suite

Cette section vise à nous faire passer d’une logique de scripts fonctionnels à une approche plus proche du développement logiciel réel.  
Nous allons apprendre à :

- documenter et sécuriser notre code avec les **annotations de type**,
- organiser nos programmes avec des **modules Python**,
- structurer progressivement nos projets,
- découvrir les bases de la **programmation orientée objet (POO)**,
- adopter de **bonnes pratiques de développement**.

---

## Section 44 : Les annotations de type

## 📌 Objectif de la section

Dans cette section, nous découvrons les **annotations de type** (_type hints_) en Python :  
elles permettent d’indiquer clairement quels types de données sont attendus en entrée d’une fonction, et quel type est renvoyé en sortie.

🎯 L’objectif est de rendre notre code :

- plus lisible,
- plus fiable,
- plus simple à maintenir,
- et mieux assisté par les outils (autocomplétion, vérifications, IDE).

---

## 🔹 À quoi servent les annotations de type ?

Les annotations de type ne changent pas l’exécution du programme (Python reste dynamiquement typé),  
mais elles apportent une **documentation explicite** et permettent aux outils de détecter des incohérences.

✅ Elles servent notamment à :

- clarifier l’intention du développeur (contrat d’utilisation d’une fonction),
- réduire les erreurs liées aux mauvais types,
- améliorer l’autocomplétion dans l’IDE,
- faciliter le travail en équipe (code plus “auto-explicatif”),
- permettre une vérification statique avec des outils comme `mypy`.

💡 **Exemple textuel :** une fonction qui attend un `int` et reçoit une `str` ne plantera pas toujours immédiatement, mais cela peut provoquer un bug logique — les annotations aident à le repérer plus tôt.

---

## 🔸 La syntaxe (type hints)

Les annotations de type se placent :

- après le nom du paramètre : `param: type`
- après la flèche : `-> type` pour le type de retour

👉 Exemple 1 :

```python
def addition(a: int, b: int) -> int:
    """
    Additionne deux entiers et retourne un entier.
    """
    return a + b


resultat = addition(3, 5)
print(resultat)
```

💡 On peut annoter :

- des variables,
- des paramètres de fonctions,
- des retours de fonctions,
- et même des structures plus complexes (listes, dictionnaires, tuples…).

👉 Exemple 2 :

```python
age: int = 25
nom: str = "Jordani"
prix: float = 19.99
est_actif: bool = True

print(age, nom, prix, est_actif)
```

---

## 🔹 Types courants à connaître

- `int`, `float`, `str`, `bool`
- `list`, `dict`, `tuple`, `set`
- `None` (pour indiquer “ne retourne rien”)
- `Optional[...]` (valeur ou None)
- `Union[...]` (plusieurs types possibles)
- `Any` (type non spécifié / flexible)

💡 **Exemple textuel :**

- une fonction peut renvoyer soit un nombre, soit `None` si aucune valeur n’est trouvée → `Optional[int]`.

---

## 🔸 Annoter des collections (listes, dictionnaires…)

Pour des structures de données, on précise le type des éléments.

👉 Exemple 1 :

```python
def somme_notes(notes: list[float]) -> float:
    """
    Calcule la moyenne d'une liste de notes.
    """
    return sum(notes) / len(notes)


print(somme_notes([12.5, 15.0, 17.5]))
```

💡 **Exemple textuel :**

- une liste de prénoms → `list[str]`
- un dictionnaire “nom → âge” → `dict[str, int]`

👉 Exemple 2 :

```python
def afficher_personne(personne: dict[str, int]) -> None:
    """
    Affiche les informations d'une personne.
    """
    for cle, valeur in personne.items():
        print(f"{cle}: {valeur}")


afficher_personne({"age": 25, "score": 96})
```

---

## 🔸 Cas pratique : fonctions plus sûres et plus claires

Grâce aux annotations, une fonction devient plus facile à comprendre sans avoir à lire tout son contenu.

💡 **Exemple textuel :**

- une fonction `calculer_moyenne(notes: list[float]) -> float` annonce immédiatement :
  - le format attendu,
  - et ce qu’elle renvoie.

---

## 🧰 Configurer les annotations de type dans Visual Studio Code

Visual Studio Code peut exploiter les annotations via l’analyseur Python (souvent Pylance).

✅ Ce que cela apporte :

- surlignage d’erreurs potentielles,
- suggestions de types,
- autocomplétion plus intelligente,
- “hover” informatif sur les fonctions.

💡 Dans l’IDE, nous pouvons choisir un mode de vérification (souple → strict), selon le niveau de rigueur souhaité.

---

## ✅ Utiliser `mypy` pour vérifier notre code

`mypy` est un outil de **vérification statique des types**.

Il analyse le code et signale :

- les types incohérents,
- les retours de fonctions incorrects,
- les usages non conformes aux annotations.

💡 **Point clé :**

- on peut l’utiliser progressivement (pas besoin d’un typage parfait dès le début),
- c’est idéal pour rendre un projet plus solide avec le temps.

---

## 🧠 Concepts clés

- Python reste dynamiquement typé : les annotations n’empêchent pas l’exécution.
- Les annotations améliorent la lisibilité, la maintenance, et la documentation.
- Les IDE (VS Code) utilisent ces indications pour guider et prévenir des erreurs.
- `mypy` permet de valider la cohérence des types de manière automatique.
- Les annotations deviennent particulièrement utiles sur les projets complexes et en équipe.

---

## 🔍 Améliorations possibles

- Ajouter progressivement des annotations dans nos projets existants (ex : trieur de fichiers, liste de courses, etc.).
- Introduire des types plus avancés (`TypedDict`, `Protocol`, `Literal`) au fur et à mesure de notre progression.
- Passer d’un typage “léger” à un typage plus strict sur les projets plus sérieux.
- Coupler typage + tests unitaires pour un maximum de fiabilité.

---

## 💡 Pourquoi cette section est importante

Cette section marque une transition vers une programmation plus professionnelle :  
nous ne cherchons plus seulement à écrire du code qui fonctionne, mais à écrire du code :

- robuste,
- explicite,
- maintenable,
- et assisté par des outils modernes.

C’est une base essentielle pour les grandes applications, les projets en équipe, et même les projets data/IA.

---

## 🗒️ Résumé

Cette section nous a permis de :

- comprendre l’utilité des annotations de type,
- apprendre la syntaxe et les types courants,
- annoter des fonctions et des structures de données,
- configurer l’aide dans VS Code,
- et découvrir `mypy` pour vérifier la cohérence de notre code.

👉 En résumé, les annotations de type nous permettent de passer d’un code “simple” à un code **plus clair, plus fiable, et plus professionnel**.

## Section 45 : Les modules

## 📌 Objectif de la section

Dans cette section, nous découvrons le concept fondamental de **module Python**.  
Un module permet d’organiser le code en plusieurs fichiers, de le rendre réutilisable et plus facile à maintenir.

Cette notion est essentielle dès que les programmes commencent à grandir, et constitue une base indispensable avant d’aborder les **packages** et la **programmation orientée objet**.

---

## 🔹 Qu’est-ce qu’un module Python ?

Un module est simplement un **fichier Python (`.py`)** contenant :

- des fonctions,
- des variables,
- des classes,
- ou du code exécutable.

L’objectif principal d’un module est de **regrouper logiquement du code** et de pouvoir le réutiliser dans d’autres scripts.

💡 Exemple concret :  
plutôt que d’avoir toutes nos fonctions dans un seul fichier, nous pouvons créer un module `utils.py` qui regroupe des fonctions utilitaires, puis l’importer ailleurs.

---

## 🔸 Définition et syntaxe des imports

Python fournit plusieurs manières d’importer un module, selon le niveau de contrôle et de lisibilité souhaité.

### Importer un module entier

Cette méthode importe le module comme un tout.

```python
import random
print(random.randint(1, 10))
```

Les fonctions du module sont alors appelées via le nom du module.

---

### Importer un élément précis d’un module

Il est possible d’importer uniquement ce dont on a besoin.

```python
from random import randint
print(randint(1, 10))
```

Cette approche améliore la lisibilité mais nécessite de bien connaître le contenu du module.

---

### Importer avec un alias

Les alias permettent de raccourcir les noms de modules ou d’éviter les conflits.

```python
import random as rd
print(rd.randint(1, 10))
```

```python
import datetime as dt
print(dt.datetime.now())
```

C’est une pratique très courante dans le code professionnel.

---

## 🔹 Créer notre propre module Python

Créer un module personnalisé consiste simplement à créer un nouveau fichier `.py`.

📌 Étapes générales :

1. créer un fichier Python (ex : `mon_module.py`),
2. y définir des fonctions, variables ou classes,

```python
def additionner(a, b):
    return a + b
```

3. importer ce module dans un autre fichier.

```python
from mon_module import additionner
print(additionner(1, 2))
```

💡 Cette pratique est essentielle pour structurer correctement un projet.

---

## 🔸 La variable spéciale `__name__`

Python fournit une variable spéciale appelée `__name__`.

Elle permet de distinguer :

- un fichier exécuté directement,
- d’un fichier importé comme module.

```python
def main():
    print("Hello world !")
if __name__ == "__main__":
    main()
```

💡 Grâce à `if __name__ == "__main__":`, nous pouvons :

- exécuter du code de test,
- tout en empêchant son exécution lors de l’import.

C’est une **bonne pratique incontournable** en Python.

---

## 🔹 Le Python Path

Pour qu’un module soit importable, Python doit savoir **où le trouver**.  
Cette recherche s’effectue à travers le **Python Path**, une liste de dossiers parcourus lors des imports.

💡 Les modules peuvent être trouvés :

- dans le dossier courant,
- dans les bibliothèques standards,
- dans les chemins définis par le système.

---

On peut l'afficher ainsi :

```python
import sys
print(sys.path)
```

On peut aussi ajouter un dossier au Python Path (temporairement).

```python
import sys
sys.path.append("/chemin/vers/mon/dossier")
```

## 🔸 Modifier le Python Path (selon le système)

Il est parfois nécessaire d’ajouter manuellement un chemin pour rendre un module accessible.
La formation montre aussi comment modifier le Python Path selon notre OS (Windows, macOS, Linux).

Pour la démonstration complète, voir :

➡️ [Modification du Python Path selon le système](https://www.udemy.com/course/formation-complete-python/learn/lecture/18014223#overview)

---

⚠️ Bonne pratique :  
éviter de modifier le Python Path globalement si ce n’est pas nécessaire.  
Privilégier les **environnements virtuels** et une bonne organisation de projet.

---

## 🔹 Actualiser un module Python

Lorsqu’un module est modifié pendant une session, Python ne le recharge pas automatiquement.

Il est parfois nécessaire de forcer le rechargement.

```python
import importlib
import mon_module
importlib.reload(mon_module)
```

💡 Ce cas se rencontre souvent en phase de développement ou dans les notebooks.

---

## 🧠 Concepts clés

- Un module est un fichier Python réutilisable.

- Les imports permettent de structurer et partager le code.
- `__name__` permet de contrôler le comportement d’un fichier.
- Le Python Path détermine où Python cherche les modules.
- Une bonne organisation en modules est essentielle pour les projets moyens et grands.

---

## 💡 Pourquoi cette section est importante

Cette section marque une étape clé vers une programmation plus professionnelle.

Grâce aux modules, nous pouvons :

- éviter la duplication de code,
- améliorer la lisibilité des projets,
- structurer nos applications,
- préparer le terrain pour les **packages** et la **POO**.

Les modules sont la pierre angulaire de toute application Python sérieuse.

---

## 🗒️ Résumé

Dans cette section, nous avons appris à :

- comprendre ce qu’est un module Python,
- utiliser différentes syntaxes d’import,
- créer nos propres modules,
- exploiter la variable `__name__`,
- comprendre le rôle du Python Path,
- et structurer notre code de manière plus propre et maintenable.

👉 Cette section nous prépare directement à la suivante :  
**les packages Python**, qui permettent d’organiser des projets encore plus complexes.

## Section 46 : Les packages

## 📌 Objectif de la section

Comprendre ce qu’est un package Python, comment il se distingue d’un module simple, et comment organiser un projet Python de manière professionnelle, scalable et maintenable.
Cette section marque une étape importante : on ne pense plus en fichiers isolés, mais en architecture de projet.

## 🔹 Qu’est-ce qu’un package ?

Un package est un dossier Python qui regroupe plusieurs modules (fichiers .py) liés par une même logique fonctionnelle.

👉 Autrement dit :

- un module = un fichier `.py`

- un package = un dossier contenant plusieurs modules

Un package permet :

- de structurer un projet complexe,

- d’éviter les fichiers trop longs,

- de mieux organiser les responsabilités du code,

- de faciliter la réutilisation et la maintenance.

## 🔹 Pourquoi utiliser des packages ?

L’utilisation de packages devient indispensable dès que :

- un projet dépasse quelques fichiers,

- plusieurs fonctionnalités doivent cohabiter,

- on travaille en équipe,

- on souhaite publier ou partager du code.

**Avantages principaux :**

- 📦 Organisation logique du code

- 🔁 Réutilisabilité des modules

- 🧭 Lisibilité de l’architecture

- 🚫 Réduction des conflits de noms

- 🧪 Meilleure testabilité

## 🔹 Structure typique d’un package

Voici une structure conceptuelle classique :

```python
mon_package/
    __init__.py
    module1.py
    module2.py
    utils.py
    ...
```

- `mon_package/` → le package

- `module_1.py`, `module_2.py` → modules internes

- `__init__.py` → fichier spécial qui définit le comportement du package

## 🔹 Le fichier `__init__.py`

📍 Rôle du fichier `__init__.py`

Le fichier `__init__.py` :

- indique à Python que le dossier est un package,

- est exécuté lors de l’import du package,

- peut exposer certaines fonctions ou classes,

- permet de contrôler ce qui est importé depuis le package.

Aujourd’hui, `__init__.py` n’est plus strictement obligatoire (Python ≥ 3.3),
mais il reste une bonne pratique dans les projets structurés.

## 🔸 Exemple de comportement de `__init__.py`

Dans `__init__.py`, on peut :

- importer certains éléments internes,

- définir une API claire du package,

- éviter des imports trop profonds côté utilisateur.

👉 Cela permet ensuite d’importer plus proprement le package.

## 🔹 Importer depuis un package

On peut importer :

- un module entier,

- une fonction précise du module,

- plusieurs éléments à la fois.

**Types d’imports possibles :**

- import direct du package

- import d’un module du package

- import d’éléments spécifiques

⚠️ Bonnes pratiques :

- éviter les imports globaux excessifs,

- privilégier des imports explicites et lisibles,

- limiter l’usage de `from ... import *`.

## 🔹 Packages et hiérarchie

Un package peut contenir des sous-packages, ce qui permet une organisation hiérarchique.

Exemple conceptuel :

```python
application/
│
├── core/
│   ├── __init__.py
│   ├── logic.py
│
├── services/
│   ├── __init__.py
│   ├── api.py
│
├── main.py
```

👉 Cette organisation est très proche des standards professionnels (web, data, IA, backend…).

## 💡 Concepts clés à retenir

- Un package est un dossier structurant plusieurs modules

- `__init__.py` permet de contrôler l’interface du package

- Les packages rendent le code plus clair, plus robuste et plus professionnel

- Ils sont indispensables pour les projets de taille moyenne à grande

- C’est une base incontournable avant d’aborder :

  - la POO,

  - les tests,

  - les frameworks,

  - la distribution de code

## 🗒️ Résumé

Avec les packages, nous passons :

- d’un code linéaire à une architecture organisée,

- de scripts isolés à des projets structurés,

- d’un apprentissage débutant à une vision développeur professionnel.

👉 Les packages constituent une étape essentielle vers une programmation plus professionnelle et modulaire.

## Section 47 : Documenter son code

## 🎯 Objectif de la section

Comprendre comment documenter correctement son code afin de le rendre plus clair, plus professionnel et plus facile à maintenir.  
Une bonne documentation est essentielle dans tout projet sérieux, qu’il soit personnel, académique ou collaboratif.

Elle permet aux développeurs y compris à soi-même plusieurs mois plus tard de comprendre rapidement le rôle et le fonctionnement du code.

---

# ✏️ Pourquoi documenter son code ?

Documenter son code présente plusieurs avantages importants :

- Facilite la compréhension du code, même longtemps après son écriture.
- Aide les autres développeurs à utiliser correctement les fonctions, classes et modules.
- Permet aux outils de développement (IDE) d’afficher des informations utiles automatiquement.
- Réduit les erreurs en clarifiant les intentions et la logique du programme.
- Rend le projet plus professionnel et plus maintenable.

Dans les projets collaboratifs ou open-source, la documentation est souvent aussi importante que le code lui-même.

---

# 📌 Les commentaires

Les **commentaires** permettent d'expliquer certaines parties spécifiques du code.

Ils sont précédés du symbole `#` et ne sont pas exécutés par Python.

## Commentaires simples

Les commentaires sont utilisés pour expliquer une ligne ou un bloc précis du programme.

```python
# On calcule la moyenne des notes
moyenne = sum(notes) / len(notes)
```

### Bonnes pratiques

Un bon commentaire doit être :

- court et pertinent
- clair et précis
- utile pour comprendre l’intention du développeur

Une règle importante consiste à **expliquer le "pourquoi" plutôt que le "comment"**, car le code lui-même décrit généralement déjà le fonctionnement.

---

## 📚 Les docstrings

Les **docstrings** (documentation strings) sont des chaînes de caractères utilisées pour documenter les éléments principaux d’un programme Python.

Elles sont placées au début :

- d'une fonction
- d'une classe
- d'un module

Contrairement aux commentaires, les docstrings peuvent être **consultées dynamiquement par Python et les outils de développement**.

Elles décrivent généralement :

- le rôle de l'élément
- ses paramètres
- sa valeur de retour
- parfois des exemples d'utilisation

## Exemple pour une fonction

```python
def addition(a: int, b: int) -> int:
    """
    Additionne deux nombres entiers.

    Paramètres :
        a (int) : premier nombre
        b (int) : second nombre

    Retour :
        int : la somme de a et b
    """
    return a + b
```

---

## 🧱 Docstring pour un module

Un module Python peut également contenir une docstring placée au tout début du fichier.

Cette docstring décrit généralement :

- le rôle du module
- les fonctionnalités principales qu’il contient
- éventuellement l’auteur ou la version.

```python
"""
Module utilitaires pour le projet.

Contient des fonctions de calcul et de formatage.
"""
```

---

## 🏗️ Docstring pour une classe

Les classes peuvent aussi être documentées avec une docstring afin d'expliquer leur rôle et leur fonctionnement.

On y décrit généralement :

- l’objectif de la classe
- ses attributs principaux
- ses méthodes importantes.

```python
class Personne:
    """
    Classe représentant une personne.

    Attributs :
        nom (str) : le nom de la personne
        age (int) : l'âge de la personne

    Métodes :
        saluer() : affiche un message de salutation
    """
```

---

## 🧠 Styles de documentation

Python accepte plusieurs styles de docstrings.  
Le choix du style dépend souvent des conventions du projet ou de l’équipe.

Les styles les plus courants sont :

- **Style classique**  
  Souvent utilisé dans les projets simples ou personnels.

- **Google Style**  
  Très populaire dans les projets modernes.

- **NumPy Style**  
  Utilisé dans les projets scientifiques et les bibliothèques de calcul.

- **reStructuredText (Sphinx)**  
  Utilisé pour générer une documentation automatique complète.

## Exemple Google Style

```python
def division(a: float, b: float) -> float:
    """
    Une fonction qui divise a par b.

    Args:
        a (float): Numérateur.
        b (float): Dénominateur.

    Returns:
        float: Résultat de la division.

    Raises:
        ZeroDivisionError: Si b vaut 0.
    """
    return a / b

```

---

## 🔍 Accéder à la documentation dans Python

Les docstrings peuvent être consultées directement dans Python.

Dans un terminal Python ou un notebook, on peut utiliser la fonction `help()` :

```python
help(division)
```

Dans un **IDE moderne** (VS Code, PyCharm, etc.), la docstring apparaît automatiquement :

- au survol d’une fonction
- lors de l’autocomplétion
- dans la documentation intégrée.

---

## 🧠 Concepts clés

Quelques idées importantes à retenir :

- Les **commentaires** expliquent des détails locaux du code.
- Les **docstrings** décrivent le rôle global d’une fonction, d’une classe ou d’un module.
- Une bonne documentation rend le code plus **maintenable**, **compréhensible** et **professionnel**.
- Des outils comme **Sphinx** peuvent générer automatiquement une documentation complète à partir des docstrings.

---

## 📌 Résumé

La documentation est une partie essentielle du développement logiciel.

En Python, elle repose principalement sur deux éléments :

- les **commentaires**, utilisés pour expliquer certains détails du code
- les **docstrings**, utilisées pour décrire les fonctions, classes et modules

En adoptant de bonnes pratiques de documentation, il devient beaucoup plus facile de comprendre, maintenir et partager un projet Python.
