import random

from librairie.classes.Deck import Deck
from librairie.classes.Visu_carte import Affichage


class JeuBataille:
    def __init__(self):
        self.deck = Deck()
        self.affichage = Affichage()
        self.main_joueur = self.deck.tirer(26)
        self.main_adv = self.deck.tirer(26)
        self.couleur_bonus = random.choice(Deck.couleurs)
        print(f"\nCouleur bonus : {self.couleur_bonus}")
        
    def afficher_regles(self):
        print("\n================= RÈGLE DU JEU : LA BATAILLE =================")
        print("Le paquet est partagé équitablement : 26 cartes pour vous, 26 pour l'adversaire.")
        print("À chaque tour, vous révélez chacun la première carte de votre paquet.")
        print(" - La carte la plus forte remporte le pli.")
        print(" - Les cartes gagnées vont en bas du paquet du vainqueur.")
        print("\nBATAILLE :")
        print("Si les deux cartes ont la même force, il y a bataille !")
        print("Chacun pose une carte face cachée, puis une carte face visible.")
        print("La carte visible la plus forte remporte tout le pot.")
        print("\nCOULEUR BONUS :")
        print(f"Une couleur bonus est tirée au hasard au début de la partie.")
        print("Si votre carte est de cette couleur et pas celle de l'adversaire, vous gagnez le pli.")
        print("\nFIN DE PARTIE :")
        print("Le jeu s'arrête quand l'un des joueurs n'a plus de cartes.")
        print("Celui qui possède encore des cartes remporte la partie.")
        print("================================================================\n")


    def bataille(self):
        pot = []
        indices_v = []
        indices_s = []

        while True:
            if len(self.main_joueur) < 1 or len(self.main_adv) < 1:
                return "FIN", pot
            
            #input("Appuyez sur Entrée pour piocher...")

            carte_j = self.main_joueur.pop(0)
            carte_a = self.main_adv.pop(0)

            self.affichage.Afficher_cartes(carte_j, carte_a)

            # Victoire simple
            if carte_j.force() != carte_a.force():
                
                if len(pot) >= 4:
                    for start in range(2, len(pot), 4):  # tous les 6 éléments
                        indices_v.extend([start])
                    indices_v = [i for i in indices_v if i < len(pot)]
                    vos_cachées = [pot[i] for i in indices_v]
                    print("Vos cartes cachées :", vos_cachées)
                    for start in range(3, len(pot), 4):  # tous les 6 éléments
                        indices_s.extend([start])
                    indices_s = [i for i in indices_s if i < len(pot)]
                    ses_cachées = [pot[i] for i in indices_s]
                    print("Ses cartes cachées :", ses_cachées)

                if carte_j.force() > carte_a.force():
                    pot.extend(random.sample([carte_j, carte_a], k=2))
                    return "GAGNE_J", pot
                else:
                    pot.extend(random.sample([carte_j, carte_a], k=2))
                    return "GAGNE_A", pot

            # Bonus couleur
            if self.couleur_bonus == carte_j.couleur and self.couleur_bonus != carte_a.couleur:
                
                if len(pot) >= 4:
                    for start in range(2, len(pot), 4):  # tous les 6 éléments
                        indices_v.extend([start])
                    indices_v = [i for i in indices_v if i < len(pot)]
                    vos_cachées = [pot[i] for i in indices_v]
                    print("Vos cartes cachées :", vos_cachées)
                    for start in range(3, len(pot), 4):  # tous les 6 éléments
                        indices_s.extend([start])
                    indices_s = [i for i in indices_s if i < len(pot)]
                    ses_cachées = [pot[i] for i in indices_s]
                    print("Ses cartes cachées :", ses_cachées)
                
                pot.extend(random.sample([carte_j, carte_a], k=2))
                return "GAGNE_J", pot
            
            if self.couleur_bonus == carte_a.couleur and self.couleur_bonus != carte_j.couleur:
                
                if len(pot) >= 4:
                    for start in range(2, len(pot), 4):  # tous les 6 éléments
                        indices_v.extend([start])
                    indices_v = [i for i in indices_v if i < len(pot)]
                    vos_cachées = [pot[i] for i in indices_v]
                    print("Vos cartes cachées :", vos_cachées)
                    for start in range(3, len(pot), 4):  # tous les 6 éléments
                        indices_s.extend([start])
                    indices_s = [i for i in indices_s if i < len(pot)]
                    ses_cachées = [pot[i] for i in indices_s]
                    print("Ses cartes cachées :", ses_cachées)
                
                pot.extend(random.sample([carte_j, carte_a], k=2))
                return "GAGNE_A", pot

            print("\033[93m!!! BATAILLE !!!\033[0m") #IA

            # Pas assez de cartes pour bataille
            if len(self.main_joueur) < 2 or len(self.main_adv) < 2:
                pot.append(carte_j)
                pot.append(carte_a)
                
                if len(pot) >= 4:
                    for start in range(2, len(pot), 4):  # tous les 6 éléments
                        indices_v.extend([start])
                    indices_v = [i for i in indices_v if i < len(pot)]
                    vos_cachées = [pot[i] for i in indices_v]
                    print("Vos cartes cachées :", vos_cachées)
                    for start in range(3, len(pot), 4):  # tous les 6 éléments
                        indices_s.extend([start])
                    indices_s = [i for i in indices_s if i < len(pot)]
                    ses_cachées = [pot[i] for i in indices_s]
                    print("Ses cartes cachées :", ses_cachées)
                    
                return "MANQUE_CARTE", pot

            pot.extend(random.sample([carte_j, carte_a], k=2))
            
            # Cartes cachées
            pot.append(self.main_joueur.pop(0))
            pot.append(self.main_adv.pop(0))
            print("Cartes cachées !")


    def jouer(self):
        self.afficher_regles()
        tours = 0

        while self.main_joueur and self.main_adv:
            print(f"\n--- SCORE : VOUS [{len(self.main_joueur)}] | ADVERSAIRE [{len(self.main_adv)}] ---") #IA

            resultat, pot = self.bataille()

            if resultat == "GAGNE_J":
                print("\033[92m-> Vous gagnez le pot !\033[0m") #IA
                self.main_joueur.extend(pot)

            elif resultat == "GAGNE_A":
                print("\033[91m-> L'adversaire gagne le pot !\033[0m") #IA
                self.main_adv.extend(pot)
                
            elif resultat == "MANQUE_CARTE":
                print("\033[96mPas assez de cartes pour la bataille !\033[0m") #IA
                self.main_joueur.extend(pot[0::2])
                self.main_adv.extend(pot[1::2])

            else:
                break

            tours += 1

        print(f"\n--- FIN DU JEU EN {tours} TOURS ---") #IA
        if len(self.main_joueur) > len(self.main_adv):
            print(" Vous avez gagné !")
        else:
            print(" L'adversaire a gagné...")
