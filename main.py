import pygame
from random import randint
from time import sleep

pygame.init()
back = pygame.image.load("Background.png")
window = pygame.display.set_mode((585, 585))
clock = pygame.time.Clock()

step = 15

move_right = False
move_up = False
move_down = False
move_left = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = (0, 0, 0)

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.collidepoint(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=back)
        self.image = pygame.image.load(filename)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    #def player_collision(self, player_filler):
            #if self.rect.x <= player_filler.rect.x and player_filler.rect.colliderect(self.rect):
                #move_left = False
            #if self.rect.x >= player_filler.rect.x and player_filler.rect.colliderect(self.rect):
                #move_right = False
            #if self.rect.y <= player_filler.rect.y and player_filler.rect.colliderect(self.rect):
                #move_down = False
            #if self.rect.y >= player_filler.rect.y and player_filler.rect.colliderect(self.rect):
                #move_up = False


# Блок об'єктів

WestWall = Picture('Metal_wall_10.png', 5, 5, 50, 500)
SouthWall = Picture("Metal_wall_half_11.5.png", 5, 550, 575, 31)
NorthWall = Picture("Metal_wall_10.5.png", 55, 5, 525,45)
EastWall = Picture("Metal_wall_9.png", 530, 100, 50, 450)
Obstacle_1 = Picture("Obstacle_2x1.png", 55, 455, 100, 50)
Obstacle_2 = Picture("Obstacle_1x3.png", 205, 355, 50, 150)
Obstacle_3 = Picture("Obstacle_2x1.png", 105, 355, 100, 50)
Obstacle_4 = Picture("Obstacle_4x1.png", 255, 455, 200, 50)
Obstacle_5 = Picture("Obstacle_5x1.png", 255, 355, 250, 50)
Obstacle_6 = Picture("Obstacle_0.5x1.png", 505, 355, 25, 50)
Obstacle_7 = Picture("Obstacle_1x5.png", 205, 105, 50, 250)
Obstacle_8 = Picture("Obstacle_2x1.png", 55, 255, 100, 50)
Obstacle_9 = Picture("Obstacle_2x1.png", 105, 105, 100, 50)
Obstacle_9_5 = Picture("Obstacle_1x1.png", 105, 155, 50, 50)
Obstacle_10 = Picture("Obstacle_1x5.png", 305, 55, 50, 250)
Obstacle_11 = Picture("Obstacle_2x1.png", 355, 255, 100, 50)
Obstacle_12 = Picture("Obstacle_0.5x1.png", 455, 255, 25, 50)
Obstacle_13 = Picture("Obstacle_2x1.png", 430, 100, 100, 50)
Obstacle_14 = Picture("Obstacle_1x1.png", 430, 205, 50, 50)
Obstacle_15 = Picture("Obstacle_0.5x1.png", 405, 100, 25, 50)
Door = Picture("Door.png", 505, 55, 30, 47)
Door_bt = Picture("Door.png", 10, 505, 30, 47)
Player = Picture("Player.png", 40, 505, 27, 43)
walls = [SouthWall, WestWall, NorthWall, EastWall, Obstacle_1, Obstacle_2, Obstacle_3, Obstacle_4, Obstacle_5,
              Obstacle_6, Obstacle_7, Obstacle_8, Obstacle_9, Obstacle_9_5, Obstacle_10, Obstacle_11, Obstacle_12,
              Obstacle_13, Obstacle_14, Obstacle_15]
Area_1 = Area(205, 105, 50, 400)
Area_2 = Area(255, 355, 275, 50)
Area_3 = Area(355, 255, 125, 50)
Area_4 = Area(405, 100, 125, 50)
Door_open = False
i = 3

# Блок рандомних ключів

rand_key = randint(0, 2)
if rand_key == 0:
    Key = Picture("Key.png", 278, 430, 17, 10)
elif rand_key == 1:
    Key = Picture("Key.png", 178, 180, 17, 10)
elif rand_key == 2:
    Key = Picture("Key.png", 367, 230, 17, 10)

# Блок гри


