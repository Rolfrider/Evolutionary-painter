from random import seed
from random import randint
from evolutionary_algorithm.individual import Individual
from typing import List
from evolutionary_algorithm.crossing import *

class Population:
    def __init__(self, individuals: List[Individual]):
        self.individuals = individuals
    
    def createSubPopulation(self, subPopulationSize: int) -> list(Individual):
        new_inviduals = []
        seed()
        for i in range(0, subPopulationSize):
            index = randint(0, len(self.individuals)-1)
            new_inviduals.append(self.individuals[index])
        return new_inviduals

    def createOffspringByCrossing(self, crossingStrategy: CrossingStrategy) -> list(Individual):
        offspring = []
        for i in range(0, len(self.individuals)):
            offspring.append(self.individuals[i].cross(self.individuals[(i+1)%len(self.individuals)], crossingStrategy))
        return offspring

