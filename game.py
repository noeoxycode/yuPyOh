from random import Random, random, randrange
from re import I
import types
from unicodedata import digit, name
from xml.etree.ElementPath import find
from colorama import Fore,Style,init
init(autoreset=True)
Types=["Guerrier","Bete"]
class Player:
    name=""
    deck=[]
    hand=[]
    board=[]
    defause=[]
    HP=8000
    def __init__(self, name="",HP=8000):
        self.name=name
        self.HP=HP
        self.hand=[]
        self.deck=[]
        self.board=[]
        self.defause=[]


class Game:
    turn=1
    player1=Player("Yugi")
    player2=Player("Kaiba")
    nbSummon=0
    phase=""
    target=""
    def __init__(self, name1="Yugi",name2="Kaiba"):
        self.player1=Player(name1)
        self.player2=Player(name2)

    def switchTurn(self):
        self.nbSummon=0
        self.target=""
        if self.turn==1:
            self.turn=2
        else:
            self.turn=1
    def getMain(self):
        if self.turn==1:
            return self.player1
        elif self.turn==2:
            return self.player2
        else:
            return -1
    def getAdv(self):
        if self.turn==1:
            return self.player2
        elif self.turn==2:
            return self.player1
        else:
            return -1


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
    canAttack=False
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
    def printi(self):
        print("Monstre :",self.name)
        print("Holder :",self.holder)
        print("LVL :",self.level,"Type :",self.types)
        print("ATK :",self.attack,"  DEF :",self.defence,)
        if self.attack != self.bAttack or self.defence != self.bDefence:
            print("ATK de base :",self.bAttack,"  DEF de base :",self.bDefence)
        if self.effect !="":
            print("Effet :",self.effect)
            print("Effet :",self.effectInt)
    def copy(self):
        return Monstre(self.name,self.bAttack,self.bDefence,self.bLevel,self.types,self.effect,self.effectInt)

class Magie:
    name=""
    effect=""
    effectInt=""
    holder=""
    def __init__(self, name,effect,effectInt=""):
        self.name=name
        self.effect=effect
        if type(effectInt) is type([]):
            self.effectInt=effectInt
        else:
            self.effectInt=effectInt.split(" ")
    def printi(self):
        print("Magie :",self.name)
        print("Effet :",self.effect)
    def copy(self):
        return Magie(self.name,self.effect,self.effectInt)

