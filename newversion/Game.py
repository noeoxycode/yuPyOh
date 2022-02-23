from Player import Player
class Game:
    turn=1
    nbTurn=1
    player1=Player("Yugi")
    player2=Player("Kaiba")
    nbSummon=0
    target=""
    def __init__(self, name1="Yugi",name2="Kaiba"):
        self.player1=Player(name1)
        self.player2=Player(name2)

    def endTurn(self):
        self.nbSummon=0
        self.target=""
        self.nbTurn+=1
        for i in self.player1.board:
            i.canAttack=True
        for i in self.player2.board:
            i.canAttack=True
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