from random import Random, random, randrange
from unicodedata import digit, name
from colorama import Fore,Style,init
init(autoreset=True)

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
    def __init__(self, name1="Yugi",name2="Kaiba"):
        self.player1=Player(name1)
        self.player2=Player(name2)

    def switchTurn(self):
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
    types=""
    effect=""
    effectInt=""
    def __init__(self, name="",attack=0,defence=0,level=0,types="",effect="",effectInt=""):
        self.name = name
        self.attack = self.bAttack=attack
        self.bDefence=self.defence = defence
        self.level = level
        self.types = types
        self.effect = effect
        self.effectInt=effectInt.split(" ")
    def printi(self):
        print("Monstre :",self.name)
        print("ATK :",self.attack,"  DEF :",self.defence,)
        if self.attack != self.bAttack or self.defence != self.bDefence:
            print("ATK de base :",self.bAttack,"  DEF de base :",self.bDefence)
        print("LVL :",self.level,"Type :",self.types)
        print("Effet :",self.effect)

class Magie:
    name=""
    effect=""
    effectInt=""
    def __init__(self, name,effect,effectInt=""):
        self.name=name
        self.effect=effect
        self.effectInt=effectInt.split(" ")
    def printi(self):
        print("Magie :",self.name)
        print("Effet :",self.effect)
"CHOOSE hand SUMMON cible"
game=Game
deckList=[]
deckList.append(Monstre("Avian",1000,1000,3,"Guerrier"))
deckList.append(Monstre("Clayman",800,2000,3,"Guerrier"))
deckList.append(Monstre("Burstinatrix",1300,800,3,"Guerrier","Choisi un monstre ennemie, si sa DEF est inférieur à l'ATK de ce monstre, le détruit","CHOOSE ennemie IF cible.DEF < him.ATK DESTROY cible"))
deckList.append(Monstre("Bubbleman",800,1200,3,"Guerrier"))
deckList.append(Monstre("Flipper",900,1400,3,"Bete","Choisie un monstre de votre main et l'invoque si c'est possible","BOOSTA him 500"))
deckList.append(Monstre("Colibri",800,1000,3,"Bete","Choisi un monstre que vous controlez, vous vous soignez de 200 x son niveau", "CHOOSE allie  HEAL* 200 allie.niveau"))
deckList.append(Monstre("Panthere noir",1300,1500,4,"Bete"))
deckList.append(Monstre("Topitaupe",1400,1000,4,"Bete"))
deckList.append(Monstre("Sparkman",1600,1200,4,"Guerrier"))
deckList.append(Monstre("Nécrombre",1500,1200,4,"Guerrier"))
deckList.append(Monstre("Airman",1800,1000,4,"Guerrier","Donne 300 DEF à un monstre allié","CHOOSE allie BOOST allie.DEF 300"))
deckList.append(Monstre("Capitaine dorée",1800,1000,4,"Guerrier","Pioche une carte","DRAW 1"))
deckList.append(Monstre("Blazeman",1600,1600,4,"Guerrier"))
deckList.append(Monstre("Ocean",1500,1700,4,"Guerrier"))
deckList.append(Monstre("Tranchant",2200,2000,6,"Guerrier"))
deckList.append(Monstre("Géant du tonnerre",2400,2200,6,"Guerrier"))
deckList.append(Monstre("Homme-Oiseau de feu",2100,1800,6,"Guerrier","Choisi un monstre ennemie, gagne sa DEF en ATK","CHOOSE ennemie BOOST him.ATK cible.DEF"))
deckList.append(Monstre("Néos",2500,2200,7,"Guerrier"))
deckList.append(Monstre("Chevalier Néos",2700,2300,7,"Guerrier","Choisi un monstre ennemie, divise son ATK par 2","CHOOSE ennemie DIVIDEA ennemie 2"))
deckList.append(Monstre("Homme-Oiseau à l'éclat lumineux",2500,2500,8,"Guerrier","Quant il est invoqué, gagne 200 ATK par monstre Guerrier dans votre cimetière","BOOST* him.ATK 200 cimetiere.guerrier"))
deckList.append(Magie("Signal du héro","Choisisez un monstre guerrier que vous controlez, il gagne 500 ATK","CHOOSE allie BOOST allie.ATK 500"))
deckList.append(Magie("Appel d'urgence","Pioche 1 carte si c'est un monstre guerrier pioche une carte de plus","DRAW 1 IF him = guerrier DRAW;1"))
deckList.append(Magie("Soin de la justice","Vous soigne de 200 x nombre de carte dans la main","HEAL* 200 hand.nb"))
deckList.append(Magie("Ravage de foudre","Si vous controler \"Géant du tonnerre\", détruit un monstre ennemie","IF \"Géant du tonnerre\" CHOOSE ennemie DESTROY cible"))
deckList.append(Magie("Dernier espoir","Détruit tous vos monstres et infliger 400 point de dégat à votre adversaire par monstre détruit","DAMAGE* allie.board.nb 400 DESTROY bord "))
deckList.append(Magie("Reigne animal","Toutes vos betes gagne 1 niveau, 400 ATK et DEF","ALL bete BOOST cible.ATK 400 BOOST cible.DEF 400 BOOST cible.lvl 1"))
deckList.append(Magie("Prison héroique","Choisisez un monstre guerrier que vous controlez, un monstre ennemie pert un montant d'ATK égal à 100 x le niveau de votre monstre","CHOOSE allie CHOOSE ennemie MINUS* ennemie.ATK 100 allie.lvl"))
deckList.append(Magie("Super blocage","Choisisez un monstre guerrier que vous controlez, il gagne 800 DEF","CHOOSE allie.guerrier BOOST him.DEF 800"))
deckList.append(Magie("Rappel de secours","Choisisez un monstre guerrier que vous cimetière, l'ajoute à votre main","CHOOSE cimetiere.guerrier TO hand"))
deckList.append(Magie("Destruction de Néos","Choisisez un \"Néos\" que vous controlez, il gagne 500 ATK, attaque tous les monstre ennemis, puis le détruit","CHOOSE allie.\"Néos\" BOOST him.ATK 500 ATTACK ennemie.all DESTROY him"))

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
    for i in range(len(tab)):
        newe.append(tab[i])
    for i in range(len(newe)):
        a=randrange(len(newe))
        b=randrange(len(newe))
        c=newe[a]
        newe[a]=newe[b]
        newe[b]=c
    return newe