game_over = False
while not game_over:
    #Музика
    pygame.mixer.music.load("Spoopy_music.mp3")
    # Блок інсталяції об'єктів
    SouthWall.fill()
    WestWall.fill()
    NorthWall.fill()
    EastWall.fill()
    Obstacle_1.fill()
    Obstacle_2.fill()
    Obstacle_3.fill()
    Obstacle_4.fill()
    Obstacle_5.fill()
    Obstacle_6.fill()
    Obstacle_7.fill()
    Obstacle_8.fill()
    Obstacle_9.fill()
    Obstacle_9_5.fill()
    Obstacle_10.fill()
    Obstacle_11.fill()
    Obstacle_12.fill()
    Obstacle_13.fill()
    Obstacle_14.fill()
    Obstacle_15.fill()
    Door.fill()
    Door_bt.fill()
    Key.fill()
    Player.fill()
    Area_1.fill()
    if Player.rect.colliderect(Area_1.rect):
        move_right = False
        move_left = False
        move_up = False
        move_down = False
    Area_2.fill()
    if Player.rect.colliderect(Area_2.rect):
        move_up = False
        move_down = False
    Area_3.fill()
    if Player.rect.colliderect(Area_3.rect):
        move_left = False
        move_down = False
        move_up = False
    Area_4.fill()
    if Player.rect.colliderect(Area_4.rect):
        move_right = False
        move_down = False
        move_up = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
    if move_right:
        Player.rect.x += 3
    if move_left:
        Player.rect.x -= 3
    if move_up:
        Player.rect.y -= 3
    if move_down:
        Player.rect.y += 3
    if Player.rect.colliderect(Key.rect):
        i -= 1
        rand_key = randint(0, 2)
        if rand_key == 0:
            Key = Picture("Key.png", 278, 430, 17, 10)
        elif rand_key == 1:
            Key = Picture("Key.png", 178, 180, 17, 10)
        elif rand_key == 2:
            Key = Picture("Key.png", 367, 230, 17, 10)
    if i <= 0:
        Key = Picture("Key.png", 367, 650, 17, 10)
        Door = Picture("Door.png", 505, 700, 30, 47)
        Door_open = True
        pygame.mixer.music.play(-1, 0.0)
    window.blit(back, (0, 0))
    if Door_open == True:
        if Player.rect.x >= 555 and Player.rect.y <= 55:
            win_text = Label(150, 150, 350, 50, back)
            win_text.set_text("Гра закінчена...", 60, (0, 255, 0))
            win_text.draw(10, 10)
            sleep(3)
            pygame.display.update()
            clock.tick(60)
            game_over = True
        else:
            x_rand = randint(0, 500)
            y_rand = randint(0, 500)
            spooky_text = Label(x_rand, y_rand, 350, 50, back)
            rand_text = randint(0, 2)
            if rand_text == 0:
                spooky_text.set_text("Він йде за тобою", 60, (0, 255, 0))
            elif rand_text == 1:
                spooky_text.set_text("Тобі не втекти", 60, (0, 255, 0))
            elif rand_text == 2:
                spooky_text.set_text("Τανατος", 60, (0, 255, 0))
            spooky_text.draw(10, 10)

    SouthWall.draw()
    if Player.rect.colliderect(SouthWall.rect):
        move_down = False
    WestWall.draw()
    if Player.rect.colliderect(WestWall.rect):
        move_left = False
        move_up = False
    NorthWall.draw()
    if Player.rect.colliderect(NorthWall.rect):
        move_up = False
    EastWall.draw()
    if Player.rect.colliderect(EastWall.rect):
        move_right = False
        move_down = False
    Obstacle_1.draw()
    if Player.rect.colliderect(Obstacle_1.rect):
        move_left = False
        move_down = False
        move_up = False
    Obstacle_2.draw()
    Obstacle_3.draw()
    if Player.rect.colliderect(Obstacle_3.rect):
        move_right = False
        move_down = False
        move_up = False
    Obstacle_4.draw()
    if Player.rect.colliderect(Obstacle_4.rect):
        move_left = False
        move_down = False
        move_up = False
    Obstacle_5.draw()
    Obstacle_6.draw()
    Obstacle_7.draw()
    Obstacle_8.draw()
    if Player.rect.colliderect(Obstacle_8.rect):
        move_left = False
        move_down = False
        move_up = False
    Obstacle_9.draw()
    if Player.rect.colliderect(Obstacle_9.rect):
        move_right = False
        move_down = False
        move_up = False
    Obstacle_9_5.draw()
    if Player.rect.colliderect(Obstacle_9_5.rect):
        move_left = False
        move_right = False
        move_up = False
    Obstacle_10.draw()
    if Player.rect.colliderect(Obstacle_10.rect):
        move_left = False
        move_right = False
        move_up = False
    Obstacle_11.draw()
    Obstacle_12.draw()
    Obstacle_13.draw()
    Obstacle_14.draw()
    if Player.rect.colliderect(Obstacle_14.rect):
        move_left = False
        move_right = False
        move_up = False
    Obstacle_15.draw()
    Door.draw()
    if Player.rect.colliderect(Door.rect):
        move_right = False
        move_up = False
    Door_bt.draw()
    if Player.rect.colliderect(Door_bt.rect):
        move_left = False
    Key.draw()
    Player.draw()
    pygame.display.update()
    clock.tick(60)