# Шигалева_Александра 2_группа 4_поток
# Дано целое число n, каковы все его делители?
# Делитель, также известный как фактор или множитель, — это такое целое число m, на
# которое n делится без остатка. Например, делителями числа 12 являются 1, 2, 3, 4, 6 и 12.

import itertools

int_chislo = int(input("Введите целое число: "))
list_factor = itertools.count(1)
factor_chisla = 0

action = input(f"Найти делители числа {int_chislo}? (да/нет)")

if action == "да":
    print(f"Поиск всех делителей числа {int_chislo}...")
    for factor_chisla in list_factor:
        if int_chislo % factor_chisla == 0:
            if factor_chisla == int_chislo:
                break
            else:
                print(factor_chisla, end=" ")
    print(factor_chisla, end=" ")
elif action == "нет":
    print("завершение работы(")
else:
    print("ERROR: данного действия не существует...")