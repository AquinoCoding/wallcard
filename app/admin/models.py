from PIL import Image

class CutPhoto:
    
    def cutSize(self):

        imga = 'horse.png'
        img = Image.open(f"{imga}")

        area = (220, 220, 380, 380)
        cropped_img = img.crop(area)
        cropped_img.save(f'{imga}')