from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual
from typing import List, Tuple
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator
from random import choices
from math import exp


class PickingStrategy(ABC):

    @abstractmethod
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], sizeOfPopulation: int) -> List[Individual]:
        pass


class BestFittingStrategy(PickingStrategy):

    def pick(self, individuals_fitting: List[Tuple[Individual, float]], sizeOfPopulation: int) -> List[Individual]:
        sortedFitting = sorted(individuals_fitting,
                               key=lambda x: float(x[1]), reverse=True)
        sortedPopulation = []
        for x in sortedFitting:
            sortedPopulation.append(x[0])
        return [sortedPopulation[i] for i in range(0, sizeOfPopulation)]


class RouletteWheelStrategy(PickingStrategy):
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], sizeOfPopulation: int) -> List[Individual]:
        individuals = list(map(lambda x: x[0], individuals_fitting))
        weights = list(map(lambda x: x[1], individuals_fitting))
        return choices(individuals, weights=weights, k=sizeOfPopulation)


class RankingSelectionStrategy(PickingStrategy):
    def pick(self, individuals_fitting: List[Tuple[Individual, float]], sizeOfPopulation: int) -> List[Individual]:
        sortedFitting = list(
            sorted(individuals_fitting, key=lambda x: float(x[1])))
        n = len(sortedFitting)
        rank_sum = n * (n + 1) / 2  # sum of values 1...N
        ranked_individuals = [(indi[0], float(rank)/rank_sum)
                              for rank, indi in enumerate(sortedFitting, 1)]
        individuals = list(map(lambda x: x[0], ranked_individuals))
        weights = list(map(lambda x: x[1], ranked_individuals))
        return choices(individuals, weights=weights, k=sizeOfPopulation)


def pick(population: Population, comp: Comparator, pickingStartegy: PickingStrategy, sizeOfPopulation: int) -> Population:
    fitting = [comp.evaluate(individual)
               for individual in population.individuals]
    mappedFitting = zip(population.individuals, fitting)
    newPopulation = pickingStartegy.pick(list(mappedFitting), sizeOfPopulation)
    return Population(newPopulation)
