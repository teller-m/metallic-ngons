import logging
import mpmath as mp

from lib import args
from lib.linesegment import LineSegment
from lib.vector2 import Vector2
from lib.utils import mmf, getkey

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    n = args.n
    logger.info('ngon(%d)', n)

    # generate metallic mean
    mean = mmf(args.mean_id)
    logger.info('mmf(%d)= %s', args.mean_id, getkey(mean))

    theta = 2*mp.pi/n

    # calculate vertices
    vertices = []
    for i in range(n):
        x = mp.cos(theta*i)
        y = mp.sin(theta*i)
        vertex = Vector2(x, y)
        vertices.append(vertex)

    # generate diagonals
    diagonals = []
    for i in range(n):
        for j in range(i+1, n):
            v1 = vertices[i]
            v2 = vertices[j]
            diag = LineSegment(v1, v2)
            diagonals.append(diag)

    # calculate line segments lengths
    lengths = dict()
    for i, diag in enumerate(diagonals[:n//2]):
        # find intersection points
        points = set()
        for other in diagonals[i+1:]:
            # find the intersection point between diagonals
            point = diag.intersect(other)

            # ensure point lies within unit circle
            if point and point not in points and point.len() <= 1:
                points.add(point)

        # calculate lengths for each pair of points on the same diagonal
        if len(points):
            points = list(points)
            for j, point1 in enumerate(points):
                for point2 in points[j+1:]:
                    dist = point1.dist(point2)

                    if not mp.almosteq(dist, 0):
                        key = getkey(dist)
                        if key not in lengths:
                            lengths[key] = dist

    logger.info('lengths= %d', len(lengths))

    if args.show_matches:
        matches = []

    # test for metallic means ratio
    count = 0
    for k,l in lengths.items():
        key = getkey(mean*l)
        if key in lengths:
            count += 1
            if args.show_matches:
                matches.append((getkey(l), key))

    logger.info('matches= %d', count)

    if args.show_matches:
        matches.sort(key=lambda x:x[1])
        for base, target in matches:
            logger.info('base= {:<54} target= {:<50}'.format(base, target))

if __name__ == '__main__':
    main()
