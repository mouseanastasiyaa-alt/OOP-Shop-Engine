from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты Product или его наследников. Получен {type(product).__name__}")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для получения списка продуктов в виде строки"""
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
