from src.product import Product
from src.category import Category


class TestCategory:
    def test_category_initialization(self):
        """Тест корректной инициализации категории"""
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)
        products = [product1, product2]

        category = Category("Test Category", "Test Description", products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert len(category._Category__products) == 2

    def test_category_count_increment(self):
        """Тест подсчета количества категорий"""
        initial_count = Category.category_count

        product = Product("Test Product", "Description", 100.0, 5)
        Category("Test Category", "Test Description", [product])

        assert Category.category_count == initial_count + 1

    def test_product_count_increment(self):
        """Тест подсчета количества продуктов"""
        initial_count = Category.product_count

        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)
        products = [product1, product2]
        Category("Test Category", "Test Description", products)

        assert Category.product_count == initial_count + len(products)

    def test_multiple_categories(self):
        """Тест создания нескольких категорий"""
        Category.category_count = 0
        Category.product_count = 0

        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)

        Category("Category 1", "Description 1", [product1])
        Category("Category 2", "Description 2", [product2])

        assert Category.category_count == 2
        assert Category.product_count == 2

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        initial_count = Category.product_count
        Category("Empty Category", "No products", [])

        assert Category.product_count == initial_count

    def test_add_product(self):
        """Тест метода add_product"""
        category = Category("Test", "Desc", [])
        product = Product("New", "Desc", 100.0, 5)
        initial_count = Category.product_count

        category.add_product(product)

        assert len(category._Category__products) == 1
        assert category._Category__products[0] == product
        assert Category.product_count == initial_count + 1

    def test_products_getter(self):
        """Тест геттера products"""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])

        result = category.products
        expected = "Product 1, 100.0 руб. Остаток: 5 шт.\nProduct 2, 200.0 руб. Остаток: 3 шт.\n"

        assert result == expected
