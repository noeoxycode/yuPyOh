def turn(game):
    la propriete turn est de 1 ou -1 pour savoir à qui est le tour
    if(game.turn == 1):
        currentPlayer = game.player1
        opponent = game.player2
    else:currentPlayer = game.player2
        opponent = game.player1
    addCard(currentPlayer)
    chooseAction()

    if(turn == 1):
        game.player1 = currentPlayer
        game.player2 = opponent
    else:game.player2 = currentPlayer
        game.player1 = opponent
    game.turn = game.turn * -1

#prend la carte du dessus du deck et l'ajoute à la main du joueur
def addCard(player):
    return player

#propose toutes les actions possibles au joueur
def chooseAction():
