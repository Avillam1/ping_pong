from pygame import *
from random import randint

init()
SW, SH = 800, 600
FPS = 60
window = display.set_mode((SW, SH))
display.set_caption('Batalla de Paletas Flipantes')

BACKGROUND = "background.png"
PLAYER1 = "player1.png"
PLAYER2 = "player2.png"
BOLA_IMG = "bola.png"
VICTORY_PLAYER1 = "victoryplayer1.png"
VICTORY_PLAYER2 = "victoryplayer2.png"

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_player1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SH - self.rect.height:
            self.rect.y += self.speed

    def update_player2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < SH - self.rect.height:
            self.rect.y += self.speed

def random_sign():
    return 1 if randint(0, 1) == 1 else -1

player1 = Player(PLAYER1, 30, SH//2 - 70, 20, 150, 10)
player2 = Player(PLAYER2, SW - 80, SH//2 - 70, 20, 150, 10)
bola = GameSprite(BOLA_IMG, SW//2, SH//2, 50, 50)

speed_x = 7 * random_sign()
speed_y = 7 * random_sign()
score_player1 = 0
score_player2 = 0

font.init()
game_font = font.SysFont('Arial', 50)
clock = time.Clock()
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        player1.update_player1()
        player2.update_player2()

        bola.rect.x += int(speed_x)
        bola.rect.y += int(speed_y)

        if bola.rect.y >= SH - bola.rect.height or bola.rect.y <= 0:
            speed_y *= -1

        if sprite.collide_rect(player1, bola) or sprite.collide_rect(player2, bola):
            speed_x *= -1  

        if bola.rect.x <= 0:
            score_player2 += 1
            bola.rect.center = (SW//2, SH//2)
            speed_x = 7 * random_sign()
            speed_y = 7 * random_sign()

        if bola.rect.x >= SW - bola.rect.width:
            score_player1 += 1
            bola.rect.center = (SW//2, SH//2)
            speed_x = 7 * random_sign()
            speed_y = 7 * random_sign()

        window.blit(transform.scale(image.load(BACKGROUND), (SW, SH)), (0, 0))
        player1.reset()
        player2.reset()
        bola.reset()
        
        score_player1_text = game_font.render(str(score_player1), True, (255, 255, 255))
        score_player2_text = game_font.render(str(score_player2), True, (255, 255, 255))

        score_player1_rect = score_player1_text.get_rect(center=(SW // 4, 20))
        score_player2_rect = score_player2_text.get_rect(center=(SW * 3 // 4, 20))

        window.blit(score_player1_text, score_player1_rect)
        window.blit(score_player2_text, score_player2_rect)


        if score_player1 >= 5:
            window.blit(transform.scale(image.load(VICTORY_PLAYER1), (SW, SH)), (0, 0))
            finish = True
        elif score_player2 >= 5:
            window.blit(transform.scale(image.load(VICTORY_PLAYER2), (SW, SH)), (0, 0))
            finish = True

    display.update()
    clock.tick(FPS)

quit()
