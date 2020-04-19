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
        return Population([individual.cross(self.individuals[(index+1)%len(self.individuals)], crossingStrategy) for index, individual in enumerate(self.individuals)])

    def bestIndividual(self, comp: Comparator):
        fitting = [comp.evaluate(x) for x in self.individuals]
        best = 0
        index = -1
        for i in range(0, len(fitting)):
            if best<fitting[i]:
                best = fitting[i]
                index = i
        return self.individuals[index], best

    def mutate(self):
        for individual in self.individuals:
            individual.mutate()

    def correct(self, width:int, height:int):
        for individual in self.individuals:
            individual.correct(width, height)

    def plus(self, other):
        return Population(self.individuals + other.individuals)

