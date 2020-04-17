from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.crossing import CrossingStrategy
from random import seed, randint, random
from typing import List
from math import exp, sqrt

class IndividualRect:
    
    def __init__(self, rect: RGBARect, deviation: RGBARect):
        self.rect = rect
        self.deviation = deviation

    def cross(self, other,  strategy: CrossingStrategy):
        new_rect = strategy.cross(self.rect, other.rect)
        new_deviation = strategy.cross(self.deviation, other.deviation)
        return IndividualRect(new_rect, new_deviation)

    def mutate(self, numberOfRects: int, randomN: float):
        seed()
        multi = exp((1/sqrt(2*numberOfRects))*randomN+(1/sqrt(2*sqrt(numberOfRects))))
        multiRect = RGBARect(multi*random(), multi*random(), multi*random(), multi*random(), multi*random(), multi*random(), multi*random(), multi*random())
        self.deviation.mutateDeviation(multiRect)
        self.rect.mutateRect(self.deviation)

    def correct(self, width:int, height:int):
        self.rect.correct(width, height)

        


class Individual:
    def __init__(self, data: List[IndividualRect]):
        self.data = data

    def cross(self, individual, strategy: CrossingStrategy):
        assert len(self.data) == len(individual.data)
        new_data = [me.cross(other, strategy) for me, other in zip(self.data, individual.data)]
        return Individual(new_data)
 
    def mutate(self):
        seed()
        for x in self.data:
            x.mutate(len(self.data), random())
    
    def correct(self, width:int, height:int):
        for x in self.data:
            x.correct(width, height)