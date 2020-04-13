from PIL import Image
from image_processing.comparator import Comparator
im = Image.open("YouDidIt.png")

comp = Comparator(im)
percent = comp.evaluate([])

print(percent)
