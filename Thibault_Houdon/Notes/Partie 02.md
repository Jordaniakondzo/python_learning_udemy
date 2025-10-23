# 📘 Partie 2 — Vers des projets plus avancés

## 📑 Table des matières

- [📝 Introduction](#-introduction)
- [🎯 Objectif de cette nouvelle phase](#-objectif-de-cette-nouvelle-phase)
- [📚 Ce que cette partie va apporter](#-ce-que-cette-partie-va-apporter)
- [🧠 État d’esprit pour cette partie](#-état-desprit-pour-cette-partie)
- [Section 34 : Les fichiers](#section-34--les-fichiers)
- [Section 35 : Projet #6 — Liste de courses avec sauvegarde](#section-35--projet-6--liste-de-courses-avec-sauvegarde)

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
