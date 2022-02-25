import utility,data
from Monstre import Monstre
from Magie import Magie
from colorama import Fore
def effected(game,card):
    player=game.getMain(game)
    effe=[]
    if card.effectInt==['']:
        return
    effe=card.effectInt.split(" ")
    while effe!=[]and effe!=['']:
        if effect(game,card,player,effe)==-1:
            print(Fore.RED+"Condition impossible à remplir !")
            return -1
    game.target=""
    return 0


def effect(game,card,player,effe):
    if effe[0]=="HEAL":
        player.HP+=expression(effe[1],game,card)
        utility.popi(effe,2)
    elif effe[0]=="HEAL*":
        player.HP+=expression(effe[1],game,card)*expression(effe[2],game,card)
        utility.popi(effe,3)
    elif effe[0]=="DRAW":
        game.target=utility.draw(game.getMain(game),expression(effe[1],game,card))
        utility.popi(effe,2)
    elif effe[0]=="BOOSTA":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)
        utility.popi(effe,3)
    elif effe[0]=="BOOSTA*":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)*expression(effe[3],game,card)
        utility.popi(effe,4)
    elif effe[0]=="BOOSTD":
        cible=expression(effe[1],game,card)
        cible.defence+=expression(effe[2],game,card)
        utility.popi(effe,3)
    elif effe[0]=="BOOSTD*":
        cible=expression(effe[1],game,card)
        cible.defence+=expression(effe[2],game,card)*expression(effe[3],game,card)
        utility.popi(effe,4)
    elif effe[0]=="BOOSTL":
        cible=expression(effe[1],game,card)
        cible.attack+=expression(effe[2],game,card)
        utility.popi(effe,3)
    elif effe[0]=="MINUSA":
        cible=expression(effe[1],game,card)
        cible.attack-=expression(effe[2],game,card)
        if cible.attack<0:cible.attack=0
        utility.popi(effe,3)
    elif effe[0]=="MINUSA*":
        cible=expression(effe[1],game,card)
        cible.attack-=expression(effe[2],game,card)*expression(effe[3],game,card)
        if cible.attack<0:cible.attack=0
        utility.popi(effe,4)
    elif effe[0]=="MINUSD":
        cible=expression(effe[1],game,card)
        cible.defence-=expression(effe[2],game,card)
        if cible.defence<0:cible.defence=0
        utility.popi(effe,3)
    elif effe[0]=="MINUSD*":
        cible=expression(effe[1],game,card)
        cible.defence-=expression(effe[2],game,card)*expression(effe[3],game,card)
        if cible.defence<0:cible.defence=0
        utility.popi(effe,4)
    elif effe[0]=="CHOOSE":
        c=utility.chooser(expression(effe[1],game,card))
        if c==-1:
            return c
        else:
            game.target=c
        utility.popi(effe,2)
    elif effe[0]=="DAMAGE":
        game.getAdv(game).HP-=expression(effe[1],game,card)
        utility.popi(effe,2)
    elif effe[0]=="DAMAGE*":
        game.getAdv(game).HP-=expression(effe[1],game,card)*expression(effe[2],game,card)
        utility.popi(effe,3)
    elif effe[0]=="DESTROY":
        cible=expression(effe[1],game,card)
        if type(cible)!=type([]):
            pos=utility.findNumber(utility.findHolder(game,cible).board,cible)
            utility.destroy(game,utility.findHolder(game,cible),pos)
        else:
            while cible!=[]:
                utility.destroy(game,utility.findHolder(game,cible[0]),0)
        utility.popi(effe,2)
    elif effe[0]=="RESTORE":
        cible = expression(effe[1],game,card)
        pos = utility.findNumber(game.getMain(game).defause,card)
        game.getMain(game).hand.append(game.getMain(game).defause[pos])
        game.getMain(game).defause.pop(pos)
        utility.popi(effe,2)
    elif effe[0]=="DIVIDEA":
        cible=expression(effe[1],game,card)
        cible.attack/=2
        utility.popi(effe,2)
    elif effe[0]=="DIVIDED":
        cible=expression(effe[1],game,card)
        cible.defence/=2
        utility.popi(effe,2)
    elif effe[0]=="SUMMON":
        cible=expression(effe[1],game,card)
        pos=utility.findNumber(game.getMain(game).hand,cible)
        utility.summon(game,pos)
        utility.popi(effe,2)
    elif effe[0]=="IF":
        condition=expression(effe[1],game,card)
        if condition :
            copy=effe[2].split("$")
            while(copy!=[]):
                copy=effect(game,card,game.getMain(game),copy)
        utility.popi(effe,3)
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
        utility.popi(effe,4)
    elif effe[0]=="ATTACK":
        ally=utility.findNumber(game.getMain(game).board,expression(effe[1],game,card))
        ennemie=expression(effe[2],game,card)
        if type(ennemie)==type([]):
            for i in range(len(ennemie)):
                pos=utility.findNumber(game.getAdv(game).board,ennemie[len(ennemie)-i-1])
                utility.attack(game,ally,pos)
        else:
            pos=utility.findNumber(game.getAdv(game).board,ennemie)
            utility.attack(game,ally,pos)
        utility.popi(effe,3)
    return effe

def expression(coucou,game,card):
    if coucou.isdigit():
        return int(coucou)
    elif coucou == "allie":
        return game.getMain(game)
    elif coucou in data.typeList():
        return coucou
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
            elif tmp[0] in data.typeList():
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