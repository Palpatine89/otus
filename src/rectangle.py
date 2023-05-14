from figure import Figure


class Rectangle(Figure):
    def __init__(self, side1: float, side2: float):
        self.side1 = side1
        self.side2 = side2
        super().__init__('Rectangle')
        if not self.valid_rectangle():
            raise ValueError('Такой прямоугольник нельзя создать')

    def valid_rectangle(self):
        return self.side1 > 0 and self.side2 > 0

    @property
    def perimeter(self):
        return (self.side1 + self.side2) * 2

    @property
    def area(self):
        return self.side1 * self.side2


