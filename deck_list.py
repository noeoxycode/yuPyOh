class Magie:
    name = ""
    effect = ""
    effectInt = ""

    def __init__(self, name, effect, effectInt=""):
        self.name = name
        self.effect = effect
        self.effectInt = effectInt

    def __str__(self):
        return f'Nom : {self.name}' + f'\nEffet : {self.effect}'






magie = Magie("Nono", "Tornade")

print(magie)

#     def printi(self):
#         print("Nom :", self.name)
#         print("Effet :", self.effect)
#
#
# deckList = []
# deckList.append(Monstre("Avian", 1000, 1000, 3, "Guerrier"))
# deckList.append(Monstre("Clayman", 800, 2000, 3, "Guerrier"))
# deckList.append(Monstre("Burstinatrix", 1300, 800, 3, "Guerrier",
#                         "Choisi un monstre ennemie, si sa DEF est inférieur à l'ATK de ce monstre, le détruit",
#                         "CHOOSE ennemie IF cible.DEF < him.ATK DESTROY cible"))
# deckList.append(Monstre("Bubbleman", 800, 1200, 3, "Guerrier"))
# deckList.append(
#     Monstre("Flipper", 900, 1400, 3, "Bete", "Choisie un monstre de votre main et l'invoque si c'est possible",
#             "CHOOSE hand SUMMON cible"))
# deckList.append(Monstre("Colibri", 800, 1000, 3, "Bete",
#                         "Choisi un monstre que vous controlez, vous vous soignez de 200 x son niveau",
#                         "CHOOSE allie  SOIN* 200 allie.niveau"))
# deckList.append(Monstre("Panthere noir", 1300, 1500, 4, "Bete"))
# deckList.append(Monstre("Topitaupe", 1400, 1000, 4, "Bete"))
# deckList.append(Monstre("Sparkman", 1600, 1200, 4, "Guerrier"))
# deckList.append(Monstre("Nécrombre", 1500, 1200, 4, "Guerrier"))
# deckList.append(Monstre("Airman", 1800, 1000, 4, "Guerrier", "Donne 300 DEF à un monstre allié",
#                         "CHOOSE allie BOOST allie.DEF 300"))
# deckList.append(Monstre("Capitaine dorée", 1800, 1000, 4, "Guerrier", "Pioche une carte", "DRAW 1"))
# deckList.append(Monstre("Blazeman", 1600, 1600, 4, "Guerrier"))
# deckList.append(Monstre("Ocean", 1500, 1700, 4, "Guerrier"))
# deckList.append(Monstre("Tranchant", 2200, 2000, 6, "Guerrier"))
# deckList.append(Monstre("Géant du tonnerre", 2400, 2200, 6, "Guerrier"))
# deckList.append(
#     Monstre("Homme-Oiseau de feu", 2100, 1800, 6, "Guerrier", "Choisi un monstre ennemie, gagne sa DEF en ATK",
#             "CHOOSE ennemie BOOST him.ATK cible.DEF"))
# deckList.append(Monstre("Néos", 2500, 2200, 7, "Guerrier"))
# deckList.append(Monstre("Chevalier Néos", 2700, 2300, 7, "Guerrier", "Choisi un monstre ennemie, divise son ATK par 2",
#                         "CHOOSE ennemie DIVIDE ennemie.ATK 2"))
# deckList.append(Monstre("Homme-Oiseau à l'éclat lumineux", 2500, 2500, 8, "Guerrier",
#                         "Quant il est invoqué, gagne 200 ATK par monstre Guerrier dans votre cimetière",
#                         "BOOST* him.ATK 200 cimetiere.guerrier"))
# deckList.append(Magie("Signal du héro", "Choisisez un monstre guerrier que vous controlez, il gagne 500 ATK",
#                       "CHOOSE allie BOOST allie.ATK 500"))
# deckList.append(Magie("Appel d'urgence", "Pioche 1 carte si c'est un monstre guerrier pioche une carte de plus",
#                       "DRAW 1 IF him = guerrier DRAW 1"))
# deckList.append(Magie("Soin de la justice", "Vous soigne de 200 x nombre de carte dans la main", "SOIN* 200 hand.nb"))
# deckList.append(Magie("Ravage de foudre", "Si vous controler \"Géant du tonnerre\", détruit un monstre ennemie",
#                       "IF \"Géant du tonnerre\" CHOOSE ennemie DESTROY cible"))
# deckList.append(Magie("Dernier espoir",
#                       "Détruit tous vos monstres et infliger 400 point de dégat à votre adversaire par monstre détruit",
#                       "DESTROY bord DAMAGE* nb 400"))
# deckList.append(Magie("Reigne animal", "Toutes vos betes gagne 1 niveau, 400 ATK et DEF",
#                       "ALL bete BOOST cible.ATK 400 BOOST cible.DEF 400 BOOST cible.lvl 1"))
# deckList.append(Magie("Prison héroique",
#                       "Choisisez un monstre guerrier que vous controlez, un monstre ennemie pert un montant d'ATK égal à 100 x le niveau de votre monstre",
#                       "CHOOSE allie CHOOSE ennemie MINUS* ennemie.ATK 100 allie.lvl"))
# deckList.append(Magie("Super blocage", "Choisisez un monstre guerrier que vous controlez, il gagne 800 DEF",
#                       "CHOOSE allie.guerrier BOOST him.DEF 800"))
# deckList.append(Magie("Rappel de secours", "Choisisez un monstre guerrier que vous cimetière, l'ajoute à votre main",
#                       "CHOOSE cimetiere.guerrier TO hand"))
# deckList.append(Magie("Destruction de Néos",
#                       "Choisisez un \"Néos\" que vous controlez, il gagne 500 ATK, attaque tous les monstre ennemis, puis le détruit",
#                       "CHOOSE allie.\"Néos\" BOOST him.ATK 500 ATTACK ennemie.all DESTROY him"))
