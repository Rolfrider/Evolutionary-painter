from abc import ABC, abstractmethod
from evolutionary_algorithm.individual import Individual

class PickingStrategy(ABC):

    @abstractmethod
    def pick(self, mappedFitting, sizeOfPopulation:int) ->list(Individual):
        pass

class BestFittingStrategy(PickingStrategy):
    
    def pick(self, mappedFitting, sizeOfPopulation:int) ->list(Individual):
        sortedFitting = sorted(mappedFitting, key = lambda x: float(x[1]), reverse=True)
        newPopulation = []
        for i in range(0, sizeOfPopulation):
            newPopulation.append(sortedFitting[i][0])
        return newPopulation