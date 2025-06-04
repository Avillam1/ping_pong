from pygame import *
from random import randint

init()
BACKGROUND = 
PLAYER1 = 
PLAYER2 = 
FPS = 60
VICTORY = 
DERROTA = 
SW, SH = 800, 600
init()


window = display.set_mode((SW, SH))
display.set_caption('Los chavalines contra las flipantes aventuras del cohete flipante')

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, cor_x, cor_y, ancho, alto, speed=0):
        super().__init__()
        self.width = ancho
        self.heigh = alto
        self.image = transform.scale(image.load(img), (self.width, self.heigh))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

clock = time.Clock()
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)

quit()
