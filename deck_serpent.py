
# ------------------------------------------   DEFINITION  --------------------------------------------


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

    # -- Fonctions :

    def switchTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


class Monster:
    name = ""
    attack = 0
    defence = 0
    level = 0
    types = ""
    effect = ""
    effectInt = ""

    # -- Constructeurs :
    def __init__(self, name="", attack=0, defence=0, level=0, types="", effect="", effectInt=""):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.level = level
        self.types = types
        self.effect = effect
        self.effectInt = effectInt.split(" ")

    # -- Méthodes (fonctions) :

    # Affichage infos Monstres :
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

    # -- Constructeurs :
    def __init__(self, name, effect, effectInt=""):
        self.name = name
        self.effect = effect
        self.effectInt = effectInt

    # Affichage infos magie :
    def printi(self):
        print("Nom :", self.name)
        print("Effet :", self.effect)


# -----------------------------------------    UTILISATION ---------------------------------------------

game = Game()
deckList = []

deckList.append(Monster("Tigrex", 900, 1100, 2, "Felin"))
deckList.append(Monster("Sphinx", 1100, 700, 3, "Felin"))
deckList.append(Monster("Homme-jaguar", 1600, 1300, 4, "Felin"))
deckList.append(Monster("Lion de Némée", 1800, 1600, 5, "Felin"))
deckList.append(Monster("Chat d'argent", 1000, 1200, 3, "Felin"))
deckList.append(Monster("Akamataa", 1300, 1400, 4, "Serpent"))
deckList.append(Monster("Aspic", 1000, 800, 3, "Serpent"))
deckList.append(Monster("Python", 900, 1100, 2, "Serpent"))
deckList.append(Monster("Tireur de l'Atlantide", 1400, 1600, 4, "Empreur"))
deckList.append(Monster("Poseidra", 1600, 1700, 4, "Empreur"))
deckList.append(Monster("Destructeur du Grand Bleu", 1300, 1300, 4, "Empreur"))
deckList.append(Monster("Chasseur des Mers", 2400, 2100, 6, "Empreur"))
deckList.append(Monster("Soldat Triton", 2600, 2100, 6, "Empreur"))
deckList.append(Monster("Dragon Océan", 1600, 1700, 6, "Seigneur"))
deckList.append(Monster("Sirène Archère", 1500, 1200, 4, "Empreur"))
deckList.append(Monster("Codarus", 1800, 1000, 3, "Empreur"))
deckList.append(Monster("Reese", 1700, 2000, 5, "Empreur"))
deckList.append(Monster("Condamné", 1300, 1400, 4, "Ange"))
deckList.append(Monster("Superbia", 1600, 1000, 4, "Ange"))
deckList.append(Monster("Zerato", 1800, 2000, 5, "Ange"))
deckList.append(Monster("Valkyrie de la Puissance", 2300, 2600, 6, "Ange"))
deckList.append(Monster("Explosion BM-4", 1800, 2000, 5, "Arraignée"))
deckList.append(Monster("Némésis Subterreur", 1800, 2000, 5, "Archer"))
deckList.append(Monster("Meklord de Granel", 1800, 2000, 4, "Armée"))
deckList.append(Monster("Ambidextre", 2900, 2400, 8, "Boxeur"))
deckList.append(Monster("Enchaîneur", 2600, 2000, 7, "Boxeur"))
deckList.append(Monster("Harrliard", 1800, 2000, 5, "Fantôme"))
deckList.append(Monster("Hamstrat", 1800, 2000, 5,  "Fantôme"))

print(deckList[0])
# deckList.append(Magie())
# deckList.append(Magie())





# class player()
#     # un deck, contenant des cartes
#     # une main, contenant des cartes
#     # vie restante
#
# class deck()
#         # une liste de carte
#
# class defausse()
#     # une liste de carte
#
# class board()
#     # deck 1 et 2
#     # defausse 1 et 2
#     # liste des cartes posées sur le board (joueur 1 et 2)
#
# class carte()
#     # nom ....
#
# class magie(carte):
#     ...
#
# class monstre(carte):
#     ...
