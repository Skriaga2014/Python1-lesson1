'''
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
'''

a = input ("Введите значение переменной а: ")
b = input ("Введите значение переменной b: ")

c = a
a = b
b = c

# ИЛИ a,b = b,a

print("a =", a, "   b =", b)

#