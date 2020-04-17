from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual
from typing import List
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator

class PickingStrategy(ABC):

    @abstractmethod
    def pick(self, mappedFitting, sizeOfPopulation:int) -> List[Individual]:
        pass

class BestFittingStrategy(PickingStrategy):
    
    def pick(self, mappedFitting, sizeOfPopulation:int) -> List[Individual]:
        sortedFitting = sorted(list(mappedFitting), key = lambda x: float(x[1]), reverse=True)
        sortedPopulation = []
        for x in sortedFitting:
            sortedPopulation.append(x[0])
        return [sortedPopulation[i] for i in range(0, sizeOfPopulation)]

def pick(population: Population, comp: Comparator, pickingStartegy: PickingStrategy, sizeOfPopulation: int) -> Population:
    fitting = [comp.evaluate(individual) for individual in population.individuals]
    mappedFitting = zip(population.individuals, fitting)
    newPopulation = pickingStartegy.pick(mappedFitting, sizeOfPopulation)
    return Population(newPopulation)