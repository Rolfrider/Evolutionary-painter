from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.crossing import CrossingStrategy
from random import seed, randint
from typing import List

class IndividualRect:
    
    def __init__(self, rect: RGBARect[int], deviation: RGBARect[float]):
        self.rect = rect
        self.deviation = deviation

    def cross(self, other: IndividualRect,  strategy: CrossingStrategy) -> IndividualRect:
        new_rect = strategy.cross(self.rect, other.rect)
        new_deviation = strategy.cross(self.deviation, other.deviation)
        return IndividualRect(new_rect, new_deviation)


class Individual:
    def __init__(self, data: List[IndividualRect]):
        self.data = data

    def cross(self, individual: Individual, strategy: CrossingStrategy):
        assert len(self.data) == len(individual.data)
        new_data = [me.cross(other, strategy) for me, other in zip(self.data, individual)]
        return Individual(new_data)
 