class Book:
    def __init__(self, title="", year="", publisher="", genre="", author="", price=""):
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price

    @property
    def title(self):
        return self._title

    @property
    def year(self):
        return self._year
    
    @property
    def publisher(self):
        return self._publisher
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def author(self):
        return self._author
    
    @property
    def price(self):
        return self._price

    @title.setter
    def title(self, title):
        self._title = title

    @year.setter
    def year(self, year):
        self._year = year

    @publisher.setter
    def publisher(self, publisher):
        self._publisher = publisher

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @author.setter
    def author(self, author):
        self._author = author

    @price.setter
    def price(self, price):
        self._price = price

    def input_data(self):
        self._title = input("Введите название книги: ")
        self._year = input("Введите год выпуска: ")
        self._publisher = input("Введите издателя: ")
        self._genre = input("Введите жанр: ")
        self._author = input("Введите автора: ")
        self._price = input("Введите цену: ")

    def output_data(self):
        print("Название книги: ", self._title)
        print("Год выпуска: ", self._year)
        print("Издатель: ", self._publisher)
        print("Жанр: ", self._genre)
        print("Автор: ", self._author)
        print("Цена: ", self._price)
