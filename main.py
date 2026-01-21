import pygame
from random import randint

dx = 1366
dy = 768

window = pygame.display.set_mode((dx, dy))
pygame.display.set_caption("Меню")

bg_list = ["main_menu.png", "bedroom.png", "corridor.png", "cupboard.png", "painting.png", 'mirror.png']

background = pygame.transform.scale(
    pygame.image.load(bg_list[0]), (dx, dy)
)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.h = h
        self.w = w

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


w_butt = dx * 1 / 8
h_butt = dy * 1 / 8

w_door = dx / 6
h_door = dy / 1.63

w_butt_2 = dx / 1
h_butt_2 = dy / 15

bt_start = GameSprite("bt_start.png", (dx / 2) - w_butt, (dy / 2) - h_butt, 0, w_butt*2, h_butt*2)
bt_pause = GameSprite("bt_pause.png", dx - w_butt, dy - h_butt, 0, w_butt, h_butt)
bt_resume = GameSprite("bt_resume.png", (dx / 2) - w_butt, (dy / 2) - h_butt, 0, w_butt*2, h_butt*2)
bt_exit = GameSprite("bt_exit.png", dx - w_butt, dy - h_butt, 0, w_butt, h_butt)
bt_back = GameSprite("bt_back.png", dx - w_butt_2, dy - h_butt_2, 0, w_butt_2 - w_butt, h_butt_2)

door_1 = GameSprite("door.png", (dx / 2.5) - w_door, (dy / 1.26) - h_door, 0, w_door, h_door)
door_2 = GameSprite("door_2.png", (dx / 1.88) - w_door, (dy / 1.2) - h_door, 0, w_door*1.46, h_door*0.93)

LP = "lupa.png"
bt_drawer = GameSprite(LP, dx * 0.62, dy * 0.6, 0, dx / 12, dy / 7)
bt_balcony = GameSprite(LP, dx * 0.835, dy * 0.5, 0, dx / 16, dy / 11)
bt_mirror = GameSprite(LP, dx * 0.22, dy * 0.45, 0, dx / 13, dy / 8)
bt_pot = GameSprite(LP, dx * 0.8, dy * 0.85, 0, dx / 16, dy / 11)

bt_toybox = GameSprite(LP, dx * 0.62, dy * 0.55, 0, dx / 12, dy / 7)
bt_revolver = GameSprite(LP, dx * 0.37, dy * 0.55, 0, dx / 13, dy / 8)

bt_drawer_1 = GameSprite(LP, dx * 0.35, dy * 0.45, 0, dx / 14, dy / 9)
drawer = GameSprite('drawer.png', dx * 0.25, dy * 0.45, 0, dx / 2.7, dy / 3)
bt_painting = GameSprite(LP, dx * 0.65, dy * 0.27, 0, dx / 13, dy / 8)

bt_secret_key = GameSprite(LP, dx / 2.35, dy / 1.8, 0, dx / 17, dy / 12)

game = True
finish = False
screen = False  # ///////////////////////////////////////////////// True
pause = False
clock = pygame.time.Clock()
FPS = 60

mouse_x, mouse_y = pygame.mouse.get_pos()

pygame.font.init()
print(pygame.font.get_fonts())
size_f = int(dx/40)
font1 = pygame.font.SysFont('consolas', size_f)


# Тексти
text_intro_1 = font1.render(
                "Ти прокидаєшся у невідомому будинку.", 1, (255, 255, 255)
            )
text_intro_2 = font1.render(
    "Твоє завдання: знайти вихід і дізнатися правду.", 1, (255, 255, 255)
)

text_outro_1 = font1.render(
                "Ти вийшов із будинка. Запах волі б'є в лице.", 1, (255, 255, 255)
            )
text_outro_2 = font1.render(
    "Аж тут ти розумієш, що наступного разу опинишся на тому самому місці.", 1, (255, 255, 255)
)

text_outro_3 = font1.render(
    "Погана кінцівка.", 1, (255, 0, 0)
)

text_secret_1 = font1.render(
                "Вийшовши на балкон, ти нічого не бачиш.", 1, (255, 255, 255)
            )
