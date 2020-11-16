from basetarget import BaseTarget
from random import randint
import math

GREEN = (0, 255, 0)

class Square(BaseTarget):
	def __init__(self, x, y):
		super().__init__(x, y, 20, GREEN)
		self.v = 30

	def intersect(self, x, y):
		dx = abs(self.x - x + 10)
		dy = abs(self.y - y + 10)
		print(dx, dy)
		return dx < self.r and dy < self.r

	def step(self, DT, WIDTH, HEIGHT):
		self.x += int(self.v * math.cos(self.alpha * 6.28/360) * DT)
		self.y += int(self.v * math.sin(self.alpha * 6.28/360) * DT)
		self.correct_coords(WIDTH, HEIGHT)
		if randint(0, 100) > 90:
			self.alpha = randint(0, 360)