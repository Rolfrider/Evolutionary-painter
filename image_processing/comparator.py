from PIL import Image, ImageChops
from typing import List
from data_struct.rgba_rect import RGBARect
import numpy


class Comparator:

    def __init__(self, image: Image):
        self.refImage = image

    def evaluate(self, individual: List[RGBARect]) -> float:
        image = self.__createImage(individual)
        diff = ImageChops.difference(self.refImage.convert('RGBA'), image)
        return 1 - self.__calculatePercentage(diff)

    def __calculatePercentage(self, diffImage: Image) -> float:
        pixelsNo = diffImage.size[0] * diffImage.size[1]
        diff = numpy.sum(diffImage) / float(3 * pixelsNo)
        return diff / 255.0

    def __createImage(self, individual: List[RGBARect]) -> Image:
        image = Image.new(
            'RGBA', (self.refImage.size[0], self.refImage.size[1]))
        return image
