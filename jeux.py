
from librairie.jeux.bataille import JeuBataille
from librairie.jeux.justeprix import JeuJustePrix
from librairie.jeux.blackjack import JeuBlackJack

choix = input("Appuyez sur entrée pour rentrer dans le jeu...")

while choix != 0 :
    choix = input("A quel jeu voulez-vous jouer ? (1 -> bataille, 2 -> juste prix, 3 -> BlackJack, 4 -> quitter) : ").lower()
    
    if choix == "1" :
        jeu = JeuBataille()
        jeu.jouer()
        
    elif choix == "2" :
        jeu = JeuJustePrix()
        jeu.jouer()
        
    elif choix == "3":
        ia = int(input("Niveau IA (1 à 4) : "))
        jeu = JeuBlackJack()
        jeu.jouer()
    
    elif choix == "4":
        print("Au revoir !")
        break
    
    else:
        print("Choix invalide.")