def start(game):
        draw(game.player1,4)
        draw(game.player2,5)
        game.player1.hand.append(deckList[22])

def draw(player,nbr=1):
    for i in range(nbr):
        player.hand.append(player.deck[0])
        player.deck.pop(0)
     
        
        

def play(game,nb=0):
    player=game.getMain(game)
    if(type(player.hand[nb])==Magie):
        effected(game,player.hand[nb])
        defausse(game,nb)
    elif(len(player.board)<5 and type(player.hand[nb])==Monstre):
        player.board.append(player.hand[nb])
        player.hand.pop(nb)
        effected(game,player.board[len(player.board)-1])

        
    
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
        joueur.defause.append(joueur.board[nbmonstre])
        joueur.board.pop(nbmonstre)

def ecran(game):
    print("\n")
    print(game.player2.name,"\n"+str(game.player2.HP),"\nmain 2: ",end="")
    for i in game.player2.hand:
        printColorName(i)
    print("\n\nboard 2: ",end="")
    for i in game.player2.board:
        printColorName(i)
    print("\n\nboard 1: ",end="")
    for i in game.player1.board:
        printColorName(i)   
    print("\n\nmain 1: ",end="")
    for i in game.player1.hand:
        printColorName(i)
    print("\n"+str(game.player1.HP))
    print(game.player1.name)
    
def turn(game):
    a=""
    player=game.getMain(game)
    adv=game.getAdv(game)
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
            print("numeros de la carte :")
            e=int(input())
            if e<len(b) and e>=0:
                b[e].printi()
        elif a=="exit":
            return -1
    game.switchTurn(game)
    return 1

def printColorName(card):
    if type(card)==Monstre:
        print(Fore.YELLOW + Style.DIM + card.name,end="")
    elif type(card)==Magie:
        print(Fore.CYAN + Style.DIM + card.name,end="")
    print("",end=" | ")


def effected(game,card):
    player=game.getMain(game)
    if card.effectInt==['']:
        return
    effe=card.effectInt
    while effe!=[]:
        effect(game,card,player,effe)


def effect(game,card,player,effe):
    if effe[0]=="HEAL":
        player.HP+=expression(effe[1],game,card)
        popi(effe,2)
    elif effe[0]=="HEAL*":
        player.HP+=expression(effe[1],game,card)*expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="DRAW":
        draw(game.getMain(game,card),expression(effe[1],game),card)
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
    elif effe[0]=="CHOOSE":
        pass
    elif effe[0]=="DAMAGE":
        game.getAdv(game).HP-=expression(effe[1],game,card)
        popi(effe,2)
    elif effe[0]=="DAMAGE*":
        game.getAdv(game).HP-=expression(effe[1],game,card)*expression(effe[2],game,card)
        popi(effe,3)
    elif effe[0]=="DESTROY":
        cible=expression(effe[1],game,card)
        pass
    elif effe[0]=="DISCARD":
        pass
    elif effe[0]=="DIVIDEA":
        cible=expression(effe[1],game,card)
        cible.attack/=2
        popi(effe,2)
    elif effe[0]=="DIVIDED":
        cible=expression(effe[1],game,card)
        cible.defence/=2
        popi(effe,2)
    elif effe[0]=="SUMMON":
        pass
    elif effe[0]=="IF":
        pass
    return effe

def chooser(tab):
    print("Selectionner la carte :")
    for i in range(len(tab)):
        print(i+1,":",i.name,end=" | ")
    print("Numeros de la carte choisis : ",end="")
    c=input()
    while c<"0" or c>=str(len(tab)):
        print("Chiffre invalide veuillez resaisir un chiffre :")
        c=input()
    return tab[int(c)]


def popi(effe,nb=1):
    for i in range(nb):
        effe.pop(0)

def expression(coucou,game,card):
    if coucou.isdigit():
        return int(coucou)
    if coucou == "allie":
        return game.getMain(game)
    if coucou == "ennemie":
        return game.getAdv(game)
    if coucou == "him":
        return card
    if '.' in coucou:
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
            tmp.pop(0)
        return a
    
        
                


#game.player1.hand.append(deckList[22])
#game.player2.board.append(deckList[0])
game.player1.deck=shuffle(deckList)
game.player2.deck=shuffle(deckList)
start(game)


while game.player1.HP>0 and game.player2.HP>0:
    if(turn(game)==-1):
        break
