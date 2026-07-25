class LogMixin:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # Получаем имя класса
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        params = ", ".join([repr(arg) for arg in args])
        if kwargs:
            params += ", " + ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])

        # Выводим информацию о создании объекта
        print(f"{class_name}({params})")

        # Вызываем следующий конструктор в цепочке наследования
        super().__init__(*args, **kwargs)
