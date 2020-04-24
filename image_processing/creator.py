from PIL import Image, ImageDraw
from typing import List
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual


def create_image(individual: Individual, width: int, height: int) -> Image:
    final_image = Image.new('RGBA', (width, height))
    for rect in map(lambda x: x.rect, sorted(individual.data, key=lambda x: x.rect.a, reverse=True)):
        rect.correct(width, height)
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle(calc_vertexes(rect),
                       (rect.r, rect.g, rect.b, rect.a))
        final_image = Image.alpha_composite(final_image, image)
    return final_image


def calc_vertexes(rect: RGBARect) -> (int, int, int, int):
    return (rect.x, rect.y, rect.x + rect.w, rect.y + rect.h)
