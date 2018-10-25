#!/usr/bin/python3

import random, sys

class Cards:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def print_card(self, text):
        print(text)
        print(' '.join(self.numbers[0:9]))
        print(' '.join(self.numbers[9:18]))
        print(' '.join(self.numbers[18:27]))
        print("---------------------------")

    def generate_cards(self):
        a = []
        for random_number in range(1,91): a.append((str(random_number)).rjust(2))
        random.shuffle(a)
        x = a[0:5]
        y = a[50:55]
        z = a[85:90]
        for random_number in range(1,5): x.append('  ')
        for random_number in range(1,5): y.append('  ')
        for random_number in range(1,5): z.append('  ')
        random.shuffle(x)
        random.shuffle(y)
        random.shuffle(z)
        return x + y + z

    def count(self,numbers,i):
        return self.numbers.count(i)

class Bochonki:
    def __init__(self, bochonok_list):
        self.bochonok_list = bochonok_list

    # Бочонки генерим сразу все в случайном порядке
    def bochonki_generate(self):
        a = []
        for number in range(1,91): a.append((str(number)).rjust(2))
        random.shuffle(a)
        return a

def game(card_m, card_c):
    # переменные для подсчета удачных ходов, если = 25, то победа
    card_m_success_count = 0
    card_c_success_count = 0

    for i in bochonki.bochonok_list:
        # выводим очередной бочонок
        print("\nВыпало число:", i)
        card_m.print_card("\n---- Это ваша карточка ----")
        card_c.print_card("\n- Это карточка компьютера -")
        otvet = input("Закрыть число? y/[n]:")

        # Закрываем свое число
        if otvet == 'y':
            if card_m.numbers.count(i) == 1:
                for n,m in enumerate(card_m.numbers):
                    if m == i:
                        card_m.numbers[n] = '--'
                        card_m_success_count += 1
                        if card_m_success_count == 25:
                            print("Вы выиграли!")
                            sys.exit()
            else:
                print("Вы ошиблись! Игра окончена.")
                sys.exit()
        if otvet != 'y' and card_m.numbers.count(i) == 1:
            print("Вы ошиблись! Игра окончена.")
            sys.exit()

        # Закрываем число компьютера
        if card_c.numbers.count(i) == 1:
            for n,m in enumerate(card_c.numbers):
                  if m == i:
                      card_c.numbers[n] = '--'
                      card_c_success_count += 1
                      if card_c_success_count == 25:
                            print("Выиграли компьютер!")
                            sys.exit()

# инициализируем пустые экземпляры классов
my_card = Cards([])
comp_card = Cards([])
bochonki = Bochonki([])

# заполняем экземпляры классов через вызовы методов
my_card.numbers = my_card.generate_cards()
comp_card.numbers = comp_card.generate_cards()
bochonki.bochonok_list = bochonki.bochonki_generate()

# вызываем функцию игры
game(my_card, comp_card)
