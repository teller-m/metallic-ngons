import mpmath as mp

class LineSegment(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.vec = end-start

    def intersect(self, other):
        numerator = (other.start-self.start).cross(other.vec)
        denominator = self.vec.cross(other.vec)

        if (not numerator or mp.isnormal(numerator)) and mp.isnormal(denominator):
            ratio = numerator/denominator
            return self.vec*ratio + self.start

        return None
