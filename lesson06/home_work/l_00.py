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
