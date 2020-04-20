from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.crossing import CrossingStrategy
from typing import List
from math import exp, sqrt
from numpy import random


class IndividualRect:

    def __init__(self, rect: RGBARect, deviation: RGBARect):
        self.rect = rect
        self.deviation = deviation

    def cross(self, other,  strategy: CrossingStrategy):
        new_rect = strategy.cross(self.rect, other.rect)
        new_deviation = strategy.cross(self.deviation, other.deviation)
        return IndividualRect(new_rect, new_deviation)

    def mutate(self, number_of_rects: int, randomN: float):
        multi_rect = RGBARect(
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN),
            self.__multiply(number_of_rects, randomN)
        )
        self.deviation.mutate_deviation(multi_rect)
        self.rect.mutate_rect(self.deviation)

    def correct(self, width: int, height: int):
        self.rect.correct(width, height)

    def __multiply(self, number_of_rects: int, randomN: float) -> float:
        return exp((1/sqrt(2*number_of_rects*8))*randomN+(1/sqrt(2*sqrt(number_of_rects*8)))*random.normal())


class Individual:
    def __init__(self, data: List[IndividualRect]):
        self.data = data
        self.score = None

    def cross(self, individual, strategy: CrossingStrategy):
        assert len(self.data) == len(individual.data)
        new_data = [me.cross(other, strategy)
                    for me, other in zip(self.data, individual.data)]
        return Individual(new_data)

    def mutate(self):
        randomFactor = random.normal()
        for x in self.data:
            x.mutate(len(self.data), randomFactor)
        self.score = None

    def correct(self, width: int, height: int):
        for x in self.data:
            x.correct(width, height)

    def evaluate(self, comparator) -> float:
        if self.score == None:
            self.score = comparator.evaluate(self)
        return self.score
