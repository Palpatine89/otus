from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius
        super().__init__('Circle')
        if not self.valid_circle():
            raise ValueError('Такой круг нельзя создать')

    def valid_circle(self):
        return self.radius > 0

    @property
    def perimeter(self):
        return round((2 * pi * self.radius), 0)

    @property
    def area(self):
        return round((pi * (self.radius ** 2)), 0)
