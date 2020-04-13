from PIL import Image
from typing import List
from data_struct.rgba_rect import RGBARect


class Comparator:

    def __init__(self, image: Image):
        self.refImage = image

    def evaluate(self, individual: List[RGBARect]) -> float:
        return 1.0
