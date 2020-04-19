from random import randint
from evolutionary_algorithm.individual import Individual
from typing import List
from evolutionary_algorithm.crossing import *
from image_processing.comparator import Comparator

class Population:
    def __init__(self, individuals: List[Individual]):
        self.individuals = individuals
    
    def create_subpopulation(self, subpopulation_size: int):
        new_individuals = []
        for i in range(0, subpopulation_size):
            index = randint(0, len(self.individuals)-1)
            new_individuals.append(self.individuals[index])
        return Population(new_individuals)

    def create_offspring_by_crossing(self, crossing_strategy: CrossingStrategy):
        return Population([individual.cross(self.individuals[(index+1)%len(self.individuals)], crossing_strategy) for index, individual in enumerate(self.individuals)])

    def best_individual(self, comp: Comparator):
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

