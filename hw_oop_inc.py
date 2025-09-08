'''ИНКАПСУЛЯЦИЯ:
    1) Создай класс BankAccount с приватным __balance. Добавь методы:
	    1) deposit(amount) – пополнение баланса
		2) withdraw(amount) – снятие (он должен снимать не больше текущего баланса)
		3) get_balance() – возвращает баланс
    
    3) Создайте класс Employee у которого есть:
		1) name – имя сотрудника
		2) __salary (приватный атрибут)
		3) salary (геттер) – возвращает зарплату
		5) salary (сеттер) – изменяет зарплату (не меньше 30_000)
    4) Создайте класс Circle у которого есть:
		1) radius (геттер/сеттер, не < 0).
		2) area (геттер) – вычисляет площадь (число пи * радиус в квадрате).

        Затем:

        Создайте дочерний класс Cylinder(Circle) и добавьте в него:
		    1)height (геттер/сеттер, не < 0)

'''

# class BankAccount:
#     def __init__ (self, balance=0):
#       self.__balance = balance

#     def deposit (self,amount):
#       self.__balance  += amount

#     def withdraw (self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print('Недостаточно средств')


#     def get_balance(self):
#          return self.__balance


'''
2) Создай класс User в котором (задание по теме getters/setters):
		1) name — публичный атрибут
		2) password — приватный атрибут
		3) Метод get_password() который будет возвращать * вместо пароля
		4) Метод set_password(new_password), который будет проверять длину пароля, 
        и если она больше 6 символов, то меняет предыдущий на новый
        ПРИМЕЧАНИЕ: пароль должен состоять из букв и цифр
'''
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password

#     @property
#     def password(self):
#         return '*' * len(self.__password)

#     @password.setter
#     def password(self, new_password):
#         if len(new_password) <= 6:
#             print("Пароль слишком короткий!")
#             return

#         if not any(ch.isalpha() for ch in new_password):
#             print("Пароль должен содержать буквы!")
#             return

#         if not any(ch.isdigit() for ch in new_password):
#             print("Пароль должен содержать цифры!")
#             return

#         self.__password = new_password
#         print("Пароль изменён!")




''' 3) Создайте класс Employee у которого есть:
		1) name – имя сотрудника
		2) __salary (приватный атрибут)
		3) salary (геттер) – возвращает зарплату
		5) salary (сеттер) – изменяет зарплату (не меньше 30_000)
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 30000:
            self.__salary = new_salary
            print(f"Зарплата изменена на {new_salary}")
        else:
            print("Зарплата не может быть меньше 30_000")


'''
4) Создайте класс Circle у которого есть:
		1) radius (геттер/сеттер, не < 0).
		2) area (геттер) – вычисляет площадь (число пи * радиус в квадрате).

        Затем:

        Создайте дочерний класс Cylinder(Circle) и добавьте в него:
		    1)height (геттер/сеттер, не < 0)
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self.__radius = value
        else:
            print("Радиус не может быть меньше 0!")

    @property
    def area(self):
        return math.pi * self.__radius ** 2  

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)  
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value
        else:
            print("Высота не может быть меньше 0!")
            

# закончен, в гитхаб надо добавить 