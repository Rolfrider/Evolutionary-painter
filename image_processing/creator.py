from PIL import Image, ImageDraw
from typing import List
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual


def createImage(individual: Individual, width: int, height: int) -> Image:
    finalImage = Image.new('RGBA', (width, height))
    finalDraw = ImageDraw.Draw(finalImage)
    for rect in map(lambda x: x.rect, individual.data):
        image = Image.new('RGBA', (rect.w, rect.h))
        draw = ImageDraw.Draw(image)
        draw.rectangle(calcVertexes(rect),
                       (rect.r, rect.g, rect.b, rect.a))
        finalDraw.bitmap(
            (rect.x, rect.y),
            image,
            (rect.r, rect.g, rect.b, rect.a)
        )
    return finalImage


def calcVertexes(rect: RGBARect) -> (int, int, int, int):
    return (rect.x, rect.y, rect.x + rect.w, rect.y + rect.h)
