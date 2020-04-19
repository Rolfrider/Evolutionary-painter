from abc import ABC, abstractmethod
from data_struct.rgba_rect import RGBARect
from numpy import random

class CrossingStrategy(ABC):

    @abstractmethod
    def cross(self, first: RGBARect, second: RGBARect) -> RGBARect:
        pass



class MeanCrossing(CrossingStrategy):

    def cross(self, first: RGBARect, second: RGBARect) -> RGBARect:
        return first.mean_with(second)


class InterpolateCrossing(CrossingStrategy):

    def __init__(self, factor = None):
        super().__init__()
        if factor == None:
            self.factor = random.normal()
        else:
            self.factor = factor

    def cross(self, first: RGBARect, second: RGBARect) -> RGBARect:
        return first.interpolate(second, self.factor)