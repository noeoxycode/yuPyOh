from Magie import Magie
from Monstre import Monstre
from Game import Game
import utility,data
def sauvegarde(game,name):
    file=open("save.csv","a")
    file.write(".azertyuiop.\n")
    file.write(name+"\n")
    file.write(".!.\n")
    file.write(str(game.turn)+";"+str(game.nbTurn)+"\n")
    file.write(game.player1.name+";"+str(game.player1.HP)+";"+game.player2.name+";"+str(game.player2.HP)+"\n")
    file.write(".!.\n")    
    cardWrite(file,game.player1.deck)
    cardWrite(file,game.player1.hand)
    cardWrite(file,game.player1.board)
    cardWrite(file,game.player1.defause)
    cardWrite(file,game.player2.deck)
    cardWrite(file,game.player2.hand)
    cardWrite(file,game.player2.board)
    cardWrite(file,game.player2.defause)
    file.close()
    addSaveName(name)

def addSaveName(name):
    with open("decklist.txt") as file:
        contenu=file.read()
    contenu=contenu.split(".&.")
    if ">.>" in contenu[0]:
        contenu[0]=contenu[0].split(">.>")
    contenu[0].append(name)
    file=open("decklist.txt","w")
    for i in contenu[0]:
        if i!= contenu[0][0]:
            file.write(">.>")
        file.write(i)
    file.write(".&.")
    file.write(contenu[1])
    file.close()

def cardWrite(file,zone):
    for i in zone:
        if type(i)==Magie:
                file.write("Magie;"+i.name+";"+i.effect+";"+i.effectInt+"\n")
        elif type(i)==Monstre:
            file.write("Monstre;"+i.name+";"+str(i.attack)+";"+str(i.defence)+";"+str(i.level)+";"+str(i.bAttack)+";"+str(i.bDefence)+";"+str(i.bLevel)+";"+i.types)
            if i.effect!="":
                file.write(";"+i.effect+";"+i.effectInt)
            file.write("\n")
    file.write(".!.\n")

def load(name):
    save=0
    with open("save.csv") as file:
        contenu=file.read()
    contenu=contenu.split(".azertyuiop.\n")
    for i in range(len(contenu)):
        contenu[i]=contenu[i].split(".!.\n")
    for i in contenu:
        if i[0]==name+"\n":
            save=i[1:]
    for i in range(len(save)):
        save[i]=save[i].split("\n")
    for i in range(len(save)):
        for j in range(len(save[i])):
            save[i][j]=save[i][j].split(";")
    game=Game
    game.turn=int(save[0][0][0])
    game.nbTurn=int(save[0][0][1])
    game.player1.name=save[0][1][0]
    game.player1.HP=int(save[0][1][1])
    game.player2.name=save[0][1][2]
    game.player2.HP=int(save[0][1][3])
    utility.popi(save)
    loadPLayer(game.player1,save)
    loadPLayer(game.player2,save)
    return game

def loadPLayer(player,contenu):
    loadCard(player.deck,contenu[0])
    loadCard(player.hand,contenu[1])
    loadCard(player.board,contenu[2])
    loadCard(player.defause,contenu[3])
    utility.popi(contenu,4)

def loadCard(tab,contenu):
    if contenu!=[]:
        for i in contenu:
            if i[0]=="Magie":
                tab.append(Magie(i[1:]))
            elif i[0]=="Monstre":
                tab.append(Monstre(i[1:]))

def loadSave():
    print("Sauvegarde disponible :")
    contenu=data.saveList()
    for i in range(len(contenu)):
        print(i+1," : ",contenu[i])
    num='0'
    while num>str(len(contenu)) or num<=str(0):
        num=input("Choix :")
    return contenu[int(num)-1]
    
