# КАЛЬКУЛЯТОР ИСПОЛЬЗУЯ СЛОВАРЬ И LAMBDA ФУНКЦИИ:
#     Напишите Калькулятор, который:
# 	1) Запрашивает у пользователя два числа.
# 	2) Запрашивает у пользователя операцию (+, -, *, /).
# 	3) Использует lambda-функции для выполнения соответствующей операции.
# 	4) Выводит результат на экран.
# 	5) Программа должна корректно обрабатывать деление на ноль(используйте try except)
# 	6) Можно использовать if-else для выбора нужной lambda-функции.
# 	7) реализовать программу с помощью словаря, где ключи — операции (+, -, *, /), а значения — соответствующие lambda-функции.

# **ПРИМЕЧАНИЕ: СРОК ВЫПОЛНЕНИЯ БУДЕТ СТОЯТЬ НА ПОНЕДЕЛЬНИК СЛЕДУЮЩЕЙ НЕДЕЛИ, ЗАДАЧА НЕОБЫЧНАЯ И НЕМНОГО ТРУДНАЯ, ПОЭТОМУ БУДЕТ ДАНО БОЛЬШЕ ВРЕМЕНИ**



lambda_func = lambda num1, num2: ... 
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
oper = input ('Какую операцию выполнить (+, -, *, /)\n')

# if oper == "+":
#     res = num1 + num2
# elif oper == "-":
#     res = num1 - num2
# elif oper =="*":
#     res = num1*num2
# elif oper == "/":
#     res = num1/num2
#     try:
#             raise ZeroDivisionError
#     except ZeroDivisionError:
#                 print ("Делить на ноль нельзя" or (res))
# else:
#     res = num1/num2
# print (res)

# lambda_func (num1,num2)

lambda_func = lambda num1, num2: ... 
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
oper = input ('Какую операцию выполнить (+, -, *, /)\n')

if oper == "+":
    res = num1 + num2
elif oper == "-":
    res = num1 - num2
elif oper =="*":
    res = num1*num2
   
try:
    res = num1/0
    print (res)
except ZeroDivisionError:
        print ("Делить на ноль нельзя")
else:
    res1 = num1/num2
    print (res1)
lambda_func (num1,num2)

