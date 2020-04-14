from data_struct.rgba_rect import RGBARect
from random import seed
from random import randint
from typing import List

class Individual:
    def __init__(self, offspringRects: List[RGBARect]):
        if offspringRects == None :
            self.rects = list()
        else:
            self.rects = offspringRects

    def createRandomRects(self, numberOfRects: int, width: int, height: int):
        seed()
        for i in range(numberOfRects):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            a = randint(0, 255)
            x = randint(0, width)
            y = randint(0, height)
            w = randint(0, width-x)
            h = randint(0, height-y)
            self.rects.append(RGBARect(r, g, b, a, x, y, w, h))