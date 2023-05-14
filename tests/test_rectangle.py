import pytest
from src.rectangle import Rectangle


class TestRectangle:
    """TestRectangle"""

    def test_rectangle_class(self):
        """Проверка принадлежности созданного объекта прямоугольник классу Rectangle"""

        # Создание объекта прямоугольник
        rectangle = Rectangle(side1=10, side2=11)

        # Проверка принадлежности созданного прямоугольника классу
        assert isinstance(rectangle, Rectangle)

    def test_rectangle_params(self):
        """Проверка параметров созданного прямоугольника"""

        # Создание объекта прямоугольник
        rectangle = Rectangle(side1=10, side2=11)

        # Проверка параметров созданного прямоугольника
        assert rectangle.perimeter == 42
        assert rectangle.area == 110
        assert rectangle.name == 'Rectangle'
        assert rectangle.side1 == 10
        assert rectangle.side2 == 11

    @pytest.mark.parametrize('side1, side2',
                             [(-1, 1), (1, -1), (0, 1), (1, 0)],
                             ids=['side1 = -1, side2 = 1', 'side1 = 1, side2 = -1',
                                  'side1 = 0, side2 = 1', 'side1 = 1, side2 = 0'])
    def test_create_rectangle_err(self, side1, side2):
        """Проверка генерации исключения при некорректных параметрах"""

        with pytest.raises(ValueError):
            Rectangle(side1=side1, side2=side2)

    def test_add_area_rectangle(self):
        """Проверка суммы площадей двух фигур"""

        # Создание объекта прямоугольник
        rectangle = Rectangle(side1=10, side2=11)

        # Проверка суммы двух фигур
        assert rectangle.add_area(rectangle) == 220




