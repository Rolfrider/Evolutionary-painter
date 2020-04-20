from random import seed
from random import randint
from evolutionary_algorithm.population import Population
from evolutionary_algorithm.crossing import *
from evolutionary_algorithm.picking import *
from image_processing.comparator import Comparator
from image_processing.creator import create_image
from evolutionary_algorithm.individual_generator import generate_individual
from PIL import Image
from data_struct.result import Result


class Algorithm:

    crossing_strategy: CrossingStrategy = MeanCrossing()
    picking_strategy: PickingStrategy = BestFittingStrategy()

    def __init__(self):
        self.population = None

    def start(self, image: Image, size_of_population: int, number_of_rects: int, subpopulation_size: int, maxIter: int, condition: float):
        result = Result()
        result.popultion = size_of_population
        result.subpopulation = subpopulation_size
        result.number_of_rect = number_of_rects

        width, height = image.size
        self.comp = Comparator(image)
        iter = 0

        self.population = self.create_initial_population(
            size_of_population, number_of_rects, width, height)
        while iter != maxIter:

            subpopulation = self.population.create_subpopulation(
                subpopulation_size)

            offspring = subpopulation.create_offspring_by_crossing(
                self.crossing_strategy)

            offspring.mutate()

            sum_of_populations = self.population.plus(offspring)
            self.population = pick(
                sum_of_populations, self.comp, self.picking_strategy, size_of_population)

            best_individual, best_fitting = self.population.best_individual(
                self.comp)
            result.add_point(best_fitting, iter)
            iter += 1
            print("Iteration:", iter, ", Fitting:", best_fitting)
            if best_fitting >= condition:
                break

            result.finalScore = best_fitting
            result.finalIter = iter
        individual_image = create_image(
            best_individual, image.size[0], image.size[1])

        return (result, individual_image)

    def create_initial_population(self, size_of_population: int, number_of_rects: int, width: int, height: int):
        individuals = [generate_individual(
            number_of_rects, width, height) for i in range(0, size_of_population)]
        return Population(individuals)
