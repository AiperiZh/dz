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
#     def __init__ (self, balance):
#         self.__balance = balance

#     def deposit(amount):
#         print('пополнение баланса')

#     def withdraw (amount):
#         if amount > 0:
#             ...


'''
2) Создай класс User в котором (задание по теме getters/setters):
		1) name — публичный атрибут
		2) password — приватный атрибут
		3) Метод get_password() который будет возвращать * вместо пароля
		4) Метод set_password(new_password), который будет проверять длину пароля, 
        и если она больше 6 символов, то меняет предыдущий на новый
        ПРИМЕЧАНИЕ: пароль должен состоять из букв и цифр
'''
 
class User:
    def __init__(self):
        
    name = 'Aiperi'
    __password = int('123aiperi')

    def get_password():
        return