text_secret_2 = font1.render(
    "Спокута роздирає тебе зсередини, але вже надто пізно.", 1, (255, 255, 255)
)

text_secret_3 = font1.render(
    "Альтернативна кінцівка.", 1, (150, 0, 0)
)

text_key = font1.render(
    "ЗНАЙДЕНО КЛЮЧ ВІД ВХІДНИХ ДВЕРЕЙ", 1, (0, 0, 0)
)

text_nokey = font1.render(
    "ЗНАЙДІТЬ КЛЮЧ ВІД ВХІДНИХ ДВЕРЕЙ", 1, (0, 0, 0)
)

text_toybox = font1.render(
    "Коробка, повна дитячих іграшок. Дуже цікаво. Чиї вони?", 1, (0, 0, 0)
)

text_revolver = font1.render(
    "Старенький поліцейський револьвер. Заряджено 3 патрони.", 1, (0, 0, 0)
)
text_revolver_2 = font1.render(
    "2 вже використані.", 1, (0, 0, 0)
)

text_painting = font1.render(
    "Сім'я. Чоловік, дружина і донька.", 1, (0, 255, 0)
)

text_mirror = font1.render(
    "Самотній чоловік.", 1, (0, 0, 0)
)

text_secret = font1.render(
    "Знайдено ключ.", 1, (0, 0, 0)
)

# Етапи
stage = 0   # ///////////////////////////////////// stage 2

# Допоміжні змінні
a = 0

b = 0

c = 0

d = 0

f = 0

g = 0

i = 0

j = 0

room = 0    # |||||||||||||||||||||||||||||||||||||||||||||||\ room 1

cupboard = 0

exit_key = 0

secret_key = 0

r = 0

reminder = 0

toybox_story = 0

revolver_story = 0

drawer_state = 0

painting_state = 0

painting_story = 0

mirror_state = 0

mirror_story = 0

secret_ending = 0

pygame.mixer.init()
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

door_sound = pygame.mixer.Sound("door.mp3")
finish_sound = pygame.mixer.Sound("lock.mp3")
open_sound = pygame.mixer.Sound("open.mp3")
close_sound = pygame.mixer.Sound("close.mp3")
balcony_sound = pygame.mixer.Sound("balcony_door.mp3")


