from PIL import Image
from typing import List


class RGBARect:

    def __init__(self, r: int, g: int, b: int, a: float, x: int, y: int, w: int, h: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class Comparator:

    def __init__(self, image: Image):
        self.refImage = image

    def evaluate(self, individual: List[RGBARect]) -> float:
        return 1.0
