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
        
        self.population = self.createInitialPopulation(
            sizeOfPopulation, numberOfRects, width, height)
        while iter != maxIter:
            
            subPopulation = self.population.createSubPopulation(
                subPopulationSize)

            
            offspring = subPopulation.createOffspringByCrossing(
                self.crossingStrategy)
            
            offspring.mutate()
            offspring.correct(width, height)

            
            sum_of_populations = self.population.plus(offspring)
            self.population = pick(
                sum_of_populations, self.comp, self.pickingStrategy, sizeOfPopulation)
           
            bestIndividual, bestFitting = self.population.bestIndividual(
                self.comp)
            iter += 1  
            if bestFitting >= condition:
    
                break
            else:
                print(iter)
                print(bestFitting)
        individualImage = createImage(
            bestIndividual, image.size[0], image.size[1])
        individualImage.show()

    def createInitialPopulation(self, sizeOfPopulation: int, numberOfRects: int, width: int, height: int):
        individuals = [generateIndividual(
            numberOfRects, width, height) for i in range(0, sizeOfPopulation)]
        return Population(individuals)
