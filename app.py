import sys
from evolutionary_algorithm.algorithm import Algorithm
from evolutionary_algorithm.crossing import *
from evolutionary_algorithm.picking import *
from PIL import Image
import matplotlib.pyplot as plt

def parse_crossing(arg) -> CrossingStrategy:
    if arg == "inter":
        return InterpolateCrossing()
    else:
        return MeanCrossing()


def parse_picking(arg) -> CrossingStrategy:
    if arg == "roulette":
        return RouletteWheelStrategy()
    elif arg == "ranking":
        return RankingSelectionStrategy()
    else:
        return BestFittingStrategy()


def run(image, population, rects, subpopulation, maxIter, target, crossing, picking):
    algo = Algorithm()
    algo.crossing_strategy = crossing
    algo.picking_strategy = picking
    result, img = algo.start(
        image,
        population,
        rects,
        subpopulation,
        maxIter,
        target
    )
    result.save_here("result")
    img.save("result_img.png")
    img.show()

    fig = plt.figure()
    plt.plot(result.iters, result.scores)
    plt.xlabel("Iterations")
    plt.ylabel("Score")
    fig.savefig("result.pdf")


if __name__ == "__main__":
    image = Image.open(sys.argv[1])
    population = int(sys.argv[2])
    rects = int(sys.argv[3])
    subpopulation = int(sys.argv[4])
    maxIter = int(sys.argv[5])
    target = float(sys.argv[6])
    crossing = parse_crossing(sys.argv[7])
    picking = parse_picking(sys.argv[8])
    run(image, population, rects, subpopulation,
        maxIter, target, crossing, picking)
