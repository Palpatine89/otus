import pytest
from src.triangle import Triangle


class TestTriangle:
    """TestTriangle"""

    def test_triangle_class(self):
        """Проверка принадлежности созданного объекта треугольник классу Triangle"""

        # Создание объекта треугольник
        triangle = Triangle(side1=10, side2=11, side3=12)

        # Проверка принадлежности созданного треугольника классу
        assert isinstance(triangle, Triangle)

    def test_triangle_params(self):
        """Проверка параметров созданного треугольника"""

        # Создание объекта треугольник
        triangle = Triangle(side1=10, side2=11, side3=12)

        # Проверка параметров созданного треугольника
        assert triangle.perimeter == 33
        assert triangle.area == 52
        assert triangle.name == 'Triangle'
        assert triangle.side1 == 10
        assert triangle.side2 == 11
        assert triangle.side3 == 12

    @pytest.mark.parametrize('side1, side2, side3',
                             [(1, 2, 3), (0, 10, 11), (-1, 10, 12)],
                             ids=['side1 = 1, side2 = 2, side3 = 3',
                                  'side1 = 0, side2 = 10, side3 = 11',
                                  'side1 = -1, side2 = 10, side3 = 12'])
    def test_create_triangle_err(self, side1, side2, side3):
        """Проверка генерации исключения при некорректных параметрах"""

        with pytest.raises(ValueError):
            Triangle(side1=side1, side2=side2, side3=side3)

    def test_add_area_triangle(self):
        """Проверка суммы площадей двух фигур"""

        # Создание объекта треугольник
        triangle = Triangle(side1=10, side2=11, side3=12)

        # Проверка суммы двух фигур
        assert triangle.add_area(triangle) == 104




