from random import random, randint
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual, IndividualRect


def generate_individual(number_of_rects: int, width: int, height: int):
    rects = [generate_random_rects(width, height)
             for i in range(0, number_of_rects)]
    deviations = [genreate_rect_with_value(
        1) for i in range(0, number_of_rects)]
    data = list(map(create_data_chunk, zip(rects, deviations)))

    return Individual(data)


def create_data_chunk(chunk: (RGBARect, RGBARect)) -> IndividualRect:
    return IndividualRect(chunk[0], chunk[1])


def generate_random_rects(width: int, height: int) -> RGBARect:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    a = randint(0, 255)
    x = randint(0, width)
    y = randint(0, height)
    w = randint(0, width-x)
    h = randint(0, height-y)
    return RGBARect(r, g, b, a, x, y, w, h)


def genreate_rect_with_value(value) -> RGBARect:
    return RGBARect(value, value, value, value, value, value, value, value)
