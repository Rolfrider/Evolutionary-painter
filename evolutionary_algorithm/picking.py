from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual

class PickingStrategy(ABC):

    @abstractmethod
    def pick(self, mappedFitting, sizeOfPopulation:int) ->list(Individual):
        pass

class BestFittingStrategy(PickingStrategy):
    
    def pick(self, mappedFitting, sizeOfPopulation:int) ->list(Individual):
        sortedFitting = sorted(list(mappedFitting), key = lambda x: float(x[1]), reverse=True)
        sortedPopulation = []
        for x in sortedFitting:
            sortedPopulation.append(x[0])
        return [sortedPopulation[i] for i in range(0, sizeOfPopulation)]