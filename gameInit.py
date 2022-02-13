#préparation de la partie
def gameInit():
    game.player1 = createPlayer()
    game.player2 = createPlayer()
    gameStart(game)

#fonction qui crée un objet player, demande le nom du joueur et lui fais choisir son deck
def createPlayer():
    player.nom = nomdemandé
    player.deck = mixDeck(getDEck(player.deck))
    #mélange le deck et retourne un tab avec [0] le deck moins la main et [1] la main
    handAndDeck = getHand(player.deck)
    player.deck = deckAndHand[0]
    player.hand = deckAndHand[1]
    return player

#fonction montrant au joueur tous les decks dispo et lui fais choisir, puis le retourne
def getDeck():
    CHOIX DECK
    return deck

#mélange le deck et retourne un tab avec [0] le deck moins la main et [1] la main (5 cartes)
def getHand(deck):
    deck = mixDeck(deck)
    prend les 5 premières cartes du joueur et les met dans la main du joueur
    return [deck, hand]

#mélange le deck et le retourne
def mixDeck(deck):

    return deck