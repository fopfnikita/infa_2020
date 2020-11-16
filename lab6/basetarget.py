from random import randint
import math

class BaseTarget(object):
    """Class of game ball"""
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.v = randint(1, 40)
        self.alpha = randint(0, 360)

    def step(self, DT, WIDTH, HEIGHT):
        self.x += int(self.v * math.cos(self.alpha * 6.28/360) * DT)
        self.y += int(self.v * math.sin(self.alpha * 6.28/360) * DT)
        self.correct_coords(WIDTH, HEIGHT)

    def correct_coords(self, WIDTH, HEIGHT):
        if self.x + self.r > WIDTH:
            self.alpha = randint(90, 270)
        if self.y + self.r > HEIGHT:
            self.alpha = randint(180, 360)
        if self.y - self.r < 0:
            self.alpha = randint(0, 180)
        if self.x - self.r < 0:
            self.alpha = randint(-90, 90)

    def intersect(self, x, y):
        pass