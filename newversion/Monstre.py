class Monstre:
    name=""
    attack=0
    defence=0
    bAttack=0
    bDefence=0
    level=0
    bLevel=0
    types=""
    effect=""
    effectInt=""
    holder=""
    canAttack=True
    def __init__(self, name="",attack=0,defence=0,level=0,types="",effect="",effectInt=""):
        self.name = name
        self.attack = self.bAttack=attack
        self.bDefence=self.defence = defence
        self.level = self.bLevel=level
        self.types = types
        self.effect = effect
        if type(effectInt) is type([]):
            self.effectInt=effectInt
        else:
            self.effectInt=effectInt.split(" ")
    def __init__(self, tab):
        self.name = tab[0]
        self.attack =int(tab[1])
        self.defence = int(tab[2])
        self.level=int(tab[3])
        self.bAttack=int(tab[4])
        self.bDefence= int(tab[5])
        self.bLevel=int(tab[6])
        self.types = tab[7]
        if(len(tab))>8:
            self.effect =tab[8]
            self.effectInt=tab[9]
    def printi(self):
        print("Monstre :",self.name)
        print("Holder :",self.holder)
        print("LVL :",self.level,"Type :",self.types)
        print("ATK :",self.attack,"  DEF :",self.defence,)
        if self.attack != self.bAttack or self.defence != self.bDefence:
            print("ATK de base :",self.bAttack,"  DEF de base :",self.bDefence)
        if self.effect !="":
            print("Effet :",self.effect)
            print(self.effectInt)
    def copy(self):
        return Monstre(self.name,self.bAttack,self.bDefence,self.bLevel,self.types,self.effect,self.effectInt)