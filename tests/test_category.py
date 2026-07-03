import pytest
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
        assert len(category.products) == 2
        assert category.products == products

    def test_category_count_increment(self):
        """Тест подсчета количества категорий"""
        # Сохраняем начальное значение
        initial_count = Category.category_count

        # Создаем новую категорию
        product = Product("Test Product", "Description", 100.0, 5)
        category = Category("Test Category", "Test Description", [product])

        # Проверяем, что счетчик увеличился
        assert Category.category_count == initial_count + 1

    def test_product_count_increment(self):
        """Тест подсчета количества продуктов"""
        # Сохраняем начальное значение
        initial_count = Category.product_count

        # Создаем продукты и категорию
        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)
        products = [product1, product2]
        category = Category("Test Category", "Test Description", products)

        # Проверяем, что счетчик увеличился на количество продуктов
        assert Category.product_count == initial_count + len(products)

    def test_multiple_categories(self):
        """Тест создания нескольких категорий"""
        # Сбрасываем счетчики для чистоты теста
        Category.category_count = 0
        Category.product_count = 0

        product1 = Product("Product 1", "Description 1", 100.0, 5)
        product2 = Product("Product 2", "Description 2", 200.0, 3)

        category1 = Category("Category 1", "Description 1", [product1])
        category2 = Category("Category 2", "Description 2", [product2])

        assert Category.category_count == 2
        assert Category.product_count == 2

    def test_category_with_empty_products(self):
        """Тест категории с пустым списком продуктов"""
        initial_count = Category.product_count
        category = Category("Empty Category", "No products", [])

        assert len(category.products) == 0
        # product_count не должен меняться, так как продуктов нет
        assert Category.product_count == initial_count
