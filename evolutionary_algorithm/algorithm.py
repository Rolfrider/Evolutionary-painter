from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator
from evolutionary_algorithm.individual_generator import generateIndividual
from PIL import Image

class Algorithm:
    def __init__(self, image: Image, sizeOfPopulation: int, numberOfRects):
        self.population = Population()
        self.width, self.height = image.size
        self.population.individuals = [generateIndividual(numberOfRects, self.width, self.height) for i in range(0, sizeOfPopulation)]
        self.comp = Comparator(image)

    def createNextGeneration(self, numberOfParents):
        offspring = Population()
        seed()
        for i in range(0, numberOfParents):
            index = randint(0, len(self.population.individuals)-1)
            offspring.individuals.append(self.population.individuals[index])
        for i in range(0, numberOfParents-1):
            for j in range(i+1, numberOfParents):
                offspring.individuals.append(offspring.individuals[i].cross(offspring.individuals[j]))
        for i in range(0, numberOfParents):
            del offspring.individuals[1]
        self.population.individuals = self.population.individuals + offspring.individuals
        
        