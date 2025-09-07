'''
ДЕКОРАТОРЫ:
    1) Напишите декоратор, который перед вызовом функции будет выводить сообщение "Выполнение функции..."
    2) Создайте декоратор, который будет умножать результат выполнения числовой функции на 2
    3) Создайте декоратор, который к строковому результату функции добавляет "!" в конце
    4) Создайте декоратор, который ограничит выполнение функции 3 вызовами
    Если функция вызывается больше 3 раз, выводить сообщение "Функция больше недоступна"
    5) Создайте декоратор, который будет выводить переданные аргументы перед вызовом функци
'''

#1 
# def notice (func):
#     def wrapper():
#         print( 'выполнение функции')
#         func()
#     return wrapper
    
# @notice
# def func():
#     print('Готово')

# func()


#2
# def result2(func):
#     def wrapper():
#         result = func()
#         return result * 2
#     return wrapper

# @result2
# def num ():
#     return 5
# print(num())



#3 
# def exclamation (func):
#     def wrapper():
#         result = func()
#         return result + "!"
#     return wrapper

# @exclamation
# def func_():
#     return 'Привет'

# print(func_())



#4 
# def limit (func):
#     func.calls = 0

#     def wrapper():
#         if func.calls < 3:
#             func.calls +=1
#             return func()
#         else:
#             print(" функция больше не доступна")
#     return wrapper

# @limit
# def word():
#     print("Привет")

# word()
# word()
# word()
# word()
# word()


#5
