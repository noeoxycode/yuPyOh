from random import Random, random, randrange
from unicodedata import name


class Game:
    turn = 1
    deck1 = []
    hand1 = []
    board1 = []
    defause1 = []
    HP1 = 8000
    deck2 = []
    hand2 = []
    board2 = []
    defause2 = []
    HP2 = 8000

    def switchTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


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


class Magie:
    name = ""
    effect = ""
    effectInt = ""

    def __init__(self, name, effect, effectInt=""):
        self.name = name
        self.effect = effect
        self.effectInt = effectInt

    def printi(self):
        print("Nom :", self.name)
        print("Effet :", self.effect)


game = Game
deckList = []
deckList.append(Monstre("Avian", 1000, 1000, 3, "Guerrier"))
deckList.append(Monstre("Clayman", 800, 2000, 3, "Guerrier"))
deckList.append(Monstre("Burstinatrix", 1300, 800, 3, "Guerrier",
                        "Choisi un monstre ennemie, si sa DEF est inférieur à l'ATK de ce monstre, le détruit",
                        "CHOOSE ennemie IF cible.DEF < him.ATK DESTROY cible"))
deckList.append(Monstre("Bubbleman", 800, 1200, 3, "Guerrier"))
deckList.append(
    Monstre("Flipper", 900, 1400, 3, "Bete", "Choisie un monstre de votre main et l'invoque si c'est possible",
            "CHOOSE hand SUMMON cible"))
deckList.append(Monstre("Colibri", 800, 1000, 3, "Bete",
                        "Choisi un monstre que vous controlez, vous vous soignez de 200 x son niveau",
                        "CHOOSE allie  SOIN* 200 allie.niveau"))
deckList.append(Monstre("Panthere noir", 1300, 1500, 4, "Bete"))
deckList.append(Monstre("Topitaupe", 1400, 1000, 4, "Bete"))
deckList.append(Monstre("Sparkman", 1600, 1200, 4, "Guerrier"))
deckList.append(Monstre("Nécrombre", 1500, 1200, 4, "Guerrier"))
deckList.append(
    Monstre("Airman", 1800, 1000, 4, "Guerrier", "Donne 300 DEF à un monstre allié", "CHOOSE allie ADD allie.DEF 300"))
deckList.append(Monstre("Capitaine dorée", 1800, 1000, 4, "Guerrier", "Pioche une carte", "DRAW 1"))
deckList.append(Monstre("Blazeman", 1600, 1600, 4, "Guerrier"))
deckList.append(Monstre("Ocean", 1500, 1700, 4, "Guerrier"))
deckList.append(Monstre("Tranchant", 2200, 2000, 6, "Guerrier"))
deckList.append(Monstre("Géant du tonnerre", 2400, 2200, 6, "Guerrier"))
deckList.append(
    Monstre("Homme-Oiseau de feu", 2100, 1800, 6, "Guerrier", "Choisi un monstre ennemie, gagne sa DEF en ATK",
            "CHOOSE ennemie ADD him.ATK cible.DEF"))
deckList.append(Monstre("Néos", 2500, 2200, 7, "Guerrier"))
deckList.append(Monstre("Chevalier Néos", 2700, 2300, 7, "Guerrier", "Choisi un monstre ennemie, divise son ATK par 2",
                        "CHOOSE ennemie DIVIDE ennemie.ATK 2"))
deckList.append(Monstre("Homme-Oiseau à l'éclat lumineux", 2500, 2500, 8, "Guerrier",
                        "Quant il est invoqué, gagne 200 ATK par monstre Guerrier dans votre cimetière",
                        "ADD* him.ATK 200 cimetiere.guerrier"))
deckList.append(Magie("Signal du héro", "Choisisez un monstre guerrier que vous controlez, il gagne 500 ATK",
                      "CHOOSE allie ADD allie.ATK 500"))
deckList.append(Magie("Appel d'urgence", "Pioche 1 carte si c'est un monstre guerrier pioche une carte de plus",
                      "DRAW 1 IF him = guerrier DRAW 1"))
deckList.append(Magie("Soin de la justice", "Vous soigne de 200 x nombre de carte dans la main", "SOIN* 200 hand.nb"))
deckList.append(Magie("Ravage de foudre", "Si vous controler \"Géant du tonnerre\", détruit un monstre ennemie",
                      "IF \"Géant du tonnerre\" CHOOSE ennemie DESTROY cible"))
deckList.append(Magie("Dernier espoir",
                      "Détruit tous vos monstres et infliger 400 point de dégat à votre adversaire par monstre détruit",
                      "DESTROY bord DAMAGE* nb 400"))
