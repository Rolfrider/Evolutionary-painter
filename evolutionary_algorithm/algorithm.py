from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from evolutionary_algorithm.crossing import *
from image_processing.comparator import Comparator
from evolutionary_algorithm.individual_generator import generateIndividual
from PIL import Image

class Algorithm:
    
    crossingStrategy: CrossingStrategy = MeanCrossing()

    def __init__(self):
        self.population = None

    def start(self, image: Image, sizeOfPopulation: int, numberOfRects: int, subPopulationSize: int):

        width, height = image.size
        self.comp = Comparator(image)
        # create initial 
        self.population = Population(self.createInitialPopulation(sizeOfPopulation, numberOfRects, width, height))
        # create sub population
        subPopulation = Population(self.population.createSubPopulation(subPopulationSize))

        # cross: każdy kolejny czyli 1 z 2, 2 z 3 i tak dalej i ostatni z pierwszym
        offspring = Population(subPopulation.createOffspringByCrossing(self.crossingStrategy))
        # mutation
        for individual in offspring.individuals:
            individual.mutate()
        # picking next population

        # checking if finish
        pass

    def createNextGeneration(self, numberOfParents):
        new_inviduals = []
        seed()
        for i in range(0, numberOfParents):
            index = randint(0, len(self.population.individuals)-1)
            new_inviduals.append(self.population.individuals[index])

        offspring = Population(new_inviduals)
            
        #TODO: Make it happen in population
        for i in range(0, numberOfParents-1):
            for j in range(i+1, numberOfParents):
                offspring.individuals.append(offspring.individuals[i].cross(offspring.individuals[j], self.crossingStrategy))

        for i in range(0, numberOfParents):
            del offspring.individuals[0] # to nie rozumiem totalnie dla każdego parenta usuwamy tą samą rzecz ? to chyba jakiś błąd zaraz wleci

        self.population = Population(self.population.individuals + offspring.individuals) #TODO: Check if logic correct
        
    def createInitialPopulation(self, sizeOfPopulation: int, numberOfRects: int, width: int, height: int):
        individuals = [generateIndividual(numberOfRects, width, height) for i in range(0, sizeOfPopulation)]
        return individuals