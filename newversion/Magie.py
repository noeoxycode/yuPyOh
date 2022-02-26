from newversion.card import Card


class Magie(Card):
    def __init__(self, name,effect,effectInt=""):
        super().__init__(0, 0, name, "Magie", effect, effectInt)
    def __init__(self, tab):
        self.name=tab[0]
        self.effect=tab[1]
        self.effectInt=tab[2]
    def printi(self):
        print("Magie :",self.name)
        print("Effet :",self.effect)
    def copy(self):
        return Magie(self.name,self.effect,self.effectInt)