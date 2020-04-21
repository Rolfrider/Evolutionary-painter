from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.crossing import MeanCrossing, InterpolateCrossing
from PIL import Image
import matplotlib.pyplot as plt

test_image = Image.open("simple_img.jpg")

algorithm = Algorithm()

population = 20
number_of_rect = 20
subpopulation = 30
target = 0.99


def examine_mean_strategy(iter_limit: int = 1000):
    algorithm.crossing_strategy = MeanCrossing()
    all_results = []
    title = "mean_crossing_"
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
        result.save("data/crossing")
        all_results.append(result)
        image_name = "data/crossing/" + title + ".png"
        image.save(image_name)
    save_plot(title, all_results)


def examine_interpolate_strategy(iter_limit: int = 1000):
    algorithm.crossing_strategy = InterpolateCrossing()
    all_results = []
    title = "interpolate_crossing_"
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
        result.save("data/crossing")
        all_results.append(result)
        image_name = "data/crossing/" + title + ".png"
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
    fig.savefig("data/crossing/" + title + ".pdf")
