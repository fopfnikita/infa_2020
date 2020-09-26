#9_2.png
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

BLACK = (100, 100, 100)
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
CYAN = (0, 255, 255)
DARK_CYAN = (0, 60, 60)
DARK_GRAY = (70, 70, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 200)

def drel(surface, color, cords):
	ellipse(surface, color, cords)
	ellipse(surface, BLACK, cords, 1)

def draw_sky():
	global screen
	circle(surface1, WHITE, (453, 178), 270, 50)
	line(surface2, WHITE, (171, 171), (742, 182), 50)
	line(surface3, WHITE, (461, -30), (440, 440), 50)
	ellipse(screen, WHITE, (420, 151, 60, 50))
	ellipse(screen, WHITE, (680, 169, 40, 30))
	ellipse(screen, WHITE, (185, 156, 30, 30))
	ellipse(screen, WHITE, (427, 408, 30, 30))
	#screen = pygame.transform.smoothscale(screen, (1, 2))
	#screen = pygame.transform.smoothscale(screen, (794, 1123))

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

	circle(surface, BLUE, (x + 159, y + 37), 10)
	circle(surface, BLACK, (x + 159, y + 37), 5)
	circle(surface, WHITE, (x + 162, y + 41), 1)

def draw_bear(s):
	drel(s, GRAY, (115, 410, 294-115, 100))

	drel(s, GRAY, (0, 470, 240, 450))

	#arc(s, BLACK, (-300, -300, 5000, 5000), 47*PI/64, 408*PI/512, 5)
	line(s, BLACK, (240, 640), (525, 345), 10)
	line(s, BLACK, (525, 345), (525, 810), 2)

	drel(s, GRAY, (196, 572, 130, 60))
	drel(s, GRAY, (122, 812, 180, 120))
	drel(s, GRAY, (236, 912, 70, 30))
	drel(s, GRAY, (127, 408, 30, 20))
	drel(s, BLACK, (193, 428, 10, 10))
	drel(s, BLACK, (285, 439, 10, 10))
	arc(s, BLACK, (105, 430, 190, 50), -PI/2, 0)

def draw_scene(x, y, scale, dir):
	surf = pygame.Surface((794, 1123))
	surf.set_colorkey((0, 0, 0))
	surffish = pygame.Surface((794, 1123))
	surffish.set_colorkey((0, 0, 0))
	surffish.set_alpha(128)

	draw_fish(481, 907, surffish)
	draw_fish(405, 907, surffish)
	draw_fish(512, 956, surffish)
	draw_fish(550, 940, surffish)
	draw_fish(512, 606, surffish)
	draw_fish(550, 590, surffish)
	draw_fish(400, 590, surffish)
	drel(surf, DARK_GRAY, (425, 765, 300, 80))
	drel(surf, DARK_CYAN, (460, 800, 230, 45))
	draw_bear(surf)
	surf = pygame.transform.smoothscale(surf, (int(794*scale), int(1123*scale)))
	surffish = pygame.transform.smoothscale(surffish, (int(794*scale), int(1123*scale)))
	if dir < 0:
		surf = pygame.transform.flip(surf, True, False)
		surffish = pygame.transform.flip(surffish, True, False)
	screen.blit(surffish, (x, y))
	screen.blit(surf, (x, y))


rect(screen, CYAN, (0, 0, 794, 603))
rect(screen, GRAY, (0, 603, 794, 1123))
line(screen, BLACK, (0, 603), (794, 603))

draw_sky()


screen.blit(surface1, (0, 0))
screen.blit(surface2, (0, 0))
screen.blit(surface3, (0, 0))
draw_scene(580, 500, 0.2, -1)
draw_scene(300, 500, 0.3, -1)
draw_scene(0, 600, 0.4, 1)
draw_scene(400, 700, 0.5, -1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()