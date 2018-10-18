# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Person:
    def __init__(self, name, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name

# Добавлены аттрибуты mother, father
class Student(Person):
    def __init__(self, name, surname, birth_date, school, class_room, mother, father):
        # Явно вызываем конструктор родительского класса
        Person.__init__(self, name, surname, birth_date, school)
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),'class_char': class_room.split()[1]}
        self.mother = mother
        self.father = father

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'],
        self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

    # Метод для вывода родителей
    def parents(self):
        return "{} {}".format(self.mother, self.father)

class Teacher(Person):
    def __init__(self, name, surname, birth_date, school, teach_classes, school_subject, unique_subject ):
        Person.__init__(self, name, surname, birth_date, school)
        self.teach_classes = list(map(self.convert_class, teach_classes))
        self.school_subject = school_subject
        self.unique_subject = unique_subject

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        return {'class_num': int(class_room.split()[0]),'class_char': class_room.split()[1]}

# Теперь мы пользуемся классом Student, я его импортирую в свои различные программы.
students = [
    Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5 А", "Маргарита С.", "Петр И."),
    Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8 Б", "Петровна А.", "Инокентий С."),
    Student("Иван", "Петров", '12.11.1999', "8 гимназия", "4 В", "Лидова В.", "Абрам П."),
]

teachers = [Teacher("Александр", "Иванов", '10.11.1998', "8 гимназия", "1 А", "Математика", "да"),
            Teacher("Михаил", "Петров", '21.07.2000', "8 гимназия", "5 А", "Литература", "нет")
]

# Учебный год закончился
for student in students:
    student.next_class()

for num, student in enumerate(students, start=1):
    print("{}) {} класс: {}. Родители: {}".format(num, student.get_full_name(), student.class_room, student.parents()))

for num, teacher in enumerate(teachers, start=1):
    print("{}) {} класс: {}".format(num, teacher.get_full_name(), teacher.convert_class()))
