# 📘 Partie 2 — Vers des projets plus avancés

## 📑 Table des matières

- [📝 Introduction](#-introduction)
- [🎯 Objectif de cette nouvelle phase](#-objectif-de-cette-nouvelle-phase)
- [📚 Ce que cette partie va apporter](#-ce-que-cette-partie-va-apporter)
- [🧠 État d’esprit pour cette partie](#-état-desprit-pour-cette-partie)
- [Section 34 : Les fichiers](#section-34--les-fichiers)
- [Section 35 : Projet #6 — Liste de courses avec sauvegarde](#section-35--projet-6--liste-de-courses-avec-sauvegarde)
- [Section 36 : Gérer les chemins de fichiers avec Pathlib](#section-36--gérer-les-chemins-de-fichiers-avec-pathlib)
- [Section 37 : Les dictionnaires](#section-37--les-dictionnaires)
- [Section 38 : Projet #7 — Le trieur de fichiers](#section-38--projet-7--le-trieur-de-fichiers)
- [Section 39 : Projet #8 — Le créateur de dossiers](#section-39--projet-8--le-créateur-de-dossiers)
- [Section 40 : Projet #9 — Organiser des données](#section-40--projet-9--organiser-des-données)
- [Section 41 : Gestion des erreurs avec les exceptions](#section-41--gestion-des-erreurs-avec-les-exceptions)

---

## 📝 Introduction

Cette deuxième partie marque une **étape importante** dans mon apprentissage de Python.  
Après avoir posé les fondations techniques dans la première partie (types, variables, boucles, conditions, projets simples), il est maintenant temps de **monter en puissance**.

L’objectif n’est plus seulement de faire fonctionner un script, mais de **penser comme un développeur** :  
structurer, organiser, réutiliser et rendre le code plus professionnel.  

Cette phase me fera découvrir les outils essentiels du quotidien d’un programmeur Python — depuis la **manipulation de fichiers** jusqu’à la **programmation orientée objet**, en passant par la **gestion d’erreurs**, la **création de fonctions**, et la **modularité du code**.

---

## 🎯 Objectif de cette nouvelle phase

Entrer dans une programmation **plus professionnelle, modulaire et polyvalente**.  
Cette deuxième partie marque le passage du code d’apprentissage à la **construction d’applications réelles**, en posant les bases de l’ingénierie logicielle en Python.

---

## 📚 Ce que cette partie va apporter

Cette phase va consolider la maîtrise du langage et introduire des pratiques de développeur professionnel :

- 🗂️ **Manipulation de fichiers** : lire, écrire et organiser des données persistantes  
- ⚙️ **Gestion d’erreurs** : anticiper et corriger les bugs avec `try/except`  
- 🧩 **Fonctions** : structurer le code pour le rendre **réutilisable et lisible**  
- 🧾 **Annotations de type** : documenter et sécuriser les fonctions  
- 📦 **Modules et packages** : organiser le code en plusieurs fichiers logiques  
- 🧠 **Logging** : suivre l’exécution du programme pour faciliter le débogage  
- 🌐 **Environnements virtuels** : isoler chaque projet Python proprement  
- 🧱 **Programmation orientée objet (POO)** : créer des classes, méthodes et objets  
- 🗃️ **Bases de données** : stocker et interroger des données avec SQLite ou TinyDB  

---

## 🧠 État d’esprit pour cette partie

> “On ne code plus seulement pour que ça fonctionne, mais pour que ce soit maintenable, clair et évolutif.”

- On passe d’un apprentissage **linéaire** à une **construction modulaire et pensée à long terme**.  
- Les projets deviennent plus **réalistes**, **robustes** et **orientés utilisateur**.  
- On apprend à penser comme un **développeur** :  
  - structurer,  
  - tester,  
  - documenter,  
  - et déboguer avec méthode.  

---

## Section 34 : Les fichiers

## 📌 Objectif de la section

Apprendre à **lire, écrire et manipuler des fichiers texte et JSON** en Python.  
Comprendre comment interagir avec le système de fichiers pour **stocker et récupérer des données de manière persistante**.

---

## 🔹 Étape 1 : Lire un fichier `.txt`

Lire un fichier texte permet d’extraire son contenu pour traitement ou affichage.

- Mode `"r"` = lecture seule  
- L’instruction `with open(...)` permet d’ouvrir un fichier **en toute sécurité** : elle gère automatiquement la fermeture du fichier, même en cas d’erreur.  
- La méthode `.read()` lit tout le contenu d’un coup, tandis que `.readlines()` renvoie une liste de lignes.

📂 Exemple pratique : [Lire_un_fichier.py](../Exercices/Partie_02/Lire_un_fichier.py)

**✅ Bonnes pratiques:**

- Toujours préciser l’encodage (`utf-8` par défaut) pour éviter les erreurs de lecture.
- Utiliser `strip()` ou `splitlines()` pour nettoyer le texte.
- Pour de gros fichiers, lire ligne par ligne avec une boucle `for`.

---

## 🔹 Étape 2 : Écrire dans un fichier `.txt`

Écrire dans un fichier consiste à créer ou modifier un fichier existant.

**Modes d’ouverture :**

- `"w"` ➡️ écrase le contenu existant (écriture neuve).
- `"a"` ➡️ ajoute du texte à la fin du fichier sans le supprimer.
- `"x"` ➡️ crée un nouveau fichier et génère une erreur s’il existe déjà.

📂 Exemple pratique : [Ecrire_dans_le_fichier.py](../Exercices/Partie_02/Ecrire_dans_le_fichier.py)

---

## 🔹 Étape 3 : Lire un fichier JSON

Les fichiers JSON permettent de stocker des données structurées (sous forme de dictionnaires ou de listes).
C’est le format le plus courant pour échanger des données entre applications.

**Méthode :**

- `json.load()` lit et convertit le contenu JSON en objet Python (dictionnaire ou liste).
- Le fichier doit être correctement formaté : les clés entre guillemets, pas de virgule finale, etc.

📂 Exemple pratique : [Lire_un_fichier_Json.py](../Exercices/Partie_02/Lire_un_fichier_Json.py)

**⚠️ Attention :**

Une erreur `json.decoder.JSONDecodeError` est levée si le fichier est vide ou mal formé.
Il est donc judicieux d’utiliser `try/except` pour sécuriser la lecture.

---

## 🔹 Étape 4 : Écrire dans un fichier JSON

L’écriture dans un fichier JSON permet de sauvegarder un dictionnaire Python de façon persistante.

**Méthode :**

- `json.dump()` convertit un dictionnaire en texte JSON.
- L’argument `indent=4` rend le fichier plus lisible.
- L’argument `ensure_ascii=False` garde les caractères accentués.  
- Toujours ouvrir le fichier en mode `"w"` pour réécrire proprement  

📂 Exemple pratique : [Ecrire_dans_un_fichier_Json.py](../Exercices/Partie_02/Ecrire_dans_un_fichier_Json.py)

**✅ Bonnes pratiques :**

- Toujours réécrire un JSON complet plutôt que d’essayer de le “modifier” directement.
- Sauvegarder une copie avant chaque réécriture.

---

## 🔹 Étape 5 : Ajouter des données dans un fichier JSON

L’ajout de données dans un fichier `JSON` implique de charger les données existantes, de les modifier en mémoire, puis de les réécrire intégralement.

**Pratique :**

- Lire d’abord le contenu du fichier avec `json.load()`  
- Vérifier que la structure est bien une **des données JSON**  
- Ajouter la nouvelle donnée avec une méthode spécifique  
- Réécrire le fichier complet avec `json.dump()`  

📂 Exemple pratique : [Ajout_donnees_fichier_Json.py](../Partie_02/Ajout_donnees_fichier_Json.py)

---

## 🧠 Concepts clés

- Toujours utiliser **`with open(...)`** pour éviter les oublis de fermeture de fichier  
- Bien choisir le mode d’ouverture :  
  - `"r"` → lecture  
  - `"w"` → écriture (écrase)  
  - `"a"` → ajout  
  - `"x"` → création d’un nouveau fichier  
- Les fichiers JSON doivent être **correctement formatés** pour être lus
- Anticiper les exceptions (`FileNotFoundError`, `JSONDecodeError`, `PermissionError`) avec `try/except`.

---

## 🧾 Résumé

Cette section constitue un pivot essentiel de l’apprentissage Python :
elle introduit la persistance des données, indispensable pour toute application réelle.

Grâce à la lecture et à l’écriture dans les fichiers texte et JSON, on peut désormais :

- sauvegarder les résultats d’un programme,
- stocker des informations entre plusieurs exécutions,
- et manipuler des structures de données complexes.

>💡 Cette étape prépare directement aux prochaines sections consacrées à la structuration du code, la gestion d’erreurs avancée, et l’intégration avec des bases de données.

---

## Section 35 : Projet #6 — Liste de courses avec sauvegarde

## 🎯 Objectif du projet

Améliorer le projet précédent **“Liste de courses”** en ajoutant une **sauvegarde automatique dans un fichier JSON**.  
L’objectif est de rendre le programme **persistant entre les sessions**, c’est-à-dire que la liste reste disponible même après la fermeture du script.

---

## 🛠️ Compétences mobilisées

- Utilisation du module **`json`** pour la sérialisation (écriture) et désérialisation (lecture) de données.  
- Utilisation du module **`os`** pour vérifier l’existence du fichier.  
- Gestion de l’encodage avec `utf-8`.  
- Structure logique du programme avec une **boucle principale** et un **menu utilisateur**.  
- Sauvegarde automatique à la sortie du programme.  
- Utilisation de **`sys.exit()`** pour une sortie propre.  

---

## 🧪 Fonctionnalités implémentées

1. **Chargement initial de la liste :**  
   - Si le fichier `liste_de_courses.json` existe, le programme le lit et charge les données.  
   - Sinon, il crée une liste vide.

2. **Ajout d’un élément :**  
   - L’utilisateur saisit un article à ajouter à la liste.  
   - L’élément est ajouté, et une confirmation est affichée.

3. **Suppression d’un élément :**  
   - Vérifie si l’élément existe dans la liste.  
   - Gère le cas d’une liste vide ou d’un élément inexistant.  
   - Affiche la liste mise à jour avec les indices.

4. **Affichage de la liste actuelle :**  
   - Affiche les éléments avec leur index.  
   - Indique clairement si la liste est vide.

5. **Vidage de la liste :**  
   - Supprime tous les éléments avec `clear()`.  
   - Affiche un message de confirmation.

6. **Sauvegarde automatique et sortie :**  
   - Avant de quitter (`option 5`), le programme enregistre la liste actuelle dans `liste_de_courses.json`.  
   - Les données sont stockées au format lisible avec `indent=4` et `ensure_ascii=False`.

📂 [Liste_de_courses_avec_sauvegarde.py](../Projets/Liste_de_courses_avec_sauvegarde.py)

---

## 🔹 Structure recommandée du code

```python
import json, os, sys

# 1. Définir le chemin du fichier
# 2. Charger les données existantes
# 3. Boucle principale : menu et choix utilisateur
# 4. Fonctions internes pour chaque action (ajout, suppression, affichage, vidage)
# 5. Sauvegarde automatique avant de quitter
```

Cette structure prépare le terrain pour une future refactorisation en fonctions ou classes, rendant le code plus modulaire.

---

## 💡 Points forts de mon implémentation

- ✅ Persistance des données : la liste est conservée d’une exécution à l’autre.
- ✅ Utilisation du module json pour un format standard, lisible et portable.
- ✅ Gestion des erreurs élémentaires (fichier absent, saisie invalide).
- ✅ Structure claire et cohérente du menu.
- ✅ Lisibilité du code : indentations propres, messages explicites, séparateurs visuels (`"_" * 50`).

---

## 🔍 Améliorations possibles (selon progression)

Les évolutions suivantes serviront de support pour approfondir les notions de modularité et de conception logicielle :

- Refactorisation fonctionnelle :
Extraire les actions (`ajouter_article, supprimer_article, sauvegarder_liste, etc`) dans des fonctions séparées.
- Gestion d’erreurs avancée :
Ajouter un `try/except` autour de la lecture/écriture JSON pour éviter les plantages si le fichier est corrompu.
- Chemin relatif :
Utiliser `os.path.join()` pour rendre le programme portable sur tous les systèmes d’exploitation.
- Refactorisation en **POO** :
Transformer le programme en une classe `ListeDeCourses`, avec méthodes et attribut

---

## 💡 Pourquoi ce projet est important

Ce projet introduit la notion de persistance : les données sauvegardées permettent au programme de conserver son état.

C’est un premier pas vers des applications réelles qui ne se “réinitialisent” pas à chaque exécution.

Il consolide aussi les notions de :

- lecture et écriture de fichiers,
- validation d’entrées,
- organisation du code,
- manipulation de données JSON.

---

## 🗒️ Résumé

Ce projet marque une étape clé dans notre progression.  
Il nous a permis de transformer une simple application interactive en un **programme réellement persistant et structuré**, capable de sauvegarder et de restaurer des données.  

En le réalisant, on a pu :

- renforcer notre compréhension de la **manipulation de fichiers** et du format **JSON**,  
- apprendre à **séparer la logique du code** pour plus de clarté,  
- découvrir l’importance de la **gestion des erreurs** et de la **préparation des données**,  
- et surtout, comprendre la différence entre **un script qui s’exécute** et **un programme qui vit dans le temps**.  

La fluidité du menu, la clarté des messages et la sauvegarde automatique rendent le programme agréable à utiliser, tout en introduisant des concepts professionnels comme la persistance, la validation et la modularité.  

👉 En somme, ce projet a consolidé nos compétences fondamentales en Python et posé les bases de ce que sera la suite de notre apprentissage :  
une approche orientée **structuration, réutilisation et fiabilité du code**.  

---

## Section 36 : Gérer les chemins de fichiers avec Pathlib

## 📌Objectif de la section

Apprendre à manipuler les **chemins de fichiers et de dossiers** de manière moderne, portable et sécurisée grâce au module `pathlib`.  
Ce module, intégré nativement à Python, **remplace avantageusement** les anciennes fonctions du module `os` en offrant une interface **orientée objet** et **multiplateforme**.

---

## 🔹 Pourquoi utiliser Pathlib ?

- ✅ Plus **lisible** et **intuitif** que `os.path`  
- ✅ Compatible avec **tous les systèmes** (Windows, macOS, Linux)  
- ✅ Permet de **manipuler les chemins comme des objets** (`Path`)  
- ✅ Offre des **méthodes intégrées** pour lire, écrire, créer et supprimer des fichiers assez facilement.

---

**🔸Créer un chemin:**

```python
from pathlib import Path

chemin = Path("dossier/fichier.txt")
```

`Path()` crée un objet chemin, qui peut représenter un fichier ou un dossier.
L’opérateur `/` permet de concaténer des segments, même sous Windows :

```python
dossier = Path("dossier")
fichier = dossier / "fichier.txt"
```

**🔸Obtenir des informations sur un chemin:**

```python
chemin.name       # Nom du fichier (ex : "fichier.txt")
chemin.stem       # Nom sans extension (ex : "fichier")
chemin.suffix     # Extension (ex : ".txt")
chemin.parent     # Dossier parent
chemin.exists()   # True si le chemin existe
chemin.is_file()  # True si c’est un fichier
chemin.is_dir()   # True si c’est un dossier
```

💡 Ces méthodes permettent d’écrire un code plus robuste, capable de vérifier l’existence d’un fichier avant de le manipuler.

**🔸Créer et supprimer des dossiers:**

```python
chemin.mkdir(parents=True, exist_ok=True)  # crée le dossier et ses parents
chemin.rmdir()                             # supprime un dossier vide
```

💡 `mkdir()` crée le dossier spécifié ; les paramètres :

- `parents=True` -> crée aussi les dossiers parents manquants ;

- `exist_ok=True` -> évite les erreurs si le dossier existe déjà.

Pour supprimer un dossier non vide, on peut utiliser `shutil.rmtree()` en important la bibliothèque `shutil`.

**🔸 Lire et écrire un fichier avec Pathlib:**

```python
chemin.write_text("Bonjour Jordani !", encoding="utf-8")  # Écrit du texte
contenu = chemin.read_text(encoding="utf-8")              # Lit le contenu

```

- ➡️ Les méthodes `.write_text()` et `.read_text()` simplifient énormément la manipulation de fichiers texte.

- Ces méthodes remplacent avantageusement le couple `open()/close()` ; elles simplifient la manipulation des fichiers texte.

**🔸 Scanner un dossier:**

```python
for fichier in Path("dossier").iterdir():
    print(fichier.name)
```

- `iterdir()` liste tous les éléments d’un répertoire (fichiers et sous-dossiers).

- `glob("*.txt")` et `rglob("*.py")` permettent de filtrer les fichiers selon un motif.

---

**🔹 Gestion avancée et pratiques personnelles:**

**📂 Fichier :** [Gestion des chemins de fichiers avec Pathlib](../Exercices/Partie_02/GesChFichier_avec_Pathlib.py)

Cette section nous a permis d’expérimenter :

- la création dynamique de fichiers et dossiers avec `mkdir()` et `touch()` ;

- la lecture et écriture directe via `read_text()` et `write_text()` ;

- la suppression sélective de fichiers `(unlink())` ;

- la navigation dans l’arborescence avec `parent`, `cwd()` et `resolve`() ;

- la recherche par motif à l’aide de `glob()` et `rglob()` ;

- et l’utilisation complémentaire du module `shutil` pour les opérations de nettoyage.

Ces manipulations ont renforcé notre compréhension de la structure du système de fichiers et des chemins relatifs/absolus.

---

**🔹 Mini-projet : Trier les fichiers selon leur extension:**

**📂 Fichier :** [Trier les fichiers selon leur extension](../Projets/Trier_fichiers_selon_extension.py)

**🎯 Objectif:**

Créer un script capable de trier automatiquement les fichiers de mon dossier _Downloads_ (et de _Telegram Desktop_) selon leur extension.

**⚙️ Fonctionnement général:**

1. Détection du dossier utilisateur via `Path.home() / "Downloads"`.

2. Parcours de tous les fichiers avec `iterdir()`.

3. Classification selon l’extension à l’aide d’un dictionnaire `(extension_folders)`.

4. Création automatique des dossiers cibles `(mkdir(parents=True, exist_ok=True))`.

5. Déplacement des fichiers avec `shutil.move()`.

6. Gestion d’un dossier spécial `“Telegram Desktop”`.

7. Catégorisation des fichiers inconnus dans un dossier `“Autres”` ou `“Logiciels”`.

---

**💡 Analyse personnelle:**

Ce mini-projet a concrètement démontré la puissance de `pathlib` pour l’automatisation de tâches système.
Il m’a appris à :

- travailler avec des chemins dynamiques et relatifs ;

- manipuler des structures de données;

- gérer les erreurs de fichiers inexistants ;

- et produire un script réellement utile dans mon environnement quotidien.

---

**🔍 Améliorations possibles:**

- Ajouter un **journal (log)** des fichiers déplacés avec le module `logging`.

- Créer une **fonction principale `trier_fichiers()`** pour modulariser le script.

- Gérer les **doublons** en renommant automatiquement les fichiers existants.

- Ajouter une **gestion d’erreurs avancée (`try/except`)** autour des déplacements.

- Créer une **interface graphique (`Tkinter`)** pour sélectionner le dossier à trier.

- Paramétrer les extensions via un **fichier JSON externe**.

- Sauvegarder un **rapport de tri** (ex. : nombre de fichiers déplacés, tailles cumulées).

- Étendre le projet à la **sauvegarde automatique** ou au **nettoyage programmé** (planifier le script via `cron` ou `task scheduler` pour un tri automatique quotidien).

---

## 🧠Concepts clés

- `Path` introduit une approche orientée objet de la gestion des chemins.

- La portabilité est garantie sans se soucier du séparateur (`/` ou `\`).

- `pathlib` s’intègre naturellement avec d’autres modules comme `json` et `shutil`.

- Méthodes essentielles :

  - `exists(), is_file(), is_dir()` ➡️ vérification.

  - `mkdir(), rmdir()` ➡️ création / suppression de dossiers.

  - `write_text(), read_text()` ➡️ manipulation de fichiers texte.

  - `iterdir(), glob(), rglob()` ➡️ navigation et filtrage.

Ces simplifient et fiabilisent le code.

- `shutil` reste utile pour supprimer récursivement ou déplacer des éléments.

- C’est un **outil incontournable** pour tout développeur manipulant des fichiers.

---

## 💡 Pourquoi cette section est importante

Cette section marque le passage d’une simple manipulation de fichiers à une véritable automatisation logicielle.
Elle combine théorie et pratique en reliant :

- la gestion d’arborescences,

- la manipulation d’objets `Path`,

- et la logique d’organisation de données réelles sur le système.

C’est une étape clé pour comprendre comment Python interagit avec le système d’exploitation et préparer la suite : la **modularisation**, la **POO**, et la **création d’outils complets**.

---

## 🧾Résumé

Ce module nous a permis de :

- maîtriser la bibliothèque `pathlib` et ses avantages sur `os` ;

- automatiser une tâche réelle (tri des fichiers de _Downloads_) ;

- écrire un code plus lisible, maintenable et multiplateforme ;

- comprendre la structure et la navigation dans le système de fichiers ;

- et renforcer notre capacité à créer des **scripts utiles et intelligents**.

👉 En résumé, cette section nous a fait passer du simple `“manipulateur de fichiers”` au **développeur capable d’automatiser son environnement**.

---

## Section 37 : Les dictionnaires

## 🧠Objectif de la section

Découvrir et maîtriser les **dictionnaires**, une structure de données essentielle en Python.  
Les dictionnaires permettent d’associer des **clés uniques** à des **valeurs**, offrant un moyen rapide et flexible d’organiser, de rechercher et de modifier des informations.  

Ils constituent la base de nombreuses structures modernes : **fichiers JSON**, **bases de données**, **configurations**, **réponses d’API**, etc.

---

## 🔹 Définition et caractéristiques

Un **dictionnaire** est une collection **non ordonnée**, **modifiable** et **indexée** par des clés uniques.  
Chaque élément est une paire **clé : valeur**.

```python
mon_dico = {"nom": "Jordani", "score": 96}
```

- Les clés doivent être **immuables** (par exemple : `str`, `int`, `tuple`),  
- Les valeurs peuvent être **n’importe quel type** (nombre, chaîne, liste, autre dictionnaire…).

💡 **But de cette partie :** comprendre la structure interne et les types de données acceptés dans un dictionnaire.

---

## 🔸 Accéder à une valeur

Pour obtenir une valeur, on utilise sa clé entre crochets.  
Si la clé n’existe pas, une erreur `KeyError` est levée.

```python
mon_dico = {"nom": "Jordani", "score": 96}
print(mon_dico["prenom"])  # KeyError: 'prenom'
```

👉 Pour éviter cette erreur, on peut utiliser la méthode `.get()` qui renvoie une valeur par défaut si la clé est absente.

```python
mon_dico = {"nom": "Jordani", "score": 96}
print(mon_dico.get("prenom", "Inconnu"))  # Inconnu
print(mon_dico.get("nom", "Inconnu"))  # Jordani
```

💡 **But de cette partie :** savoir accéder de façon sécurisée aux données d’un dictionnaire sans risquer d’interrompre le programme.

---

## 🔸 Ajouter ou modifier une entrée

Un dictionnaire est **modifiable** :  

- si la clé n’existe pas, une nouvelle paire est ajoutée ;  
- si la clé existe déjà, la valeur correspondante est mise à jour.

```python
mon_dico = {"nom": "Jordani", "score": 96}
mon_dico["score"] = 97
print(mon_dico)  # {'nom': 'Jordani', 'score': 97}
```  

💡 **But de cette partie :** comprendre comment les dictionnaires gèrent dynamiquement les ajouts et modifications sans nécessiter de structure fixe.

---

## 🔸 Supprimer une entrée

Pour retirer un élément d’un dictionnaire, plusieurs méthodes sont possibles.

```python
mon_dico = {"nom": "Jordani", "score": 96}
del mon_dico["nom"]
print(mon_dico)  # {'score': 96}
mon_dico = {"nom": "Jordani", "score": 96}
print(mon_dico.pop("nom"))  # Jordani
print(mon_dico)  # {'score': 96}
mon_dico = {"nom": "Jordani", "score": 96}
mon_dico.clear()
print(mon_dico)  # {}
```  

💡 **Remarque :**  

- `del` supprime une entrée spécifique sans retourner la valeur, possible aussi de supprimer un dictionnaire entier de façon définitive (exemple `del mon_dico`),  
- `.pop()` supprime et retourne la valeur,
- `.popitem()` supprime le dernier elément et retourne une paire clé/valeur (un `tuple`),
- `.clear()` vide entièrement le dictionnaire et retourne un dictionnaire vide.

---

## 🔸 Parcourir un dictionnaire

Il est souvent nécessaire de parcourir un dictionnaire pour traiter ses données.  
Trois méthodes principales permettent d’accéder aux éléments :  

- `.keys()` → renvoie la liste des **clés**  
- `.values()` → renvoie la liste des **valeurs**  
- `.items()` → renvoie les **paires clé/valeur** (idéal pour les boucles)

```python
mon_dico = {"nom": "Jordani", "score": 96}
for cle in mon_dico.keys():
    print(cle)
for valeur in mon_dico.values():
    print(valeur)
for cle, valeur in mon_dico.items():
    print(cle, valeur)
```  

💡 **But de cette partie :** apprendre à itérer efficacement sur les éléments d’un dictionnaire, notamment dans les cas de traitements ou de conversions de données.

---

## 🔹 Fonctions et méthodes utiles

Les dictionnaires possèdent plusieurs méthodes intégrées très puissantes comme :  

| Méthode | Rôle |
|----------|------|
| `.get(cle)` | Récupère la valeur sans générer d’erreur si la clé est absente |
| `.pop(cle)` | Supprime et retourne la valeur associée |
| `.popitem()` | Supprime et retourne la paire clé/valeur le plus ancienne |
| `.update(dico)` | Ajoute ou met à jour plusieurs paires clé/valeur |
| `.clear()` | Vide le dictionnaire |
| `.keys()` | Retourne un itérable de toutes les clés |
| `.values()` | Retourne un itérable de toutes les valeurs |
| `.items()` | Retourne un itérable de toutes les paires clé/valeur |

💡 **But de cette partie :** maîtriser les opérations fondamentales pour manipuler les dictionnaires de manière fluide et efficace.

---

## 🧠 Concepts clés

- Les dictionnaires sont **optimisés pour l’accès rapide** grâce à leurs clés (recherche quasi instantanée).  
- Ils permettent de **structurer les données sous forme d’association** logique.  
- Très utilisés dans les **fichiers JSON**, les **API**, et la **programmation orientée objet**.  
- La **flexibilité** du dictionnaire permet d’y imbriquer d’autres structures (listes, dictionnaires, tuples…).  
- C’est l’un des types de données les plus puissants et polyvalents du langage Python.

---

## 💡 Exemple d’application typique

Dans un programme de gestion de notes, chaque étudiant peut être représenté par une clé (nom), et ses résultats par une valeur (autre dictionnaire contenant les matières et les scores).  
Cette structure permet un accès rapide, une mise à jour facile, et une lecture intuitive des données.

---

## 🗒️Résumé

Cette section nous a permis de :

- comprendre la structure **clé/valeur** et le fonctionnement interne des dictionnaires ;  
- manipuler des données associatives de manière **souple et dynamique** ;  
- découvrir les méthodes intégrées (`get`, `update`, `pop`, etc.) ;  
- apprendre à **parcourir et modifier** un dictionnaire en toute sécurité ;  
- préparer le terrain pour la **manipulation de données complexes** (JSON, APIs, bases de données).  

👉 En résumé, les dictionnaires sont le **cœur organisationnel du langage Python** : ils permettent de représenter efficacement les relations entre des entités et d’accéder aux données avec élégance et rapidité.

---

## Section 38 : Projet #7 — Le trieur de fichiers

## 📌 Objectif du projet

Créer un programme Python capable de **trier automatiquement les fichiers** d’un dossier (par exemple _Downloads_) selon leur **type ou extension**.  
Ce projet illustre parfaitement l’utilité pratique de Python dans l’automatisation de tâches répétitives et dans la **gestion intelligente des fichiers personnels**.

💡 Ce projet prolonge directement la section précédente sur `pathlib`, en ajoutant une véritable logique d’organisation et d’automatisation complète.

---

## 🛠️Compétences mobilisées

- Utilisation du module **`pathlib`** pour la gestion des chemins de fichiers.  
- Manipulation de répertoires avec `.iterdir()`.  
- Création dynamique de dossiers via `.mkdir()`.  
- Déplacement de fichiers avec `shutil.move()` (ou `.rename()` dans certaines variantes).  
- Gestion des **extensions de fichiers** à l’aide de dictionnaires.  
- Utilisation de **conditions et de boucles** pour trier les fichiers selon leur type.  
- Gestion de cas particuliers (doublons, dossiers spécifiques comme *Telegram Desktop*).  

---

## 🔹 Étapes de réalisation

### 1️⃣ Identifier le dossier cible

Le programme commence par définir le **dossier de travail**, souvent `Downloads`, obtenu via `Path.home()` pour garantir la compatibilité multiplateforme.  
👉 Cette approche assure que le script s’adapte automatiquement à tout environnement utilisateur.

---

### 2️⃣ Définir les catégories de fichiers

On crée un **dictionnaire de correspondance** (`extension_folders`) reliant chaque type de fichier à une liste d’extensions :  
par exemple `"Images"` → `[".jpg", ".png", ".gif"]`, `"Documents"` → `[".pdf", ".txt", ".docx"]`, etc.

💡 Cette étape rend le script **modulaire** et **facilement personnalisable** : il suffit d’ajouter une extension pour qu’elle soit automatiquement prise en charge.

---

### 3️⃣ Parcourir le dossier et trier les fichiers

À l’aide de `.iterdir()`, le programme parcourt tous les fichiers présents dans le dossier cible.  
Chaque fichier est analysé :  

- s’il correspond à une extension connue, il est déplacé dans le dossier correspondant ;  
- sinon, il est redirigé vers un dossier “Logiciels” ou “Autres”.

💡 Cette approche montre comment **intégrer la logique de tri dans une boucle**, rendant le script plus dynamique et polyvalent.

---

### 4️⃣ Gérer le dossier “Telegram Desktop”

Une particularité personnnelle du projet : le programme gère également le **sous-dossier `Telegram Desktop`**.  
Ce dossier contient des fichiers multimédias téléchargés via Telegram, que le programme trie dans des sous-dossiers spécifiques (`Telegram_Images`, `Telegram_Videos`, etc.).

💡 Cette approche montre comment **intégrer la logique de tri dans plusieurs niveaux hiérarchiques**, rendant le script plus complet et polyvalent.

---

### 5️⃣ Créer les dossiers et déplacer les fichiers

Le programme crée automatiquement les dossiers nécessaires grâce à :  
`mkdir(parents=True, exist_ok=True)`  
puis déplace les fichiers avec :  
`shutil.move(str(fichier), str(dossier_destination / fichier.name))`

💡 **But de cette partie :** maîtriser la gestion de la création dynamique de répertoires et du déplacement sécurisé des fichiers.

---

### 6️⃣ Gérer les doublons ou fichiers inconnus

Si un fichier ne correspond à aucune catégorie d’extension connue, il est automatiquement placé dans un dossier générique (“Logiciels” ou “Autres”).  
Cette gestion préventive évite les erreurs et garantit qu’aucun fichier ne reste à la racine du dossier.

---

## 🔹 Exemple de logique globale du programme

_(description textuelle d’un exemple concret)_  

- Le script analyse le dossier **Downloads**.  
- Il trouve par exemple :
  - un fichier `document.pdf` → déplacé vers le dossier `/Documents`  
  - un fichier `photo.png` → déplacé vers `/Images`  
  - un fichier `musique.mp3` → déplacé vers `/Musiques`  
  - un fichier `script.py` → déplacé vers `/Codes`  
  - un fichier inconnu `setup.exe` → déplacé vers `/Logiciels`  
- Si un dossier `Telegram Desktop` existe, il effectue le même tri à l’intérieur.

💡 Résultat : un dossier Downloads propre, structuré et organisé automatiquement selon le type de fichiers.

Ce projet nous a permis de mettre en pratique toutes les notions vues précédemment sur la manipulation de fichiers avec **`pathlib`**.  
J’y ai implémenté ma propre version du trieur automatique, en intégrant une gestion personnalisée des extensions et des sous-dossiers spécifiques comme **Telegram Desktop**.

📁 Fichier : [Le trieur de fichiers](../Projets/Trieur_de_fichiers.py)

---

## 💡 Concepts clés

- **`pathlib`** simplifie toutes les manipulations de chemins et rend le code lisible.  
- **Les dictionnaires** permettent une classification claire et rapide des extensions.  
- **`shutil`** complète `pathlib` pour les déplacements et suppressions de fichiers.  
- La **combinaison logique de conditions, boucles et structures de données** rend le code flexible et maintenable.  
- Ce type de script illustre la **puissance de Python dans l’automatisation personnelle et professionnelle**.  

---

## 🔍 Améliorations possibles

- Ajouter un **système de journalisation (`logging`)** pour suivre les fichiers déplacés.  
- Détecter les **doublons** et les renommer automatiquement.  
- Intégrer une **interface graphique (Tkinter ou PySide)** pour sélectionner le dossier cible.  
- Créer une **version planifiée** (exécutée automatiquement à intervalle régulier).  
- Transformer le script en **module réutilisable** ou en **application CLI**.  

---

## 💡Pourquoi ce projet est important

Ce projet prouve que Python n’est pas seulement un langage académique, mais un **outil d’automatisation puissant** dans la vie quotidienne.  
En automatisant le tri des fichiers :

- nous améliorons la **productivité**,  
- nous découvrons la **programmation orientée tâches**,  
- et nous appliquons les notions fondamentales de **structures de données, conditions et chemins**.

C’est aussi une première étape vers la **programmation orientée objet**, où ce script pourrait devenir une **classe “FileOrganizer”** avec des méthodes dédiées (`trier_fichiers()`, `creer_dossiers()`, etc.).

---

## 🗒️ Résumé

Ce projet nous a permis de :

- consolider notre maîtrise de `pathlib`, de `shutil`, et surtout sans oublier la méthode `rename()`, qui, à l’instar de `shutil.move()`, permet également de déplacer des fichiers ;
  - `rename()` → déplace ou renomme un fichier (plus rapide, même disque),
  - `shutil.move()` → plus polyvalent (gère les systèmes différents, copie/suppression).
- comprendre la gestion de dossiers et de fichiers,  
- manipuler efficacement les fichiers et répertoires,  
- créer une structure d’organisation dynamique et automatisée,  
- et comprendre l’importance de la modularité dans la conception de scripts.  

👉 En résumé, ce projet nous a fait passer du simple script utilitaire à un **outil d’automatisation complet**, ouvrant la voie à la **programmation orientée objet** et à des applications encore plus robustes.

---

## Section 39 : Projet #8 — Le créateur de dossiers

## 📌Objectif du projet

Dans ce projet, nous avons pour mission de **générer automatiquement une arborescence de dossiers** à partir d’un **dictionnaire Python**.  
Ce programme, simple mais extrêmement utile, nous apprend à automatiser la création de structures de travail répétitives — un gain de temps considérable dans de nombreux contextes professionnels :

- organisation de projets (films, séries, entreprises, etc.),
- préparation de dossiers administratifs ou pédagogiques,  
- structuration de répertoires de développement.

💡 Ce projet illustre parfaitement la philosophie du développeur : _“ne jamais refaire à la main ce qu’on peut automatiser intelligemment 😅😉.”_

---

## ⚒️ Compétences mobilisées

- Manipulation de **chemins de fichiers** avec `pathlib`.  
- Utilisation d’un **dictionnaire imbriqué** pour représenter la hiérarchie de dossiers.  
- Création dynamique de répertoires avec `.mkdir(parents=True, exist_ok=True)`.  
- Boucles `for` imbriquées pour parcourir les clés et les valeurs du dictionnaire.  
- Gestion de la suppression et du nettoyage de répertoires avec `shutil.rmtree()`.  
- Compréhension de la **modularité** et de la **réutilisabilité** du code.

---

## 🔹Étapes de réalisation

### 1️⃣ Définir le dossier parent

Nous commençons par définir le **chemin du dossier racine** dans lequel sera créée toute la structure.  
Ce chemin est obtenu avec `Path.cwd()` ou `Path.home()`, garantissant la compatibilité multiplateforme.

---

### 2️⃣ Définir la structure de dossiers

Nous définissons ensuite un **dictionnaire** où chaque **clé** représente un dossier principal,  
et chaque **valeur** est une **liste de sous-dossiers** à créer.  

💡 Par exemple, la clé `"Films"` contient une liste de titres de films, `"Series"` contient les noms de séries, etc.  
Cette approche rend le programme **souple** et **facilement extensible** : il suffit de modifier le dictionnaire pour créer une autre arborescence.

---

### 3️⃣ Parcourir le dictionnaire et créer les dossiers

Grâce à une double boucle `for` et la méthode `.items()`, nous parcourons entierement le dictionnaire.  
Pour chaque combinaison, un **chemin complet** est construit, puis le dossier correspondant est créé avec :

`mkdir(parents=True, exist_ok=True)`

Cette méthode permet de créer tous les dossiers intermédiaires automatiquement (même s’ils n’existent pas encore) sans provoquer d’erreur.

---

### 4️⃣ Option : Nettoyage après test

Une fois la structure créée, il est possible de **supprimer automatiquement** le dossier de test pour éviter l’encombrement de l’espace de travail.  
Cela se fait en une seule ligne grâce à la fonction `shutil.rmtree()` utilisée lorque le dossier n'est pas vide (composé de sous-dossiers), au cas contraire on aurait pu utiliser la méthode `rmdir()`.

💡 Cette étape est optionnelle, mais elle démontre une bonne pratique : toujours penser à la maintenance et au nettoyage automatique des fichiers temporaires.

---

## 🔹Exemple de logique globale du programme

_(description textuelle d’un exemple concret)_  

1. Nous exécutons le script.  
2. Le programme crée un dossier principal nommé `Dossier_test` dans le répertoire `Projets`.  
3. À l’intérieur, il crée automatiquement les sous-dossiers :
   - `Films` → `Le Seigneur des Anneaux`, `Harry Potter`, `Moon`, `Forrest Gump`  
   - `Series` → `Breaking Bad`, `Game of Thrones`, etc.  
   - `Documentaires`, `Animes`, `Mangas` → chacun avec leurs sous-dossiers respectifs.  
4. À la fin, toute la hiérarchie de dossiers est créée **en quelques secondes**, sans intervention manuelle.  

Ce projet nous a permis de mettre en pratique l’association entre les **dictionnaires** (pour représenter la structure logique) et les **objets `Path`** (pour matérialiser cette structure sur le disque).

📁 Fichier : [Créateur de dossiers](../Projets/Createur_de_dossiers.py)

---

## 💡Concepts clés

- Un **dictionnaire** peut être utilisé pour modéliser une hiérarchie complète (clé → sous-dossiers).  
- Le module **`pathlib`** rend la gestion des chemins **plus simple et lisible** que `os.path`.  
- L’option `parents=True` dans `.mkdir()` garantit la création récursive de l’arborescence.  
- L’option `exist_ok=True` évite les erreurs si le dossier existe déjà.  
- Le module **`shutil`** complète `pathlib` pour gérer les suppressions et nettoyages automatiques.  

---

## 🔎 Améliorations possibles

- Ajouter une **interface CLI** (via `argparse` ou `typer`) pour définir le dossier cible et le dictionnaire.  
- Lire la structure depuis un **fichier JSON externe**, pour permettre à des non-programmeurs de définir leur propre arborescence.  
- Intégrer un **système de logs (`logging`)** pour suivre la création des dossiers.  
- Ajouter une option de **confirmation** avant suppression automatique.  
- Transformer le script en **classe Python** (`FolderCreator`) pour plus de modularité et de réutilisabilité.

---

## 💡 Pourquoi ce projet est important

Ce projet nous enseigne à **automatiser la création de structures récurrentes**, ce qui est extrêmement utile dans les environnements professionnels (cinéma, bureautique, développement, gestion documentaire).  
Il met en pratique la logique d’association vue avec les **dictionnaires**, et la relie à la **gestion des chemins** étudiée précédemment.  

En quelques lignes de code, nous avons transformé une tâche manuelle et répétitive en un **processus automatisé, propre et extensible**.

---

## 🗒️ Résumé

Ce projet nous a permis de :

- combiner l’utilisation des **dictionnaires** et de **`pathlib`** pour créer des structures complexes,  
- renforcer notre logique de **boucles imbriquées et conditions**,  
- apprendre à **automatiser la création de répertoires** selon un schéma défini,  
- et découvrir comment rendre un script plus **générique et professionnel**.  

👉 En résumé, nous avons franchi une nouvelle étape vers la **programmation modulaire et orientée objet**, en construisant un outil utile, adaptable et applicable à de nombreux domaines professionnels.

---

## Section 40 : Projet #9 — Organiser des données

## 📌 Objectif du projet

Le but de ce projet est de **manipuler, nettoyer et organiser des données textuelles** contenues dans un fichier.  
Nous apprenons à lire un fichier, extraire son contenu, le trier puis réécrire les données de manière ordonnée.  

Ce projet marque notre première incursion dans l’univers de la **data-science**, en appliquant des opérations basiques d’analyse et de traitement de données sans recourir encore à des bibliothèques externes comme `pandas`.

💡 Ce type d’exercice, bien qu’en apparence simple, introduit des notions fondamentales : la lecture de fichiers, la gestion de chaînes, et la logique algorithmique du tri.

---

## 🛠️ Compétences mobilisées

- Lecture et écriture de fichiers texte avec `pathlib` et ses méthodes `.read_text()` / `.write_text()`.  
- Utilisation de **listes** et de **listes en compréhension** pour extraire et transformer les données.  
- Nettoyage des chaînes de caractères avec `.strip()`, `.split()`, et gestion des lignes vides.  
- Tri des données avec `.sort()` ou `sorted()`.  
- Structuration logique du code : séparer les étapes de lecture, nettoyage, tri et écriture.  
- Gestion de l’encodage et des chemins de fichiers.

---

## 🔹🔹 Étapes de réalisation

### 1️⃣ Lecture du fichier source

Nous commençons par définir le chemin du fichier contenant les données (`prenoms.txt`) à l’aide de `Path`.  
Ensuite, nous utilisons `.read_text()` pour récupérer son contenu.

💡 **But de cette partie :** apprendre à lire un fichier complet en une seule ligne, tout en s’assurant de l’encodage correct (`utf-8`).

---

### 2️⃣ Extraction des noms

Le contenu brut du fichier est ensuite **séparé en lignes** grâce à la méthode `.splitlines()`, puis chaque ligne est découpée en mots individuels.  
L’objectif est d’obtenir une **liste complète de prénoms**, même si ceux-ci sont séparés par des espaces, des virgules ou plusieurs retours à la ligne.

💡 **But de cette partie :** convertir un texte brut en structure de données exploitable.

---

### 3️⃣ Nettoyage des données

Nous supprimons les espaces, les points, les virgules et les lignes vides afin de conserver uniquement les prénoms valides.  
Ce processus de _“data cleaning”_ est une étape essentielle dans tout pipeline de traitement de données.

💡 **But de cette partie :** comprendre l’importance du prétraitement avant toute analyse de données.

---

### 4️⃣ Tri alphabétique

La liste propre est ensuite triée en ordre alphabétique, soit :

- **en place** avec `.sort()`,  
- ou **en créant une nouvelle liste** avec `sorted()`.

💡 **But de cette partie :** découvrir la puissance et la simplicité du tri intégré en Python.

---

### 5️⃣ Écriture du fichier nettoyé et trié

Enfin, nous écrivons la liste obtenue dans un nouveau fichier nommé `prenoms_organises.txt` à l’aide de `.write_text()`.  
Chaque prénom est séparé par un retour à la ligne `\n`.

💡 **But de cette partie :** comprendre l’importance de la structuration logique du code.

---

## 🔹🔹 Exemple de logique globale du programme

(description textuelle d’un exemple concret)

1. Le fichier `prenoms.txt` contient une liste désordonnée de prénoms, avec des espaces et des doublons.  
2. Le script lit tout le contenu, puis nettoie les données en supprimant les caractères parasites.  
3. Il trie les prénoms par ordre alphabétique.  
4. Il réécrit le tout dans `prenoms_organises.txt`.  
5. Résultat : une liste propre, ordonnée et prête à l’usage.

Ce projet nous a permis d’appliquer les notions de manipulation de texte et de structuration des données de manière pratique et efficace.

📁 Fichier : [Organiser des données](../Projets/Organiser_des_donnees.py)

---

## 💡 Possibilité d’implémenter le code le plus simplement possible

Une **liste de compréhension** permet de condenser le traitement complet en quelques lignes :

Exemple :

```python
from pathlib import Path

chemin = Path("noms.txt")
contenu = chemin.read_text()

noms = [nom.strip() for nom in contenu.splitlines() if nom.strip()]
noms.sort()

chemin_tri = Path("noms_tries.txt")
chemin_tri.write_text("\n".join(noms))

```

💡 **But de cette partie :** comprendre la puissance et la simplicité des listes en compréhension en Python.

💡 Cette approche démontre la **lisibilité et la puissance expressive** du langage Python : peu de lignes, beaucoup d’efficacité.

---

## 🧠 Concepts clés

- La lecture et l’écriture de fichiers sont les bases de la manipulation de données.  
- Les **listes en compréhension** permettent un code concis et lisible.  
- Le **nettoyage des données** (data cleaning) avec les méthodes comme `.strip()` ou `.split()` est une étape cruciale avant toute analyse.  
- Les fonctions intégrées comme `.sort()` ou `sorted()` simplifient les opérations de tri.  

---

## 🔍Améliorations possibles

- Ajouter une **vérification automatique** de l’existence du fichier source.  
- Implémenter une **gestion d’erreurs** (`try/except`) pour les cas de fichiers vides ou corrompus.  
- Créer une **fonction générique** (`organiser_fichier(path_source, path_sortie)`).  
- Ajouter un **compteur de lignes traitées** ou un **rapport d’exécution**.  
- Étendre le script à d’autres formats de données (`.csv`, `.json`).  

---

## 💡 Pourquoi ce projet est important

Ce projet nous initie à la **pensée “data”**, c’est-à-dire à la manière de transformer un contenu brut en données structurées et exploitables.  
Il nous apprend à :

- analyser un problème de traitement de texte,  
- découper la logique en étapes claires,  
- et implémenter un flux de transformation cohérent (lecture → nettoyage → tri → écriture).  

Ces bases seront indispensables pour les prochains projets, où nous irons vers la **programmation orientée données** et la **visualisation**.

---

## Résumé

Ce projet nous a permis de :

- maîtriser la lecture et l’écriture de fichiers texte avec `pathlib`,  
- manipuler et nettoyer des données textuelles,  
- trier efficacement des informations à l’aide de méthodes Python natives,  
- et appliquer la logique de traitement de données à un cas concret.  

👉 En résumé, nous avons découvert la **puissance de Python pour organiser et transformer des données**, jetant les fondations de la future exploration de la data-science.

---

## Section 41 : Gestion des erreurs avec les exceptions

## 📌 Objectif de la section

Dans cette section, nous apprenons à **anticiper, intercepter et gérer les erreurs** dans un programme Python grâce aux blocs `try/except`.  
L’objectif est de rendre notre code **plus robuste, plus professionnel et plus agréable à utiliser**.

💡 En pratique : un bon développeur ne cherche pas seulement à faire fonctionner son programme,  
il veille aussi à ce qu’il _ne plante pas_ face aux imprévus.

---

## 🔹 Pourquoi gérer les erreurs ?

Lorsqu’un programme rencontre une situation imprévue (fichier manquant, saisie invalide, division par zéro…),  
Python interrompt par défaut son exécution et affiche une **exception**.  
En capturant ces erreurs avec `try/except`, nous pouvons :

- éviter les plantages brutaux,  
- afficher des **messages clairs** à l’utilisateur,  
- et exécuter du **code alternatif ou de nettoyage**.

💡 **But de cette partie :** comprendre la nécessité de prévoir les erreurs pour fiabiliser les programmes.

---

## 🔸 Syntaxe de base

```python
try:
    # Code à tester
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro interdite !")
```  

Le bloc `try` contient le code **potentiellement risqué**, tandis que le bloc `except` intercepte une erreur spécifique.  
Il est possible d’intercepter plusieurs types d’erreurs selon le contexte.

💡 **Exemple textuel :**

Un programme tente de diviser deux nombres ; si l’utilisateur saisit 0, on affiche _“Division par zéro interdite !”_ au lieu d’un message d’erreur Python.

---

## 🔸 Gérer plusieurs types d’erreurs

Dans un même bloc `try`, plusieurs exceptions peuvent être anticipées à l’aide de plusieurs blocs `except`.

```python
try:
    # Code à tester
    valeur = int(input("Entrez une valeur : "))
    resultat = 10 / valeur
    print(resultat)
except ValueError:
    print("Valeur invalide !")
except ZeroDivisionError:
    print("Division par zéro interdite !")
```

💡 **But de cette partie :** différencier les types d’erreurs (valeur invalide, division impossible, etc.) pour fournir une réponse adaptée à chaque cas.

---

## 🔸 Utiliser `else` et `finally`

- Le bloc `else` s’exécute uniquement si **aucune exception n’est levée**,  
- tandis que `finally` s’exécute **quoi qu’il arrive**,  
même si une erreur survient ou que le programme est interrompu.

```python
try:
    # Code à tester
    valeur = int(input("Entrez une valeur : "))
    resultat = 10 / valeur
    print(resultat)
except ValueError:
    print("Valeur invalide !")
except ZeroDivisionError:
    print("Division par zéro interdite !")
else:
    print("Tout va bien !")
finally:
    print("Fin du programme.")
```

💡 **But de cette partie :** apprendre à effectuer des actions finales indispensables, comme fermer un fichier, libérer une ressource ou afficher un message de fin proprement.

---

## 🔹 Exemple de logique globale du programme

(description textuelle d’un exemple concret)

1. Le programme demande à l’utilisateur d’entrer le nom d’un fichier à ouvrir.  
2. Il tente d’ouvrir ce fichier avec encodage `utf-8`.  
3. Si le fichier n’existe pas → `FileNotFoundError` est levée.  
4. Si l’utilisateur n’a pas la permission → `PermissionError`.  
5. Si le contenu n’est pas décodable → `UnicodeDecodeError`.  
6. En cas d’autre erreur système → `OSError`.  
7. Le contenu du fichier est affiché seulement si tout se passe bien.  
8. Le bloc `finally` s’exécute toujours pour signaler la fin de l’opération.

Ce projet nous a permis d’appliquer la gestion d’exceptions dans un cas concret —  
celui de la **lecture sécurisée d’un fichier** en anticipant toutes les erreurs possibles.

📁 Fichier : [Les exceptions](../Exercices/Partie_02/Les_exceptions.py)

---

## 🧠 Concepts clés

- Les erreurs en Python sont des **exceptions** que l’on peut **intercepter** et **traiter**.  
- Les blocs `try/except` permettent de **prévenir les interruptions** du programme.  
- `else` et `finally` ajoutent de la **logique conditionnelle et de la sécurité** aux traitements.  
- Une **bonne gestion d’erreurs** améliore l’expérience utilisateur et la qualité du code.  
- La **spécificité des exceptions** (attraper uniquement ce qu’on prévoit) est une bonne pratique.  

---

## 💡 Pourquoi ce projet est important

Ce projet nous apprend que **l’erreur fait partie du code**.  
Un programme professionnel n’est pas celui qui ne contient aucune erreur,  
mais celui qui **sait les gérer intelligemment**.  

En anticipant les exceptions :

- nous rendons le code **plus stable**,  
- nous améliorons l’**interaction avec l’utilisateur**,  
- et nous adoptons une démarche **préventive et responsable**.

C’est une compétence clé pour passer du _"code qui marche"_ à du **code fiable et maintenable**.

---

## 🗒️ Résumé

Cette section nous a permis de :

- comprendre le fonctionnement des exceptions Python,  
- apprendre à utiliser les blocs `try`, `except`, `else`, `finally`,  
- gérer proprement les erreurs liées aux fichiers et aux entrées utilisateur,  
- et améliorer la **robustesse et la lisibilité** de nos programmes.  

👉 En résumé, nous avons découvert comment faire de nos erreurs non plus des obstacles, mais des **opportunités d’amélioration et de contrôle du flux d’exécution**.
