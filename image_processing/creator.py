from PIL import Image, ImageDraw
from typing import List
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual


def create_image(individual: Individual, width: int, height: int) -> Image:
    final_image = Image.new('RGBA', (width, height))
    final_draw = ImageDraw.Draw(final_image)
    for rect in map(lambda x: x.rect, individual.data):
        image = Image.new('RGBA', (rect.w, rect.h))
        draw = ImageDraw.Draw(image)
        draw.rectangle(calc_vertexes(rect),
                       (rect.r, rect.g, rect.b, rect.a))
        final_draw.bitmap(
            (rect.x, rect.y),
            image,
            (rect.r, rect.g, rect.b, rect.a)
        )
    return final_image


def calc_vertexes(rect: RGBARect) -> (int, int, int, int):
    return (rect.x, rect.y, rect.x + rect.w, rect.y + rect.h)
