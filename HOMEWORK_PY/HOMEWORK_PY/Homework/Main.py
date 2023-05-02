from Book import Book
from Car import Car
from Stadium import Stadium


book1 = Book("Книга", "2023", "Астана", "роман", "Имя Фамилия", 500)
book1.output_data()

book1.price = 600
print("Новая цена: ", book1.price)

book2 = Book()
book2.input_data()
book2.output_data()



car1 = Car("Машина", "2019", "машина", "2 л", "белый", 2000000)
car1.output_data()

car1.set_price(2200000)
print("Новая цена: ", car1.get_price())

car2 = Car()
car2.input_data()
car2.output_data()



stadium1 = Stadium("Стадион", "31 июля 2023", "Казахстан", "Алматы", 81000)
stadium1.output_data()

stadium1.set_capacity(85000)
print("Новая вместимость: ", stadium1.get_capacity())

stadium2 = Stadium()
stadium2.input_data()
stadium2.output_data()

