import mpmath as mp
from .utils import getkey

class Vector2(object):
    def __init__(self, x=0, y=0):
        if mp.almosteq(x, 0): x = 0.0
        if mp.almosteq(y, 0): y = 0.0

        self.x = mp.mpf(x)
        self.y = mp.mpf(y)

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x*other.x, self.y*other.y)
        else:
            return Vector2(self.x*other, self.y*other)

    def __str__(self):
        return '<Vector2 x=%s y=%s>'%(str(self.x)[:10], str(self.y)[:10])

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((getkey(self.x), getkey(self.y)))

    def cross(self, other):
        return self.x*other.y - self.y*other.x

    def dist(self, other):
        return (self-other).len()

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def len(self):
        return mp.sqrt(self.dot(self))
