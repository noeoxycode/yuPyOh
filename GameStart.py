#boucle pour la partie, tant que gameOver est false
def gameStart(game):
    Bool gameOver = false;
    while(!gameOver):
        turn(game);
        gameOver = checkEndGame();


#check les conditions de fin de partie, false si conditions non remplies, true si elles sont remplies
def checkEndGame():
    if(player1.hp <= 0 || player2.hp <= 0):
        return true
    else
        return false