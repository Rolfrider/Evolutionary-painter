from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.crossing import MeanCrossing, InterpolateCrossing
from PIL import Image
import matplotlib.pyplot as plt

test_image = Image.open("simple_img.jpg")

algorithm = Algorithm()

number_of_rect = 20
target = 0.99


def examine_population(iter_limit: int = 1000, populations=[2, 10, 15, 30, 40, 50, 100]):
    algorithm.crossing_strategy = MeanCrossing()
    title = "population_size_"
    for population in populations:
        all_results = []
        for i in range(0, 5):
            result, image = algorithm.start(
                test_image,
                population,
                number_of_rect,
                int(population*1.5),  # testować na stałej czy procentowej 🤔
                iter_limit,
                target
            )
            result.title = title + str(population) + "_" + str(i)
            result.save("data/population")
            all_results.append(result)
            image_name = "data/population/" + title + \
                str(population) + "_" + str(i) + ".png"
            image.save(image_name)
        save_plot(title + str(population), all_results)


def examine_subpopulation(iter_limit: int = 1000, subpopulations=[2, 10, 15, 30, 40, 50, 100]):
    algorithm.crossing_strategy = MeanCrossing()
    title = "subpopulation_size_"
    for subpopulation in subpopulations:
        all_results = []
        for i in range(0, 5):
            result, image = algorithm.start(
                test_image,
                30,
                number_of_rect,
                subpopulation,
                iter_limit,
                target
            )
            result.title = title + str(subpopulation) + "_" + str(i)
            result.save("data/population")
            all_results.append(result)
            image_name = "data/population/" + title + \
                str(subpopulation) + "_" + str(i) + ".png"
            image.save(image_name)
        save_plot(title + str(subpopulation), all_results)


def save_plot(title: str, results):
    fig = plt.figure()
    for n, result in enumerate(results):
        label = "test_" + str(n)
        plt.plot(result.iters, result.scores, label=label)

    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend(loc='best')
    fig.savefig("data/population/" + title + ".pdf")
