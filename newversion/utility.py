from Magie import Magie
from Monstre import Monstre
import effecting
from colorama import Fore
from random import randrange
def findHolder(game, card):
    if card.holder==game.player1.name:
        return game.player1
    elif card.holder==game.player2.name:
        return game.player2
    else:
        return -1

def shuffle(tab):
    for i in range(len(tab)):
        a=randrange(len(tab))
        b=randrange(len(tab))
        c=tab[a]
        tab[a]=tab[b]
        tab[b]=c
    return tab

def chooser(tab):
    if len(tab)==0:
        print("Pas de cible valide")
        return -1
    print("Carte disponible :")
    for i in range(len(tab)):
        print(i+1,":",tab[i].name,end=" | ")
    print()
    print("Numeros de la carte choisis : ",end="")
    c=input()
    while c.isdigit() and (int(c)<1 or int(c)>=len(tab)+1):
        print("Chiffre invalide veuillez resaisir un chiffre :",end="")
        c=input()
    return tab[int(c)-1]

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

def popi(effe,nb=1):
    for i in range(nb):
        effe.pop(0)

def draw(player,nbr=1):
    for i in range(nbr):
        card=player.deck[0]
        player.hand.append(player.deck[0])
        player.deck.pop(0)
    return card
        
def sacrifice(game,nb=1):
    cmp=0
    player=game.getMain(game)
    if nb>len(player.board):
        print(Fore.RED+"Vous ne possedez pas assez de monstre sacrifiable pour l'invoquer.")
        return -1
    while cmp<nb:
        print("Choisissez un monstre a sacrifier:")
        carte=chooser(player.board)
        destroy(game,player,findNumber(player.board,carte))
        cmp+=1
    return 1

def play(game,nb=0):
    player=game.getMain(game)
    if(type(player.hand[nb])==Magie):
        card=player.hand[nb]
        if effecting.effected(game,card)!=-1:
            defausse(game,findNumber(player.hand,card))
    elif(type(player.hand[nb])==Monstre):
        if game.nbSummon==0:
            res=1
            if 7>player.hand[nb].level>4:
                res=sacrifice(game)
            elif player.hand[nb].level>6:
                res=sacrifice(game,2)
            if res==1:
                summon(game,nb)
                game.nbSummon+=1
        else:
            print(Fore.RED +"Vous ne pouvez invoquer qu'un seul monstre par tour.")

def summon(game,nb):
    player=game.getMain(game)
    if len(player.board)<5:
        player.board.append(player.hand[nb])
        player.hand.pop(nb)
        effecting.effected(game,player.board[len(player.board)-1])                
    else:
        print(Fore.RED +"Vous n'avez plus de place pour invoquer un monstre.")
    
def attack(game,nba=0,nbe=0):
    player=game.getMain(game)
    adversaire=game.getAdv(game)
    if game.nbTurn==1:
        print(Fore.RED +"Vous ne pouvez pas attaquer le premier tour !")
        return
    if player.board[nba].canAttack==False:
        print(Fore.RED +"Ce monstre a deja attaquer pendant ce tour !")
        return
    if nbe==-1:
        adversaire.HP-=player.board[nba].attack
        player.board[nba].canAttack=False
        return
    dif=player.board[nba].attack-adversaire.board[nbe].defence
    player.board[nba].canAttack=False
    if(dif>0):
        adversaire.HP-=dif
        destroy(game,adversaire,nbe)
    elif(dif<0):
        player.HP+=dif
                
def defausse(game,nb):    
    player=game.getMain(game)
    player.defause.append(player.hand[nb])
    player.hand.pop(nb)
    
def destroy(game,joueur,nbmonstre=0):
    if(type(joueur.board[nbmonstre])==Monstre):
        joueur.board[nbmonstre].attack=joueur.board[nbmonstre].bAttack
        joueur.board[nbmonstre].defence=joueur.board[nbmonstre].bDefence
        joueur.board[nbmonstre].level=joueur.board[nbmonstre].bDefence
        joueur.defause.append(joueur.board[nbmonstre])
        joueur.board.pop(nbmonstre)

def findNumber(zone,card):
    for i in range(len(zone)):
        if zone[i]==card:
            return i
    return -1