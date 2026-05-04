import random

from librairie.classes.Carte import Carte

class Deck:
    cartes = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    couleurs = ["♠","♦","♥","♣"]

    def __init__(self):
        self.paquet = [Carte(v, c) for c in Deck.couleurs for v in Deck.cartes]
        random.shuffle(self.paquet)

    def tirer(self, n=1):
        """Retire n cartes du dessus du paquet."""
        cartes = self.paquet[:n]
        self.paquet = self.paquet[n:]
        return cartes
