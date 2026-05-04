class Carte:
    valeurs_bataille = {"1": 14, "K": 13, "Q": 12, "J": 11}

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def force(self):
        if self.valeur in Carte.valeurs_bataille:
            return Carte.valeurs_bataille[self.valeur]
        return int(self.valeur)

    def est_rouge(self):
        return self.couleur in ["♥", "♦"]

    def __repr__(self):
        return f"{self.valeur}{self.couleur}"