# Introduction a l'intelligence artificielle

[card title="Definition"]
L'ia est une branche de l'informatique permettants aux machines de simuler des capaciter humaine comme le raisonnement,l'apprentissage et la prise de dcisions

---
## Objectif
\
1. Automatisation des taches complexes \
2. Analyse et interpretation des donnes
\
3. Interaction naturelle avec les humains
\
4. Resolution de problemes complexes
\
5. Personnalisation des experiences utilisateur

## Pricipaux type d'AI
### Selon les capacite
\
1. IA Faible (Narrow AI)
\
2. IA General (Strong AI)
\
3. IA Super (Super AI)

### Selon le fonctionnement
\
1. IA Predicitve
\
2. IA Diagnostique
\
3. IA Prescriptive
\
4. IA Generative
\
5. IA Reactive
\
6. IA a memoire limitee
\
7. IA de la theorie et de l'esprit
\
8. IA auto-consciente

---

# Chatbots d'IA

[card title="Definition"]
Les chatbots utilisent l'IA pour repondre aux utilisateursm comprendre leurs besoins et executer des taches.

## Fonctionnement
\
1. L'utilisateur saisit une requete
\
2. Analyse des intentions via des algorithmes de traitement du language naturel ***NLP***
\
3. Recherche de reponses adaptees en fonction du contexte
\
4. Generation et retour de la reponse
\
5. Amelioration continue basee sur les interactions passees
\\
[✓]Utiliser dans le diagnostique simplifier pour quider des patient ou repondre a des questions frequents dans des universites par exemple

---

--config
font: Arial
color: blue
--

# Introdution a l'apprentissage automatique

[card title="Definition"]
L'apprentissage automatique est une branche de l'informatique qui se concentre sur le developpement de modeles capable d'apprendre a partir de donnees avec l'objectif d'automatiser les taches et d'ameliorer les performances


[card title="Qu'est ce que le machine learning"]
Le machine learning est une discipline qui utilise des algorithmes pour analyser et apprendre a partir de donnees afin de predire ou prendre des decisions sans etre explicitement programmee, il permet de reduire l intervention humaine pour resoudre des problemes complexe et est utiliser dans des application comme la reconnaissance faciale

## Types d'apprentisage automatique
\
### Apprentissage supervise
\
- **Principe** : L'algorithme apprend a partir de donnes etiquetees. Chaque donnes est associer a une sortie connu
- **Objectif** : Predire les resutats
- **Types de problemes** : Clasification (Attribuer une categorie a une donnee) / Regression (Predire une valeur continue)
---
### Apprentissage non supervise
\
- **Principe** : Les donnes ne sont pas etiquetees. L'objectif est de trouver des structures cachees dans les donnees.
- **Objectif** : Decouvrir des groupes,motifs ou relations dans les donnees
- **Types de problemes** : Clustring (regroupement) / Reduction de dimensionnalite
### Apprentissage semi-supervisé :
\
- **Principe** : Mélange de données étiquetées et non étiquetées.
- **Exemple** : Modèle de reconnaissance vocale où une partie des échantillons est
labellisée.

---
## Etapes pour contruire un modele ML:
\
- Collecte des donnees
- Pretraitement et nettoyage des donnees
- Choix du modele
- Entrainement du modele
- Evaluation de la performance
- Optimisation et ajustement
- Deploiement

---
# Fondamentaux de la Regression, Classification et Clusting
## 1.Introduction a la regression
### Qu'est ce que la regression ?
[card title="Definition"]
Methode d'apprentissage supervise utilisee pour predire une valeur

[i]Objectif : Comprendre les relations entre les varicales d'entree (caracteristiques) et la variable de sortie (cible) pour effectuer des predictions futurs

### Type de regression
\
1. **Regression lineaire simple** : Modele base sur une seule variable independante (x) \
2. **Regression lieaire multiple** : Modele utilisant plusieurs variables independantes (X1,X2,....,Xn)

## 2.La classification en machine learning
### Qu'est ce que la classification ?
[card title="Definition"]
Methode d'apprentissage supervise utilisee pour predire une categorie ou une classe a partir des caracteristiques d'une donnee

[i]Objectif : Attribuer une etiquette a une nouvelle donnee basee sur un modele entraine avec des donnees prealablement etiquetees

### Type de classification
\
1. **Classification binaire** : Deux classes possible (oui / non)\
2. **Classification multi-classe** : Plusieurs classes (Type de fruit)\
3. **Classification multi-etiquette** : Une donne peut apartenir a plusieurs classes

### Algorithme principaux
\
1. **K-Nearest Neighbors (KNN)** : Une nouvelle donnee est classee selon les ***K voisins les plus proches***
\\
[i] Etapes : Choisir la valeur de K - Calculer les distances entre la donnee cible et les autres - Assigner la classe majoritaire parmis les voisins
[!]**Importance du choix de K ** : Tester plusieurs valeurs pour choisir celle qui optimise la precision
1. **Arbres de decision** : Structure arborescente compose de **Noeuds** (Test baser sur une caracteristique) - **Branches** (Resultats possibles des tests) - **Feuilles** (Classes ou valeurs predictives finales)
\\
[i] Etapes : Diviser les donnees en fonction des caracteristiques les plus discriminantes - Repeter jusqu a atteindre un critere d'arret - Prediction : une nouvelle donnee suit le chemin jusqu a la feuille corespandante

## 3.Le clustring en machine learning
### Qu'est ce que le clustring ?
[card title="Definition"]
Methode d'apprentissage non supervise qui divise un ensemble de donnees en groupe homogenes (clusters)

[i]Objectif : Identifier des sous-groupes naturels sans etiquettes - Decouvrir des structures ou motifs caches dans les donnees

### Algorithme principal : K-Means
[card title="Principe"]
Diviser les donnees en K clusters,ou chaque donnee appartient au cluster dont le centroide (centre) est le plus proches 

**Etapes**\
1. Initialiser K centroides de facon aleatoire\
2. Assigner chaque point au cluster dont le centroide est le plus proche\
3. Recalculer les centroides comme moyenne des points du cluster\
4. Repeter jusqu a stabilisation ou ateinte d'un critere d'arret
\\
[x]Probleme du choix de K : Choisir un mauvais KKK peut mener a des clusters peu pertinents.
[✓]Soulution : <br/><b>Methode du coude (Elbow Method)</b> : Identifier le point ou la reduction de l'inertie (distance intra-cluster) ralentit. <br/> <b>Indice de silouette</b> : Evaluer la cohesion interne et la separation externe des clusters.

[badge color=red size=26]fafdwd