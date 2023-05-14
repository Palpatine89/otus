import pytest
from src.figure import Figure
from src.square import Square


class TestFigure:
    """TestFigure"""

    def test_name_figure(self):
        """Проверка атрибута name"""

        # Создание объекта фигура
        figure = Figure(name='Square')

        # Проверка имени созданной фигуры
        assert figure.name == 'Square'

    def test_add_area_err(self):
        """Проверка генерации исключения при некорректных параметрах"""

        with pytest.raises(ValueError):
            square = Square(side=10)  # Создание объекта квадрат
            square.add_area('not_figure')
