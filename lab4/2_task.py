#9_1.png
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
surface1 = pygame.Surface((794,1123))
surface2 = pygame.Surface((794,1123))
surface3 = pygame.Surface((794,1123))

surface1.set_colorkey((0,0,0))
surface1.set_alpha(128)
surface2.set_colorkey((0,0,0))
surface2.set_alpha(128)
surface3.set_colorkey((0,0,0))
surface3.set_alpha(128)

PI = 3.14

BLACK = (0, 0, 1)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
CYAN = (0, 255, 255)
DARK_GRAY = (70, 70, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 200)

def drel(surface, color, cords):
	ellipse(surface, color, cords)
	ellipse(surface, BLACK, cords, 1)

def draw_sky():
	circle(surface1, WHITE, (453, 178), 270, 50)
	line(surface2, WHITE, (171, 171), (742, 182), 50)
	line(surface3, WHITE, (461, -30), (440, 440), 50)
	ellipse(screen, WHITE, (420, 151, 60, 50))
	ellipse(screen, WHITE, (680, 169, 40, 30))
	ellipse(screen, WHITE, (185, 156, 30, 30))
	ellipse(screen, WHITE, (427, 408, 30, 30))

def draw_fish(x, y, surface):
	cords = [[x+41, y+68], [x+76, y+41], [x+110, y+23], [x+149, y+18], [x+189, y+30], [x+164, y+54], [x+136, y+67], [x+81, y+72]]
	polygon(surface, DARK_GRAY, cords)
	lines(surface, BLACK, True, cords, 1)

	cords = [[x+42, y+67], [x, y+116], [x+1, y+75]]
	polygon(surface, DARK_GRAY, cords)
	lines(surface, BLACK, True, cords, 1)

	cords = [[x+141, y+19], [x+130, y], [x+59, y+13], [x+104, y+26]]
	polygon(surface, RED, cords)
	lines(surface, BLACK, False, cords, 1)

	cords = [[x+141, y+65], [x+157, y+93], [x+179, y+65], [x+147, y+61]]
	polygon(surface, RED, cords)
	lines(surface, BLACK, False, cords, 1)

	cords = [[x+77, y+73], [x+69, y+95], [x+101, y+91], [x+94, y+71]]
	polygon(surface, RED, cords)
	lines(surface, BLACK, False, cords, 1)

	circle(surface, BLUE, (640, 944), 10)
	circle(surface, BLACK, (640, 944), 5)
	circle(surface, WHITE, (643, 948), 1)

def draw_bear(s):
	drel(s, GRAY, (115, 410, 294-115, 100))

	drel(s, GRAY, (-10, 470, 240, 450))

	arc(s, BLACK, (-300, -300, 5000, 5000), 47*PI/64, 408*PI/512, 5)
	line(s, BLACK, (525, 345), (525, 810))

	drel(s, GRAY, (196, 572, 130, 60))
	drel(s, GRAY, (122, 812, 180, 120))
	drel(s, GRAY, (236, 912, 70, 30))
	drel(s, GRAY, (127, 408, 30, 20))
	drel(s, BLACK, (193, 428, 10, 10))
	drel(s, BLACK, (285, 439, 10, 10))
	arc(s, BLACK, (105, 430, 190, 50), -PI/2, 0)

rect(screen, CYAN, (0, 0, 794, 603))
rect(screen, GRAY, (0, 603, 794, 1123))
line(screen, BLACK, (0, 603), (794, 603))
draw_sky()

draw_fish(481, 907, surface3)


drel(screen, DARK_GRAY, (425, 765, 300, 80))
drel(surface3, CYAN, (460, 800, 230, 45))


screen.blit(surface1, (0, 0))
screen.blit(surface2, (0, 0))
screen.blit(surface3, (0, 0))
draw_bear(screen)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()