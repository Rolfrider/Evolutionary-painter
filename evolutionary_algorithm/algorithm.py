from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from image_processing.comparator import Comparator

class Algorithm:
    def __init__(self):
        self.mi = Population()
        self.mi.newPopulation(3, 10, 500, 500)
        self.comp = Comparator("YouDidIt.png")

    def createNextGeneration(self, numberOfParents):
        l = Population()
        seed()
        for i in range(numberOfParents):
            index = randint(0, 3)
            l.addIndividual(self.mi.getIndividual(index))
        