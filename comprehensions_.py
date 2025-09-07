'''
1) Напишите list comprehension, который создаст список квадратов чисел от 1 до 10
2) Используя list comprehension, создайте список только из четных чисел от 1 до 20
3) Используя dict comprehension, создайте словарь, где ключ — число от 1 до 5, а значение — его квадрат.
4) вам дан список words = ["python", "java", "swift", "golang", "javascript"], используя list comprehension, создайте новый список из слов длиной больше 5 символов
5) Вам дан список, words = ["apple", "banana", "cherry"], используя list comprehension, получите список этих слов в верхнем регистре

'''

# 1
# 1) Напишите list comprehension, который создаст список квадратов чисел от 1 до 10

num1 = [i**2 for i in range(1, 11)]
print(num1)


# 2) Используя list comprehension, создайте список только из четных чисел от 1 до 20
num2 = [i for i in range(1, 21) if i % 2 == 0]
print(num2)


# 3) Используя dict comprehension, создайте словарь, где ключ — число от 1 до 5, а значение — его квадрат.
num3 = {i: i**2 for i in range(1, 6)}
print(num3)

# 4) вам дан список words = ["python", "java", "swift", "golang", "javascript"], 
# используя list comprehension, создайте новый список из слов длиной больше 5 символов
words = ["python", "java", "swift", "golang", "javascript"]
new_words = [i for i in words if len(i)> 5 ]
print(new_words)

#5) Вам дан список, words = ["apple", "banana", "cherry"],
#  используя list comprehension, получите список этих слов в верхнем регистре
words = ["apple", "banana", "cherry"]
upper_words = [i.upper() for i in words]
print(upper_words)