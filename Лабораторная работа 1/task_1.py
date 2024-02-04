class Car:
    """Auto"""

    def __init__(self, color: str, type_body: int, name: str):
        if not isinstance(color, str):
            raise TypeError("Incorrect type(color)")

        if not isinstance(name, str):
            raise TypeError("Incorrect type(name)")

        if not type_body > 4:
            raise TypeError("incorrect number of type_body")

        self.color = color
        self.type_bode = type_body
        self.name = name

    def get_smb(self, number_of_wheels: int, mileage: int = 0) -> int:
        """
        Находит цену автомобиля по двум параметрам.


        :param number_of_wheels:  Количество колес автомобиля
        :param mileage:  Пробег автомобиля
        :return:  Возвращает значение типа int

        >>> machine = Car("red", 10, "ford")
        >>> machine.get_smb(4, 20000)

        """
        ...

    def get_smt(self, mass: int) -> int:
        """
        Высчитывает количество мест для пассажиров, на расчетах его массы (в кг)

        :param mass:  Масса автомобиля
        :return:    Возвращает значение типа int

        >>> machine = Car("red", 10, "ford")
        >>> machine.get_smt(1500)

        """
        ...

    def get_distance(self, fuel: str = "petrol", volume: int = "92") -> int:
        """
        Вычисляет примерное расстояние автомобиля, которое он сможет проехать (в км)

        :param fuel:  Тип топлива, такие как бензин, дизель и тд
        :param volume:  Вместимость бака
        :return:  Возвращает значение типа int
        """
        ...


class Hero:
    """ Герой Dota 2"""

    def __init__(self, attribute: str, type_of_attack: int, name: str):
        """
        Создает объект класса Hero

        :param attribute:  Выбрать атрибут героя (S - сила, U - универсал, A - ловкость, I - интеллект)
        :param type_of_attack:  Выбрать тип атаки героя (1 - ближняя атака, 2 - дальняя атака)
        :param name: Написать название героя
        """
        if not isinstance(attribute, str) and (
        not (attribute == "S" or attribute == "U" or attribute == "A" or attribute == "I")):
            raise TypeError("Incorrect attribute(type)")

        if not (0 < type_of_attack <= 2):
            raise TypeError("Incorrect type_of_attack")

        if len(name) > 20:
            raise TypeError("Incorrect length name")

        self.attribute = attribute
        self.type_of_attack = type_of_attack
        self.name = name

    def pick_rate(self, winrate: float) -> float:
        """
        Вычисляет winrate героя, основываясь на его частоте выбора
        :param winrate:  Написать частоту побед героя
        :return:  Возвращает значение типа float

        >>> AW = Hero("A", 2, "arc_warden")
        >>> AW.pick_rate(55.65)
        """
        ...

    def popular_item(self) -> str:
        """
        Находит самый популярный айтем на героя
        :return:  Возвращает значение типа str

        >>> AW = Hero("A", 2, "arc_warden")
        >>> AW.popular_item()
        """
        ...


class Table:
    """ Стол """

    def __init__(self, color: str, numbers_of_legs: int, material: str):
        """
        :param color: Цвет стола
        :param numbers_of_legs: Количество ножек у стола
        :param material: Материал из которого сделан стол
        """

        if not isinstance(color, str):
            raise TypeError("Incorrect type of color")
        if not isinstance(material, str):
            raise TypeError("Incorrect type of material")
        if not isinstance(numbers_of_legs, int):
            raise TypeError("Incorrect type of numbers of legs")

        self.color = color
        self.numbers_of_legs = numbers_of_legs
        self.material = material

    def strength_table(self) -> float:
        """
        Вычисляет прочность стола
        :return: Возвращает значение типа float

        >>> t1 = Table("green", 4, "wood")
        >>> t1.strength_table()
        """
        ...

    def mass_table(self, len: float, hight: float) -> float:
        """
        Вычисляет значение массы стола, используя его длину и высоту
        :param len:  Длина стола
        :param hight:  Высота стола
        :return:   Возвращает значение типа float

        >>> t1 = Table("green", 4, "wood")
        >>> t1.mass_table(12.12, 45.18)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
