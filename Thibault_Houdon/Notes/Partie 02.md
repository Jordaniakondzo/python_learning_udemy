# 📘 Partie 2 — Vers des projets plus avancés

## 📑 Table des matières

- [📝 Introduction](#-introduction)
- [🎯 Objectif de cette nouvelle phase](#-objectif-de-cette-nouvelle-phase)
- [📚 Ce que cette partie va apporter](#-ce-que-cette-partie-va-apporter)
- [🧠 État d’esprit pour cette partie](#-état-desprit-pour-cette-partie)
- [Section 34 : Les fichiers](#section-34--les-fichiers)

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

📂 Exemple pratique : [Ajout_donnees_fichier_Json.py](../Partie%2002/Ajout_donnees_fichier_Json.py)

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

Cette section nous enseigne à :

- Créer et manipuler des fichiers texte et JSON  
- Comprendre les modes d’ouverture et leur comportement  
- Stocker et récupérer des données de manière persistante  
- Gérer les erreurs liées à la lecture et l’écriture de fichiers  

---
