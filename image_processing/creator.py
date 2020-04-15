from PIL import Image, ImageDraw
from typing import List
from data_struct.rgba_rect import RGBARect
from evolutionary_algorithm.individual import Individual


def createImage(individual: Individual, width: int, height: int) -> Image:
    finalImage = Image.new('RGBA', (width, height))
    #for rect in individual:
    for rect in individual.rects:
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle(calcVertexes(rect),
                       (rect.r, rect.g, rect.b, rect.a))
        finalImage = Image.alpha_composite(finalImage, image)
    return finalImage


def calcVertexes(rect: RGBARect) -> (int, int, int, int):
    return (rect.x, rect.y, rect.x + rect.w, rect.y + rect.h)
