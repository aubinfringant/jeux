

class Affichage:
    def Afficher_cartes(self, c1, c2): #IA
        v1, col1 = c1.valeur, c1.couleur
        v2, col2 = c2.valeur, c2.couleur

        print(f"      VOUS                ADVERSAIRE")
        print(f"   ┌─────────┐           ┌─────────┐")
        print(f"   │ {"\033[91m" if c1.est_rouge() else ""}{v1}{"" if v1 == "10" else " "}{"\033[0m"}      │           │ {"\033[91m" if c2.est_rouge() else ""}{v2}{"" if v2 == "10" else " "}{"\033[0m"}      │")
        print(f"   │         │           │         │")
        print(f"   │    {"\033[91m" if c1.est_rouge() else ""}{col1}{"\033[0m"}    │    VS     │    {"\033[91m" if c2.est_rouge() else ""}{col2}{"\033[0m"}    │")
        print(f"   │         │           │         │")
        print(f"   │      {"\033[91m" if c1.est_rouge() else ""}{"" if v1 == "10" else " "}{v1}{"\033[0m"} │           │      {"\033[91m" if c2.est_rouge() else ""}{"" if v2 == "10" else " "}{v2}{"\033[0m"} │")
        print(f"   └─────────┘           └─────────┘")

    def afficher_main_cartes(self, main, titre=""):
        if titre:
            print(f"\n{titre}")

        # 1) Ligne du haut
        for c in main:
            print("┌─────────┐", end=" ")
        print()

        # 2) Valeur en haut
        for c in main:
            v = c.valeur
            col = c.couleur
            rouge = "\033[91m" if c.est_rouge() else ""
            reset = "\033[0m"
            espace = "" if v == "10" else " "
            print(f"│ {rouge}{v}{reset}{espace}      │", end=" ")
        print()

        # 3) Ligne vide
        for _ in main:
            print("│         │", end=" ")
        print()

        # 4) Symbole au centre
        for c in main:
            col = c.couleur
            rouge = "\033[91m" if c.est_rouge() else ""
            reset = "\033[0m"
            print(f"│    {rouge}{col}{reset}    │", end=" ")
        print()

        # 5) Ligne vide
        for _ in main:
            print("│         │", end=" ")
        print()

        # 6) Valeur en bas
        for c in main:
            v = c.valeur
            rouge = "\033[91m" if c.est_rouge() else ""
            reset = "\033[0m"
            espace = "" if v == "10" else " "
            print(f"│      {rouge}{espace}{v}{reset} │", end=" ")
        print()

        # 7) Bas
        for _ in main:
            print("└─────────┘", end=" ")
        print()
