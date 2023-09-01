# 1) Есть два словаря, объедините их:
# dict1 = {
#    'meat': 90,
#    'milk': 15,
#    'bread': 3,
#    'potato': 6,
#    'apple': 20,
#    'banana': 25,
#    'chicken wings': 45,
#    'chocolate': 17
# }
# dict2 = {
#    'kiwi': 30,
#   'orange': 25,
#   'coca-cola': 10,
#    'chips': 18
# }

dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
 }
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
 }
dict1.update(dict2)
print(dict1)

# 2) Напишите сценарий Python для создания и печати словаря, содержащего число (от 1 до n включительно)
# (где n — введенное пользователем число) в форме (x, x * x).

n = int(input("Введите число n: "))
dict3 = {x: x * x for x in range(1, n + 1)}
print(dict3)

# 3) Напишите код для суммирования всех значений словаря и вывод среднего арифметического значения.



# 4) Напишите код для объединения двух списков в словарь ключ: значение. СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА
# (содержимое списков произвольное)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict5 = dict(zip(keys, values))
print(dict5)

# 5) Есть словарь координат городов:
# cities = {
# 'Moscow': (550, 370),
# 'London': (510, 510),
# 'Paris': (480, 480),
# }
# Составьте словарь расстояний между городами по формуле: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# Используйте часть кода:
# distances = {}
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']

cities = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480)
}
distances = {}
for city1, coord1 in cities.items():
    distances[city1] = {}
    for city2, coord2 in cities.items():
        if city1 != city2:
            distance = ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5
distances[city1][city2] = distance
print(distances)
