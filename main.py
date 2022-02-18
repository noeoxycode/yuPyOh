from Game import Game

if __name__ == '__main__':

    name_p1 = input('Player 1 name: ')
    name_p2 = input('Player 2 name: ')

    game = Game(name1=name_p1, name2=name_p2)

    game.fight()

