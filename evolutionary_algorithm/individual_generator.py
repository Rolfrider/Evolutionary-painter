from random import seed
from random import randint
from random import random
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual, IndividualRect


def generateIndividual(numberOfRects: int, width: int, height: int):
    seed()
    rects = [generateRandomRects(width, height) for i in range(0, numberOfRects)]
    deviations = [1 for i in range(0, numberOfRects)]
    tuples = zip(rects, deviations)
    data = list(map(createDataChunk, tuples))

    return Individual(data)

def createDataChunk(self, chunk: (RGBARect[int], RGBARect[float])) -> IndividualRect:
        return IndividualRect(chunk[0], chunk[1])

def generateRandomRects(width: int, height: int):
    seed()
    r = randint(0, 255)
    g = randint(0, 255)        
    b = randint(0, 255)
    a = randint(0, 255)
    x = randint(0, width)
    y = randint(0, height)
    w = randint(0, width-x)
    h = randint(0, height-y)
    return RGBARect(r, g, b, a, x, y, w, h)
