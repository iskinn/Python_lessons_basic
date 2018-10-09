# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def round_ext(a,b):
    x = round(a,b)
    return x

digit = float((input("Введите целое число с десятичной частью: ")))
number_of_characters = int((input("Введите кол-во знаков для округления дробной части введеного числа: ")))
x = round_ext(digit,number_of_characters)
print ("Округленное число: ",x)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# Функция работает для номеров билетов любой длинны, даже нечетной
def check_ticket(ticket):
    ticket_first_half = ticket[0:int(len(ticket)/2)]
    ticket_second_half = ticket[-int(len(ticket)/2):]
    if sum(int(i) for i in ticket_first_half) == sum(int(i) for i in ticket_second_half):
        return True
    else:
        return False

ticket = (input("Введите номер вашего билета: "))
result = check_ticket(ticket)
