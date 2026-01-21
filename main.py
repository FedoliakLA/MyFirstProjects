from pygame import *
from random import randint
import time as timer

dx = 1366
dy = 768
window = display.set_mode((dx, dy))
display.set_caption("Полювання.")

background = transform.scale(
    image.load("Forest.jpg"), (dx, dy)
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


lost = 0
score = 0
Ammo = 5
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
        self.a = randint(1, 2)
        self.save = transform.scale(image.load(player_image), (w, h))
        self.save_s = player_speed

    def update(self):
        global lost
        global score
        if self.rect.y < (dy - 100):
            self.rect.y += self.speed * self.a
            roll = randint(0, 100)
            if roll == 1 and self.rect.x < (dx - self.w):
                self.rect.x += self.speed * 30
            if roll == 0 and self.rect.x > 0:
                self.rect.x -= self.speed * 30
            if sprite.spritecollide(self, Bullets, True):
                self.rect.y = 0
                self.rect.x = randint(0, (dx - 100))
                self.image = self.save
                self.speed = self.save_s
                score += 1
                return score
        else:
            self.rect.y = 0
            self.rect.x = randint(0, (dx - 100))
            self.image = self.save
            self.speed = self.save_s
            lost += 1
            print(lost)
            egg = randint(0, 10)
            if egg == 0:
                self.image = transform.scale(image.load("Shark.png"), (700, 700))
                self.speed = 12
                self.rect.x = (dx / 2 - 350)
                print("Акула в лісі!?")
            return lost


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < dx - self.w:
            self.rect.x += self.speed

    def fire(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            bullet = Bullet("Bullet.bmp", self.rect.centerx, self.rect.top, -15, 10, 20)
            Bullets.add(bullet)
            global Ammo
            Ammo -= 1
            fire_sound.play()

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)

    def update(self):
        if self.rect.y > 0:
            self.rect.y += self.speed
        else:
            self.kill()


Hunter = Player("Hunter.bmp", dx/2, (dy-(dy * 0.13)), 10, (dx * 0.13), (dy * 0.13))

w_butt = 494
h_butt = 212
Play = GameSprite("Play.png", (dx / 2) - (w_butt / 2), (dy / 2) - (h_butt / 2), 0, w_butt, h_butt)
Stop = GameSprite("Stop.png", (dx - (w_butt / 2)), (dy - (h_butt / 2)), 0, w_butt / 2, h_butt / 2)

Enema = Enemy("Vepr.png", randint(0, (dx - 100)), randint(0, 20), 1, 100, 100)
Enema_1 = Enemy("Vepr.png", randint(0, (dx - 100)), randint(0, 20), 1, 100, 100)
Enema_2 = Enemy("Vepr.png", randint(0, (dx - 100)), randint(0, 20), 1, 100, 100)
Enema_3 = Enemy("Tiger.png", randint(0, (dx - 100)), randint(0, 20), 1.5, 150, 150)
Enema_4 = Enemy("Tiger.png", randint(0, (dx - 100)), randint(0, 20), 1.5, 150, 150)

Animals = sprite.Group()

Animals.add(Enema)
Animals.add(Enema_1)
Animals.add(Enema_2)
Animals.add(Enema_3)
Animals.add(Enema_4)

Bullets = sprite.Group()

global Life
Life = 3

game = True
Finish = False
screen = False
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont('Arial', 32)
font2 = font.SysFont('Arial', 148)
font2.set_bold(True)


text_lost = font1.render(
    "Пропущено: " + str(lost), 1, (255, 255, 255)
)

text_score = font1.render(
    "Збито: " + str(score), 1, (255, 255, 255)
)

text_health = font1.render(
    "Життя: " + str(Life), 1, (0, 127, 0)
)

text_ammo = font1.render(
    "Набої: " + str(Ammo), 1, (255, 128, 75)
)

text_lose = font2.render(
    "Поразка!", 1, (255, 0, 0)
)

text_win = font2.render(
    "Перемога!", 1, (0, 255, 0)
)

mixer.init()
mixer.music.load("Back.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

start_time = timer.time()
reload_time = timer.time()
reload = False

fire_sound = mixer.Sound('gun.mp3')
reload_sound = mixer.Sound('Reload.ogg')

while game:
    clock.tick(FPS)
    if not screen:
        mixer.music.pause()
        window.blit(background, (0, 0))
        Play.reset()
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if Play.rect.collidepoint(x, y):
                    screen = True
    if screen:
        mixer.music.unpause()
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == MOUSEBUTTONDOWN:
                x, y = e.pos
                if Stop.rect.collidepoint(x, y):
                    screen = False

        if not Finish:
            window.blit(background, (0, 0))
            Stop.reset()
            Hunter.reset()
            Hunter.update()
            if timer.time() - start_time > 0.2 and Ammo > 0:
                Hunter.fire()
                start_time = timer.time()

            if Ammo <= 0 and reload == False:
                reload_sound.play()
                reload_time = timer.time()
                reload = True
            if timer.time() - reload_time >= 3 and reload == True:
                Ammo = 5
                reload = False



            Animals.draw(window)
            Animals.update()
            Bullets.draw(window)
            Bullets.update()

            text_lost = font1.render(
                "Пропущено: " + str(lost), 1, (255, 0, 255)
            )
            text_score = font1.render(
                "Збито: " + str(score), 1, (255, 0, 255)
            )
            text_health = font1.render(
                "Життя: " + str(Life), 1, (255, 0, 255)
            )
            text_ammo = font1.render(
                "Набої: " + str(Ammo), 1, (255, 220, 0)
            )
            window.blit(text_lost, (dx / 12, dy / 9))
            window.blit(text_score, (dx / 12, (dy / 9) + 25))
            window.blit(text_health, (dx / 12, (dy / 9) + 50))
            window.blit(text_ammo, (dx / 12, (dy / 9) + 75))
            if lost == 10:
                lost = 0
                Life -= 1
            if Life == 0:
                window.blit(text_lose, (dx / 3, dy / 3))
                Finish = True
            if score == 25:
                window.blit(text_win, (dx / 3, dy / 3))
                Finish = True

    display.update()