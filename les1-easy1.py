'''
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
'''

from random import randint as rand

a = rand(1,100000000)                                               # Случайное число от 1 до 100000000
n = 0                                                               # Количество цифер в случайном числе
for i in range(100):                                                # Устанавливаем максимальное кол-во цифер - 100
    if 10**i < a:                                                   # Смотрим, в какую макс. степень нужно возвести 10,
        n = i+1                                                     # чтобы число оставалось < случ.числа. Прибавляем 1

                                                # ВАРИАНТ 1:
print("Число -", a)
print("Вариант 1:")
for i in reversed(range(1, n+1)):                                   # Определяем каждую цифру в случайной числе
    if a > 10 ** (i - 1): print(a % (10 ** i) // (10 ** (i - 1)))


                                                #ВАРИАНТ 2:
print("Число -", a)
print("Вариант 2:")
while n != 0:
    if a > 10 ** (n-1): print(a % (10 ** n) // (10 ** (n-1)))
    n -= 1

                                                #ВАРИАНТ 3:
print("Число -", a)
print("Вариант 3:")
for i in range(len((str(a)))): print(str(a)[i])

