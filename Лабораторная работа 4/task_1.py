class Auto:
    """
    Класс "Автомобиль". Базовый класс
    :param mark: Марка машины (неизменяемая переменная)
    :param vinNumber: ВИН номер автомобиля (protect переменная, имеющая getter и setter)
    :param color: Цвет машины (protect переменная, имеющая getter и setter)
    :param yearOfIssue: Год выпуска автомобиля (неизменяемая переменная)
    """
    def __init__(self, mark: str, vinNumber: str, color: str, yearOfIssue: int):
        self.mark = mark
        self.vinNumber = vinNumber
        self.color = color
        self.yearOfIssue = yearOfIssue

    # getters
    @property
    def mark(self) -> str:
        return self._mark

    @property
    def yearsOfIssue(self) -> int:
        return self._yearsOfIssue

    @property
    def vinNumber(self) -> str:
        return self._vinNumber

    @vinNumber.setter
    def vinNumber(self, vinNumber: str) -> None:
        if not isinstance(vinNumber, str):
            raise TypeError("Incorrect type VIN number")
        if len(vinNumber) != 20:
            raise ValueError("Incorrect VIN number")

        self.vinNumber = vinNumber

    @property
    def color(self) -> str:
        return self.color

    @color.setter
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError("Incorrect type color")

        self.color = color


    def get_price(self, country: str) -> float:
        """
        Метод должен выводить цену автомобиля в зависимости от страны, в которой он продается
        """
        return f"Цена автобомиля = {self.yearOfIssue * 1000 * len(self.mark)}"


    def __str__(self) -> str:
        return f"Автомобиль марки:{self._mark!r}"

    def __repr__(self) -> None:
        return f"{self.__class__.__name__}(mark={self._mark!r}, vinNumber={self._vinNumber}, color={self._color}, yearOfIssue={self.yearOfIssue})"

class PassAuto(Auto):
    """
    Класс "Автомобиль". Базовый класс
    :param mark: Марка машины (неизменяемая переменная)
    :param vinNumber: ВИН номер автомобиля (protect переменная, имеющая getter и setter)
    :param color: Цвет машины (protect переменная, имеющая getter и setter)
    :param yearOfIssue: Год выпуска автомобиля (неизменяемая переменная)
    :param numberOfPass: Количество пассажиров, вместимость автомобиля(неизменяемая переменная)
    :param maxSpeed: Максимальная скорость (изменяемая переменная)
    """

    def __init__(self, mark: str, vinNumber: str, color: str, yearOfIssue: int, numberOfPass, maxSpeed: float):
        super().__init__(mark, vinNumber, color, yearOfIssue)
        self.numberOfPass = numberOfPass
        self.get_maxSpeed = maxSpeed

    @property
    def numberOfPass(self) -> int:
        return self._numberOfPass

    @property
    def maxSpeed(self) -> float:
        return self._maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed: float) -> None:
        if not isinstance(maxSpeed, float):
            raise TypeError("Incorrect type max speed")
        self.maxSpeed = maxSpeed

    def get_maxDistance(self, maxSpeed: float, power: int) -> float:
        """
        Находит максимальное расстояние, которое машина способная проехать
        """
        return f"Максимальное расстояние = {(self.maxSpeed * 2 - self.power)}"

    def get_price(self, country: str) -> float:
        """
        Перегружаем метод нахождения цены автомобиля, допускаем, что цена за пассажирский транспорт облагается бОльшим налогом
        """
        return f"Цена автобомиля = {self.yearOfIssue * 1000 * len(self.mark) * 1.13}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self._mark!r}, vinNumber={self._vinNumber}, color={self._color}, yearOfIssue={self.yearOfIssue}, numberOfPass={self.numberOfPass}, maxSpeed={self.maxSpeed})"

if __name__ == "__main__":
    # Write your solution here
    pass
