'''
1. Абстрактный транспорт
Создай абстрактный класс Transport с абстрактным методом move(). 
Реализуй два класса Car и Plane, которые наследуются от Transport и реализуют метод move() по-
своему.
Пример вывода:
Car is moving on the road
Plane is flying in the sky
# '''

from abc import ABC, abstractmethod
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         ...

# class Car(Transport):
#     def move(self):
#         print('Car is moving on the road')

# class Plane(Transport):
#     def move(self):
#         print('Plane is flying in the sky')

'''
2. Платёжная система
Создай абстрактный класс PaymentMethod с методом pay(amount). Сделай классы
CreditCard и PayPal, реализующие этот метод с выводом способа оплаты и суммы.
Пример вывода:
Оплата 1000 через Credit Card
Оплата 500 через PayPal
'''

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         ...

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         print('Оплата 1000 через Credit Card')

# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         print('Оплата 500 через PayPal')


'''
3. Фигуры и площадь
Создай абстрактный класс Shape с методом area(). Реализуй классы Circle и Rectangle с
соответствующим вычислением площади.
Пример вывода:
Площадь круга: 78.5
Площадь прямоугольника: 200
'''
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self,width,heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth
    
circle = Circle(5)
rectangle = Rectangle(20, 10)

print(f" Площадь круга: {circle.area()}")
print(f" площадь прямоугльника: {rectangle.area()}")


'''
4. Устройства вывода
Определи абстрактный класс OutputDevice с методом display(text). Создай Monitor и
Printer, которые выводят текст по-разному (например, просто через print, но с
разными префиксами).
Пример вывода:
[Monitor] Hello, world!
[Printer] Hello, world!
'''

class OutputDevice(ABC):
    @abstractmethod
    def display(self,text):
        ...

class Printer(OutputDevice):
    def display(self, text):
        print(f"[Printer]{text}")

class Monitor(OutputDevice):
    def display(self, text):
        print(f"[Monitor] {text}")

devices= [Printer(), Monitor()]
for device in devices:
    device.display('Hello, world')


'''
5. Абстрактный животный класс
Создай абстрактный класс Animal с методом make_sound(). Создай два класса Dog и
Cat, которые реализуют этот метод (выводят «Гав!» и «Мяу!» соответственно).
Пример вывода:

Гав!
Мяу!
'''
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         ...

# class Dog(Animal):
#     def make_sound(self):
#         print('гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('мяуу')

# animals = [Dog(), Cat()]
# for a in animals:
#     a.make_sound()

'''
6. Абстрактный работник
Определи класс Employee с методом calculate_salary(). Сделай Developer и Manager,
возвращающие зарплату с разными расчётами (фикс + бонус, почасовая и т.п.).
Пример вывода:
Зарплата разработчика: 5000
Зарплата менеджера: 7000
'''
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         ...

# class Developer(Employee):
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def calculate_salary(self):
#         return self.salary + self.bonus


# class Manager(Employee):
#     def __init__(self, salary, hours_worked):
#         self.hours_worked = hours_worked
#         self.salary = salary

#     def calculate_salary(self):
#         return self.hours_worked * self.salary

# dev = Developer(salary=4000, bonus=1000)
# mgr = Manager(hours_worked=140, salary=50)

# print(f"Зарплата разработчика: {dev.calculate_salary()}")
# print(f"Зарплата менеджера: {mgr.calculate_salary()}")

'''
7. Интерфейс базы данных
Создай абстрактный класс Database с методами connect() и disconnect(). Реализуй
классы MySQLDatabase и PostgreSQLDatabase, которые выводят информацию о
подключении/отключении.
Пример вывода:
Подключение к MySQL
Отключение от MySQL
Подключение к PostgreSQL
Отключение от PostgreSQL
'''
class Database(ABC):
    @abstractmethod
    def connect(self):
        ...
    def disconnect(self):
        ...

class MySQLDatabase(Database):
    def connect(self):
        print('подключение к MySQL')
    def disconnect(self):
        print('Отключение от MySQL')

class PostgreSQLDatabase(Database):
    def connect(self):
        print('подключение к PostgreSQL')
    def disconnect(self):
        print('Отключение от PostgreSQL')

databases = [ MySQLDatabase(), PostgreSQLDatabase()]

for db in databases:
    db.connect()
    db.disconnect()