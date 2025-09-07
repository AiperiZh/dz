# mkdir metalabs > cd metalabs > touch metalabs.py
# 2) cd .. > mkdir lesson 
# 3 rm - rf metalabs lesson 
# 4)mkdir hidden >  cd hidden > touch .secret > touch .env  > ls -a 
# 5) mkdir hello > mv .env hello/ 
# 6) cd .. > mv .secret .metalabs
# 7) cd ../../..  > ls -a Desktop / hidden / hello

'============ Data -types============'
#1) 
'''
1 способ:
num1 = int(input ('введите первое число: ')) #12
num2 = int (input ('Введите второе число: ')) #2
res = (((num1 + num2)*2)**2)- 5555
print (res) #-4771

2 способ:
a) res1 = num1 + num2
b)res2 = res1 * 2
c)res3 = res2**2
d) res4 = res3 - 5555
e) print(res4) #-4771
'''
'''
age = int (input ('Введите год вашего рождения: '))
#сколько ему будет через 2 года 
age1 = 2025 - age
print ('Через 2 года Вам будет',(age1 + 2),'лет.')
#сколько ему было 2 года назад
print ('2 года назад вам было ', (age1 - 2), 'лет')
#умножить возраст на 365
print (age1 * 365)
'''


#3
"""
age = int (input ('Введите Ваш возраст: '))
year = 31536000
sec = (age * 3153600)
print(f'Возраст человека {age}, количество секунд прожито - {sec}') 
"""
#4
'''
shokolad = int (input ('Напишите цену 1 шт шоколада: ')) #40
moloko = int (input ('Введите стоимость 1 бутылки молока: ')) #50
coffee = int (input ('Введите цену 1 банки кофе: ')) #60
amountsh = int (input ('Введите количество шоколада в 1 упаковке: ' )) #4
amountm = int (input ('Введите количество бутылок молока в 1 упаковке: ' )) #5
amountс = int (input ('Введите количество банок кофе в 1 упаковке: ' )) #6
pricesh = shokolad * amountsh
pricem = moloko * amountm
pricec = coffee * amountс
res = pricesh + pricem + pricec
print (f' Общая стоимость товаров в корзине {res} сом')
'''

#5
a = int(input ('Введите ширину прямоугольника: '))
b = int(input ('Введите длину прямоугольника: '))
p = 2 * (a + b)
print (f'Периметр прямоугольника равен: {p}')