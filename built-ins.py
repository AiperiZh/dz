'''
Перейти к основному контенту
Google КлассКласс
Python
Задание. Тема "Built-in functions"

BUILT-INS:
    1) Даны два списка:
    names = ['Nikita', 'Katana', 'Toma']
    ages = [25, 30, 35]
    Создайте словарь, в котором ключи — это имена, а значения — соответствующие им возраста

    2) Дана строка:
    text = "python"
    при помощи определенной встроенной функции выведите индексы и символы, начиная с 1

    3) Дан список строк с числами:
    numbers = ["10", "20", "30", "40"]
    Преобразуйте его в список целых чисел

    4) Дан список слов:
    words = ["apple", "banana", "cherry", "dog", "elephant"]
    Отфильтруйте и оставьте только те слова, которые начинаются с буквы d

    5) Дан список чисел:
    numbers = [1, -2, 3, -4, 5, -6]
    Сначала удалите отрицательные числа при помощи filter, затем возведите оставшиеся числа в квадрат с помощью map

    6) Даны два списка:
    students = ["Alice", "Bob", "Charlie", "David"]
    scores = [85, 92, 78, 90]
    УСЛОВИЯ ЗАДАНИЯ:
    	1.	Используйте zip, чтобы соединить студентов и их оценки
	    2.	С помощью filter оставьте только тех, у кого оценка больше 80
	    3.	Пронумеруйте оставшихся студентов, начиная с 1, используя enumerate
	    4.	Преобразуйте результат в список кортежей (номер, имя, оценка)
'''

#1
# names = ['Nikita', 'Katana', 'Toma']
# ages = [25, 30, 35]
# people = dict(zip(names, ages))
# print(people)

# 2
# text = "python"
# text = enumerate('text', start = 1)
# print(list(text))

# #3
# numbers = ["10", "20", "30", "40"]
# mapped = map(int, numbers)
# print(list(mapped))

#4
words = ["apple", "banana", "cherry", "dog", "elephant"]
filtered = (filter(lambda word: word.startswith('d'), words))
print(list(filtered))

#5
numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = list(filter(lambda x: x > 0, numbers))
squared_numbers = list(map(lambda x: x**2, positive_numbers))
print(squared_numbers)


#6
# students = ["Alice", "Bob", "Charlie", "David"]
# scores = [85, 92, 78, 90]
# student_scores = zip(students, scores)
# # print(list(student_scores))

# high_scores = filter(lambda x: x[1] > 80, student_scores)
# result = list(enumerate(high_scores, start=1))
# result = [(num, name, score) for num, (name, score) in result]
# print(result)
