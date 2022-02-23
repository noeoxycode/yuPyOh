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