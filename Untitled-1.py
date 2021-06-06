from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, dx, dy):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.dx = dx
        self.dy = dy
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if self.rect.x >= 700 or self.rect.x <= 0:
            self.rect.x += dx 
        if self.rect.y <= 0 or self.rect.y >= 500:
            self.rect.y += dy
class Enemy(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x >= 0:
            self.rect.x -= self.dy
        if keys[K_DOWN] and self.rect.x <= 500:
            self.rect.x += self.dy

dy = 5
dx = 5
font.init()
font1 = font.Font(None, 80)
win1 = font1.render('PLAYER 1 WIN!', True, (255, 255, 255))
win2 = font1.render('PLAYER 2 WIN', True, (255, 255, 255))
win_width = 700
win_height = 500
green = (0, 188, 0)
wind = display.set_mode((win_width, win_height))
ball = Player('мячик.png', 300, 250, 20, 20, dx, dy)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if game:
        wind.fill(green)
        ball.reset()
        ball.update()
    display.update()
