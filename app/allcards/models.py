import os

class AllCards:

    def AllCardsReturn(self):

        cardsIMG = "./app/static/cards"
        cardsImage = os.listdir(cardsIMG)
        print(cardsImage)

        return cardsImage
