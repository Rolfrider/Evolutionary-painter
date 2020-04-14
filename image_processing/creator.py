from PIL import Image, ImageDraw
from typing import List
from data_struct.rgba_rect import RGBARect


def createImage(individual: List[RGBARect], width: int, height: int) -> Image:
    finalImage = Image.new('RGBA', (width, height))
    for rect in individual:
        image = Image.new('RGBA', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle(calcVertexes(rect),
                       (rect.r, rect.g, rect.b, int(rect.a * 255)))
        finalImage = Image.alpha_composite(finalImage, image)
    return finalImage


def calcVertexes(rect: RGBARect) -> (int, int, int, int):
    return (rect.x, rect.y, rect.x + rect.w, rect.y + rect.h)
