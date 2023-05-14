from figure import Figure


class Square(Figure):
    def __init__(self, side: float):
        self.side = side
        super().__init__('Square')
        if not self.valid_square():
            raise ValueError('Такой квадрат нельзя создать')

    def valid_square(self):
        return self.side > 0

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def area(self):
        return self.side * self.side

