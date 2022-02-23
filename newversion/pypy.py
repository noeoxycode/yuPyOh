from random import randrange
from colorama import Fore,init
from Player import Player
from Game import Game
from Monstre import Monstre
from Magie import Magie
import utility,data,turn,save
init(autoreset=True)



def start(game):
    for i in game.player1.deck:
        i.holder=game.player1.name
    for i in game.player2.deck:
        i.holder=game.player2.name
    utility.draw(game.player1,5)
    utility.draw(game.player2,5)
    
def checkWinner(game):
    print("Victoire de ",end="")
    if game.player1.HP<=0:
        print(game.player2.name,"\nVous avez reduis les point de vie de votre adversaire a 0")
        return
    if game.player2.HP<=0:
        print(game.player1.name,"\nVous avez reduis les point de vie de votre adversaire a 0")
        return
    if len(game.player1.deck)==0:
        print(game.player2.name,"\nLe deck de votre adversaire ne contient plus de carte")
        return
    if len(game.player2.deck)==0:
        print(game.player1.name,"\nLe deck de votre adversaire ne contient plus de carte")
        return
    print("partie annuler")

                
def menu():
    option=0
    print("                 YuPyOh\n")
    print("Bienvenue dans le jeu de carte original YuPyOh")
    while option!="1" and option!="4":
        print("\nVeuillez selectionner une option :\n1 - Commencer une partie\n2 - Voir les deck disponible\n3 - Explication\n4 - Charger une partit\n5 - Quitter")
        option=input("Choix : ")
        if option == "1":
            return initGame(),1
        elif option=="2":
            showDeck()
        elif option=="3":
            showExplication()
        elif option=="4":
            return save.load(),2
        elif option=="5":
            return -1,-1

def initGame():
    print("Selectionner le type de partit :\n1 - Rapide\n2 - Normal")
    HP=input()
    if HP=="1":HP=4000
    else:HP=8000
    game=Game
    print("Joueur 1")
    game.player1=selectPlayer(HP)
    print("Joueur 2")
    game.player2=selectPlayer(HP)
    return game

def showDeck():
    with open("decklist.txt") as f:
        contenu=f.read()
    print("Deck disponible dans le jeu :\n",contenu,sep="")

def showExplication():
    with open("explication.txt") as f:
        contenu=f.read()
    print("Explication du jeu :\n",contenu,sep="")

def chargingDeck(deckName):
    with open("deck/"+deckName+".csv") as f:
        contenu=f.read()
    contenu=contenu.split('\n')	 				 					 		 		  
    for i in range(len(contenu)): contenu[i]=contenu[i].split(';')
    deck=[]
    for i in range(len(contenu)):
        if contenu[i][0]=="Monstre":
            deck.append(Monstre(contenu[i][1:]))
        elif contenu[i][0]=="Magie":
            deck.append(Magie(contenu[i][1:]))
    return deck


def selectPlayer(HP=8000):
    print("Nom du joueur : ",end="")
    name=input()
    list=data.deckList()
    print("Selectionner votre deck :")
    for i in range(len(list)):
        print(i+1,"-",list[i])
    deck=list[int(input())-1]
    player=Player(name,HP)
    player.deck=chargingDeck(deck)
    return player

def main():
    game,mode=menu()
    if mode==-1: return -1
    if mode==1:
        game.player1.deck=utility.shuffle(game.player1.deck)
        game.player2.deck=utility.shuffle(game.player2.deck)
        start(game)
        print("Debut de la partit")
    elif mode==2:
        print("Reprise de la partit")
    result=0
    while result!=-1 and result !=2:
        result=turn.turn(game)
        if result==2:
            save.sauvegarde(game)
    if result==-1:checkWinner(game)



#menu()
#game.player2.board.append(Heros.deckList[0])
#data.game.player1.deck=utility.shuffle(Heros.deckList)
#data.game.player2.deck=utility.shuffle(Heros.deckList)
#start(data.game)

#while data.game.player1.HP>0 and data.game.player2.HP>0:
#    if(turn.turn(data.game)==-1):
#        break
#checkWinner(data.game)
if __name__ == "__main__":
    main()