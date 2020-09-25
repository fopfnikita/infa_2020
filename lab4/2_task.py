#9_1.png
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))

PI = 3.14

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
CYAN = (0, 255, 255)
DARK_GRAY = (70, 70, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 200)

def drel(color, cords):
	ellipse(screen, color, cords)
	ellipse(screen, BLACK, cords, 1)

rect(screen, CYAN, (0, 0, 794, 603))
rect(screen, GRAY, (0, 603, 794, 1123))
line(screen, BLACK, (0, 603), (794, 603))

surface1 = pygame.Surface((794,1123))
surface1.set_colorkey((0,0,0))
surface1.set_alpha(128)
circle(surface1, WHITE, (453, 178), 270, 50)

surface2 = pygame.Surface((794,1123))
surface2.set_colorkey((0,0,0))
surface2.set_alpha(128)
line(surface2, WHITE, (171, 171), (742, 182), 50)

surface3 = pygame.Surface((794,1123))
surface3.set_colorkey((0,0,0))
surface3.set_alpha(128)
line(surface3, WHITE, (461, -30), (440, 440), 50)

drel(DARK_GRAY, (425, 765, 300, 80))
ellipse(surface3, CYAN, (460, 800, 230, 45))
ellipse(surface3, BLACK, (460, 800, 230, 45), 1)
cords = [[522, 975], [557, 948], [591, 930], [630, 925], [670, 937], [645, 961], [617, 974], [562, 979]]
polygon(surface3, DARK_GRAY, cords)
lines(screen, BLACK, True, cords, 1)

cords = [[521, 976], [481, 1023], [462, 982]]
polygon(surface3, DARK_GRAY, cords)
lines(screen, BLACK, False, cords, 1)

cords = [[621, 926], [611, 907], [540, 920], [585, 933]]
polygon(surface3, RED, cords)
lines(screen, BLACK, False, cords, 1)

cords = [[622, 972], [638, 1000], [660, 972], [628, 968]]
polygon(surface3, RED, cords)
lines(screen, BLACK, False, cords, 1)

cords = [[558, 980], [550, 1002], [582, 998], [575, 978]]
polygon(surface3, RED, cords)
lines(screen, BLACK, False, cords, 1)

circle(surface3, BLUE, (640, 944), 10)
circle(surface3, BLACK, (640, 944), 5)
circle(surface3, BLUE, (643, 948), 1)

screen.blit(surface1, (0, 0))
screen.blit(surface2, (0, 0))
screen.blit(surface3, (0, 0))


drel(GRAY, (115, 410, 294-115, 100))

drel(GRAY, (-10, 470, 240, 450))

ellipse(screen, WHITE, (420, 151, 60, 50))
ellipse(screen, WHITE, (680, 169, 40, 30))
ellipse(screen, WHITE, (185, 156, 30, 30))
ellipse(screen, WHITE, (427, 408, 30, 30))

arc(screen, BLACK, (-300, -300, 5000, 5000), 47*PI/64, 408*PI/512, 5)
line(screen, BLACK, (525, 345), (525, 810))

drel(GRAY, (196, 572, 130, 60))
drel(GRAY, (122, 812, 180, 120))
drel(GRAY, (236, 912, 70, 30))
drel(GRAY, (127, 408, 30, 20))
drel(BLACK, (193, 428, 10, 10))
drel(BLACK, (285, 439, 10, 10))
arc(screen, BLACK, (105, 430, 190, 50), -PI/2, 0)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()