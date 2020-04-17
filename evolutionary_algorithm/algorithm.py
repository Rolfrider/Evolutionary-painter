from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from evolutionary_algorithm.crossing import *
from image_processing.comparator import Comparator
from evolutionary_algorithm.individual_generator import generateIndividual
from PIL import Image

class Algorithm:
    
    crossingStrategy: CrossingStrategy = MeanCrossing()

    def __init__(self, image: Image, sizeOfPopulation: int, numberOfRects):
        self.width, self.height = image.size
        individuals = [generateIndividual(numberOfRects, self.width, self.height) for i in range(0, sizeOfPopulation)]
        self.population = Population(individuals)
        self.comp = Comparator(image)

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
            del offspring.individuals[1] # to nie rozumiem totalnie dla każdego parenta usuwamy tą samą rzecz ? to chyba jakiś błąd zaraz wleci

        self.population = Population(self.population.individuals + offspring.individuals) #TODO: Check if logic correct
        
        