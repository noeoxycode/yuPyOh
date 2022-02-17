from Player import Player
import random
# Faire choisir le deck pour les deux joueurs / mélanger
# Attribuer le deck choisi au joueur
# Mélanger le deck
# Piocher les 5 cartes du dessus //
# Les cartes piocher doivent ne plus être dans le deck

class Game:

    def __init__(self, name1="Yugi", name2="Kaiba"):
        self.player1 = Player(name1)
        self.player2 = Player(name2)
        self.turn = 1
        self.current_player = 1
        self.game_over = False

        print(f'{self.player1.name} starting the game')

    def get_current_player(self):
        return self.player1 if self.current_player == 1 else self.player2

    def end_player_turn(self):
        if self.current_player == 1:
            self.current_player = 2
            print(f'Switching to {self.player2.name}')
        else:
            print(
                f'End of turn {self.turn}. {self.player1.name} {self.player1.HP} HP / {self.player2.name} {self.player2.HP} HP\n')
            self.turn += 1
            self.current_player = 1
            print(f'{self.player1.name} starting turn {self.turn}')

    def get_other_player(self):
        return self.player2 if self.current_player == 1 else self.player1

    def player_did_lose(self):
        return self.player1.HP == 0 or self.player2.HP == 0

    # boucle pour la partie, tant que gameOver est false
    def fight(self):

        while not self.player_did_lose():

            # action current player (Example
            if random.randint(0, 10) > 4:
                self.player1.HP -= 1000
            else:
                self.player2.HP -= 1000

            # end turn player
            self.end_player_turn()
