# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = [name["first_name"] for name in students]
# first variant
for name in set(names):
    print(f'{name}: {names.count(name)}')
# second variant
for name in list(dict.fromkeys(names)):
    print(f"{name}: {names.count(name)}")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = [name["first_name"] for name in students]
famous_count_name = 0
famous_name = ""
for name in names:
    if names.count(name) > famous_count_name:
        famous_count_name = names.count(name)
        famous_name = name

print(f"Самое частое имя среди учеников: {famous_name}")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ], [  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
class_count = len(school_students)


def get_famous_name(names):
    famous_count_name = 0
    famous_name = ""
    for name in names:
        if names.count(name) > famous_count_name:
            famous_count_name = names.count(name)
            famous_name = name
    return famous_name


for class_room in range(class_count):
    names = [name["first_name"] for name in school_students[class_room]]
    print(f"Самое частое имя в классе {class_room + 1}: {get_famous_name(names)}")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_room in school:
    male = 0
    female = 0
    for student in class_room['students']:
        if is_male.get(student['first_name']):
            male += 1
        else:
            female += 1
    print(f"Класс {class_room['class']}: девочки {female}, мальчики {male}")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

max_male_count = 0
max_male_class_room = ""
max_female_count = 0
max_female_class_room = ""
for class_room in school:
    male = 0
    female = 0
    for student in class_room['students']:
        if is_male.get(student['first_name']):
            male += 1
        else:
            female += 1
    if male > max_male_count:
        max_male_count = male
        max_male_class_room = class_room['class']
    if female > max_female_count:
        max_female_count = female
        max_female_class_room = class_room['class']
print(f"Больше всего мальчиков в классе {max_male_class_room}")
print(f"Больше всего девочек в классе {max_female_class_room}")
