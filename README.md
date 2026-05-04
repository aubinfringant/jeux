## Système de cartes (Deck / Carte / Affichage)
Le projet contient un moteur de cartes réutilisable :
- Carte : valeur, couleur, couleur rouge/noire, affichage.
- Deck : création d’un paquet de 52 cartes, mélange, tirage.
- Affichage : rendu ASCII des cartes (1 carte, 2 cartes, ou plusieurs cartes).
Ce système sert de base aux jeux de cartes comme le Blackjack.

## Bataille


## Jeu du Juste Prix
Un classique : devinez un nombre secret généré par l’ordinateur.
Modes disponibles
- Mode 1 : Vous devinez
- Mode 2 : L’IA devine votre nombre
- Mode 3 : Duel (vous et l’IA devinez chacun un nombre)
IA réglable
Plusieurs niveaux d’IA

 
## Blackjack
Un jeu complet de Blackjack utilisant le moteur de cartes :
Fonctionnalités
- Distribution réelle depuis un paquet mélangé
- Gestion des As (1 ou 11)
- Affichage ASCII des cartes
- Tour du joueur : tirer ou rester
- Tour de l’IA selon son niveau
- Comparaison finale des scores
IA du Blackjack
- Niveau d'IA

# Architecture générale
Chaque jeu est organisé dans sa propre classe :
- JeuBataille
- JeuJustePrix
- JeuBlackJack
Un menu principal permet de choisir le jeu et son mode.
Le code est structuré pour être :
- modulaire
- facile à étendre
- compatible entre jeux
- réutilisable

# Comment jouer
- Lancez le programme principal
- Choisissez un jeu dans le menu
- Suivez les instructions affichées
- Amusez‑vous !