while game:
    clock.tick(FPS)
    if not screen:
        pygame.mixer.music.pause()
        window.blit(background, (0, 0))
        bt_start.reset()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if bt_start.rect.collidepoint(x, y):
                    stage = 1
                    screen = True
    if screen and not pause:
        if not finish:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if stage == 1:
                pygame.mouse.set_visible(False)
                window.fill((0, 0, 0))
                window.blit(text_intro_1, (dx / 15, dy / 4))
                window.blit(text_intro_2, (dx / 15, dy / 2))
                clock.tick(1)
                a += 1
            if a >= 5 and stage != 3:
                stage = 2
                room = 1
                a = 0
            if stage == 2:
                pygame.mixer.music.unpause()
                pygame.mouse.set_visible(True)
                window.blit(background, (0, 0))
                if room == 1:
                    background = pygame.transform.scale(
                        pygame.image.load(bg_list[1]), (dx, dy)
                    )
                    if cupboard == 0:
                        door_1.reset()
                        if bt_drawer.rect.collidepoint(mouse_x, mouse_y):
                            bt_drawer.reset()
                        if bt_balcony.rect.collidepoint(mouse_x, mouse_y):
                            bt_balcony.reset()
                    if cupboard == 1:
                        background = pygame.transform.scale(
                            pygame.image.load(bg_list[3]), (dx, dy)
                        )

                        if bt_back.rect.collidepoint(mouse_x, mouse_y):
                            bt_back.reset()
                        if bt_toybox.rect.collidepoint(mouse_x, mouse_y) and painting_state == 0:
                            bt_toybox.reset()
                        if drawer_state == 1:
                            drawer.reset()
                            if bt_revolver.rect.collidepoint(mouse_x, mouse_y):
                                bt_revolver.reset()
                            bt_drawer_1.rect.x, bt_drawer_1.rect.y = dx * 0.45, dy * 0.67
                            if bt_drawer_1.rect.collidepoint(mouse_x, mouse_y):
                                bt_drawer_1.reset()
                        if drawer_state == 0 and painting_state == 0:
                            if bt_drawer_1.rect.collidepoint(mouse_x, mouse_y):
                                bt_drawer_1.rect.x, bt_drawer_1.rect.y = dx * 0.35, dy * 0.47
                                bt_drawer_1.reset()
                        if toybox_story == 1:
                            if d < 90:
                                window.blit(text_toybox, (dx / 14, dy / 10))
                                d += 1
                            else:
                                d = 0
                                toybox_story = 0
                        if revolver_story == 1:
                            if f < 120:
                                window.blit(text_revolver, (dx / 18, dy / 10))
                                window.blit(text_revolver_2, (dx / 18, dy / 10 + size_f))
                                f += 1
                            else:
                                f = 0
                                revolver_story = 0
                        if painting_state == 0:
                            bt_painting.rect.x, bt_painting.rect.y = dx * 0.65, dy * 0.27
                            if bt_painting.rect.collidepoint(mouse_x, mouse_y):
                                bt_painting.reset()
                        if painting_state == 1:
                            bt_painting.rect.x, bt_painting.rect.y = dx / 2.25, dy / 2
                            background = pygame.transform.scale(
                                pygame.image.load(bg_list[4]), (dx, dy)
                            )
                            bt_back.reset()
                            if bt_painting.rect.collidepoint(mouse_x, mouse_y):
                                bt_painting.reset()
                            if painting_story == 1:
                                if g < 80:
                                    window.blit(text_painting, (dx / 18, dy / 10))
                                    g += 1
                                else:
                                    g = 0
                                    painting_story = 0

                if room == 2:
                    background = pygame.transform.scale(
                        pygame.image.load(bg_list[2]), (dx, dy)
                    )

                    if mirror_state == 0:
                        bt_mirror.rect.x, bt_mirror.rect.y = dx * 0.22, dy * 0.45
                        if bt_mirror.rect.collidepoint(mouse_x, mouse_y):
                            bt_mirror.reset()
                        door_2.reset()
                        if bt_back.rect.collidepoint(mouse_x, mouse_y):
                            bt_back.reset()
                        if bt_mirror.rect.collidepoint(mouse_x, mouse_y):
                            bt_mirror.reset()
                        if bt_pot.rect.collidepoint(mouse_x, mouse_y):
                            bt_pot.reset()
                    if mirror_state == 1:
                        background = pygame.transform.scale(
                            pygame.image.load(bg_list[5]), (dx, dy)
                        )
                        bt_back.reset()
                        bt_mirror.rect.x, bt_mirror.rect.y = dx / 2.2, dy / 2.5
                        if bt_mirror.rect.collidepoint(mouse_x, mouse_y):
                            bt_mirror.reset()
                        if bt_secret_key.rect.collidepoint(mouse_x, mouse_y):
                            bt_secret_key.reset()
                        if mirror_story == 1:
                            if i < 80:
                                window.blit(text_mirror, (dx / 18, dy / 10))
                                i += 1
                            else:
                                i = 0
                                mirror_story = 0
                    if reminder == 1:
                        if c < 80:
                            window.blit(text_nokey, (dx / 4, dy / 3))
                            c += 1
                        else:
                            c = 0
                            reminder = 0
                    if exit_key == 1 and b < 80:
                        window.blit(text_key, (dx/4, dy/3))
                        b += 1
                    if secret_key == 1 and j < 80:
                        window.blit(text_secret, (dx / 18, dy / 10))
                        b += 1
                bt_pause.reset()

            if stage == 3:
                pygame.mixer.music.pause()
                room = 0
                if secret_key == 1:
                    if a == 0:
                        balcony_sound.play()
                    pygame.mouse.set_visible(False)
                    window.fill((0, 0, 0))
                    window.blit(text_secret_1, (dx / 15, dy / 4))
                    window.blit(text_secret_2, (dx / 15, dy / 2 + size_f))
                    window.blit(text_secret_3, (dx / 15, dy / 2 + size_f * 2))
                    a += 1
                else:
                    if a == 0:
                        finish_sound.play()
                    pygame.mouse.set_visible(False)
                    window.fill((0, 0, 0))
                    window.blit(text_outro_1, (dx / 22, dy / 4))
                    window.blit(text_outro_2, (dx / 22, dy / 2 + size_f))
                    window.blit(text_outro_3, (dx / 22, dy / 2 + size_f * 2))
                    a += 1
                if a >= 560:
                    game = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if bt_pause.rect.collidepoint(x, y):
                    r = (randint(0, 255), randint(0, 255), randint(0, 255))
                    pause = True
                if (door_1.rect.collidepoint(x, y) and room == 1 and cupboard == 0
                        and not bt_mirror.rect.collidepoint(x, y)):
                    room = 2
                    door_sound.play()
                if (door_2.rect.collidepoint(x, y) and room == 2 and not door_1.rect.collidepoint(x, y) and
                        exit_key == 1):
                    stage = 3
                if (door_2.rect.collidepoint(x, y) and room == 2 and not door_1.rect.collidepoint(x, y) and
                        exit_key == 0 and mirror_state != 1):
                    reminder = 1
                if bt_back.rect.collidepoint(x, y) and painting_state == 1:
                    painting_state = 0
                if bt_back.rect.collidepoint(x, y) and mirror_state == 1:
                    mirror_state = 0
                elif bt_back.rect.collidepoint(x, y) and mirror_state == 0 and room == 2:
                    room = 1
                if bt_back.rect.collidepoint(x, y) and painting_state == 0:
                    cupboard = 0
                if bt_drawer.rect.collidepoint(x, y) and room == 1:
                    print("Комод")
                    cupboard = 1

                if bt_secret_key.rect.collidepoint(x, y) and mirror_state == 1:
                    secret_key = 1

                if bt_balcony.rect.collidepoint(x, y) and room == 1 and secret_key == 1:
                    print("Балкон")
                    secret_ending = 1
                    stage = 3
                if bt_mirror.rect.collidepoint(x, y) and room == 2 and mirror_state == 1:
                    print("Дзеркало")
                    mirror_story = 1
                elif bt_mirror.rect.collidepoint(x, y) and room == 2:
                    mirror_state = 1
                if bt_pot.rect.collidepoint(x, y) and room == 2:
                    print("Горщик")
                    exit_key = 1
                if bt_toybox.rect.collidepoint(x, y) and cupboard == 1 and not bt_drawer.rect.collidepoint(x, y):
                    print("Коробка")
                    toybox_story = 1
                if (bt_drawer_1.rect.collidepoint(x, y) and cupboard == 1 and not bt_drawer.rect.collidepoint(x, y)
                        and drawer_state == 0 and painting_state == 0):
                    print("Шухляда")
                    open_sound.play()
                    drawer_state = 1
                elif (bt_drawer_1.rect.collidepoint(x, y) and cupboard == 1 and not bt_drawer.rect.collidepoint(x, y)
                        and drawer_state == 1):
                    print("Шухляда")
                    close_sound.play()
                    drawer_state = 0
                if (bt_revolver.rect.collidepoint(x, y) and cupboard == 1 and not bt_drawer_1.rect.collidepoint(x, y)
                        and drawer_state == 1):
                    print("Револьвер")
                    revolver_story = 1
                if bt_painting.rect.collidepoint(x, y) and cupboard == 1 and painting_state == 1:
                    painting_story = 1
                elif bt_painting.rect.collidepoint(x, y) and cupboard == 1:
                    print("Картина")
                    painting_state = 1

    if pause:
        window.fill(r)
        bt_resume.reset()
        bt_exit.reset()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if bt_resume.rect.collidepoint(x, y):
                    pause = False
                if bt_exit.rect.collidepoint(x, y):
                    game = False
    pygame.display.update()
