from image_processing.comparator import Comparator
from data_struct.rgba_rect import RGBARect
from image_processing.creator import createImage

individual = [
    RGBARect(255, 0, 0, 0.5, 10, 0, 100, 200),
    RGBARect(0, 255, 0, 0.5, 50, 0, 100, 200),
    RGBARect(0, 0, 255, 0.5, 30, 100, 100, 200),
    RGBARect(90, 100, 155, 0.5, 100, 100, 300, 300),
    RGBARect(0, 100, 25, 0.5, 290, 190, 200, 200),
    RGBARect(200, 100, 105, 1, 400, 100, 100, 200),
    RGBARect(200, 100, 205, 0.6, 220, 210, 200, 250),
]

individualImage = createImage(individual, 500, 500)
individualImage.show()


comp = Comparator("YouDidIt.png")
percent = comp.evaluate(individual)

print(percent)
