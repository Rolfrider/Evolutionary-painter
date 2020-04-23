from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.picking import BestFittingStrategy, RouletteWheelStrategy, RankingSelectionStrategy
from PIL import Image
import matplotlib.pyplot as plt

test_image = Image.open("simple_img.jpg")

algorithm = Algorithm()

population = 10

subpopulation = 15
target = 0.99


def examine_rect_number(iter_limit: int = 1000, rect_numbers: [int] = [10, 20, 50, 100, 200, 300]):
    algorithm.picking_strategy = BestFittingStrategy()
    title = "number_of_rect_"
    for rect in rect_numbers:
        all_results = []
        for i in range(0, 5):
            result, image = algorithm.start(
                test_image,
                population,
                rect,
                subpopulation,
                iter_limit,
                target
            )
            result.title = title + str(rect) + "_" + str(i)
            result.save("data/rect_number")
            all_results.append(result)
            image_name = "data/rect_number/" + title + \
                str(rect) + "_" + str(i) + ".png"
            image.save(image_name)
        save_plot(title + str(rect), all_results)


def save_plot(title: str, results):
    fig = plt.figure()
    for n, result in enumerate(results):
        label = "test_" + str(n)
        plt.plot(result.iters, result.scores, label=label)

    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    plt.legend(loc='best')
    fig.savefig("data/rect_number/" + title + ".pdf")
