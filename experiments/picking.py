from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.picking import BestFittingStrategy, RouletteWheelStrategy, RankingSelectionStrategy
from PIL import Image
import matplotlib.pyplot as plt

test_image = Image.open("simple_img.jpg")

algorithm = Algorithm()

population = 20
number_of_rect = 20
subpopulation = 30
target = 0.99


def examine_best_fitting_strategy(iter_limit: int = 1000):
    algorithm.picking_strategy = BestFittingStrategy()
    all_results = []
    title = "best_fitting_crossing_"
    for i in range(0, 5):
        result, image = algorithm.start(
            test_image,
            population,
            number_of_rect,
            subpopulation,
            iter_limit,
            target
        )
        result.title = title + str(i)
        result.save("data/picking")
        all_results.append(result)
        image_name = "data/picking/" + title + str(i) + ".png"
        image.save(image_name)
    save_plot(title, all_results)


def examine_roulette_strategy(iter_limit: int = 1000):
    algorithm.picking_strategy = RouletteWheelStrategy()
    all_results = []
    title = "roulette_crossing_"
    for i in range(0, 5):
        result, image = algorithm.start(
            test_image,
            population,
            number_of_rect,
            subpopulation,
            iter_limit,
            target
        )
        result.title = title + str(i)
        result.save("data/picking")
        all_results.append(result)
        image_name = "data/picking/" + title + str(i) + ".png"
        image.save(image_name)
    save_plot(title, all_results)


def examine_ranking_strategy(iter_limit: int = 1000):
    algorithm.picking_strategy = RankingSelectionStrategy()
    all_results = []
    title = "ranking_crossing_"
    for i in range(0, 5):
        result, image = algorithm.start(
            test_image,
            population,
            number_of_rect,
            subpopulation,
            iter_limit,
            target
        )
        result.title = title + str(i)
        result.save("data/picking")
        all_results.append(result)
        image_name = "data/picking/" + title + str(i) + ".png"
        image.save(image_name)
    save_plot(title, all_results)


def save_plot(title: str, results):
    fig = plt.figure()
    for n, result in enumerate(results):
        label = "test_" + str(n)
        plt.plot(result.iters, result.scores, label=label)

    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend(loc='best')
    fig.savefig("data/picking/" + title + ".pdf")
