from basetarget import BaseTarget
import math

class Ball(BaseTarget):
    def intersect(self, x, y):
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return math.sqrt( dx * dx + dy * dy) < self.r