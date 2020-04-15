from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator
from evolutionary_algorithm.individual_generator import generateIndividual
from PIL import Image

class Algorithm:
    def __init__(self, image: Image, sizeOfPopulation: int):
        self.population = Population()
        self.population.individuals = [generateIndividual(10, 500, 500) for i in range(0, sizeOfPopulation)]
        self.comp = Comparator(image)

    def createNextGeneration(self, numberOfParents):
        offspring = Population()
        seed()
        for i in range(numberOfParents):
            index = randint(0, 3)
            offspring.individuals.append(self.population.individuals[index])
        