from image_processing.comparator import Comparator
from data_struct.rgba_rect import RGBARect
from image_processing.creator import create_image
from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.picking import *
from evolutionary_algorithm.individual import *
from PIL import Image
from random import seed


# individual = [
#     RGBARect(255, 0, 0, 125, 10, 0, 100, 200),
#     RGBARect(0, 255, 0, 125, 50, 0, 100, 200),
#     # RGBARect(0, 0, 255, 125, 30, 100, 100, 200),
#     RGBARect(90, 100, 155, 125, 100, 100, 300, 300),
#     RGBARect(0, 100, 25, 125, 290, 190, 200, 200),
#     RGBARect(200, 100, 105, 255, 400, 100, 100, 200),
#     RGBARect(200, 100, 205, 145, 220, 210, 200, 250),
# ]
image = Image.open("simple_img.jpg")
seed()
algorithm = Algorithm()
algorithm.start(
    image,
    size_of_population=20,
    number_of_rects=20,
    subpopulation_size=15,
    maxIter=10000,
    condition=0.95
)
# rects = list(map(lambda x: IndividualRect(x, x), individual))
# img = create_image(Individual(rects), 600, 600)
# img.show()
# comp = Comparator(image)
# resultWheel = pick(algorithm.population, comp, RouletteWheelStrategy(), 10)
# resultRank = pick(algorithm.population, comp, RankingSelectionStrategy(), 10)
# print(resultRank)
# individualImage = createImage(
#     algorithm.population.bestIndividual(comp)[0], image.size[0], image.size[1])
# individualImage.show()

# for individual in algorithm.population.individuals:

#     percent = comp.evaluate(individual)
#     print(percent)
