# OOP Shop Engine

Проект для изучения объектно-ориентированного программирования на Python.

## Описание проекта

В этом проекте реализованы базовые классы для интернет-магазина с инкапсуляцией, наследованием и магическими методами.

### Класс Product

- **Приватные атрибуты**: `__price` (цена)
- **Публичные атрибуты**: `name`, `description`, `quantity`
- **Геттер**: `price` - возвращает цену товара
- **Сеттер**: `price` - устанавливает цену с проверкой
- **Класс-метод**: `new_product()` - создает продукт из словаря
- **Магические методы**: `__str__`, `__add__`

### Класс Category

- **Приватные атрибуты**: `__products` (список товаров)
- **Публичные атрибуты**: `name`, `description`
- **Атрибуты класса**: `category_count`, `product_count`
- **Методы**: `add_product()` - добавляет товар с проверкой типа
- **Геттер**: `products` - возвращает строковое представление
- **Магический метод**: `__str__`

### Классы-наследники

- **Smartphone** (наследник `Product`)
    - Добавлены атрибуты: `efficiency`, `model`, `memory`, `color`
- **LawnGrass** (наследник `Product`)
    - Добавлены атрибуты: `country`, `germination_period`, `color`

## Структура проекта

oop-shop-engine/
├── src/
│ ├── init.py # Инициализация пакета
│ ├── product.py # Классы Product, Smartphone, LawnGrass
│ └── category.py # Класс Category
├── tests/
│ ├── init.py
│ ├── conftest.py # Фикстуры
│ ├── test_product.py # Тесты для Product и наследников
│ └── test_category.py # Тесты для Category
├── main.py # Точка входа
├── data/
│ └── data.json # Данные для загрузки (опционально)
├── pyproject.toml # Конфигурация проекта
├── poetry.lock # Зависимости
├── check_all.bat # Скрипт для полной проверки
└── README.md # Документация

## Установка и запуск

```bash
# Клонирование репозитория
git clone https://github.com/mouseanastasiyaa-alt/OOP-Shop-Engine.git

# Установка зависимостей
poetry install

# Запуск программы
poetry run python main.py
## 📊 Отчет о покрытии тестами

Покрытие функционального кода составляет **100%** (более 75%).

| Файл | Строк | Покрыто | Процент |
|------|-------|---------|---------|
| src/product.py | 36 | 36 | 100% |
| src/category.py | 24 | 24 | 100% |
| src/__init__.py | 3 | 3 | 100% |
| **Итого** | **63** | **63** | **100%** |

### Как проверить покрытие локально:

```bash
# Установить зависимости
poetry install

# Запустить тесты с покрытием
poetry run pytest --cov=src --cov-report=html tests/

# Открыть отчет в браузере
start htmlcov/index.html