deckList.append(Magie("Reigne animal", "Toutes vos betes gagne 1 niveau, 400 ATK et DEF",
                      "ALL bete ADD cible.ATK 400 ADD cible.DEF 400 ADD cible.lvl 1"))
deckList.append(Magie("Prison héroique",
                      "Choisisez un monstre guerrier que vous controlez, un monstre ennemie pert un montant d'ATK égal à 100 x le niveau de votre monstre",
                      "CHOOSE allie CHOOSE ennemie MINUS* ennemie.ATK 100 allie.lvl"))
deckList.append(Magie("Super blocage", "Choisisez un monstre guerrier que vous controlez, il gagne 800 DEF",
                      "CHOOSE allie.guerrier ADD him.DEF 800"))
deckList.append(Magie("Rappel de secours", "Choisisez un monstre guerrier que vous cimetière, l'ajoute à votre main",
                      "CHOOSE cimetiere.guerrier TO hand"))
deckList.append(Magie("Destruction de Néos",
                      "Choisisez un \"Néos\" que vous controlez, il gagne 500 ATK, attaque tous les monstre ennemis, puis le détruit",
                      "CHOOSE allie.\"Néos\" ADD him.ATK 500 ATTACK ennemie.all DESTROY him"))


def list(tab):
    print("Deck List :", len(tab), "cartes")
    for i in tab:
        if (type(i) is Monstre):
            print("Monstre :", end=" ")
        else:
            print("Magie :", end=" ")
        print(i.name)


def shuffle(tab):
    newe = []
    for i in range(len(tab)):
        newe.append(tab[i])
    for i in range(len(newe)):
        a = randrange(len(newe))
        b = randrange(len(newe))
        c = newe[a]
        newe[a] = newe[b]
        newe[b] = c
    return newe


def draw(game, nbr=1):
    for i in range(nbr):
        if (game.turn == 1):
            game.hand1.append(game.deck1[0])
            game.deck1.pop(0)
        else:
            game.hand2.append(game.deck2[0])
            game.deck2.pop(0)


def summon(game, nb=0):
    if (game.turn == 1):
        if (len(game.board1) < 5 and type(game.hand1[nb]) == Monstre):
            game.board1.append(game.hand1[nb])
            game.hand1.pop(nb)
    else:
        if (len(game.board2) < 5 and type(game.hand2[nb]) == Monstre):
            game.board2.append(game.hand2[nb])
            game.hand2.pop(nb)


def attack(game, nba=0, nbe=0):
    if (game.turn == 1):
        dif = game.board1[nba].attack - game.board2[nbe].defence
        if (dif > 0):
            game.HP2 -= dif
            destroy(game, 2, nbe)
        elif (dif < 0):
            game.HP1 += dif
    else:
        dif = game.board2[nba].attack - game.board1[nbe].defence
        if (dif > 0):
            game.HP1 -= dif
            destroy(game, 1, nbe)
        elif (dif < 0):
            game.HP2 += dif


def destroy(game, coter, nbmonstre=0):
    if (coter == 1):
        if (type(game.board1[nbmonstre]) == Monstre):
            game.defause1.append(game.board1[nbmonstre])
            game.board1.pop(nbmonstre)
    else:
        if (type(game.board2[nbmonstre]) == Monstre):
            game.defause2.append(game.board2[nbmonstre])
            game.board2.pop(nbmonstre)


def ecran(game):
    print(game.HP2, "main 2: ", end="")
    for i in game.hand2:
        print(i.name, end=" | ")
    print("\n\nboard 2: ", end="")
    for i in game.board2:
        print(i.name, end=" | ")
    print("\n\nboard 1: ", end="")
    for i in game.board1:
        print(i.name, end=" | ")
    print("\n\n", game.HP1, "main 1: ", end="")
    for i in game.hand1:
        print(i.name, end=" | ")


def start(game):
    draw(game, 5)
    game.switchTurn(game)
    draw(game, 5)
    game.switchTurn(game)


def turn(game):
    a = ""
    draw(game)
    while a != "end":
        if game.HP1 < 0 or game.HP2 < 0:
            return -2
        ecran(game)
        print("\nchoix :")
        a = input()
        if a == "s":
            print("Numeros de la carte a invoquer :")
            n = input()
            summon(game, int(n))
        elif a == "a":
            print("Numeros du monstre attaquant :")
            b = input()
            print("Numeros du monstre attaquer :")
            e = input()
            attack(game, int(b), int(e))
        elif a == "exit":
            return -1
    game.switchTurn(game)
    return 1


game.deck1 = shuffle(deckList)
game.deck2 = shuffle(deckList)
start(game)
while game.HP1 > 0 and game.HP2 > 0:
    if (turn(game) == -1):
        break