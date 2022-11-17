# Rapport de projet : Le Démineur
---
## **Rappel des modalités d'évaluation** :
Vous serez noté sur:
- **10 points pour l’implémentation et le respect des fonctionnalités minimales**
(décrites ci-dessous). Les fonctionnalités minimales comprennent essentiellement: le
respect des règles du jeu, la gestion des inputs utilisateur, la gestion de l’interface de jeu
sur le terminal.
- **5 points pour la qualité du code:<** bonnes pratiques respectées + structure de code
efficace, facilement compréhensible et maintenable.
- **5 points pour les fonctionnalités supplémentaires** de votre choix.

Les rendus attendus seront:
- **Un rapport**. Soit un document décrivant:
- **Chaque fonction de votre projet**: avec son nom, ses inputs (et le type des inputs),
le but de la fonction, l’output de la fonction (et son type), et les cas spécifiques
que la fonction gère.
- **L’architecture globale de votre projet à travers un diagramme** d'exécution de
votre projet ou figurent les fonctions décrites précédemment.
- **La/les fonctionnalités supplémentaires** que vous avez choisies. Il faudra
également décrire précisément le comportement attendu de ces fonctionnalités
et comment celles-ci s'intègrent dans l’architecture globale de votre projet.
- Les sources utilisées si .
- **Le jeu V1**, soit un fichier python (.py) implémentant les **fonctionnalités minimales**.
- **Le jeu V2**, soit un fichier python (.py) implémentant les **fonctionnalités additionnelles**.

## **Rappel des consignes du démineur** :
- Les règles du jeu sont affichées quand on lance le programme et il est possible
d’afficher les règles du jeu grâce à une commande.
- L'objectif du jeu est de découvrir toutes les cases sans bombe.
- La grille est composée de 16x16 cases pouvant être avec ou sans bombe.
- Avant le début du jeu, 40 bombes sont placées aléatoirement sur la grille.
- L’utilisateur joue contre l’ordinateur.
- Au début du jeu le contenu des cases lui est invisible et à chaque tour, la personne doit
sélectionner une case à découvrir. La grille est réaffichée à chaque tour.
- Pour désigner la case, il faut entrer un chiffre, une lettre ou une combinaison des deux.
L’ordinateur ne doit pas accepter d’autres types de réponses (exemple, si les cases sont
numérotées de 1 à 9, on ne peut pas entrer “A” ou “abcedef”).
- Si la case choisie contient une bombe, le jeu est perdu.
- Si la case ne contient pas de bombe, la case affiche le nombre de bombes dans
l’entourage proche (c'est-à-dire les huit cases autours).
- Si le joueur découvre toutes les cases sauf les 40 avec les bombes, il gagne.
- Le jeu s’arrête lorsqu’il est gagné ou perdu et révèle alors l’ensemble des cases.
- A la fin d’une partie, il est possible de rejouer sans avoir à relancer le programme.
- Il est possible de quitter le programme grâce à une commande.

## Logs du projet :
### 16/10/22 :
- Début du projet
- Création du fichier principal v1 et de ce fichier README.md
- Lien du dossier de projet avec [mon repository Github](https://github.com/marwank270/epita_files/tree/master/D%C3%A9mineur)
- Création de la fonction `int_input(val_min: int, val_max: int, display: str)`

## Les fonctions de mon projet :

|Fonction:| Nom: |Paramètres & types: | Objectif: | Sortie & type: |Cas spécifique géré: |
|:---:|:---:|:---:|:---:|:---:|:---:|
|Saisie utilisateur d'entier|  `int_input`   |   `val_min: int, val_max: int, display: str`  |   Renvoyer une saisie utilisateur seulement si elle est bien uniquement un chiffre  |  `user_input: int`   | Cas ou l'utilisateur entre des caractères grâce à un `try:` & `except:`    |
| Saisie utilisateur caractères | `char_input` | `i_min: int, i_max: int, display: str` | Renvoyer une saisie utilisateur seulement si c'est un caractère alphabétique compris entre les indexes des lettres passé en paramètres | `list` : `[user_input: str, uii: int]` | Cas ou l'utilisateur saisis plus d'un caractère|
| Saisie des coordonnées du placement | `game_input` | `null` | Utiliser les deux fonctions précédentes pour renvoyer des coordonnées de la matrice | `list` : `[line: int, column: int]` | Gestion des cas spécifiques dans les fonctions `int_input()` et `char_input()` |
| Affichage de la matrice | `disp_matrix` | `matrix: numpy.ndarray` | Afficher dans le terminal le plateau de la partie actuelle | `null` | Gestion de l'affichage des nombre des lignes et des lettres des colones | 
| Affichage et sélection des options | `menu` | `null` | Afficher le menu principal, les règles et les options pour l'utilisateur | `null` | Aucun cas spécifique à gérer |
| Jeu | `play` | `null` | Jouer (actuellement en solo seulement) | `null` | Actuellement aucun |
 
