import pygame
from pygame.draw import *
from random import randint
from ball import Ball
from square import Square

import math

USERNAME = 'Anonym'
def start_game():
    print('Enter username:')
    name = input()
    if name != '':
        USERNAME = name

highscores = open("highscores", r)
start_game()
pygame.init()
pygame.font.init() 

WIDTH = 1200
HEIGHT = 900
TIME_LEFT = 2000
DT = 0.5

FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0
balls = []
squares = []

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

def new_ball():
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    balls.append(Ball(x, y, r, color))

def new_square():
    x = randint(100,700)
    y = randint(100,500)
    squares.append(Square(x, y))

def click(event):
    global score
    x = event.pos[0]
    y = event.pos[1]
    for ball in balls:
        if ball.intersect(x, y):
            balls.remove(ball)
            score += ball.v * 100//ball.r
    for square in squares:
        if square.intersect(x, y):
            squares.remove(square)
            score += 5 * square.v * 100//square.r
    print(score)

def draw_texts():
    scoresurface = myfont.render(str(score), True, WHITE) 
    timesurface = myfont.render('Time left: ' + str(TIME_LEFT), True, WHITE) 
    rect(screen, BLACK, (0, 0, 150, 40))
    screen.blit(scoresurface,(10,10)) 
    rect(screen, BLACK, (WIDTH - 250, 0, 250, 40))
    screen.blit(timesurface,(WIDTH - 250, 10)) 

pygame.display.update()
clock = pygame.time.Clock()
finished = False
myfont = pygame.font.SysFont(str(0), 50) 

while not finished and TIME_LEFT > 0:
    TIME_LEFT -= 100//FPS
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click!')

    if randint(0, 100) > 99 or len(balls) == 0:
        new_ball()
    if randint(0, 1000) > 995:
        new_square()

    for ball in balls:
        circle(screen, ball.color, (ball.x, ball.y), ball.r)
        ball.step(DT, WIDTH, HEIGHT)

    for square in squares:
        rect(screen, GREEN, (square.x, square.y, square.r * 2, square.r * 2))
        square.step(DT, WIDTH, HEIGHT)
    draw_texts()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()