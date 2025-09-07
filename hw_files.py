'------FILES:'
'''
1) Создайте файл, внесите туда небольшой текст. 
В программе откройте этот файл и выведите содержимое на экран.
'''

# file = open ('homeworks/hw_file.txt', 'r')
# print(file.read())
# file.close()
# print(file.closed)


'--------------------------------'
'''
2)Создайте файл users.txt. Напишите программу которая спрашивает 
у пользователя его Логин и Пароль и записывает в файл users.txt.
'''

# file = open ('users.txt', 'w')
# file.write(input ('Введите Ваш логин: '))
# file.write(input ('Введите Ваш пароль: '))
# file.close()
# print(file.closed)



'----------------------------------'
'''
3) Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, 
то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. 
Подсказка: используйте ключевое слово in.
'''

# with open ('homeworks/hw_file.txt', 'r') as file:
#     text = file.read()
# if 'w' in text:
#     print('Да, в тексте есть w')
# else:
#     print('В тексте нет w')

# print(file.closed)




'--------------------------------------'
'''
 4) Создайте текстовый файл python.txt и запишите в него следующий текст:
    
    Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и
    выведите на экран все полученные слова.
'''

# with open ('python.txt', 'r') as file:
#     text = file.read()
#     print(text)

# words = text.split()
# print(words)

# o_words = []
# for word in words:
#     if 'o' in word:
#         print(word)


'---------------------------------------'
'''
 5) Возьмите следующий текст:
    """
    .detacilpmoc naht retteb si xelpmoC
    .xelpmoc naht retteb si elpmiS
    .ticilpmi naht retteb si ticilpxE
    .ylgu naht retteb si lufituaeB
    """
    Запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.
'''

# file = open ('hw_file.txt', 'r')
# text = file.read()
# print(text[::-1])
# file.close()
# print(file.closed)


'----------------------------------------------'
'''
 6) Создайте файл и запишите туда следующий текст:
    """
    123
    aaa456
    fxdya 5 0 0
    """
    В каждой строчке есть цифры, которые вместе дадут число.
    Посчитайте сумму всех чисел.
'''

file123 = open ('hw.txt', 'r')
text = file123
print(text.read())

m = []
for i in text:
    if i.isdigit():
        m.append(int(i))
print(sum(m))

