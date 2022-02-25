class Magie:
    name=""
    effect=""
    effectInt=""
    types="Magie"
    holder=""
    def __init__(self, name,effect,effectInt=""):
        self.name=name
        self.effect=effect
        if type(effectInt) is type([]):
            self.effectInt=effectInt
        else:
            self.effectInt=effectInt.split(" ")
    def __init__(self, tab):
        self.name=tab[0]
        self.effect=tab[1]
        self.effectInt=tab[2]
    def printi(self):
        print("Magie :",self.name)
        print("Effet :",self.effect)
    def copy(self):
        return Magie(self.name,self.effect,self.effectInt)