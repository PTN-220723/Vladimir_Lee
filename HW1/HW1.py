# 1) Напишите программу, которая спрашивает имя пользователя и затем приветствует его.

name = input("Введите свое имя")
print("Привет, ", name)

# 2) Напишите программу, которая считывает три числа и выводит их сумму.

num1 = input("Введите первое число")
num2 = input("Введите второе число")
num3 = input("Введите третье число")
print("Сумма трех чисел равна: ", int(num1) + int(num2) + int(num3))

# 3 Напишите программу, для решения следующей задачи: n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

apple = 17
ppl = 5
how_much_did_each_get = apple // ppl
remains = apple % ppl
print("Так как школьников", ppl, "а яблок всего", apple, "то каждому досталось по", how_much_did_each_get)
print("Осталось", remains, "яблока")

# 4 Напишите программу, которая спрашивает число у пользователя и выводит следующее:

num4 = input("Введите число еще раз")
num5 = int(num4) + 1
num6 = int(num4) - 1
print("Предыдущее число", str(num6), "Последующее число", str(num5))

# 5 Напишите программу, которая выводит текст в данном формате (1st method)

sentence1 = """
Twinkle, twinkle, little star,
    How I wonder what you are!
            Up above the world so high
            Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are!"""
print(sentence1)

# 5(2nd method)

sentence2 = """Twinkle,twinkle,little star,\n\tHow I wonder what you are!\n\t\t\tUp above the world so high. \n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!"""
print(sentence2)

# 6 Напишите программу для использования метода форматирования следующих трех переменных в соответствии с ожидаемым результатом.

totalMoney = 1000
quantity = 3
price = 450
print("У меня есть", totalMoney, "долларов могу купить", quantity, "мяча за", price, "долларов")
