# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
a=[2, -5, 8, 9, -25, 25, 4]
b=[]
for i in a:
    if i > 0:
        x = math.sqrt(i) 
        if x - int(x) == 0:
            b.append(int(x))
print(b)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

import datetime
import locale
loc=locale.getlocale()
locale.setlocale(locale.LC_ALL, ('RU','UTF8'))

days = [
"undefined",
"первое",
"второе",
"третье",
"четвертое",
"пятое",
"шестое",
"седьмое",
"восьмое",
"девятое",
"десятое",
"одиннадцатое",
"двенадцатое",
"тринадцатое",
"четырнадцатое",
"пятнадцатое",
"шестнадцатое",
"и т.п."
]

today = "02.11.2013"
b = today.split('.')
day = int(b[0])
month = int(b[1])
year = b[2]

print(days[day], datetime.date(1900, month, 1).strftime('%B'), year, "года")

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

a=[]
while len(a) <= 100:
    a.append(random.randint(-100,100))
print(a)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

a=[1, 2, 4, 5, 6, 2, 5, 2]
b=[]
c=[]

for i in a:
    if a.count(i) > 1:
        b.append(i)
    else:
        c.append(i)

print(a)
print(b)
print(c)
