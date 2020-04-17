from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from evolutionary_algorithm.crossing import *
from evolutionary_algorithm.picking import *
from image_processing.comparator import Comparator
from image_processing.creator import createImage
from evolutionary_algorithm.individual_generator import generateIndividual
from PIL import Image

class Algorithm:
    
    crossingStrategy: CrossingStrategy = MeanCrossing()
    pickingStrategy: PickingStrategy = BestFittingStrategy()

    def __init__(self):
        self.population = None

    def start(self, image: Image, sizeOfPopulation: int, numberOfRects: int, subPopulationSize: int, maxIter: int, condition: float):

        
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
        self.population = self.population.pick(self.comp, self.pickingStrategy, sizeOfPopulation)
        # checking if finish
        bestIndividual, bestFitting = self.population.bestIndividual(self.comp)
        if bestFitting >= condition:
            individualImage = createImage(bestIndividual, 500, 500)
            individualImage.show()
        pass
        
    def createInitialPopulation(self, sizeOfPopulation: int, numberOfRects: int, width: int, height: int):
        individuals = [generateIndividual(numberOfRects, width, height) for i in range(0, sizeOfPopulation)]
        return individuals