game=Game
deckList=[]
deckList.append(Monstre("Avian",1000,1000,3,"Guerrier"))
deckList.append(Monstre("Clayman",800,2000,3,"Guerrier"))
deckList.append(Monstre("Burstinatrix",1300,800,3,"Guerrier","Choisi un monstre ennemie, si sa DEF est inférieur à l'ATK de ce monstre, le détruit","CHOOSE ennemie.board IF target.DEF$<$him.ATK DESTROY$target"))
deckList.append(Monstre("Bubbleman",800,1200,3,"Guerrier"))
deckList.append(Monstre("Flipper",900,1400,3,"Bete","Choisie un monstre de votre main et l'invoque si c'est possible","CHOOSE allie.hand.Monstre SUMMON target"))
deckList.append(Monstre("Colibri",800,1000,3,"Bete","Choisi un monstre que vous controlez, vous vous soignez de 200 x son niveau", "CHOOSE allie.board HEAL* 200 target.LVL"))
deckList.append(Monstre("Panthere noir",1300,1500,4,"Bete"))
deckList.append(Monstre("Topitaupe",1400,1000,4,"Bete"))
deckList.append(Monstre("Sparkman",1600,1200,4,"Guerrier"))
deckList.append(Monstre("Nécrombre",1500,1200,4,"Guerrier"))
deckList.append(Monstre("Airman",1800,1000,4,"Guerrier","Donne 300 DEF à un monstre allié","CHOOSE allie.board.Guerrier BOOSTD target 300"))
deckList.append(Monstre("Capitaine dorée",1800,1000,4,"Guerrier","Pioche une carte","DRAW 1"))
deckList.append(Monstre("Blazeman",1600,1600,4,"Guerrier"))
deckList.append(Monstre("Ocean",1500,1700,4,"Guerrier"))
deckList.append(Monstre("Tranchant",2200,2000,6,"Guerrier"))
deckList.append(Monstre("Géant du tonnerre",2400,2200,6,"Guerrier"))
deckList.append(Monstre("Homme-Oiseau de feu",2100,1800,6,"Guerrier","Choisi un monstre ennemie, gagne sa DEF en ATK","CHOOSE ennemie.board BOOSTA him target.DEF"))
deckList.append(Monstre("Néos",2500,2200,7,"Guerrier"))
deckList.append(Monstre("Chevalier Néos",2700,2300,7,"Guerrier","Choisi un monstre ennemie, divise son ATK par 2","CHOOSE ennemie.board DIVIDEA target"))
deckList.append(Monstre("Homme-Oiseau à l'éclat lumineux",2500,2500,8,"Guerrier","Quant il est invoqué, gagne 200 ATK par monstre Guerrier dans votre cimetière","BOOSTA* him 200 allie.defause.Guerrier.nb"))
deckList.append(Magie("Signal du héro","Choisisez un monstre que vous controlez, il gagne 500 ATK","CHOOSE allie.board BOOSTA target 500"))
deckList.append(Magie("Appel d'urgence","Pioche 1 carte si c'est un monstre guerrier pioche une carte de plus","DRAW 1 IF target$==$Guerrier DRAW$1"))
deckList.append(Magie("Soin de la justice","Vous soigne de 200 x nombre de carte dans la main","HEAL* 200 allie.hand.nb"))
deckList.append(Magie("Ravage de foudre","Si vous controler \"Géant du tonnerre\", détruit un monstre ennemie","CHOOSE allie.board.Géant@du@tonnerre CHOOSE ennemie.board DESTROY target"))
deckList.append(Magie("Dernier espoir","Détruit tous vos monstres et infliger 400 point de dégat à votre adversaire par monstre détruit","DAMAGE* allie.board.nb 400 DESTROY allie.board"))
deckList.append(Magie("Reigne animal","Toutes vos betes gagne 1 niveau, 400 ATK et DEF","ALL bete BOOSTA target 400 BOOSTD target 400 BOOSTL target 1"))
deckList.append(Magie("Prison héroique","Choisisez un monstre ennemie, il pert un montant d'ATK égal à 100 x son niveau","CHOOSE ennemie.board MINUSA* target 100 target.lvl"))
deckList.append(Magie("Super blocage","Choisisez un monstre guerrier que vous controlez, il gagne 800 DEF","CHOOSE allie.board.Guerrier BOOSTD target 800"))
deckList.append(Magie("Rappel de secours","Choisisez un monstre guerrier que vous cimetière, l'ajoute à votre main","CHOOSE allie.defause.Guerrier RESTORE target"))
deckList.append(Magie("Destruction de Néos","Choisisez un \"Néos\" que vous controlez, il gagne 500 ATK, attaque tous les monstre ennemis, puis le détruit","CHOOSE allie.board.Néos IF ennemie.board.nb$>$0 BOOSTA$target$500$ATTACK$target$ennemie.board$DESTROY$target"))

def list(tab):
    print("Deck List :",len(tab),"cartes")
    for i in tab:
        if(type(i)is Monstre):
            print("Monstre :",end=" ")
        else:
            print("Magie :",end=" ")
        print(i.name)

def shuffle(tab):
    newe=[]
    for i in tab:
        newe.append(i.copy())
    for i in range(len(newe)):
        a=randrange(len(newe))
        b=randrange(len(newe))
        c=newe[a]
        newe[a]=newe[b]
        newe[b]=c
    return newe

def start(game):
    for i in game.player1.deck:
        i.holder=game.player1.name
    for i in game.player2.deck:
        i.holder=game.player2.name
    draw(game.player1,5)
    draw(game.player2,5)

def draw(player,nbr=1):
    for i in range(nbr):
        card=player.deck[0]
        player.hand.append(player.deck[0])
        player.deck.pop(0)
    return card
        
        

def play(game,nb=0):
    player=game.getMain(game)
    if(type(player.hand[nb])==Magie):
        if effected(game,player.hand[nb])!=-1:
            defausse(game,nb)
    elif(type(player.hand[nb])==Monstre):
        if game.nbSummon==0:
            summon(game,nb)
            game.nbSummon+=1
        else:
            print("Vous ne pouvez invoquer qu'un seul monstre par tour.")

def summon(game,nb):
    player=game.getMain(game)
    if len(player.board)<5:
        player.board.append(player.hand[nb])
        player.hand.pop(nb)
        effected(game,player.board[len(player.board)-1])                
    else:
        print("Vous n'avez plus de place pour invoquer un monstre.")
    
def attack(game,nba=0,nbe=0):
    player=game.getMain(game)
    adversaire=game.getAdv(game)
    dif=player.board[nba].attack-adversaire.board[nbe].defence
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

