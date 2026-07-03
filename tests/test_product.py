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
