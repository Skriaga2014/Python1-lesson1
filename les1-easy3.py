'''
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
'''

age = input("Ваш возраст: ")
while not age.isdigit(): age = input("Введено неверное значение, попробуйте снова: ")
if int(age) < 18: print("Извините, пользование данным ресурсом только с 18 лет")
else: print("Доступ разрешен")