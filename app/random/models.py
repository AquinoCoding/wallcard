import os
import random

class randomAction:

    def randomize(self):

        cardsIMG = "./app/static/cards"
        imagem = os.listdir(cardsIMG)
        print(imagem)
        
        carta1 = imagem[random.randint(0,(len(imagem)-1))]
        carta2 = imagem[random.randint(0,(len(imagem)-1))]
        carta3 = imagem[random.randint(0,(len(imagem)-1))]

        cartas = [carta1, carta2, carta3]

        # Pra cada carta se a carta tiver na lista random carta
        cartas = set(cartas)
        cartas = [x for x in cartas]

        while True:
            if len(cartas) < 3 or len(cartas) < 2:
                newCard = imagem[random.randint(0,(len(imagem)-1))]
                if newCard not in cartas:
                    cartas.append(newCard)
                    break
                
            elif len(cartas) == 3:
                break

        return cartas


        

        
