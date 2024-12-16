import doctest


class Table:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол".

        :param length: Длина стола в сантиметрах.
        :param width: Ширина стола в сантиметрах.
        :param height: Высота стола в сантиметрах.

        :raises ValueError: Если любой из размеров меньше или равен нулю, то вызываем ошибку.

        Примеры:
        >>> table = Table(90, 40, 75)
        """
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Длина, ширина и высота должны быть больше 0.")

        self.length = length
        self.width = width
        self.height = height

        def calculate_area(self) -> float:
            """
            Вычисление площади стола.

            :return: Высчитывает площадь стола.

            Примеры:
            >>> table = Table(90, 40, 75)
            >>> table.calculate_area(3600)
            """
            ...

        def adjust_height(self, new_height: float) -> None:
            """
            Устанавливает новую высоту стола.

            :param new_height: Новая высота стола в сантиметрах.

            :raises ValueError: Если новая высота меньше или равна нулю, то вызываем ошибку.

            Примеры:
            >>> table = Table(90, 40, 75)
            >>> table.adjust_height(80)
            """
            if new_height <= 0:
                raise ValueError("Новая высота должна быть больше 0.")
            ...


class Animal:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Животное".

        :param name: Имя животного
        :param age: Возраст животного (от 0 до 40)

        Примеры:
        >>> Animal = Animal("Шарик", 5)
        """
        if not (0 <= age <= 40):
            raise ValueError("Возраст животного должен быть в пределах от 0 до 40.")

        self.name = name
        self.age = age

    def eat(self, food: str) -> None:
        """
        Кормление животного.

        :param food: Название еды для животного

        Примеры:
        >>> animal = Animal("Шарик", 5)
        >>> animal.eat("Корм")
        """
        ...

    def sleep(self, hours: int) -> None:
        """
        Проверка количества часов сна животного.

        :param hours: Количество часов сна

        :raise ValueError: Если количество часов сна меньше 0, то вызываем ошибку.

        Примеры:
        >>> animal = Animal("Шарик", 5)
        >>> animal.sleep(6)
        """
        if hours <= 0:
            raise ValueError("Количество часов сна животного должно быть больше 0.")
        ...


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        """
        Чтение указанного количества страниц.

        :param pages_to_read: Количество страниц для чтения

        :raises ValueError: Если количество страниц для чтения меньше или равно 0, то вызываем ошибку.

        Примеры:
        >>> book = Book("Братья Карамазовы", "Ф. М. Достоевский", 992)
        >>> book.read(100)
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть больше 0.")
        ...

    def summary(self) -> str:
        """
        Получения краткого описания книги.

        :return: Краткая характеристика книга

        Примеры:
        >>> book = Book("Братья Карамазовы", "Ф. М. Достоевский", 992)
        >>> book.summary()
        """
        return f'Автор книги "{self.title}" - {self.author}. Она содержит {self.pages} страниц.'
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации