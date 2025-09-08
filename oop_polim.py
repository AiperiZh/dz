'''Таск 1. Универсальный принтер
Описание:
Создай базовый класс `Document`, у которого есть метод `print_info()`.
Создай два подкласса — `PDFDocument` и `WordDocument`, каждый из которых
переопределяет метод `print_info()`.
Задача:
Напиши функцию `print_document_info(doc)`, которая принимает объект и вызывает
его метод `print_info()`.
Создай список из разных документов и передай их в эту функцию по очереди.

'''

# class Document:
#     def print_info(self):
#         print('документ')
    
# class PDFDocument(Document):
#     def print_info(self):
#         print('PDF документ')

# class WordDocument(Document):
#     def print_info(self):
#         print('Word документ')

# def print_document_info(doc):
#     doc.print_info()

# documents = [PDFDocument(), WordDocument(), Document()]

# for document in documents:
#     print_document_info(document)

'''
Таск 2. Животные говорят
Описание:
Базовый класс `Animal` с методом `make_sound()`.
Подклассы: `Dog`, `Cat`, `Cow`, каждый переопределяет `make_sound()` своим способом.
Задача:
Напиши функцию `make_animals_talk(animals: list)`, которая вызывает `make_sound()`
для каждого животного.
'''

# class Animal:
#     def make_sound(self):
#         print('звук животного')

# class Dog(Animal):
#     def make_sound(self):
#         print('гав - гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('мяу - мяу')

# class Cow(Animal):
#     def make_sound(self):
#         print('му - му')

# def make_animals_talk(animals:list):
#     for animal in animals:
#         animal.make_sound()

# animals_list = [Dog(), Cat(), Cow()]
# make_animals_talk(animals_list)

'''
Таск 3. Игрушки
Описание:
Базовый класс `Toy` с методом `play_sound()`.
Подклассы: `Car`, `Doll`, `Drum`.
Задача:
Симулируй работу магазина: перебери список из разных игрушек и запусти их звук.
'''

# class Toy:
#     def play_sound(self):
#         print('звук игрушки')

# class Car(Toy):
#     def play_sound(self):
#         print('бип -бип')

# class Doll(Toy):
#     def play_sound(self):
#         print( 'ля-ля')

# class Drum (Toy):
#     def play_sound(self):
#         print('парам - парам')

# def make_toys_talk(toys:list):
#     for toy in toys:
#         toy.play_sound()

# toys_list = [ Car(), Doll(), Drum()]
# make_toys_talk(toys_list)

'''
Таск 4. Фигуры и площадь
Описание:

Базовый класс `Shape` с методом `area()`.
Подклассы: `Circle`, `Rectangle`, `Triangle`.
Задача:
Создай список из разных фигур и выведи их площади через один цикл. Используй
`math.pi`, если надо.
'''

# import math

# class Shape:
#     def area(self):
#         print("площадь")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height

# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(3, 7)
# ]

# for shape in shapes:
#     print(f"Площадь {shape.__class__.__name__}: {shape.area()}")

'''
Таск 5. Банкомат
Описание:
Базовый класс `Card`, метод `withdraw(amount)`.
Подклассы: `CreditCard` (может уходить в минус), `DebitCard` (не может уходить в
минус).
Задача:
Симулируй списание денег с разных карт, используя одну и ту же функцию.

'''

class Card:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(amount):
        print('счет на карте')

class Creditcard(Card):
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Снято {amount}. Новый баланс: {self.balance}")

class DebitCard(Card):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Новый баланс: {self.balance}")

# закончен