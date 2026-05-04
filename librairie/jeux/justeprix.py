import random

class JeuJustePrix:
    
    def __init__(self):
        
        while True:
            try:
                self.difficulte = int(input("Choisir la difficulté (1 = facile, 10 = très difficile) : "))
                if 1 <= self.difficulte <= 10:
                    break
                print("Veuillez entrer un nombre entre 1 et 10.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        self.borne_max = 10 ** self.difficulte
        print(f"\nLe nombre sera entre 1 et {self.borne_max}.")
        
        while True:
            try:
                self.ia_level = int(input("Niveau de l'IA (1 = facile, 9 = One Shot) : "))
                if 1 <= self.ia_level <= 9:
                    break
                print("Choisissez entre 1 et 9.")
            except ValueError:
                print("Nombre invalide.")
                
    def ia_choix(self, bas, haut): #aide avec IA
        if self.ia_level == 1:
            # IA moyenne
            return bas + (haut - bas) // 4

        elif self.ia_level == 2:
            # IA intelligente : dichotomie
            return (bas + haut) // 2
        
        elif self.ia_level == 3:
            guess = (bas + haut) // 2
            if haut - bas > 3:
                guess += random.choice([-1, 0, 1])
            return max(bas, min(haut, guess))
        
        elif self.ia_level == 4:
            return bas + 3 * (haut - bas) // 4
        
        elif self.ia_level == 5:
            if haut - bas > 10_000_000:
                return bas + 7 * (haut - bas) // 8   # avance à 87.5%
            elif haut - bas > 1000:
                return bas + 3 * (haut - bas) // 4   # avance à 75%
            else:
                return (bas + haut) // 2             # finit en dichotomie
        
        elif self.ia_level == 6:
            # IA quantique : teste 3 hypothèses en parallèle
            q1 = bas + (haut - bas) // 4
            q2 = (bas + haut) // 2
            q3 = bas + 3 * (haut - bas) // 4

            # Elle choisit celle qui réduit le plus la zone
            return random.choice([q1, q2, q3])
        
        elif self.ia_level == 7:
            # IA prédictive : elle anticipe la réponse
            mid = (bas + haut) // 2
            if self.secret > mid:
                return bas + 3 * (haut - bas) // 4
            else:
                return bas + (haut - bas) // 4
        
        elif self.ia_level == 8:
            # IA ultime : stratégie adaptative
            size = haut - bas

            if size > 10_000_000:
                return bas + 9 * size // 10      # avance à 90%
            elif size > 100_000:
                return bas + 3 * size // 4       # avance à 75%
            elif size > 1000:
                return (bas + haut) // 2         # dichotomie
            else:
                return bas + random.randint(0, size)  # bruit final pour éviter les pièges
            
        elif self.ia_level == 9:
            # IA omnisciente : elle devine en un coup
            return self.secret  # elle "lit dans tes pensées"

    def demander_nombre(self, message):
        """Demande un nombre entier au joueur."""
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    def indice(self, guess, secret):
        """Renvoie +, - ou = selon la comparaison."""
        if guess < secret:
            return "+"
        elif guess > secret:
            return "-"
        return "="

    # MODE 1

    def jouer_classique(self):
        secret = random.randint(1, self.borne_max)
        tours = 1

        while True:
            print(f"\nTour {tours}")
            guess = self.demander_nombre("Votre proposition : ")

            rep = self.indice(guess, secret)

            if rep == "+":
                print("IA : Plus haut !")
            elif rep == "-":
                print("IA : Plus bas !")
            else:
                print("\n Vous avez trouvé !")
                break

            tours += 1

        print(f"\n--- FIN EN {tours} TOURS ---")

    # MODE 2 : L'IA DEVINE

    def ia_devine_intelligente(self):
        self.secret = self.demander_nombre("Choisissez un nombre secret pour l'IA : ")

        bas, haut = 1, self.borne_max
        tours = 1

        while True:
            guess = self.ia_choix(bas, haut)
            print(f"\nL'IA propose : {guess}")

            rep = self.indice(guess, self.secret)

            if rep == "+":
                print("Vous : +")
                bas = guess + 1
            elif rep == "-":
                print("Vous : -")
                haut = guess - 1
            else:
                print("\n L'IA a trouvé !")
                break

            tours += 1

        print(f"L'IA a trouvé en {tours} tours.")

    # MODE 3 : DUEL

    def jouer_duel(self):
        print("\nMODE DUEL : Vous et l'IA devinez chacun un nombre.")
        secret_joueur = self.demander_nombre("Votre nombre secret : ")
        secret_ia = random.randint(1, self.borne_max)
        bas_ia, haut_ia = 1, self.borne_max
        tours = 1

        while True:
            print(f"\n--- TOUR {tours} ---")

            # Joueur devine
            guess_joueur = self.demander_nombre("Votre proposition : ")
            rep_joueur = self.indice(guess_joueur, secret_ia)

            if rep_joueur == "+":
                print("IA : Plus haut !")
            elif rep_joueur == "-":
                print("IA : Plus bas !")
            else:
                print("\n Vous avez gagné contre l'IA !")
                print("Votre nombre était ", secret_joueur)
                break

            # IA devine
            guess_ia = self.ia_choix(bas_ia, haut_ia)
            print(f"L'IA propose : {guess_ia}")

            rep_ia = self.indice(guess_ia, secret_joueur)

            if rep_ia == "+":
                print("Vous : +")
                bas_ia = guess_ia + 1
            elif rep_ia == "-":
                print("Vous : -")
                haut_ia = guess_ia - 1
            else:
                print("\n L'IA a gagné !")
                print("le nombre de l'IA était ", secret_ia)
                break

            tours += 1


    def afficher_regles(self):
        print("\n================= RÈGLE DU JEU : LE JUSTE PRIX =================")
        print("Le but est simple : trouver un nombre secret choisi aléatoirement.")
        print("La difficulté détermine la borne maximale :")
        print(" - Difficulté 1  → nombre entre 1 et 10")
        print(" - Difficulté 10 → nombre entre 1 et 10 milliards")
        print("\nMODES DE JEU :")
        print("1) Vous devinez le nombre :")
        print("   L'IA vous répond 'Plus haut' ou 'Plus bas' jusqu'à ce que vous trouviez.")
        print("\n2) L'IA devine votre nombre :")
        print("   Vous choisissez un nombre secret, et l'IA tente de le trouver.")
        print("   Son intelligence dépend du niveau choisi (1 à 9).")
        print("\n3) Mode Duel :")
        print("   Vous choisissez un nombre secret, l'IA aussi.")
        print("   Vous devinez chacun votre tour. Le premier qui trouve gagne.")
        print("\nFIN DE PARTIE :")
        print("Le jeu s'arrête dès que le nombre est trouvé.")
        print("================================================================\n")

    # MENU PRINCIPAL

    def jouer(self):
        self.afficher_regles()
        print("\nModes disponibles :")
        print("1 -> Vous devinez")
        print("2 -> L'IA devine")
        print("3 -> Duel contre l'IA")
    
        while True:
            try:
                mode = int(input("Choisissez un mode : "))
                if 1 <= mode <= 3:
                    break
                print("Choisissez entre 1 et 3.")
            except ValueError:
                print("Nombre invalide.")
    
        if mode == 1:
            self.jouer_classique()
        elif mode == 2:
            self.ia_devine_intelligente()
        elif mode == 3:
            self.jouer_duel()

        
        
