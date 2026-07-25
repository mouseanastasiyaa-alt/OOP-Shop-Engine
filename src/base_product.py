from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        """Сеттер для цены"""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение продуктов"""
        pass
   