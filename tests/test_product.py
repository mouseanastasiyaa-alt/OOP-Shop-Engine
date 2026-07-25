import pytest

from src.base_product import BaseProduct
from src.mixin import LogMixin
from src.product import Product, Smartphone, LawnGrass


class TestProduct:
    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_product_price_type(self):
        """Тест типа цены продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        assert isinstance(product.price, float)

    def test_product_quantity_type(self):
        """Тест типа количества продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        assert isinstance(product.quantity, int)

    def test_new_product_classmethod(self):
        """Тест класс-метода new_product"""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 20,
        }
        product = Product.new_product(product_data)

        assert product.name == "New Product"
        assert product.description == "New Description"
        assert product.price == 150.0
        assert product.quantity == 20

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением"""
        product = Product("Test", "Desc", 100.0, 10)
        product.price = 150.0
        assert product.price == 150.0

    def test_price_setter_negative(self, capsys):
        """Тест сеттера цены с отрицательным значением"""
        product = Product("Test", "Desc", 100.0, 10)
        product.price = -50.0
        assert product.price == 100.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_zero(self, capsys):
        """Тест сеттера цены с нулевым значением"""
        product = Product("Test", "Desc", 100.0, 10)
        product.price = 0
        assert product.price == 100.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Test Product", "Test Description", 100.0, 10)
        expected = "Test Product, 100.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add(self):
        """Тест сложения продуктов"""
        product1 = Product("Product 1", "Desc 1", 100.0, 10)
        product2 = Product("Product 2", "Desc 2", 200.0, 2)

        expected = (100.0 * 10) + (200.0 * 2)
        assert product1 + product2 == expected

    def test_product_add_type_error(self):
        """Тест сложения с неправильным типом"""
        product = Product("Test", "Desc", 100.0, 10)
        try:
            product + "string"
        except TypeError as e:
            assert str(e) == "Нельзя складывать Product и str"
        else:
            assert False, "Ожидалась TypeError"


class TestSmartphone:
    def test_smartphone_initialization(self):
        """Тест инициализации смартфона"""
        phone = Smartphone(
            "iPhone 15",
            "Смартфон Apple",
            100000.0,
            10,
            "A16 Bionic",
            "iPhone 15",
            "256GB",
            "Black",
        )
        assert phone.name == "iPhone 15"
        assert phone.description == "Смартфон Apple"
        assert phone.price == 100000.0
        assert phone.quantity == 10
        assert phone.efficiency == "A16 Bionic"
        assert phone.model == "iPhone 15"
        assert phone.memory == "256GB"
        assert phone.color == "Black"

    def test_smartphone_str(self):
        """Тест строкового представления смартфона"""
        phone = Smartphone(
            "iPhone 15",
            "Смартфон Apple",
            100000.0,
            10,
            "A16 Bionic",
            "iPhone 15",
            "256GB",
            "Black",
        )
        expected = "iPhone 15, 100000.0 руб. Остаток: 10 шт."
        assert str(phone) == expected

    def test_smartphone_add_same_type(self):
        """Тест сложения двух смартфонов"""
        phone1 = Smartphone(
            "iPhone 15", "Desc", 100000.0, 2, "A16", "15", "256GB", "Black"
        )
        phone2 = Smartphone(
            "Samsung S23", "Desc", 80000.0, 3, "Snapdragon", "S23", "256GB", "White"
        )
        result = phone1 + phone2
        expected = (100000.0 * 2) + (80000.0 * 3)
        assert result == expected


class TestLawnGrass:
    def test_lawn_grass_initialization(self):
        """Тест инициализации газонной травы"""
        grass = LawnGrass(
            "Газонная трава",
            "Трава для газона",
            500.0,
            100,
            "Россия",
            7,
            "Зеленый",
        )
        assert grass.name == "Газонная трава"
        assert grass.description == "Трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 100
        assert grass.country == "Россия"
        assert grass.germination_period == 7
        assert grass.color == "Зеленый"

    def test_lawn_grass_str(self):
        """Тест строкового представления газонной травы"""
        grass = LawnGrass(
            "Газонная трава",
            "Трава для газона",
            500.0,
            100,
            "Россия",
            7,
            "Зеленый",
        )
        expected = "Газонная трава, 500.0 руб. Остаток: 100 шт."
        assert str(grass) == expected

    def test_lawn_grass_add_same_type(self):
        """Тест сложения двух газонных трав"""
        grass1 = LawnGrass("Трава 1", "Desc", 500.0, 10, "Россия", 7, "Зеленый")
        grass2 = LawnGrass("Трава 2", "Desc", 300.0, 20, "Россия", 5, "Зеленый")
        result = grass1 + grass2
        expected = (500.0 * 10) + (300.0 * 20)
        assert result == expected


class TestBaseProduct:
    def test_base_product_is_abstract(self):
        """Тест, что BaseProduct - абстрактный класс"""
        assert hasattr(BaseProduct, "__abstractmethods__")
        # Проверяем, что все абстрактные методы есть
        abstract_methods = BaseProduct.__abstractmethods__
        assert "__add__" in abstract_methods
        assert "__str__" in abstract_methods
        assert "price" in abstract_methods

    def test_base_product_cannot_be_instantiated(self):
        """Тест, что нельзя создать экземпляр BaseProduct"""
        with pytest.raises(TypeError) as excinfo:
            BaseProduct()
        # Проверяем, что ошибка связана с абстрактным классом
        assert (
                "Can't instantiate abstract class" in str(excinfo.value)
                or "abstract" in str(excinfo.value).lower()
        )


class TestLogMixin:
    def test_log_mixin_creation(self, capsys):
        """Тест логирования создания объекта"""

        class TestClass(LogMixin):
            def __init__(self, name, value):
                super().__init__(name, value)

        # Создаем объект
        obj = TestClass("test", 123)

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass('test', 123)" in captured.out
        # Проверяем, что объект создался
        assert obj is not None
        assert obj.__class__.__name__ == "TestClass"

    def test_log_mixin_with_kwargs(self, capsys):
        """Тест логирования с именованными аргументами"""

        class TestClass(LogMixin):
            def __init__(self, name, value):
                super().__init__(name=name, value=value)

        # Создаем объект
        TestClass(name="test", value=123)

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass(name='test', value=123)" in captured.out

    def test_log_mixin_empty_args(self, capsys):
        """Тест логирования без аргументов"""

        class TestClass(LogMixin):
            def __init__(self):
                super().__init__()

        # Создаем объект
        TestClass()

        # Проверяем вывод
        captured = capsys.readouterr()
        assert "TestClass()" in captured.out
