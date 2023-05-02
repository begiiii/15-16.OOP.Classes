'''
Задание №1
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, 
цвет машины, цену. Реализуйте методы класса для ввода данных,
вывода данных, реализуйте доступ к отдельным полям через методы класса.
'''

class Car:
    def __init__(self, model="", year="", manufacturer="", engine_volume="", color="", price=""):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_volume(self):
        return self.engine_volume

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = input("Введите год выпуска: ")
        self.manufacturer = input("Введите производителя: ")
        self.engine_volume = input("Введите объем двигателя: ")
        self.color = input("Введите цвет машины: ")
        self.price = input("Введите цену: ")

    def output_data(self):
        print("Название модели: ", self.model)
        print("Год выпуска: ", self.year)
        print("Производитель: ", self.manufacturer)
        print("Объем двигателя: ", self.engine_volume)
        print("Цвет машины: ", self.color)
        print("Цена: ", self.price)