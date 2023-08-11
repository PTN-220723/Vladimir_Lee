# 1) Составить три формы присвоения следующего вида x, y, z = y, z, x (придумать способ применения )

variable1 = "x"
variable2 = "y"
variable3 = "z"
print(variable1)
print(variable2)
print(variable3)

variable1, variable2, variable3 = variable2, variable3, variable1
print(variable1)
print(variable2)
print(variable3)

temp1 = variable1
temp2 = variable2
temp3 = variable3
variable1 = temp2
variable2 = temp1
variable3 = temp3
print(variable1)
print(variable2)
print(variable3)

# 2) Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:

num1 = "3.14"
num2 = "4"
op1 = float(num1)
op2 = int(num2)
print(op1 + op2)
print(op1 - op2)
print(op1 * op2)
print(op1 / op2)
print(round(op1 ** op2))

# 3) Воспользуйтесь различными методами строк

str1 = ' << pYthOn -   '
print(str1[4:10].lower())
str2 = '   pYthOn \n .   '
print(str2.strip().rstrip(".").rstrip().upper())
str3 = ' (( pYthOn - :+   '
print(str3.strip().lstrip("(").rstrip("+").rstrip(":").rstrip().rstrip("-").strip().capitalize())

# 4) Обработайте каждую переменную и получите результат как на картинке:

string1 = "I love python"
string2 = "Hello my dear friend"
string3 = "полиморфизм"
print(string1[::-1])
print(string2[6:8], string2[14:20])
print(string3[0:11:2])

# 5) С помощью метода строк Замените слово show на display и создайте другую переменную

show = 'show ip interface brief'
display = show.replace("show", "dsiplay")
print(display)

# 6)  В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
# не вышло) можно не смотреть...
# seats = 9*4
coupe = int(input("Номер вашего места"))
SC = 1-(coupe//4+1)
print(f"Ваше место {coupe} находится в {SC} купе")

# 7) Подсчитайте общее количество цифр в числе.
# Например, число 75869 , поэтому на выходе должно быть 5 .

number = 75869
length = str(number)
print(len(length))