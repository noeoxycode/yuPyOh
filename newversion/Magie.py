from card import Card

class Magie(Card):
    def __init__(self, tab):
        super().__init__(0, 0, tab[0], "Magie", tab[1], tab[2])
    def printi(self):
        print("Magie :",self.name)
        print("Effet :",self.effect)
        print(self.holder)
    def copy(self):
        return Magie(self.name,self.effect,self.effectInt)