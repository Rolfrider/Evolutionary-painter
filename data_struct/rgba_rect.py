from math import exp, sqrt
from numpy import random


class RGBARect():

    def __init__(self, r, g, b, a, x, y, w, h):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __add__(self, other):
        return RGBARect(self.r+other.r, self.g+other.g, self.b+other.b, self.a+other.a, self.x+other.x, self.y+other.y, self.w+other.w, self.h+other.h)

    def meanWith(self, other):
        return RGBARect(
            self.__mean(self.r, other.r),
            self.__mean(self.g, other.g),
            self.__mean(self.b, other.b),
            self.__mean(self.a, other.a),
            self.__mean(self.x, other.x),
            self.__mean(self.y, other.y),
            self.__mean(self.w, other.w),
            self.__mean(self.h, other.h)
        )

    def __mean(self, first, second):
        result = (first+second)/2
        return int(result) if isinstance(first, int) else result

    def interpolate(self, other, factor):
        return RGBARect(
            self.__iterpolate(self.r, other.r, factor),
            self.__iterpolate(self.g, other.g, factor),
            self.__iterpolate(self.b, other.b, factor),
            self.__iterpolate(self.a, other.a, factor),
            self.__iterpolate(self.x, other.x, factor),
            self.__iterpolate(self.y, other.y, factor),
            self.__iterpolate(self.w, other.w, factor),
            self.__iterpolate(self.h, other.h, factor)
        )

    def __iterpolate(self, first, second, factor):
        result = first*factor + (1 - factor)*second
        return int(result) if isinstance(first, int) else result

    def __floordiv__(self, other):
        if isinstance(other, int):
            return RGBARect(self.r//other, self.g//other, self.b//other, self.a//other, self.x//other, self.y//other, self.w//other, self.h//other)

    def mutateDeviation(self, other):
        self.r *= other.r
        self.g *= other.g
        self.b *= other.b
        self.a *= other.a
        self.x *= other.x
        self.y *= other.y
        self.w *= other.w
        self.h *= other.h

    def mutateRect(self, deviation):
        self.r = int(self.r + deviation.r*random.normal())
        self.g = int(self.g + deviation.g*random.normal())
        self.b = int(self.b + deviation.b*random.normal())
        self.a = int(self.a + deviation.a*random.normal())
        self.x = int(self.x + deviation.x*random.normal())
        self.y = int(self.y + deviation.y*random.normal())
        self.w = int(self.w + deviation.w*random.normal())
        self.h = int(self.h + deviation.h*random.normal())

    def correct(self, width: int, height: int):
        strategy = self.limit
        self.r = strategy(self.r, 0, 255)
        self.g = strategy(self.g, 0, 255)
        self.b = strategy(self.b, 0, 255)
        self.a = strategy(self.a, 0, 255)
        self.x = strategy(self.x, 0, width)
        self.y = strategy(self.y, 0, height)
        self.w = strategy(self.w, 0, width-self.x)
        self.h = strategy(self.h, 0, height-self.y)

    def limit(self, value, lower_bound, upper_bound):
        if value < lower_bound:
            return lower_bound
        elif value > upper_bound:
            return upper_bound
        else:
            return value

    def overflow(self, value, lower_bound, upper_bound):
        if value < lower_bound:
            return (value*-1) % upper_bound
        elif value > upper_bound:
            return value % upper_bound
        else:
            return value
