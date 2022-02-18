class Player:

    def __init__(self, name: str, HP: int = 8000):
        self.name = name
        self.HP = HP
        self.hand = []
        self.deck = []
        self.board = []
        self.discard = []


