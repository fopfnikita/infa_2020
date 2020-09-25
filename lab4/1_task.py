import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

YELLOW = (255, 255, 10)
BLACK = (0, 0, 0)
RED = (50, 0, 0)

circle(screen, YELLOW, (300, 450), 100, 5)
rect(screen, BLACK, (0, 450, 600, 600))
circle(screen, YELLOW, (300,300), 200, 5)
circle(screen, YELLOW, (220, 220), 20)
circle(screen, RED, (200, 300), 30)
circle(screen, RED, (600 - 200, 300), 30)
circle(screen, YELLOW, (600 - 220, 220), 20)
line(screen, YELLOW, (270, 190), (90, 160), 5)
line(screen ,YELLOW, (300, 320), (270, 290), 5)
line(screen ,YELLOW, (300, 320), (600-270, 290), 5)
line(screen, YELLOW, (600 - 270, 190), (600 - 70, 150), 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()