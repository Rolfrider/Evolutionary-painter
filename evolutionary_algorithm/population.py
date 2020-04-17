from random import seed
from random import randint
from evolutionary_algorithm.individual import Individual
from typing import List
from evolutionary_algorithm.crossing import *
from image_processing.comparator import Comparator

class Population:
    def __init__(self, individuals: List[Individual]):
        self.individuals = individuals
    
    def createSubPopulation(self, subPopulationSize: int):
        new_individuals = []
        seed()
        for i in range(0, subPopulationSize):
            index = randint(0, len(self.individuals)-1)
            new_individuals.append(self.individuals[index])
        return Population(new_individuals)

    def createOffspringByCrossing(self, crossingStrategy: CrossingStrategy):
        offspring = []
        for i in range(0, len(self.individuals)):
            offspring.append(self.individuals[i].cross(self.individuals[(i+1)%len(self.individuals)], crossingStrategy))
        return Population(offspring)

    def bestIndividual(self, comp: Comparator):
        fitting = [comp.evaluate(x) for x in self.individuals]
        mappedFitting = zip(self.individuals, fitting)
        sortedFitting = sorted(mappedFitting, key = lambda x: float(x[1]), reverse=True)
        return sortedFitting[0]

    def mutate(self):
        for individual in self.individuals:
            individual.mutate()
