class Teacher:
    def __init__(self, name, surname, birth_date, school, teach_classes):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.teach_classes = list(map(self.convert_class, teach_classes))
        #self.teach_classes = teach_classes

    def convert_class(self, class_room):
        return {'class_num': int(class_room.split()[0]),'class_char': class_room.split()[1]}

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


teachers = [
    Teacher("Александр", "Иванов", '10.11.1998', "8 гимназия", "1 А"),
    Teacher("Михаил", "Петров", '21.07.2000', "8 гимназия", "5 А"),
]

for num, teacher in enumerate(teachers, start=1):
    print("{}) {} класс: {}".format(num, teacher.get_full_name(), teacher.class_room()))
