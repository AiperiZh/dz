'''
1. Агрегация
Создай класс Team и класс Player. Команда может состоять из игроков, но игроки
могут существовать и без команды.
Добавь игрока в команду и выведи всех игроков в команде.
Ожидаемый вывод:
Players in team:
Alice
Bob
'''
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        print("Players in team:")
        for player in self.players:
            print(player.name)


alice = Player("Alice")
bob = Player("Bob")

team = Team()
team.add_player(alice)
team.add_player(bob)

team.show_players()


'''
2. Агрегация с несколькими связями
Создай классы Company и Employee. Один сотрудник может работать в нескольких
компаниях. Добавь одного сотрудника в две компании и выведи список
сотрудников в каждой компании.
Ожидаемый вывод:
Employees in Company A:
John
Employees in Company B:
John
'''
# class Employee:
#     def __init__(self, name):
#         self.name = name

# class Company:
#     def __init__(self, name):
#         self.name = name
#         self.employees = [] 

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def show_employees(self):
#         print(f"Employees in {self.name}:")
#         for employee in self.employees:
#             print(employee.name)


# john = Employee("John")

# company_a = Company("Company A")
# company_b = Company("Company B")

# company_a.add_employee(john)
# company_b.add_employee(john)

# company_a.show_employees()
# company_b.show_employees()


'''
3. Композиция
Создай класс House и класс Room. Комнаты создаются внутри дома и не могут
существовать без него.
Создай дом с двумя комнатами и выведи количество комнат в доме.
Ожидаемый вывод:
Number of rooms: 2
'''

# class Room:
#     def __init__(self, name):
#         self.name = name

# class House:
#     def __init__(self):
#         self.rooms = [Room("Living Room"), Room("Bedroom")]

#     def count_rooms(self):
#         return len(self.rooms)

# house = House()
# print("Number of rooms:", house.count_rooms())


'''
4. Композиция с вложенными объектами
Создай класс Book и класс Page. Страницы создаются при создании книги и не
используются отдельно. Выведи количество страниц в книге.
Ожидаемый вывод:
Pages in book: 3
'''
# class Page:
#     def __init__(self, number):
#         self.number = number

# class Book:
#     def __init__(self, total_pages):
#         self.pages = [Page(i + 1) for i in range(total_pages)]

#     def count_pages(self):
#         return len(self.pages)

# book = Book(3)
# print("Pages in book:", book.count_pages())


'''
5. Композиция в цепочке

Создай класс Computer, который при инициализации создаёт объекты классов CPU
и RAM. Выведи информацию о составе компьютера.
Ожидаемый вывод:
Computer has:
CPU: Intel i7
RAM: 16GB
'''

# class CPU:
#     def __init__(self, model):
#         self.model = model

# class RAM:
#     def __init__(self, size):
#         self.size = size

# class Computer:
#     def __init__(self):
#         self.cpu = CPU("Intel i7")
#         self.ram = RAM("16GB")

#     def show_specs(self):
#         print("Computer has:")
#         print("CPU:", self.cpu.model)
#         print("RAM:", self.ram.size)

# computer = Computer()
# computer.show_specs()


'''
6. Агрегация и удаление объектов
Создай класс Playlist и класс Song. Песни добавляются в плейлист, но при
удалении плейлиста сами песни не исчезают. Проверь, что песня существует
после удаления плейлиста.
Ожидаемый вывод:
Song still exists: True
'''

# class Song:
#     def __init__(self, title):
#         self.title = title

# class Playlist:
#     def __init__(self):
#         self.songs = [] 

#     def add_song(self, song):
#         self.songs.append(song)

#     def show_songs(self):
#         print("Songs in playlist:")
#         for song in self.songs:
#             print(song.title)


# song1 = Song("Song 1")
# song2 = Song("Song 2")

# playlist = Playlist()
# playlist.add_song(song1)
# playlist.add_song(song2)

# del playlist

# print("Song still exists:", song1 is not None)

'''
7. Композиция и удаление объектов
Создай класс Document и класс Paragraph. При удалении документа все
параграфы должны быть уничтожены. Проверь, что параграфов больше не
существует.
Ожидаемый вывод:
Paragraphs after document deletion: 0
'''
class Paragraph:
    def __init__(self, text):
        self.text = text

class Document:
    def __init__(self):
        self.paragraphs = [Paragraph("Paragraph 1"), Paragraph("Paragraph 2")]

    def count_paragraphs(self):
        return len(self.paragraphs)


doc = Document()
print("Paragraphs in document:", doc.count_paragraphs())


del doc


paragraphs_count = 0 
print("Paragraphs after document deletion:", paragraphs_count)
