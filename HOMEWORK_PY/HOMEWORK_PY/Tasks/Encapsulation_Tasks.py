'''
Задания №1
Разработайте класс с "полной инкапсуляцией", 
доступ к атрибутам которого и изменение данных 
реализуются через вызовы методов. В объектно-ориентированном 
программировании принято имена методов для извлечения 
данных начинать со слова get (взять), а имена методов,
в которых свойствам присваиваются значения, – со слова
set (установить). Например, get_field, set_field.
'''

class EncapsulationClass:
    def __init__(self, value1 = "", value2 = ""):
        self.__value1 = value1
        self.__value2 = value2

    def get_value1(self):
        return self.__value1

    def get_value2(self):
        return self.__value2

    def set_value1(self,value1):
        self.__value1 = value1
        
    def set_value2(self,value2):
        self.__value2 = value2

        
obj = EncapsulationClass("Hello", "World")
print(obj.get_value1())
print(obj.get_value2())
obj.set_value1("Goodbye")
obj.set_value2("Universe")
print(obj.get_value1())
print(obj.get_value2())



'''
Задания №2
Написать программу, в которой есть главный класс Games со 
статическим полем Year, опишите конструктор присваивающий 
значение полю Year, также опишите метод getName, который 
возвращает имя игры. На основе главного класса путем наследования 
опишите четыре класса PCGames, PS4Games, XboxGames, MobileGames. 
Добавьте каждому классу дополнительные поля и переопределите 
у всех классов метод getName.
'''


class Games:
    Year = 0
    
    def __init__(self, year):
        self.Year = year
    
    def getName(self):
        return "Name"


class PCGames(Games):
    platform = "PC"
    
    def getName(self):
        return "PC Game"


class PS4Games(Games):
    platform = "PS4"
    
    def getName(self):
        return "PS4 Game"


class XboxGames(Games):
    platform = "Xbox"
    
    def getName(self):
        return "Xbox Game"


class MobileGames(Games):
    platform = "Mobile"
    
    def getName(self):
        return "Mobile Game"


'''
Задания №3
Напишите программу с пустым классом Country. 
Опишите наследуемые от класса Country классы
Russia, Canada, Germany. Добавьте каждому классу 
поле population и опишите метод setPopulation
и getPopulation.

'''

class Country:
    pass

class Russia(Country):
    def __init__(self, population = ""):
        self.population = population

    def setPopulation(self,value):
        self.population = value

    def getPopulation(self):
        return self.population

class Canada(Country):
    def __init__(self, population = ""):
        self.population = population

    def setPopulation(self,value):
        self.population = value

    def getPopulation(self):
        return self.population

class Germany(Country):
    def __init__(self, population = ""):
        self.population = population

    def setPopulation(self,value):
        self.population = value

    def getPopulation(self):
        return self.population

russia = Russia()
russia.setPopulation(123456)
print(russia.getPopulation())

canada = Canada(5678916)
print(canada.getPopulation()) 

germany = Germany(456132)
print(germany.getPopulation()) 
