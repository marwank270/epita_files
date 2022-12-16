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
- [x] Les règles du jeu sont affichées quand on lance le programme et il est possible d’afficher les règles du jeu grâce à une commande.
- [x] L'objectif du jeu est de découvrir toutes les cases sans bombe.
- [x] La grille est composée de 16x16 cases pouvant être avec ou sans bombe.
- [x] Avant le début du jeu, 40 bombes sont placées aléatoirement sur la grille.
- [x] L’utilisateur joue contre l’ordinateur.
- [x] Au début du jeu le contenu des cases lui est invisible et à chaque tour, la personne doit sélectionner une case à découvrir. La grille est réaffichée à chaque tour.
- [x] Pour désigner la case, il faut entrer un chiffre, une lettre ou une combinaison des deux. L’ordinateur ne doit pas accepter d’autres types de réponses (exemple, si les cases sont numérotées de 1 à 9, on ne peut pas entrer “A” ou “abcedef”).
- [x] Si la case choisie contient une bombe, le jeu est perdu.
- [x] Si la case ne contient pas de bombe, la case affiche le nombre de bombes dans l’entourage proche (c'est-à-dire les huit cases autours).
- [x] Si le joueur découvre toutes les cases sauf les 40 avec les bombes, il gagne.
- [x] Le jeu s’arrête lorsqu’il est gagné ou perdu et révèle alors l’ensemble des cases.
- [x] A la fin d’une partie, il est possible de rejouer sans avoir à relancer le programme.
- [x] Il est possible de quitter le programme grâce à une commande.

--- 

## Logs du projet :
### 16/11/22 :
- Début du projet
- Création du fichier principal v1 et de ce fichier `README.md`
- Lien du dossier de projet avec [mon repository Github](https://github.com/marwank270/epita_files/tree/master/D%C3%A9mineur)
- Création de la fonction `int_input()`
- Ajout de nouveaux commentaire de code
### 17/11/22 :
- Finalisation des premières fonctions (`int_input()`, `disp_matrix()` (cette fonction sers d'état de debug, elle montre l'emplacement des bombes))
- Ajout de nouveaux commentaire de code

### 18/11/22 :
- Création des fonctions `menu()`, `play()`, `menu()` et `char_input()`
- Amélioration des fonctions précédentes
- Supression des dépendences inutiles : `sys` utilisé pour `sys.exit()` remplacé par la fonctionnative python `exit()`, `time` utilisé pour rallentir l'execution de mon code, `maths` non utilisée
- Ajout de nouveaux commentaire de code

### 20/11/22 : 
- Création de la classe `Game` afin d'avoir accès aux matrices dans tout le code
- Création de la fonction `game_input()` et `check_around()`
- Amélioration des fonctions précédentes
- Ajout de nouveaux commentaire de code

### 23/11/22 :
- Création de fonction `display()` pour l'utilisateur
- Ajout de la commande `quit` lors de la saisie entier 
- Correction du bug principal dans la "Research loop", qui empêchait de faire fonctionner la fonction sur les bords.
- Correction de bug d'affichage et création du petit menu de confirmation pour `quit`
- Ajout de la révélation des bombes en fin de partie
- Ajout de nouveaux commentaire de code

### 24/11/22 : 
- Création de la fonction `computer_play()` et implémentation de cette fonction a mon code (le bot n'utilise que des placements aléatoire et je ne sais pas si je changerais ca même si je n'ai pas envie de laisser ca en aléatoire)
- Correction des messages de fin de partie en ajoutant les possibilité manquantes (ordinateur gagne etc)
- Correction de petits bugs

### 03/12/22 :
- Début de la v2
- Roadmap de la hess faite sur paint
- Création du fichier et début du codage
- Création de la fenêtre `win` et de l'affichage de base avec Tk
- Définition des variables globales
- Création des premières fonctions liés aux clics (`lc()` et `rc()`) et `init()` afin de débuter le programme
- Ajout de nouveaux commentaire de code


### 07/12/22 :
- Création des fonctions `count_mines()`, `neighborhood()` et `spread()` (non fonctionnelle)
- Création de la fonction `trace()`, a continuer
- Amélioration des fonctions `init()` (renommée `reinit()`) et précédentes
- Ajout de nouveaux commentaire de code


### 09/12/22 :
- Amélioration des fonctions `spread()` et `neighborhood()` (maintenant toutes les deux fonctionnelles mais non optimisée)
- Finalisation des fonctions `reinit()`, `spread()` et `trace()`
- Correction partielle du bug `index out of range` qui empéchait de cliquer sur le bord Sud et Est

### 10/12/22 : 
- Correction du bug des drapeaux, (changement de la fonction appelé dans `rc()`)
- Optimisation de la fonction `neighborhood()` et correction définitive du bug `index out of range` grace à un `try:` & `except:`

### 14/12/22 : 
- Implémentation de la classe `ToolTip()` trouvée sur [stackoverflow.com](https://stackoverflow.com/) lors de recherches sur un moyen d'afficher des textes au survol de la souris
---
## Sources:
### Mes sources pour m'aider dans ce projet sont principalement les documentations officielles de [Numpy](https://numpy.org/doc/stable/reference/index.html#reference) et de [python](https://docs.python.org/3.10/).
### Il m'est aussi arrivé d'utiliser [stackoverflow.com](https://stackoverflow.com/) pour comprendre mieux certains problèmes que j'ai rencontré.

---

## Les fonctions de mon projet :

## Fonctions de la V1 :

|Fonction:| Nom: |Paramètres & types: | Objectif: | Sortie & type: |Cas spécifique géré: |
|:---:|:---:|:---:|:---:|:---:|:---:|
|Saisie utilisateur d'entier|  `int_input`   |   `val_min: int, val_max: int, display: str`  |   Renvoyer une saisie utilisateur seulement si elle est bien uniquement un chiffre  |  `user_input: int`   | Cas ou l'utilisateur entre des caractères grâce à un `try:` & `except:`    |
| Saisie utilisateur caractères | `char_input` | `i_min: int, i_max: int, display: str` | Renvoyer une saisie utilisateur seulement si c'est un caractère alphabétique compris entre les indexes des lettres passé en paramètres | `list` : `[user_input: str, uii: int]` | Cas ou l'utilisateur saisis plus d'un caractère|
| Saisie des coordonnées du placement | `game_input` | Procédure: `null` | Utiliser les deux fonctions précédentes pour renvoyer des coordonnées de la matrice | `list` : `[line: int, column: int]` | Gestion des cas spécifiques dans les fonctions `int_input()` et `char_input()` |
| Affichage de la matrice | `disp_matrix` | `matrix: numpy.ndarray` | Afficher dans le terminal le plateau de la partie actuelle (version debug) | Procédure: `null` | Gestion de l'affichage des nombre des lignes et des lettres des colones | 
| Affichage de la matrice | `display` | `matrix: numpy.ndarray` | Afficher dans le terminal le plateau de la partie actuelle (version joueur) | Procédure: `null` | Gestion de l'affichage des nombre des lignes et des lettres des colones |
| Affichage et sélection des options | `menu` | Procédure: `null` | Afficher le menu principal, les règles et les options pour l'utilisateur | Procédure: `null` | Aucun cas spécifique à gérer |
| Jeu | `play` | Procédure: `null` | Jouer (actuellement en solo seulement) | Procédure: `null` | Actuellement aucun |
| Vérification des bombes alentours | `check_around` | `line: int, column: int, matrix: numpy.ndarray` | Vérifie le nombre de bombes dans les 8 cases adjacentes | `bomb_count: int` | Gestion du cas de la bombe sur les coordonnées du tir du joueur |
| Jeu de l'ordinateur | `computer_play` | `matrix: numpy.ndarray` | Faire jouer l'ordinateur (placement aléatoire actuellement) | `list: [rand_i: int, rand_j: int]` | Aucun cas spécifique à gérer |
 
## Fonctions de la V2 :

|Fonction:| Nom: |Paramètres & types: | Objectif: | Sortie & type: |Cas spécifique géré: |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Calcul des coordonnées du clic gauche | `lc` | `event: tk.event` | Calculer les oordonnées sur la fenêtre a partir de l'évenement du clic gauche |  Procédure: `null` | Aucun cas spécifiques à gérer |
| Calcul des coordonnées du clic droit | `rc` | `event: tk.event` | Calculer les oordonnées sur la fenêtre a partir de l'évenement du clic droit |  Procédure: `null` | Aucun cas spécifiques à gérer |
Capture des coordonnées alentour | `neighborhood` | `i: int, j: int` | Retourner une liste contenant les les cases adjacentes | `list: [...]` | Cas ou les coordonées sont hors de la matrice avec un `try:` & `except:` |
| Détecter le nombre de mines adjacentes  | `count_mines` | `i: int, j: int` | Retourner le nombre de bombes trouvées autour des coordonnées | `bombs_neighborhood: int` | Aucuns cas spécifiques à gérer |
| Procédure de propagation de la découverte des cases | `spread` | `i: int, j: int` | Propagation de la découverte des cases a l'aide de la fonction `trace()` | Procédure: `null` | Aucuns cas spécifiques à gérer |
| Initialisation de la fenêtre | `reinit` | `null` | Préparer la fenêtre tk et les variables globales du programme pour le bon déroulement du programme | Procédure: `null` | Aucuns cas spécifiques à gérer |
| Afficher le contenu de la case sélectionnée | `trace` | `i: int, j: int` | Affiche et dessine les cases découvertes et le nombre de bombes | Procédure: `null` | Vérification de l'état de découverte et des flags et gestion des cas de Win et Loose |
| Fonction de placement de drapeaux | `flag` | `i: int, j: int` |  Procédure de placement des drapeaux durant la partie | Procédure: `null` | Placement d'un drapeau sur une case contenant déjà un drapeau, vérification des conditions de Win et Loose | 

# Ce que j'ai ajouté dans ma V2:
Pour ma V2 je savais déjà dès le début que je voulais avoir une interface graphique, parce que pour moi l'interface graphique est une branche importante dans un jeu vidéo. J'ai donc décidé d'utiliser [`Tkinter`](https://tkdocs.com/) étant donnée que c'est une dépendences connu de la communautée python je savais que je n'aurais pas trop de mal à trouver de l'aide en cas de besoin. 
J'ai également choisi d'ajouter les drapeaux qui fonctionne exactement comme dans le jeu du démineur original, lors du clic droit, le programme va vérifier si cette case n'est pas déjà marquée d'un drapeau elle le devient sinon elle le retire et si tous les drapeaux sont placés sur les toutes les bombes alors la partie est gagnée.
J'ai aussi changé la méthode d'apparition des bombes, j'ai fais une boucle qui à 16% de chances de placer une bombe et de cette façon le nombre de bombes est toujours aux alentours des 40 bombes.