def ecran(game):
    cpt=0
    print("-----------------------------------------------------\n")
    print(game.player2.name,"\n"+str(game.player2.HP),"\nmain 2: ",end="")
    for i in game.player2.hand:
        print(cpt,end=" ")
        cpt+=1
        printColorName(i)
    cpt=0
    print("\n\nboard 2: ",end="")
    for i in game.player2.board:
        printColorName(i)
    print("\n\nboard 1: ",end="")
    for i in game.player1.board:
        printColorName(i)   
    print("\n\nmain 1: ",end="")
    for i in game.player1.hand:
        print(cpt,end=" ")
        printColorName(i)
        cpt+=1
    print("\n"+str(game.player1.HP))
    print(game.player1.name)
    print("-----------------------------------------------------")
    
def turn(game):
    a=""
    player=game.getMain(game)
    adv=game.getAdv(game)
    if len(player.deck)==0:
        return -1
    draw(player,1)
    while a!="end":
        if player.HP<0 or adv.HP<0:
            return -1
        ecran(game)
        print("\nchoix :")
        a=input()
        if a=="s":
            print("Numeros de la carte a invoquer :")
            n=input()
            play(game,int(n))
        elif a=="a":
            print("Numeros du monstre attaquant :")
            b=input()
            print("Numeros du monstre attaquer :")
            e=input()
            attack(game,int(b),int(e))
        elif a=="i":
            print("emplacement (m|b) :")
            b=input()
            if b =="m":
                b=player.hand
            else:
                b=player.board
            chooser(b).printi()
        elif a=="exit":
            return -1
    game.switchTurn(game)
    return 1

def printColorName(card):
    if type(card)==Monstre:
        print(Fore.YELLOW + card.name,end="")
        print("",card.attack,card.defence,end="")
    elif type(card)==Magie:
        print(Fore.CYAN +  card.name,end="")
    print("",end=" | ")


def effected(game,card):
    player=game.getMain(game)
    effe=[]
    if card.effectInt==['']:
        return
    for i in range(len(card.effectInt)):
        effe.append(card.effectInt[i])
    while effe!=[]:
        if effect(game,card,player,effe)==-1:
            print("Condition impossible à remplir !")
            return -1
    game.target=""
    return 0


def effect(game,card,player,effe):
    if effe[0]=="HEAL":
        player.HP+=expression(effe[1],game,card)
        popi(effe,2)
    elif effe[0]=="HEAL*":
        player.HP+=expression(effe[1],game,card)*expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="DRAW":
        game.target=draw(game.getMain(game),expression(effe[1],game,card))
        popi(effe,2)
    elif effe[0]=="BOOSTA":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="BOOSTA*":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)*expression(effe[3],game,card)
        popi(effe,4)
    elif effe[0]=="BOOSTD":
        cible=expression(effe[1],game,card)
        cible.defence+=expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="BOOSTD*":
        cible=expression(effe[1],game,card)
        cible.defence+=expression(effe[2],game,card)*expression(effe[3],game,card)
        popi(effe,4)
    elif effe[0]=="BOOSTL":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="MINUSA":
        cible=expression(effe[1],game,card)
        cible.attack-=expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="MINUSA*":
        cible=expression(effe[1],game,card)
        cible.attack-=expression(effe[2],game,card)*expression(effe[3],game,card)
        popi(effe,4)
    elif effe[0]=="MINUSD":
        cible=expression(effe[1],game,card)
        cible.defence-=expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="MINUSD*":
        cible=expression(effe[1],game,card)
        cible.defence-=expression(effe[2],game,card)*expression(effe[3],game,card)
        popi(effe,4)
    elif effe[0]=="CHOOSE":
        c=chooser(expression(effe[1],game,card))
        if c==-1:
            return c
        else:
            game.target=c
        popi(effe,2)
    elif effe[0]=="DAMAGE":
        game.getAdv(game).HP-=expression(effe[1],game,card)
        popi(effe,2)
    elif effe[0]=="DAMAGE*":
        game.getAdv(game).HP-=expression(effe[1],game,card)*expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="DESTROY":
        cible=expression(effe[1],game,card)
        if type(cible)!=type([]):
            pos=findNumber(findHolder(game,cible).board,cible)
            destroy(game,findHolder(game,cible),pos)
        else:
            while cible!=[]:
                destroy(game,findHolder(game,cible[0]),0)
        popi(effe,2)
    elif effe[0]=="RESTORE":
        cible = expression(effe[1],game,card)
        pos = findNumber(game.getMain(game).defause,card)
        game.getMain(game).hand.append(game.getMain(game).defause[pos])
        game.getMain(game).defause.pop(pos)
        popi(effe,2)
    elif effe[0]=="DIVIDEA":
        cible=expression(effe[1],game,card)
        cible.attack/=2
        popi(effe,2)
    elif effe[0]=="DIVIDED":
        cible=expression(effe[1],game,card)
        cible.defence/=2
        popi(effe,2)
    elif effe[0]=="SUMMON":
        cible=expression(effe[1],game,card)
        pos=findNumber(game.getMain(game).hand,cible)
        summon(game,pos)
        popi(effe,2)
    elif effe[0]=="IF":
        condition=expression(effe[1],game,card)
        if condition :
            copy=effe[2].split("$")
            while(copy!=[]):
                copy=effect(game,card,game.getMain(game),copy)
        popi(effe,3)
    elif effe[0]=="IFE":
        condition=expression(effe[1],game,card)
        if condition :
            copy=effe[2].split("$")
            while(copy!=[]):
                copy=effect(game,card,game.getMain(game),copy)
        else:
            copy=effe[3].split("$")
            while(copy!=[]):
                copy=effect(game,card,player,copy)
        popi(effe,4)
    elif effe[0]=="ATTACK":
        ally=findNumber(game.getMain(game).board,expression(effe[1],game,card))
        ennemie=expression(effe[2],game,card)
        if type(ennemie)==type([]):
            for i in range(len(ennemie)):
                pos=findNumber(game.getAdv(game).board,ennemie[len(ennemie)-i-1])
                attack(game,ally,pos)
        else:
            pos=findNumber(game.getAdv(game).board,ennemie)
            attack(game,ally,pos)
        popi(effe,3)
    return effe

