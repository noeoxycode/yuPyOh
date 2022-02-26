from Magie import Magie
from Monstre import Monstre
import utility
from colorama import Fore
def ecran(game):
    print("-----------------------------------------------------\n")
    print(game.player2.name,str(game.player2.HP),"HP\nmain 2: ",end="")
    if game.turn==2:
        for i in game.player2.hand:
            printColorName(i)
    print("\n\nboard 2: ",end="")
    for i in game.player2.board:
        printColorName(i)
    print("\n\nboard 1: ",end="")
    for i in game.player1.board:
        printColorName(i)   
    print("\n\nmain 1: ",end="")
    if game.turn==1:
        for i in game.player1.hand:
            printColorName(i)
    print()
    print(game.player1.name,str(game.player1.HP),"HP")
    print("-----------------------------------------------------")
    
def turn(game):
    a=""
    player=game.getMain(game)
    adv=game.getAdv(game)
    if len(player.deck)==0:
        return -1
    utility.draw(player,1)
    while a!="4" and a!="5":
        if player.HP<0 or adv.HP<0:
            return -1
        ecran(game)
        print("\nChoissisez une option :\n1 - Jouer une carte\n2 - Attaquer avec un monstre\n3 - Voir les informations d'une carte\n4 - Terminer votre tour\n5 - Terminer votre tour et sauvegarder la partie")
        a=input()
        if a=="1":
            print("Choisisez la carte a jouer :")
            n=utility.findNumber(player.hand,utility.chooser(player.hand))
            utility.play(game,n)
        elif a=="2":
            b=e=-1
            print("Choisisez le monstre attaquant :")
            b=utility.findNumber(player.board,utility.chooser(player.board))
            if len(adv.board)>0:
                print("Choisisez le monstre attaquer :")
                e=utility.findNumber(adv.board,utility.chooser(adv.board))
            utility.attack(game,b,e)
        elif a=="3":
            print("Position de la carte voulu :\n1 - Main\n2 - Terrain")
            b=input()
            while b!="1" and b!="2":
                print("Saisie invalide, veuillez recommancer : ")
                b=input()
            if b =="1":
                b=player.hand
            elif b=="2":
                b=player.board
            print("-----------------------------------------------------")
            utility.chooser(b).printi()
        elif a=="exit":
            return -1
    if len(player.hand)>7:utility.limitHand(player)
    game.endTurn(game)
    if a=="4":return 1
    if a=="5":return 2

def printColorName(card):
    if type(card)==Monstre:
        print(Fore.YELLOW + card.name,end="")
        print("",card.level,"",card.attack,"",card.defence,end="")
    elif type(card)==Magie:
        print(Fore.CYAN +  card.name,end="")
    print("",end=" | ")