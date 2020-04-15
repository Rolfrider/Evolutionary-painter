from evolutionary_algorithm.individual import Individual


class Population:
    def __init__(self):
        self.individuals = list()
    
    def newPopulation(self, sizeOfPopulation: int, numberOfRects: int, width: int, height: int):
        for i in range(sizeOfPopulation):
            individual = Individual(None)
            individual.createRandomRects(numberOfRects, width, height)
            self.individuals.append(individual)
    
    def addIndividual(self, individual: Individual):
        self.individuals.append(individual)

    def getIndividual(self, index: int) -> Individual:
        return self.individuals[index]
    
     #TODO: breeding