def findHolder(game, card):
    if card.holder==game.player1.name:
        return game.player1
    elif card.holder==game.player2.name:
        return game.player2
    else:
        return -1

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
        print("Chiffre invalide veuillez resaisir un chiffre",c,str(len(tab)+1)," :",end="")
        c=input()
    return tab[int(c)-1]


def popi(effe,nb=1):
    for i in range(nb):
        effe.pop(0)

def expression(coucou,game,card):
    if coucou.isdigit():
        return int(coucou)
    elif coucou == "allie":
        return game.getMain(game)
    elif coucou == "ennemie":
        return game.getAdv(game)
    elif coucou == "him":
        return card
    elif coucou == "target":
        return game.target
    elif "$" in coucou:
        tmp=coucou.split('$')
        a=expression(tmp[0],game,card)
        b=expression(tmp[2],game,card)
        if tmp[1]=="<":return a<b
        if tmp[1]==">":return a>b
        if tmp[1]=="==":return a==b
        if tmp[1]=="!=":return a!=b
    elif '.' in coucou:
        tmp=coucou.split('.')
        a=expression(tmp[0],game,card)
        tmp.pop(0)
        for i in range(len(tmp)):
            if tmp[0]=="hand":
                a=a.hand
            elif tmp[0]=="board":
                a=a.board
            elif tmp[0]=="deck":
                a=a.deck
            elif tmp[0]=="defause":
                a=a.defause
            elif tmp[0]=="ATK":
                a=a.attack
            elif tmp[0]=="DEF":
                a=a.defence
            elif tmp[0]=="LVL":
                a=a.level
            elif tmp[0]=="type":
                a=a.types
            elif tmp[0]=="nb":
                a=len(a)
            elif tmp[0] =="Monstre":
                copy=[]
                for i in a:
                    if type(i)==Monstre:
                        copy.append(i)
                a=copy
            elif tmp[0] =="Magie":
                copy=[]
                for i in a:
                    if type(i)==Magie:
                        copy.append(i)
                a=copy
            elif tmp[0] in Types:
                copy=[]
                for i in a:
                    if type(i)==Monstre:
                        if i.types==tmp[0]:
                            copy.append(i)
                a=copy
            else:
                tmp[0]=tmp[0].replace("@"," ")
                copy=[]
                for i in a:
                    if i.name==tmp[0]:
                        copy.append(i)
                a=copy  
            tmp.pop(0)
        return a
    
        
                



#game.player2.board.append(deckList[0])
game.player1.deck=shuffle(deckList)
game.player2.deck=shuffle(deckList)
start(game)


while game.player1.HP>0 and game.player2.HP>0:
    if(turn(game)==-1):
        break