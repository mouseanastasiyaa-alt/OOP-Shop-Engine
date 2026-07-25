from src import Product, Category, Smartphone, LawnGrass, BaseProduct


def main():
    """Пример использования классов Product, Category и наследников"""

    print("=== Создание продуктов ===")
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("\n=== Создание смартфонов ===")
    # Создаем смартфоны
    smartphone1 = Smartphone(
        "iPhone 15 Pro", "Смартфон Apple", 120000.0, 3,
        "A17 Pro", "iPhone 15 Pro", "256GB", "Titanium"
    )
    smartphone2 = Smartphone(
        "Samsung Galaxy S24", "Смартфон Samsung", 110000.0, 5,
        "Snapdragon 8 Gen 3", "Galaxy S24", "256GB", "Black"
    )

    print("\n=== Создание газонной травы ===")
    # Создаем газонную траву
    grass1 = LawnGrass(
        "Газонная трава Premium", "Трава для газона", 500.0, 100,
        "Россия", 7, "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава Standard", "Трава для газона", 300.0, 50,
        "Россия", 5, "Зеленый"
    )

    print("\n=== Продукты ===")
    print(product1)
    print(product2)
    print(product3)

    print("\n=== Смартфоны ===")
    print(smartphone1)
    print(smartphone2)

    print("\n=== Газонная трава ===")
    print(grass1)
    print(grass2)

    # Создаем категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3, smartphone1, smartphone2]
    )

    category2 = Category(
        "Газонная трава",
        "Трава для газона",
        [grass1, grass2]
    )

    print("\n=== Категории ===")
    print(category1)
    print(category2)

    # Проверка сложения продуктов
    print("\n=== Сложение продуктов ===")
    print(f"Сумма смартфонов: {smartphone1 + smartphone2}")
    print(f"Сумма травы: {grass1 + grass2}")
    print(f"Сумма обычных продуктов: {product1 + product2}")

    # Проверка добавления невалидного объекта
    print("\n=== Проверка добавления невалидного объекта ===")
    try:
        category1.add_product("not a product")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Проверка абстрактного класса
    print("\n=== Проверка абстрактного класса ===")
    print(f"BaseProduct - абстрактный класс: {hasattr(BaseProduct, '__abstractmethods__')}")


if __name__ == "__main__":
    main()
