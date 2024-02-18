class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def set_pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError()
        if  (pages <= 0) and (pages > 10000):
            raise ValueError
        self.pages = pages

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError()
        if (0 > duration) and (duration > 250):
            raise ValueError
        self.pages = duration

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

