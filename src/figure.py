class Figure:
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передана не геометрическая фигура')
        return self.area + figure.area
