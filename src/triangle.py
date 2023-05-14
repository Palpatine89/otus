from figure import Figure


class Triangle(Figure):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__('Triangle')
        if not self.valid_triangle():
            raise ValueError('Такой треугольник нельзя создать')

    def valid_triangle(self):
        return self.side1 + self.side2 > self.side3 and \
               self.side1 + self.side3 > self.side2 and \
               self.side2 + self.side3 > self.side1

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2  # Получение полупериметра треугольника
        return round(((p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5), 0)

