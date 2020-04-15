
class RGBARect:

    def __init__(self, r: int, g: int, b: int, a: int, x: int, y: int, w: int, h: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __add__(self, other):
        return RGBARect(self.r+other.r, self.g+other.g, self.b+other.b, self.a+other.a, self.x+other.x ,self.y+other.y ,self.w+other.w ,self.h+other.h)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return RGBARect(self.r//other, self.g//other, self.b//other, self.a//other, self.x//other, self.y//other, self.w//other, self.h//other)
