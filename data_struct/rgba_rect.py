from typing import TypeVar, Generic

T = TypeVar('T')

class RGBARect(Generic[T]):

    def __init__(self, r: T, g: T, b: T, a: T, x: T, y: T, w: T, h: T):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __add__(self, other: RGBARect) -> RGBARect:
        return RGBARect(self.r+other.r, self.g+other.g, self.b+other.b, self.a+other.a, self.x+other.x ,self.y+other.y ,self.w+other.w ,self.h+other.h)

    def meanWith(self, other: RGBARect) -> RGBARect:
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

    def __mean(self, first, second) -> T:
        return T((first+second)/2)

    def interpolate(self, other: RGBARect, factor) -> RGBARect:
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
        
    def __iterpolate(self, first, second, factor) -> T:
        return T(first*factor + (1 - factor)*second)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return RGBARect(self.r//other, self.g//other, self.b//other, self.a//other, self.x//other, self.y//other, self.w//other, self.h//other)
