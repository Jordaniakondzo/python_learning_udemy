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
- [Section 48 : Le logging](#section-48--le-logging)
- [Section 49 : Installer des packages supplémentaires avec pip](#section-49--installer-des-packages-supplémentaires-avec-pip)
- [Section 50 : Étude de cas – Le Scraping](#section-50--étude-de-cas--le-scraping)
- [Section 51 : Générer des données aléatoires avec Faker](#section-51--générer-des-données-aléatoires-avec-faker)
- [Section 52 : Les environnements virtuels](#section-52--les-environnements-virtuels)

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

1. importer ce module dans un autre fichier.

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

## Section 48 : Le Logging

## 🎯 Objectif de la section

Apprendre à utiliser le module **logging** afin de suivre l’exécution d’un programme, détecter les erreurs, comprendre son comportement et faciliter le débogage.

Le logging est un outil essentiel dans les applications professionnelles.  
Il permet d’enregistrer des informations sur le fonctionnement du programme pendant son exécution.

---

## 🔹 Pourquoi utiliser le logging ?

Dans les petits scripts, il est fréquent d’utiliser `print()` pour afficher des informations.

Cependant, cette approche devient rapidement limitée dans les applications plus complexes.

Le module **logging** offre plusieurs avantages :

- Permet de définir différents **niveaux d’importance** pour les messages.
- Peut enregistrer les messages dans un **fichier**.
- Peut afficher les messages dans la **console**.
- Peut être activé ou désactivé facilement selon l’environnement.
- Permet d’analyser le comportement d’un programme après son exécution.

Pour ces raisons, le logging est utilisé dans la plupart des projets professionnels :
applications web, scripts automatisés, systèmes distribués, etc.

---

## 🔸 Les niveaux de logging

Le module `logging` utilise plusieurs niveaux de gravité pour classer les messages.

| Niveau | Description |
|--------|-------------|
| DEBUG | Informations détaillées utiles pour le débogage |
| INFO | Informations générales sur l’exécution du programme |
| WARNING | Situation inhabituelle mais non critique |
| ERROR | Une erreur s’est produite |
| CRITICAL | Erreur grave pouvant arrêter le programme |

Ces niveaux permettent de **filtrer les messages affichés ou enregistrés**.

---

## 🔹 Configuration simple du logging

Une configuration minimale peut être réalisée avec la fonction `basicConfig()`.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Demarre du programme")
```

---

## 🔹 Ajouter un format personnalisé

Il est possible de personnaliser l’affichage des messages de log.

Par exemple, on peut afficher :

- la date
- le niveau du message
- le message lui-même

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
```

Exemple de sortie :

```
2023-01-01 10:00:00 - INFO - Demarrage du programme
```

---

## 🔹 Écrire les logs dans un fichier

Le logging permet également d’enregistrer les messages dans un fichier.

Cela est particulièrement utile pour analyser le comportement d’un programme après son exécution.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="w",
)
```

➡️ Tous les messages **WARNING** et plus graves seront enregistrés dans le fichier `app.log`.

---

## 🔹 Exemple complet

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="w",
)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

---

## 🧠 Concepts clés

Quelques points importants à retenir :

- Le module **logging** est un outil standard de Python pour suivre l’exécution d’un programme.
- Il remplace avantageusement `print()` dans les applications réelles.
- Les **niveaux de logging** permettent de filtrer les messages selon leur importance.
- Les logs peuvent être envoyés vers la **console**, un **fichier**, ou plusieurs destinations.
- Une bonne configuration de logging facilite énormément le **débogage** et la **maintenance** du code.

---

## 📌 Résumé

Le logging est un mécanisme essentiel pour observer et analyser le comportement d’un programme.

Grâce au module `logging`, il est possible :

- de classer les messages selon leur importance
- d’enregistrer les événements du programme
- de faciliter le débogage et la maintenance

Dans les projets professionnels, le logging est largement utilisé pour comprendre ce qui se passe dans une application pendant son exécution.

## Section 49 : Installer des packages supplémentaires avec pip

## 🎯 Objectif de la section

Comprendre comment installer et gérer des **packages Python supplémentaires** à l’aide de l’outil **pip**.

Python possède une grande bibliothèque standard, mais la majorité des projets utilisent également des **packages externes** développés par la communauté.

Le gestionnaire de paquets **pip** permet d’installer, mettre à jour et supprimer facilement ces bibliothèques.

---

## 🔹 Qu’est-ce que pip ?

**pip** est le gestionnaire officiel de packages pour Python.

Il permet de télécharger et d’installer des bibliothèques provenant du dépôt public **PyPI (Python Package Index)**.

Grâce à pip, il est possible d'ajouter facilement des fonctionnalités à un projet Python.

Par exemple :

- manipulation de données → `pandas`
- calcul scientifique → `numpy`
- machine learning → `scikit-learn`
- développement web → `flask` ou `django`

---

## 🔸 Installer un package

Pour installer un package, on utilise la commande suivante dans le terminal :

```python
pip install package_name
```

Cette commande télécharge et installe automatiquement la bibliothèque ainsi que ses dépendances.

---

## 🔸 Installer une version spécifique

Il est parfois nécessaire d’installer une version précise d’un package.

```python
pip install package_name==version
```

Cela est utile pour assurer la **compatibilité d’un projet**.

---

## 🔸 Mettre à jour un package

Pour installer la version la plus récente d’une bibliothèque :

```python
pip install --upgrade package_name
```

---

## 🔸 Désinstaller un package

Pour supprimer un package installé :

```python
pip uninstall package_name
```

---

## 🔸 Voir les packages installés

Il est possible d’afficher la liste des packages installés dans l’environnement Python :

```python
pip list
```

Cette commande permet de vérifier les bibliothèques disponibles dans l’environnement actuel.

---

## 🔸 Informations sur un package

Pour obtenir des informations détaillées sur une bibliothèque installée :

```python
pip show package_name
```

Cela affiche par exemple :

- la version installée
- les dépendances
- l’emplacement du package

---

## 📄 Fichier requirements.txt

Dans les projets Python, il est courant d’utiliser ou créer un fichier appelé **requirements.txt**.

Ce fichier contient la liste des bibliothèques nécessaires au projet ainsi que leurs versions specifiques définies par le developpeur.

Exemple de contenu d’un fichier requirements.txt :

```python
numpy==1.20.1
pandas==1.2.4
matplotlib==3.4.2
scikit-learn==0.24.1
seaborn==0.11.1
```

Ce fichier permet de **reproduire exactement le même environnement Python sur une autre machine**.

Pour installer toutes les dépendances listées dans ce fichier :

```python
pip install -r requirements.txt
```

Cette pratique est essentielle dans les projets collaboratifs ou open-source.

---

## 🔹 Générer un fichier requirements.txt

Python permet de générer automatiquement ce fichier avec la commande :

```python
pip freeze > requirements.txt
```

Cette commande enregistre **toutes les bibliothèques installées dans l’environnement**.

Le fichier généré peut ensuite être partagé avec d'autres développeurs.

---

## 🔹 Bonnes pratiques avec pip

Quelques bonnes pratiques importantes lors de l’utilisation de pip :

- Utiliser un **environnement virtuel** pour chaque projet.
- Garder un fichier **requirements.txt** pour documenter les dépendances.
- Spécifier les versions des bibliothèques pour éviter les problèmes de compatibilité.
- Mettre à jour les packages avec prudence dans les projets existants.

Ces pratiques permettent de rendre un projet **reproductible et maintenable**.

---

## 🧠 Concepts clés

Quelques points importants à retenir :

- **pip** est l’outil standard pour gérer les bibliothèques Python.
- Les packages sont généralement téléchargés depuis **PyPI**.
- pip permet d’installer, mettre à jour et supprimer des bibliothèques.
- Le fichier **requirements.txt** permet de partager facilement les dépendances d’un projet.

---

## 📌 Résumé

Le gestionnaire **pip** est un outil essentiel de l’écosystème Python.

Il permet :

- d’installer de nouvelles bibliothèques
- de gérer les versions des packages
- de consulter les dépendances installées
- de partager facilement l’environnement d’un projet avec un fichier **requirements.txt**

Grâce à pip et à l’écosystème PyPI, Python dispose d’un très grand nombre de bibliothèques permettant de développer rapidement des applications dans de nombreux domaines.

## Section 50 : Étude de cas – Le Scraping

## 🎯 Objectif de la section

Découvrir le principe du **web scraping** à travers une démonstration pratique en Python.

Le web scraping consiste à **extraire automatiquement des informations depuis des pages web** afin de les analyser ou de les exploiter dans un programme.

Dans cette section, l’objectif n’est pas d’apprendre toutes les techniques de scraping, mais simplement de **montrer un exemple concret d’utilisation**.

---

## 🔹 Démonstration présentée

L’exemple présenté dans la formation montre comment utiliser Python pour :

- récupérer les **paroles de chansons** de certains artistes
- analyser ces textes
- manipuler les données récupérées

Cette démonstration permet d’illustrer comment Python peut être utilisé pour **collecter des données disponibles sur Internet**.

---

## 🔹 Correction d’un projet étudiant

La section contient également une vidéo dans laquelle l’instructeur **corrige un projet de scraping réalisé par un étudiant**.

Cette correction permet de montrer :

- les erreurs fréquentes lors de l’écriture d’un script de scraping
- comment améliorer la structure et la lisibilité du code
- comment rendre un script plus robuste.

---

## 🧠 Concepts clés

Quelques idées importantes à retenir :

- Le **web scraping** permet d’automatiser la collecte de données sur Internet.
- Python est souvent utilisé pour ce type de tâche grâce à ses nombreuses bibliothèques.
- Les projets réels de scraping demandent souvent une gestion des erreurs et une bonne organisation du code.

---

## 📌 Remarque

Cette section est principalement une **démonstration pratique**.

Pour approfondir le sujet du scraping (bibliothèques, bonnes pratiques, gestion des requêtes, etc.), une formation dédiée est généralement nécessaire.

## Section 51 : Générer des données aléatoires avec Faker

## 🎯 Objectif de la section

Découvrir la bibliothèque **Faker**, qui permet de générer facilement des **données aléatoires mais réalistes**.

Cette bibliothèque est particulièrement utile pour :

- tester une application
- simuler une base de données
- générer des exemples de données
- effectuer des démonstrations ou des tests.

---

## 🔹 Installation de Faker

La bibliothèque peut être installée avec pip :

```python
pip install Faker
```

Une fois installée, il est possible de créer un générateur de données avec :

```python
from faker import Faker
```

Faker peut produire de nombreux types de données réalistes.

---

## 🔹 Générer des données uniques

Faker permet de générer des valeurs **uniques** grâce à l'attribut `unique`.

Cela garantit que certaines données (comme les noms ou les emails) ne seront pas dupliquées.

```python
from faker import Faker

fake = Faker()

name = fake.unique.name()
email = fake.unique.email()
```

Cette fonctionnalité est particulièrement utile lors de la génération de bases de données fictives.

---

## 🔹 Les "Providers"

Faker fonctionne avec des **providers**, qui sont des modules permettant de générer différents types de données.

Exemples de données disponibles :

- noms et prénoms
- adresses
- numéros de téléphone
- emails
- dates
- entreprises
- textes aléatoires

Exemple :

```python
from faker import Faker

fake = Faker()

name = fake.name()
address = fake.address()
phone_number = fake.phone_number()
email = fake.email()
date = fake.date()
company = fake.company()
text = fake.text()
```

Ces providers permettent de produire des données proches de celles utilisées dans des applications réelles.

---

## 🔹 Générer des données spécifiques

Faker permet également de générer des données adaptées à un pays ou une langue grâce au concept de **locale**.

Par exemple :

```python
from faker import Faker

fake = Faker('fr_FR') # Génération des données en français.

name = fake.name()
address = fake.address()
phone_number = fake.phone_number()

```

👉 Faker supporte de nombreuses locales : `en_US`, `fr_FR`, `de_DE`, `es_ES`, etc.

---

## 🔹 Exemple d’utilisation avec un mini-script

Pour mieux comprendre l’utilisation de la bibliothèque **Faker**, un mini-script Python a été réalisé afin de générer une base de données fictive d’utilisateurs.

Ce script permet notamment de :

- générer **1000 utilisateurs**
- créer des données réalistes (nom, email, adresse, téléphone)
- générer une **date de naissance aléatoire**
- enregistrer les données dans un **fichier JSON**

Le script complet est disponible ici :

📁 Exemple pratique : [mini-script](../Exercices/Partie_02/db_aleatoire_avec_Faker.py)

Ce script génère ensuite un fichier :

[`db_aleatoire.json`](../Exercices/Partie_02/db_aleatoire.json)

qui contient une base de données fictive pouvant être utilisée pour des tests ou des démonstrations.

---
## 🧠 Cas d'utilisation typiques

La bibliothèque Faker est souvent utilisée pour :

- tester une base de données
- remplir un site web avec des données fictives
- simuler des utilisateurs
- créer des jeux de données pour des démonstrations.
- Très utile pour les projets de data science, bases de données, tests unitaires, API, etc.

---

## 📌 Résumé

La bibliothèque **Faker** permet de générer facilement des **données réalistes et aléatoires**.

Elle est très utile pour :

- tester des applications
- créer des bases de données fictives
- simuler des utilisateurs

Grâce à ses nombreux providers et à la gestion des locales, Faker permet de produire des données proches de la réalité.

## Section 52 : Les environnements virtuels

## 🎯 Objectif de la section

Comprendre le rôle des **environnements virtuels** en Python et apprendre à les utiliser pour isoler les dépendances d’un projet.

Les environnements virtuels permettent de créer un espace indépendant dans lequel on peut installer des bibliothèques spécifiques sans affecter les autres projets Python.

---

## 🔹 Pourquoi utiliser un environnement virtuel ?

Dans un système Python classique, toutes les bibliothèques sont installées **globalement**.

Cela peut provoquer plusieurs problèmes :

- conflits de versions entre différentes bibliothèques
- incompatibilités entre plusieurs projets
- difficulté à reproduire un environnement de développement.

Les environnements virtuels permettent de résoudre ces problèmes en isolant les dépendances de chaque projet.

Chaque projet peut ainsi utiliser ses **propres versions de bibliothèques**.

---

## 🔹 Créer un environnement virtuel

Python propose un module intégré appelé **venv** permettant de créer un environnement virtuel.

Dans le terminal :

Exemple :

```python
python3 -m venv env
```

Cette commande crée un dossier env/ contenant un environnement Python isolé.

---

## 🔹 Activer l’environnement virtuel

Une fois l’environnement créé, il doit être activé.

Sur **Windows** :

```python
env\Scripts\activate
```

Sur **macOS / Linux** :

```python
source env/bin/activate
```

Lorsque l’environnement est activé, les packages installés avec `pip` seront installés uniquement dans cet environnement.

---

## 🔹 Installer des packages dans l’environnement

Une fois l’environnement activé, on peut installer des bibliothèques avec `pip` :

```python
pip install package_name
```

Ces bibliothèques seront installées **uniquement dans l’environnement virtuel actif**.

---

## 🔹 Désactiver l’environnement virtuel

Pour quitter l’environnement virtuel :

```python
deactivate
```

Le système revient alors à l’environnement Python global.

---

## 🧠 Concepts clés

Quelques idées importantes à retenir :

- Un environnement virtuel isole les dépendances d’un projet Python.
- Chaque projet peut utiliser ses propres versions de bibliothèques.
- L’outil `venv` est intégré à Python et permet de créer facilement ces environnements.
- Les environnements virtuels facilitent la gestion des dépendances et la reproductibilité des projets.

---

## 📌 Résumé

Les environnements virtuels sont une pratique essentielle en développement Python.

Ils permettent :

- d’éviter les conflits entre bibliothèques
- de maintenir des projets indépendants
- de reproduire facilement un environnement de développement

Dans les projets Python modernes, l’utilisation d’environnements virtuels est considérée comme une **bonne pratique indispensable**.
