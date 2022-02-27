from random import randrange
from Player import Player
from Game import Game
from Monstre import Monstre
from Magie import Magie
import utility,data,save,turn


def run():
    game,mode=menu()
    if mode==-1: return -1
    if mode==1:
        game.player1.deck=utility.shuffle(game.player1.deck)
        game.player2.deck=utility.shuffle(game.player2.deck)
        start(game)
        print("Debut de la partie")
    elif mode==2:
        utility.holdingPlayer(game)
        print("Reprise de la partie")
    result=0
    while result!=-1 and result !=2:
        result=turn.turn(game)
        if result==2:
            name=''
            listName=data.saveList()
            while name=='' or name in listName:
                name=input("Saisissez un nom pour la sauvegarde : ")
                if name=='' or name in listName:
                    print("Nom deja existant : ")
                    for i in listName:
                        print(i)
            save.sauvegarde(game,name)
    if result==-1:utility.checkWinner(game)

def start(game):
    ordre = 0
    while ordre > 3 or ordre < 1:
        print("Quel joueur commence :\n1 - joueur 1\n2 - joueur 2\n3 - aleatoire")
        ordre = int(input("Choix : "))
    if ordre == 1:
        game.turn = 1
    elif ordre == 2:
        game.turn = 2
    elif ordre == 3:
        game.turn = randrange(1, 3)
    for i in game.player1.deck:
        i.holder = game.player1.name
    for i in game.player2.deck:
        i.holder = game.player2.name
    utility.draw(game.player1, 5)
    utility.draw(game.player2, 5)


def menu():
    option = 0
    print("                 YuPyOh\n")
    print("Bienvenue dans le jeu de carte original YuPyOh")
    while option != "1" and option != "4":
        print("\nVeuillez selectionner une option :\n1 - Commencer une partie\n2 - Voir les deck disponible\n3 - Explication\n4 - Charger une partie\n5 - Quitter")
        option = input("Choix : ")
        if option == "1":
            return initGame(), 1
        elif option == "2":
            showDeck()
        elif option == "3":
            showExplication()
        elif option == "4":
            name=save.loadSave()
            return save.load(name), 2
        elif option == "5":
            return -1, -1

def initGame():
    choix = 0
    while choix not in (1, 2):
        print("Selectionner le type de partie :\n1 - Rapide\n2 - Normal")
        choix = int(input())
    if choix == 1:
        HP = 4000
    else:
        HP = 8000
    game = Game()
    print("Joueur 1")
    game.player1 = selectPlayer(HP)
    print("Joueur 2")
    game.player2 = selectPlayer(HP)
    return game

def showDeck():
    with open("decklist.txt") as f:
        contenu = f.read()
    contenu=contenu.split(".&.")
    print("Deck disponible dans le jeu :\n", contenu[1], sep="")

def showExplication():
    with open("explication.txt") as f:
        contenu = f.read()
    print("Explication du jeu :\n", contenu, sep="")

def chargingDeck(deckName):
    with open("deck/" + deckName + ".csv") as f:
        contenu = f.read()
    contenu = contenu.split('\n')
    for i in range(len(contenu)): contenu[i] = contenu[i].split(';')
    deck = []
    for i in range(len(contenu)):
        if contenu[i][0] == "Monstre":
            deck.append(Monstre(contenu[i][1:]))
        elif contenu[i][0] == "Magie":
            deck.append(Magie(contenu[i][1:]))
    return deck


def selectPlayer(HP=8000):
    list_deck = data.deckList()
    selection = len(list_deck)+1
    print("Nom du joueur : ", end="")
    name = input()
    nbr_list = len(list_deck)
    while selection > nbr_list:
        print("Selectionner votre deck :")
        for i in range(nbr_list):
            print(i + 1, "-", list_deck[i])
        selection = int(input())
    deck = list_deck[selection - 1]
    player = Player(name, HP)
    player.deck = chargingDeck(deck)
    return player