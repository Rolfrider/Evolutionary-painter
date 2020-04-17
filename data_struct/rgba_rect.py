from math import exp, sqrt
from random import seed, randint, random

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
        return RGBARect(self.r+other.r, self.g+other.g, self.b+other.b, self.a+other.a, self.x+other.x ,self.y+other.y ,self.w+other.w ,self.h+other.h)

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

    def interpolate(self, other, factor) :
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
    
    #zamienić expa na recta
    def mutateDeviation(self, other):
        seed()
        self.r *= other.r
        self.g *= other.g
        self.b *= other.b
        self.a *= other.a
        self.x *= other.x
        self.y *= other.y
        self.w *= other.w
        self.h *= other.h
    
    def mutateRect(self, deviation):
        self.r = self.r + deviation.r*random()
        self.g = self.g + deviation.g*random()
        self.b = self.b + deviation.b*random()
        self.a = self.a + deviation.a*random()
        self.x = self.x + deviation.x*random()
        self.y = self.y + deviation.y*random()
        self.w = self.w + deviation.w*random()
        self.h = self.h + deviation.h*random()