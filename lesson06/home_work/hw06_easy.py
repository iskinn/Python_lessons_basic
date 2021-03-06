# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# =================================
#       Основы ООП
# =================================

# class - шаблон для создания объектов
# Классы содержат атрибуты - данные, и методы - функции для обработки данных

import math

class triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 =  x1
        self.y1 =  y1
        self.x2 =  x2
        self.y2 =  y2
        self.x3 =  x3
        self.y3 =  y3

    def triangle_square(self):
        S = abs( self.x1*(self.y2 - self.y3) + self.x2*(self.y3 - self.y1) + self.x3*(self.y1 - self.y2) ) / 2.0
        return(S)

    def triangle_high(self):
        a=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        S = triangle.triangle_square(triangle1)
        ha = 2*S / a
        return(ha)

    def triangle_perimetr(self):
        a=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        b=math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
        c=math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
        P = a + b + c
        return(P)

triangle1 = triangle(1,3,2,5,6,3)

S = triangle1.triangle_square()
print("Площадь равна = ", S)

H = triangle1.triangle_high()
print("Высота вершины А = ", H)

P = triangle.triangle_perimetr(triangle1)
print("Периметр = ", P)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class trapezoid():
    def __init__(self, name, x1, y1, x2, y2, x3, y3, x4, y4):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def __str__(self):
       return self.name

    def proverka(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))

        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")


    def side(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def perimeter(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return ( a+b+c+d)

    def area(self):
        c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
        d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
        a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
        b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
        return  ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))

fis_trap = trapezoid('one', 0,0,2,2,4,2,6,0)
fis_trap.proverka()
fis_trap.side()
print("Периметр трапеции = ",fis_trap.perimeter())
print("Площадь трапеции = ",fis_trap.area())
