from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual
from typing import List, Tuple
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator
from random import choices
from math import exp


class PickingStrategy(ABC):

    @abstractmethod
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], size_of_population: int) -> List[Individual]:
        pass


class BestFittingStrategy(PickingStrategy):

    def pick(self, individuals_fitting: List[Tuple[Individual, float]], size_of_population: int) -> List[Individual]:
        sorted_fitting = sorted(individuals_fitting,
                               key=lambda x: float(x[1]), reverse=True)
        sorted_population = list(map(lambda x: x[0],sorted_fitting))
        return sorted_population[:size_of_population]


class RouletteWheelStrategy(PickingStrategy):
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], size_of_population: int) -> List[Individual]:
        individuals = list(map(lambda x: x[0], individuals_fitting))
        weights = list(map(lambda x: x[1], individuals_fitting))
        return choices(individuals, weights=weights, k=size_of_population)


class RankingSelectionStrategy(PickingStrategy):
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], size_of_population: int) -> List[Individual]:
        sorted_fitting = list(
            sorted(individuals_fitting, key=lambda x: float(x[1])))
        n = len(sorted_fitting)
        rank_sum = n * (n + 1) / 2 
        ranked_individuals = [(indi[0], float(rank)/rank_sum)
                              for rank, indi in enumerate(sorted_fitting, 1)]
        individuals = list(map(lambda x: x[0], ranked_individuals))
        weights = list(map(lambda x: x[1], ranked_individuals))
        return choices(individuals, weights=weights, k=size_of_population)


def pick(population: Population, comp: Comparator, picking_startegy: PickingStrategy, size_of_population: int) -> Population:
    fitting = [individual.evaluate(comp)
               for individual in population.individuals]
    mapped_fitting = zip(population.individuals, fitting)
    new_population = picking_startegy.pick(list(mapped_fitting), size_of_population)
    return Population(new_population)
