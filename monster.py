class Monstre:
    def __init__(self, name="", attack=0, defence=0, level=0, types="", effect="", effectInt=""):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.level = level
        self.types = types
        self.effect = effect
        self.effectInt = effectInt.split(" ")

    def __str__(self):
        return f'Nom : {self.name}' + f'\nAttack : {self.attack}' + f'\nDefence : {self.defence} ' + f'\nNiveau : {self.level}' + f'\nType : {self.types}' + f'\nEffet : {self.effect}' + f'\n-----------------'


m = Monstre("nono", 6, 7, 9, "guerrier", "yes", "5")

print(m)
