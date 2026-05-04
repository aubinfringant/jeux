from librairie.classes.Deck import Deck
from librairie.classes.Visu_carte import Affichage

class JeuBlackJack:
    def __init__(self, ia_level=1):
        self.deck = Deck()
        self.aff = Affichage()
        self.ia_level = ia_level

    # Calcul de la valeur d'une main
    def valeur_main(self, main):
        total = 0
        as_count = 0

        for carte in main:
            v = carte.valeur

            if v in ["J", "Q", "K"]:
                total += 10
            elif v == "1":  # As
                total += 11
                as_count += 1
            else:
                total += int(v)

        # Ajustement des As
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1

        return total

    # IA selon le niveau
    def ia_joue(self, main_ia):
        while True:
            total = self.valeur_main(main_ia)

            if self.ia_level == 1:
                # IA bête
                if total < 17:
                    main_ia.append(self.deck.tirer(1)[0])
                else:
                    return main_ia

            elif self.ia_level == 2:
                # IA prudente
                if total < 15:
                    main_ia.append(self.deck.tirer(1)[0])
                else:
                    return main_ia

            elif self.ia_level == 3:
                # IA intelligente
                if total < 18:
                    main_ia.append(self.deck.tirer(1)[0])
                else:
                    return main_ia

            elif self.ia_level == 4:
                # IA impossible (connait ton total)
                if total < self.total_joueur:
                    main_ia.append(self.deck.tirer(1)[0])
                else:
                    return main_ia


    def afficher_regles(self):
        print("\n================= RÈGLE DU JEU : BLACKJACK =================")
        print("Le but est simple : obtenir un total de cartes le plus proche possible de 21")
        print("sans jamais dépasser cette valeur.")
        print("\nVALEUR DES CARTES :")
        print(" - Les cartes 2 à 10 valent leur valeur.")
        print(" - Les figures (J, Q, K) valent 10.")
        print(" - L'As vaut 11, mais peut devenir 1 si vous dépassez 21.")
        print("\nDÉROULEMENT D'UNE PARTIE :")
        print("Vous recevez 2 cartes, l'IA aussi. Une seule de ses cartes est visible.")
        print("À votre tour, vous choisissez :")
        print(" - Tirer une carte (1)")
        print(" - Rester (2)")
        print("\nSi vous dépassez 21, vous perdez immédiatement.")
        print("\nTOUR DE L'IA :")
        print("L'IA tire des cartes selon son niveau d'intelligence :")
        print(" - Niveau 1 : IA simple, tire jusqu'à 17.")
        print(" - Niveau 2 : IA prudente, tire jusqu'à 15.")
        print(" - Niveau 3 : IA intelligente, tire jusqu'à 18.")
        print(" - Niveau 4 : IA 'impossible', elle connaît votre total.")
        print("\nFIN DE PARTIE :")
        print(" - Si l'IA dépasse 21, vous gagnez.")
        print(" - Sinon, le plus proche de 21 gagne.")
        print("================================================================\n")


    # Partie complète
    def jouer(self):
        self.afficher_regles()
        # Distribution
        main_joueur = [self.deck.tirer(1)[0], self.deck.tirer(1)[0]]
        main_ia = [self.deck.tirer(1)[0], self.deck.tirer(1)[0]]

        print("\n=== BLACKJACK ===")

        # Affichage initial
        self.aff.afficher_main_cartes(main_joueur, "Vos cartes")
        print(f" (Total = {self.valeur_main(main_joueur)})" )
        self.aff.afficher_main_cartes([main_ia[0]], "Carte visible de l'IA")


        # Tour du joueur
        while True:
            total_joueur = self.valeur_main(main_joueur)

            if total_joueur > 21:
                print(" Vous dépassez 21 ! Perdu.")
                return "IA"

            choix = input("Tirer (1) ou rester (2) : ")

            if choix.lower() == "1":
                main_joueur.append(self.deck.tirer(1)[0])
                self.aff.afficher_main_cartes(main_joueur, "Vos cartes")
            else:
                break

        # Tour de l'IA
        self.total_joueur = total_joueur
        main_ia = self.ia_joue(main_ia)

        # Affichage final
        self.aff.afficher_main_cartes(main_ia, "Main de l'IA")

        total_ia = self.valeur_main(main_ia)

        # Résultat
        if total_ia > 21:
            print(" L'IA dépasse 21 ! Vous gagnez.")
            return "Joueur"

        if total_joueur > total_ia:
            print(" Vous gagnez !")
            return "Joueur"
        elif total_joueur < total_ia:
            print(" L'IA gagne.")
            return "IA"
        else:
            print("Égalité.")
            return "Égalité"    