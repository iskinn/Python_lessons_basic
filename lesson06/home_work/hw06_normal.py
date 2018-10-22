# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname, second_name, birth_date, school):
        self.name = name
        self.surname = surname
        self.second_name = second_name
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_FIO(self):
        return self.name + ' ' + self.surname[0:1] + '. ' + self.second_name[0:1] + '. '

    def set_name(self, new_name):
        self.name = new_name

# Добавлены аттрибуты mother, father
class Student(Person):
    def __init__(self, name, surname, second_name, birth_date, school, class_room, mother, father):
        # Явно вызываем конструктор родительского класса
        Person.__init__(self, name, surname, second_name, birth_date, school)
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
    def __init__(self, name, surname, second_name, birth_date, school, teach_classes, school_subject, unique_subject ):
        Person.__init__(self, name, surname, second_name, birth_date, school)
        self.teach_classes = ','.join(teach_classes)
        self.school_subject = school_subject
        self.unique_subject = unique_subject

# 1. Получить полный список всех классов школы
def school_classes():
    classes = []
    for num, student in enumerate(students, start=1):
        classes.append(student.class_room)
    return list(set(classes))

# 2. Получить список всех учеников в указанном классе
def students_in_class():
    print("Это список всех классов школы: ",""','.join(school_classes()))
    school_class = input("Выберите класс из списка: ")
    list_students = []
    for num, student in enumerate(students, start=1):
        if school_class == student.class_room:
            list_students.append(student.get_FIO())
    return list_students

# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
def student_subjects():
    student_surname = input("Введите фамилию ученика: ")
    list_subjects = []
    for num, student in enumerate(students, start=1):
        if student_surname == student.surname:
            for nume, teacher in enumerate(teachers, start=1):
                if teacher.teach_classes.count(student.class_room) > 0:
                    list_subjects.append(teacher.school_subject)
    return list_subjects

# 4. Узнать ФИО родителей указанного ученика
def exact_student_parents():
    student_surname = input("Введите фамилию ученика: ")
    for num, student in enumerate(students, start=1):
        if student_surname == student.surname:
            return student.parents()

# 5. Получить список всех Учителей, преподающих в указанном классе
def teachers_in_class():
    print("Это список всех классов школы: ",""','.join(school_classes()))
    school_class = input("Выберите класс из списка: ")
    list_teachers = []
    for num, teacher in enumerate(teachers, start=1):
        if teacher.teach_classes.count(school_class) > 0:
            list_teachers.append(teacher.get_full_name())
    return list_teachers

students = [
    Student("Александр", "Иванов", "Григорьевич",'10.11.1998', "8 гимназия", "4 В", "Маргарита С.", "Петр И."),
    Student("Петр", "Сидоров", "Антонович",'10.01.1995', "8 гимназия", "8 Б", "Петровна А.", "Инокентий С."),
    Student("Иван", "Петров", "Михайлович",'12.11.1999', "8 гимназия", "4 В", "Лидова В.", "Абрам П."),
]

teachers = [Teacher("Александр", "Иванов", "Инокентиевич",'10.11.1998', "8 гимназия", ["1 А", "4 В", "8 Б"], "Математика", "да"),
            Teacher("Михаил", "Петров", "Кириллович", '21.07.2000', "8 гимназия", ["3 Б", "4 В", "8 Б"], "Литература", "нет")
]

# Учебный год закончился
#for student in students:
#    student.next_class()

print("\nВсе преподаватели:")
for num, teacher in enumerate(teachers, start=1):
    print("{}) {}. Предмет: {}. Уникальный: {}. Преподает в классах: {}".format(num, teacher.get_full_name(), teacher.school_subject, teacher.unique_subject, teacher.teach_classes))

print("Все ученики:")
for num, student in enumerate(students, start=1):
    print("{}) {} класс: {}. Родители: {}".format(num, student.get_full_name(), student.class_room, student.parents()))

#print("Все классы школы",', '.join(school_classes()))
#print("В этом классе учатся: ", ', '.join(students_in_class()))
#print("Предметы этого ученика: ", ', '.join(student_subjects()))
#print("Родители этого ученика: ", exact_student_parents())
print("Все преподаватели этого класса: ", ', '.join(teachers_in_class()))
