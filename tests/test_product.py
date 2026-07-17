from src.product import Product


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

        expected = (100.0 * 10) + (200.0 * 2)  # 1000 + 400 = 1400
        assert product1 + product2 == expected

    def test_product_add_type_error(self):
        """Тест сложения с неправильным типом"""
        product = Product("Test", "Desc", 100.0, 10)
        try:
            product + "string"
        except TypeError as e:
            assert str(e) == "Нельзя сложить Product и str"
        else:
            assert False, "Ожидалась TypeError"
