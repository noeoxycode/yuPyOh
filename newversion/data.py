def typeList():
    return ["Guerrier","Bete","Magicien","Feu","Air","Eau","Terre","Lumiere","Nature","Acier"]
def deckList():
    return["Heros","Elementaire"]
def saveList():
    with open("decklist.txt") as file:
        contenu=file.read()
    contenu=contenu.split(".&.")
    if ">.>" in contenu[0]:
        contenu=contenu[0].split(">.>")
    else:
        contenu=[contenu[0]]
    return contenu
        
