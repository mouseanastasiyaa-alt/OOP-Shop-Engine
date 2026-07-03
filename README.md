# OOP Shop Engine

Проект для изучения объектно-ориентированного программирования на Python.

## Описание проекта

Реализованы базовые классы для интернет-магазина:

- **Product** - класс для представления товара
- **Category** - класс для представления категории товаров

## Структура проекта
oop-shop-engine/
├── src/
│ ├── init.py # Инициализация пакета
│ ├── product.py # Класс Product
│ └── category.py # Класс Category
├── tests/
│ ├── init.py
│ ├── conftest.py # Фикстуры для тестов
│ ├── test_product.py # Тесты для Product
│ └── test_category.py # Тесты для Category
├── main.py # Точка входа
├── pyproject.toml # Конфигурация проекта
└── README.md # Документация

## Установка и запуск

```bash
# Установка зависимостей
poetry install

# Запуск программы
poetry run python main.py

# Запуск тестов
poetry run pytest tests/ -v

# Проверка покрытия
poetry run pytest --cov=src --cov-report=term tests/
