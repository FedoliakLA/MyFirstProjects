from pygame import *
from random import randint
dx = 1366
dy = 768
window = display.set_mode((dx, dy))
display.set_caption("Отримай лист!")

background = transform.scale(
    image.load("ground.png"), (dx,dy)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.h = h
        self.w = w
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
    def Update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < dy - self.h:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < dx - self.w:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
        self.a = randint(0,1)
    def Update(self):
        if self.a == 0:
            self.rect.x += self.speed
        if self.a == 1:
            self.rect.x -= self.speed

stina_color = (200, 120, 0)
class Stina(sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#386 638
Chad = Player("Remake.png", 386, 638, 10, 100, 100)
Prize = GameSprite("Prize.png", 850, 100, 10, 100, 100)
Enem = Enemy("Remake2.png", 146, 116, 6, 100, 100)
w_1 = Stina(stina_color, 55, 63, 69, 599)
w_2 = Stina(stina_color, 505, 250, 90, 483)
w_3 = Stina(stina_color, 306, 489, 934, 58)
w_4 = Stina(stina_color, 55, 270, 318, 60)
w_5 = Stina(stina_color, 55, 50, 1304, 44)
w_6 = Stina(stina_color, 733, 52, 102, 298)
w_7 = Stina(stina_color, 1240, 50, 112, 704)
w_8 = Stina(stina_color, 822, 245, 270,  105)
game = True
Finish = False
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("music.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

font.init()
win_font = font.Font(None, 180)
win_text = win_font.render(
    "Лист отримано!", True, (0, 255, 251)
)
lose_font = font.Font(None, 240)
lose_text = lose_font.render(
    "Поразка!", True, (255, 0, 0)
)
while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            print(e.pos)
    if not Finish:
        window.blit(background, (0, 0))
        Chad.reset()
        Chad.Update()

        Prize.reset()

        w_1.reset()
        w_2.reset()
        w_3.reset()
        w_4.reset()
        w_5.reset()
        w_6.reset()
        w_7.reset()
        w_8.reset()

        Enem.reset()
        if sprite.collide_rect(Enem, w_1):
            Enem.a = 0
        if sprite.collide_rect(Enem, w_7):
            Enem.a = 1
        Enem.Update()
        if sprite.collide_rect(Chad, Prize):
            window.blit(win_text, (300,300))
            Finish = True
            win = mixer
            win.music.load("win.mp3")
            win.music.set_volume(2)
            win.music.play()

        if sprite.collide_rect(Chad, Enem):
            window.blit(lose_text, (300,300))
            Finish = True
            lose = mixer
            lose.music.load("lose.mp3")
            lose.music.play()
        if sprite.collide_rect(Chad, w_1) or sprite.collide_rect(Chad, w_2) or sprite.collide_rect(Chad, w_3) or sprite.collide_rect(Chad, w_4) or sprite.collide_rect(Chad, w_5) or sprite.collide_rect(Chad, w_6) or sprite.collide_rect(Chad, w_7) or sprite.collide_rect(Chad, w_8):
            window.blit(lose_text, (300,300))
            lose = mixer
            lose.music.load("lose.mp3")
            lose.music.play()
            Finish = True

    display.update()