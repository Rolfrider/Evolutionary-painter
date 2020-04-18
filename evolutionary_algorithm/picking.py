from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual
from typing import List
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator
from numpy import random, arange
from math import exp

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

class RouletteWheelStrategy(PickingStrategy):
    def pick(self, mappedFitting, sizeOfPopulation:int) -> List[Individual]:
        probability = []
        listedFitting = list(mappedFitting)
        probabilitySum = 0
        for x in listedFitting:
            probability.append(exp(x[1]))
            probabilitySum += exp(x[1])
        for i in range(0, len(probability)):
            probability[i] = probability[i]/probabilitySum
        newPopulation = []
        for i in range(0, sizeOfPopulation):
            index = random.choice(arange(0, len(probability)), p = probability)
            newPopulation.append(listedFitting[index][0])
            probabilitySum - probability[index]
            del listedFitting[index]
            del probability[index]
            for i in range(0, len(probability)):
                probability[i] = probability[i]/probabilitySum
        return newPopulation

class RankingSelectionStrategy(PickingStrategy):
    def pick(self, mappedFitting, sizeOfPopulation:int) -> List[Individual]:
        sortedFitting = sorted(list(mappedFitting), key = lambda x: float(x[1]))
        probability = []
        probabilitySum = 0
        for i in range(1, len(sortedFitting)+1):
            probability.append(i/(len(sortedFitting)+1))
            probabilitySum += i
        for x in probability:
            x = x/probabilitySum
        newPopulation = []
        for i in range(0, sizeOfPopulation):
            index = random.choice(arange(0, len(probability), p = probability))
            newPopulation.append(sortedFitting[index][0])
            del sortedFitting[index]
            del probability[index]
        return newPopulation
        

def pick(population: Population, comp: Comparator, pickingStartegy: PickingStrategy, sizeOfPopulation: int) -> Population:
    fitting = [comp.evaluate(individual) for individual in population.individuals]
    mappedFitting = zip(population.individuals, fitting)
    newPopulation = pickingStartegy.pick(mappedFitting, sizeOfPopulation)
    return Population(newPopulation)