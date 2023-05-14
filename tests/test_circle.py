import pytest
from src.circle import Circle


class TestCircle:
    """TestCircle"""

    def test_circle_class(self):
        """Проверка принадлежности созданного объекта круг классу Circle"""

        # Создание объекта круг
        circle = Circle(radius=10)

        # Проверка принадлежности созданного круга классу
        assert isinstance(circle, Circle)

    def test_circle_params(self):
        """Проверка параметров созданного круга"""

        # Создание объекта круг
        circle = Circle(radius=10)

        # Проверка параметров созданного круга
        assert circle.perimeter == 63
        assert circle.area == 314
        assert circle.name == 'Circle'
        assert circle.radius == 10

    @pytest.mark.parametrize('radius', (-1, 0), ids=['radius = -1', 'radius = 0'])
    def test_create_circle_err(self, radius):
        """Проверка генерации исключения при некорректных параметрах"""

        with pytest.raises(ValueError):
            Circle(radius=radius)

    def test_add_area_circle(self):
        """Проверка суммы площадей двух фигур"""

        # Создание объекта круг
        circle = Circle(radius=10)

        # Проверка суммы двух фигур
        assert circle.add_area(circle) == 628





