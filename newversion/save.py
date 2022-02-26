from Magie import Magie
from Monstre import Monstre
from Game import Game
import utility


def sauvegarde(game):
    file = open("save.csv", "w")
    file.write(str(game.turn) + ";" + str(game.nbTurn) + "\n")
    file.write(
        game.player1.name + ";" + str(game.player1.HP) + ";" + game.player2.name + ";" + str(game.player2.HP) + "\n")
    file.write(".!.\n")
    cardWrite(file, game.player1.deck)
    cardWrite(file, game.player1.hand)
    cardWrite(file, game.player1.board)
    cardWrite(file, game.player1.defause)
    cardWrite(file, game.player2.deck)
    cardWrite(file, game.player2.hand)
    cardWrite(file, game.player2.board)
    cardWrite(file, game.player2.defause)


def cardWrite(file, zone):
    for i in zone:
        if type(i) == Magie:
            file.write("Magie;" + i.name + ";" + i.effect + ";" + i.effectInt + "\n")
        elif type(i) == Monstre:
            file.write(
                "Monstre;" + i.name + ";" + str(i.attack) + ";" + str(i.defence) + ";" + str(i.level) + ";" + str(
                    i.bAttack) + ";" + str(i.bDefence) + ";" + str(i.bLevel) + ";" + i.types)
            if i.effect != "":
                file.write(";" + i.effect + ";" + i.effectInt)
            file.write("\n")
    file.write(".!.\n")


def load():
    with open("save.csv") as file:
        contenu = file.read()
    contenu = contenu.split(".!.\n")
    for i in range(len(contenu)):
        contenu[i] = contenu[i].split("\n")
    for i in range(len(contenu)):
        for j in range(len(contenu[i])):
            contenu[i][j] = contenu[i][j].split(";")
    game = Game
    game.turn = int(contenu[0][0][0])
    game.nbTurn = int(contenu[0][0][1])
    game.player1.name = contenu[0][1][0]
    game.player1.HP = int(contenu[0][1][1])
    game.player2.name = contenu[0][1][2]
    game.player2.HP = int(contenu[0][1][3])
    utility.popi(contenu)
    loadPLayer(game.player1, contenu)
    loadPLayer(game.player2, contenu)
    return game


def loadPLayer(player, contenu):
    loadCard(player.deck, contenu[0])
    loadCard(player.hand, contenu[1])
    loadCard(player.board, contenu[2])
    loadCard(player.defause, contenu[3])
    utility.popi(contenu, 4)


def loadCard(tab, contenu):
    if contenu != []:
        for i in contenu:
            if i[0] == "Magie":
                tab.append(Magie(i[1:]))
            elif i[0] == "Monstre":
                tab.append(Monstre(i[1:]))
