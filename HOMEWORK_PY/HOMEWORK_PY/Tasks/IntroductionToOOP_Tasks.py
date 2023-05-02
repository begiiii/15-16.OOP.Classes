'''
Задание № 2
Создайте класс «Город». Необходимо хранить в полях класса:
название города, название региона, название страны,
количество жителей в городе, почтовый индекс города, 
телефонный код города. Реализуйте методы класса для ввода 
данных, вывода данных, реализуйте доступ к отдельным полям
через методы класса.

'''


class City:
    def __init__(self, name, region, country, population, index):
        self.name = name
        self.region = region
        self.country = country
        self.population =population
        self.index = index

    
