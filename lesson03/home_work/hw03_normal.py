# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 1
    i = 1
    fib_result = []
    while i <= m:
        c = a + b
        a = b
        b = c
        i += 1
        if i >= n:
            fib_result.append(c)
    return fib_result

n = 5
m = 10

print("Искомые элементы: ",fibonacci(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for n in range(0,len(origin_list)-1):
        for i in range(0,len(origin_list)-1):
            if origin_list[i+1] < origin_list[i]:
                origin_list[i+1], origin_list[i] = origin_list[i], origin_list[i+1]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def list_filter(list_a,letter):
    b = []
    for i in list_a:
        if i == letter:
            b.append(i)
    return b

list_a = ['аркан', 'бревно', 'голобь', 'бревно', 'вода', 'дерево', 'ель', 'железо', 'заря','аркан',]
print(list_a)

letter = input("Введите слово из списка: ")
print(list_filter(list_a,letter))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

from math import sqrt

A1 = [1,1]
A2 = [2,4]
A3 = [6,2]
A4 = [7,5]

# Вычисляем длину отрезка между двумя координатами
def check(M, N):
    return sqrt((M[0] - N[0]) ** 2 + (M[1] - N[1]) ** 2)

length_A_B = check(A1,A2)
length_C_D = check(A3,A4)
length_A_C = check(A1,A3)
length_B_D = check(A2,A4)

if length_A_B == length_C_D and length_A_C == length_B_D:
    print("Congratulations!")
else:
    print("Try again..")
