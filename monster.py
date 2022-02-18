
class Monstre:
    name = ""
    attack = 0
    defence = 0
    level = 0
    types = ""
    effect = ""
    effectInt = ""

    def __init__(self, name="", attack=0, defence=0, level=0, types="", effect="", effectInt=""):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.level = level
        self.types = types
        self.effect = effect
        self.effectInt = effectInt.split(" ")

    def printi(self):
        print("Nom :", self.name)
        print("Attaque :", self.attack)
        print("Défense :", self.defence)
        print("Niveau :", self.level)
        print("Type :", self.types)
        print("Effet :", self.effect)
        print("---------------")

