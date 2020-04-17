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
        iter = 0
        # create initial 
        self.population = self.createInitialPopulation(sizeOfPopulation, numberOfRects, width, height)
        while iter != maxIter :
            # create sub population
            subPopulation = self.population.createSubPopulation(subPopulationSize)

            # cross: każdy kolejny czyli 1 z 2, 2 z 3 i tak dalej i ostatni z pierwszym
            offspring = subPopulation.createOffspringByCrossing(self.crossingStrategy)
            # mutation
            offspring.mutate()
            # picking next population
            self.population = pick(self.population, self.comp, self.pickingStrategy, sizeOfPopulation)
            # checking if finish
            bestIndividual, bestFitting = self.population.bestIndividual(self.comp)
            if bestFitting >= condition:
                individualImage = createImage(bestIndividual, 500, 500)
                individualImage.show()
                iter+=1
                break
            else:
                iter+=1
                print(iter)
                print(bestFitting)
        
    def createInitialPopulation(self, sizeOfPopulation: int, numberOfRects: int, width: int, height: int):
        individuals = [generateIndividual(numberOfRects, width, height) for i in range(0, sizeOfPopulation)]
        return Population(individuals)