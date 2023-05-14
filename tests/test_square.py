import pytest
from src.square import Square


class TestSquare:
    """TestSquare"""

    def test_square_class(self):
        """Проверка принадлежности созданного объекта квадрат классу Square"""

        # Создание объекта квадрат
        square = Square(side=10)

        # Проверка принадлежности созданного квадрата классу
        assert isinstance(square, Square)

    def test_square_params(self):
        """Проверка параметров созданного квадрата"""

        # Создание объекта квадрат
        square = Square(side=10)

        # Проверка параметров созданного квадрата
        assert square.perimeter == 40
        assert square.area == 100
        assert square.name == 'Square'
        assert square.side == 10

    @pytest.mark.parametrize('side', (-1, 0), ids=['side = -1', 'side = 0'])
    def test_create_square_err(self, side):
        """Проверка генерации исключения при некорректных параметрах"""

        with pytest.raises(ValueError):
            Square(side=side)

    def test_add_area_square(self):
        """Проверка суммы площадей двух фигур"""

        # Создание объекта квадрат
        square = Square(side=10)

        # Проверка суммы двух фигур
        assert square.add_area(square) == 200




