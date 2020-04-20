from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.crossing import MeanCrossing, InterpolateCrossing
from PIL import Image

test_image = Image.open("simple_img.jpg")

algorithm = Algorithm()

population = 20
number_of_rect = 20
subpopulation = 30
target = 0.99


def examine_mean_strategy(iter_limit: int = 1000):
    algorithm.crossing_strategy = MeanCrossing()
    for i in range(0, 5):
        title = "mean_crossing_" + str(i)
        result, image = algorithm.start(
            test_image,
            population,
            number_of_rect,
            subpopulation,
            iter_limit,
            target
        )
        result.title = title
        result.save()
        image_name = "data/" + title + ".png"
        image.save(image_name)


def examine_interpolate_strategy(iter_limit: int = 1000):
    algorithm.crossing_strategy = InterpolateCrossing()
    for i in range(0, 5):
        title = "interpolate_crossing_" + str(i)
        result, image = algorithm.start(
            test_image,
            population,
            number_of_rect,
            subpopulation,
            iter_limit,
            target
        )
        result.title = title
        result.save()
        image_name = "data/" + title + ".png"
        image.save(image_name)
