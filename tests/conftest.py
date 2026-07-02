import pytest
from src.main import Product, Category


@pytest.fixture
def sample_product():
    """Фикстура с примером продукта"""
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_products():
    """Фикстура со списком продуктов"""
    return [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 3),
        Product("Product 3", "Description 3", 300.0, 7),
    ]


@pytest.fixture
def sample_category(sample_products):
    """Фикстура с примером категории"""
    return Category("Test Category", "Test Description", sample_products)
