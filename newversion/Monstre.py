from card import Card


class Monstre(Card):
    attack=0
    defence=0
    bAttack=0
    bDefence=0
    level=0
    bLevel=0
    canAttack=True
    def __init__(self, tab):
        if(len(tab))>8:
            effect =tab[8]
            effectInt=tab[9]
        else:
            effect=''
            effectInt=''
        super().__init__(tab[0], tab[7], effect, effectInt)
        self.attack =int(tab[1])
        self.defence = int(tab[2])
        self.level=int(tab[3])
        self.bAttack=int(tab[4])
        self.bDefence= int(tab[5])
        self.bLevel=int(tab[6])
    def printi(self):
        print("Monstre :",self.name)
        print("LVL :",self.level,"Type :",self.types)
        print("ATK :",self.attack,"  DEF :",self.defence,)
        if self.attack != self.bAttack or self.defence != self.bDefence:
            print("ATK de base :",self.bAttack,"  DEF de base :",self.bDefence)
        if self.effect !="":
            print("Effet :",self.effect)
    def copy(self):
        return Monstre(self.name,self.bAttack,self.bDefence,self.bLevel,self.types,self.effect,self.effectInt)