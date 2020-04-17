from evolutionary_algorithm.individual import Individual
from typing import List

class Population:
    def __init__(self, individuals: List[Individual]):
        self.individuals = individuals
    
     #TODO: breeding