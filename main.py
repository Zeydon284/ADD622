# print()
# print("hellp")
# from itertools import count
# from urllib.parse import uses_relative
# from itertools import count
# from operator import delitem
# from turtledemo.penrose import draw
#
# from pip._internal.utils import misc
# from codecs import replace_errors
# from random import setstate
#
# # name = "admin"
# # print("hello,", name, type(name), id(name))
# # age = 20.2
# # print(age, type(age), id(age))
#
# # a = b = c = 1
# # print(a, b, c)
# # print(id(a), id(b), id(c))
#
# # a, b, c = 5, "Hello", 9.2
# # print(a, b, c)
#
# # first_name = "admin"
# # print(first_name)
# #
# # firstName = "admin"
# # print(firstName)
#
# # import keyword
# # print(keyword.kwlist)
#
# # a = 1
# # b = 5
# # print("a:", a)
# # print("b:", b)
# # # c = a # 1
# # # a = b # 5
# # # b = c # 1
# #
# # a, b = b, a
# # print("a:", a) # 5
# # print("b:", b) # 1
# #
# # print("Hello"
# #       " Python")
# # print ("Hello"
# #       " Python")
# # print("Helloc \n Python")
# #
# # print("\tДокумент \"script.py\" находится по заданному пути" \rD:\\folder\\file\\
# # script.py")
#
# # s1 = "Hello"
# # s2 = "World"
# # s3 = s1 + ", " + s2 + "!\t\t"
# # print(s3 * 4)
#
# # print(6 + 2)
# # print(6 - 2)
# # print(6 * 2)
# # print(6 / 4)
# # print(6 // 4)
# # print(6 ** 3)
# # print(7 % 2)
#
# # number = (6+4)*(5**2+7)
# # print(number)
# # num = 10
# # # num = num + 5
# # num += 5
# # print(num) #15
# #
# # num -= 3
# # print(num) #12
# #
# # num *= 4
# # print(num)
# #
# # num = 9753
# # print("Исходное число:", num)
# # # one = num % 21
# # one = num % 10  #1
# # num = num // 10
# # two = num % 10  #2
# # num = num // 10
# # three = num % 10  #3
# # num = num // 10
# # four = num % 10 #4
# # print(four)
# # print(one, two, three, four)
# # print("Обратное число:", one * 1000 + two * 100 + three * 10 + four)
# # #1234
#
# # num = 9753
# # print("Исходное число:", num)
# # res = num % 10 * 1000 #1000
# # num = num // 10  #432
# # res += num % 10 *100  #1000 + 200
# # num = num // 10
# # res += num % 10 * 10  #1200 +30
# # res = num // 10
# # print(num)
# # print("Обратное число:", res)
#
#
#
# # print(int(3.8))
# # print(round(3.891, 2))
# # print(type(round(3.891, 2)))
# #
# # num1 = "2.5"
# # num2 = 3
# # res = float(num1) + num2 #2.5 + 3
# # print(res)
#
#
# # one = 1
# # two = 2
# # print("one:", one, "\ntwo:", two)
#
#
# # name = "Виктор"
# # age = 20
# # print("Меня зовут ", name, ". Мне ", age, " лет.")
# # # print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# # print("Я учу Python")
#
# # name = input("Введите имя: ")
# # print("ваше имя:", name)
#
# # num = int(input("Введите число: "))
# # power = int(input("Введите степень: "))
# # # num = int(num)
# # # power = int(power)
# # res = num ** power
# # print(res)
#
# # b1 = True
# # b2 = False
# # # print(b1, type(b1))
# # # print(b2, type(b2))
# # print(b1+5)   # 1 + 5
# # print(b2+5)   # 0 + 5
#
# # print(bool("python"))
# # print(bool(""))
# # print(bool(0.0))
# # print(bool(True))
# # print(bool(False))
# # print(bool(None))
#
# # test = None
# # print(test, type(test))
#
# # print(7 == 7)
# # print(3+5 == 7)
# # print(7 != 10 - 3)
# # print(8>5)
# # print(8<5)
# # print(9 >= 9)
# # print(9 <= 9)
# # print("привет" > "ПРИВЕТ")
#
# # print(2 < 4 < 9)  # True True
# # print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7
# # print(3 * 3 <= 7 >= 2)  # 9<= 7 >= 2 => False True##
# #
# # print(not 9 - 9)
#
# # print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# # print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# # print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# # print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)
#
# #
# # print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# # print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# # print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# # print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)
#
#
# # cnt = 15
# # if cnt < 10:
# #     cnt += 1
# # print(cnt)
# #
# # age = int(input("Введите свой возраст"))
# # if age >= 18:
# #     print("Доступ на сайт разрешён")
# # else:
# #     print("Доступ запрешён")
#
#
# # a = 25
# # b = 5
# #
# # if a > b:
# #     print("a > b")
# # if b > a:
# #     print("b > a")
# # if a == b:
# #     print("a == b")
# #
# # if a > b:
# #     print("a > b")
# # elif b > a:
# #     print("b > a")
# # else:
# #     print("a == b")
#
#
# # num1 = "равносторонний"
# # num2 = "равнобедренный"
# # num3 = "разносторонний"
# #
# # a = input("Введите первую сторону:")
# # b = input("Введите вторую сторону:")
# # c = input("Введите третью сторону:")
# # if a==b==c:
# #     print(num1)
# # if a==b or b==c or a==c:
# #     print(num2)
# # if a != b != c != a:
# #     print(num3)
#
#
# # day = int(input("Введите день недели (цифрой):"))
# # if day >= 1 and day <= 5:
# #     print("Рабочий день - ", end="")
# #     if day == 1:
# #         print("понедельник")
# #     if day == 2:
# #         print("вторник")
# #     if day == 3:
# #
# # elif day == 6 or day == 7:
# #     print("Выходной день")
# # else:
# #     print("Такого дня недели не существует")
#
#
# # month = int(input("Введите порядковый номер месяца (цифрой):"))
# # if month == 1 or month == 2 or month == 12:
# #     print("Зима")
# # if  3 <= month <= 5:
# #     print("Весна")
# # if 6 <= month <= 9:
# #     print("Лето")
# # if 10 <= month <= 11:
# #     print("Осень")
# # elif month >= 13:
# #     print("Ошибкка ввода данных")
#
#
# # crow = int(input("Введите число ворон на ветеке в диапозоне от 0 до 9:"))
# # if crow == 0:
# #     print("На ветке 0 ворон")
# # if crow == 1:
# #     print("На ветке 1 ворона")
# # if crow == 2:
# #     print("На ветке 2 вороны")
# # if crow == 3:
# #     print("На ветке 3 вороны")
# # if crow == 4:
# #     print("На ветке 4 вороны")
# # if crow == 5:
# #     print("На ветке 5 ворон")
# # if crow == 6:
# #     print("На ветке 6 ворон")
# # if crow == 7:
# #     print("На ветке 7 ворон")
# # if crow == 8:
# #     print("На ветке 8 ворон")
# # if crow == 9:
# #     print("На ветке 9 ворон")
# # if crow >= 10:
# #     print("Ошибка ввода данных")
#
#
#
# # crow = int(input("Введите число ворон на ветеке в диапозоне от 0 до 9:"))
# # if crow == 0 or 5 <= crow <= 9:
# #     print("На ветке", crow, "ворон")
# # if crow == 1:
# #     print("На ветке", crow, "ворона")
# # if  2 <= crow <= 4:
# #     print("На ветке", crow, "вороны")
# # if crow >= 10:
# #     print("Ошибка ввода данных")
#
#
# # a, b = 30, 20
# # print(a if a < b else b)
#
# # a, b = 30, 40
# # print("a == b" if a == b else "a > b" if a > b else "a < b")
#
# # try:
# #     n = int(input("Введите целое число"))
# #     print(n * 2)
# # except ValueError:
# #     print("Что-то пошло не так")
#
# # try:
# #     n = int(input("Введите делимое"))
# #     m = int(input("Введите делитель"))
# #     print(n / m)
# # except ValueError:
# #     print("Нельзя вводить строки")
# # except ZeroDivisionError:
# #     print("Нельзя делить на ноль")
# #
# # print("Код ниже")
#
#
#
# # try:
# #     n = int(input("Введите делимое"))
# #     m = int(input("Введите делитель"))
# #     print(n / m)
# #
# #     print("Код ниже")
#
#
# # try:
# #     n = int(input("Введите делимое"))
# #     m = int(input("Введите делитель"))
# #     print(n / m)
# # # except ValueError, ZeroDivisionError:
# # #     print("Нельзя вводить строки или делить на ноль")
# # # else:       #когда в блоке try не возникло ошибки
# # #     print("Всё нормально. Вы ввели числа", n, "и", m)
# # finally:    #выполняется в любом случае
# #     print("Конец программы")
#
#
# # n = input("Введите первое число: ")  # 2
# # m = input("Введите первое число: ")  # "ццц"
# #
# # try:
# #     n=int(n)  # 2
# #     m=int(m)
# # except ValueError:
# #     n=str(n)   # "2"
# #     m=str(m)
# # finally:
# #     print(n + m)
#
#
# # i = 10
# # while i > 0:
# #     print("i =", i)
# #     i -= 1
#
#
# # i = 1
# # while i <= 20:
# #     if i % 2 == 0:
# #        print(i, end=" ")
# #     i += 1
#
#
# # i = 2
# # while i <= 20:
# #     print(i, end=" ")
# #     i += 2
#
#
# # n = int(input("Укажите количество символов: "))
# # i = 0
# # while i < n:
# #     print("*", end="")
# #     i += 1
#
#
# # n = int(input("Укажите количество символов: "))
# # while n > 0:
# #     print("*", end="")
# #     n -= 1
#
# # start = int(input("Введите начало диапазона: "))
# # end = int(input("Введите конец диапазона: "))
# #
# # res = 0
# #
# # while start <= end:
# #     if start % 2 != 0:
# #        res += start
# #        # print(start)
# #     start += 1
# #
# # print("Сумма целых нечётных чисел: ", res)
#
#
# #
# # n = input("Введите целое число: ")
# #
# # while type(n) is not int:
# #     try:
# #         n = int(n)
# #     except ValueError:
# #         print("Число не целое!")
# #         n = input("Введите целое число: ")
# #
# # if n % 2 == 0:
# #     print("Чётное")
# # else:
# #     print("Нечётное")
#
#
#
# # i = 0
# # while i < 10:
# #     if i == 3:
# #         i += 1
# #         continue
# #     print(i, end=" ")
# #     if i == 5:
# #         break
# #     i += 1
# # print("\nЦикл завершён!")
#
# # i = 0
# # while True:
# #     print(i)
# #     if i == 5:
# #         break
# #     i += 1
#
# # while True:
# #     n = int(input("Введите положительное число: "))
# #     if n == 0:
# #         break
#
# # res = 1
# # while True:
# #     n = int(input("Введите положительное число: "))
# #     if n == 0:
# #         break
# #     res *= n   # res = res * n
# #
# # print("Результат:", res)
#
#
# # i = 0
# # while i < 10:
# #     if i == 5:
# #         break
# #     print(i)
# #     i += 1
# # else:
# #     print("Цикл окончен, i =", i)
#
#
# # i = 1
# # while i < 5:
# #     print("Внешний цикл: i =", i)
# #     j = 1
# #     while j < 4:
# #         print("\tВнутренний цикл: j =", j)
# #         j += 1
# #     i += 1
#
#
#
# #
# # i = 1
# # while i < 10:
# #     j = 1
# #     while j < 10:
# #         print(i, "*", j, "=", i*j, end="\t\t")
# #         j += 1
# #     print()
# #     i += 1
#
#
# # i = 0
# # while i < 5:
# #     j = 0
# #     while j < 16:
# #         if j % 2 == 0:
# #            print("+", end = "")
# #         else:
# #            print("-", end = "")
# #         j += 1
# #     print()
# #     i += 1
#
#
# # for element in collection:
# #        print(element)
#
#
# # for i in "Hello!":
# #     print(i * 2)
#
# # for i in "red", "orange", "yellow", "green", "blue", "indigo", "violet":
# #     print(i)
#
#
# #print(range(start, stop, step))
#
# # for i in range(9, 0, -1):
# #     print(i, end = " ")
# #
# # print()
# #
# # j = 2
# # while j < 9:
# #     print(j, end = " ")
# #     j += 3
#
#
# # for i in range(10, 100):
# #     if i % 10 == i // 10:
# #         print(i, end = " ")
#
#
#
#
# # for i in range(3):
# #     print(i)
# #     if i == 1:
# #         break
# # else:
# #     print("else")
#
#
# #
# # for i in range(4):
# #     for j in range(16):
# #         if i == 0 or j == 0 or i == 3 or j == 15:
# #             print("*", end="")
# #         else:
# #             print(" ", end="")
# #     print()
#
#
# # num = [i for i in range(10) if i % 2 == 0]
# # print(num)
#
#
# # nums = [8, 3, 9, 4, 1]
# # #       0, 1, 2, 3, 4
# # #      -5,-4,-3,-2,-1
# # print(nums)
# #
# # # print(nums[0])
# # # print(nums[2])
# # # print(nums[-5])
# #
# #
# # nums[-1] = 256
# # nums[3] += 100
# # print(nums)
# #
# # print("Длина спписка:", len(nums))
#
#
# # s = []
# # print(s, type(s))
#
# # b = list("Hello")
# # print(b, type(b))
#
#
#
# # n=list(range(2, 10, 2))
# # n=list(range(10, 2, -2))
# # print(n)
#
# # n = 5
# # a = [i ** 2 for i in range(1, n + 1)]
# # print(a)
#
#
# # a = [1,2,3]
# # b = [4,5]
# # c = a + b
# # print(c)
#
#
#
# # a = [0] * int(input("Введите количество элементов списка: "))
# # print(a)
# # for i in range(len(a)):
# #     a[i] = int(input("->"))
# # print(a)
#
# #
# # a = [int(input("-> ")) for i in range(int(input("n = ")))]
# # print(a)
#
# #
# # a = [9, 7, 5, 1, 2]
# #
# # for i in range(len(a)):   # i = 0 1 2 3 4
# #     print(a[i], end=" ")    #   9 7 5 1 2
# #
# # print()
# #
# # for el in a:     # el = 9 7 5 1 2
# #     print(el, end=" ")
#
#
# #
# # a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# # print(a)
# #
# # s=0
# # # for i in range(len(a)):
# # #     if a[i] < 0:
# # #         s += a[i]
# # for i in a:
# #     if i < 0:
# #         s += 1
# # print("Сумма отрицательных элементов: ", s)
#
#
#
# # a = [int(input("-> ")) for _ in range(int(input("n = ")))]
# # print(a)
# #
# # for i in range(1, len(a)):
# #     if a[i] > a[i - 1]:
# #         print(a[i], end=" ")
#
#
#
#
# # n = list(range(21, 41))
# # print(n)
# #
# # k = s = 0
# # # for i in range(len(n)):
# # #     if n[i] % 2 == 0:
# # #         k += 1
# # #     else:
# # #         s += n[i]
# #
# # for i in n:
# #     if i % 2 == 0:
# #         k += 1
# #     else:
# #         s += i
# #
# # print("Количество чётных элеметов списка: ", k)
# # print("Сумма нечётных элементов", s)
#
#
#
# # a = [7, 9, 2, 1, 3]
# # a[0], a[1] = a[1], a[0]
# # print(a)
#
#
#
# #Срезы
# # список [start:stop:step
# # a = [7, 9, 2, 1, 3, 8]
# # #    0, 1, 2, 3, 4, 5
# # print(a, len(a))
# # # print(a[1:4])
# # # print(a[2:])
# # # print(a[:2])
# # # print(a[1::2])
# # # print(a[5::-1])
# # # print(a[10:20])
# # # print(a[4:5])
# #
# # print(a[1:3])
# # a[1:3] = [0, 0, 0, 0]
# # print(a, len(a))
# # a[1:2] = [20]
# # print(a, len(a))
#
#
#
#
#
#
# # print(dir(list))   #вспомогательные функции
#
# # a = [7, 9, 2, 1, 3, 8]
# # print(a)
# # a.append(5)
# # print(a)
# # a.extend([1, 2, 3])
# # print(a)
# # a.insert(1, 100)
# # print(a)
#
# # s = []
# # n = int(input("Количество элементов списка: "))
# # for num in range(n):
# #     x = int(input("Введите число: "))
# #     # s.append(x)
# #     # s.insert(num, x)
# # print(s)
#
#
# # a = [1, 2, 3]
# # b = [11, 22, 33]
# # c = []
# #
# # for i in range(len(a)):
# #     c.append(a[i])
# #     c.append(b[i])
# #
# # print(c)
#
#
# # a = [7, 9, 2, 1, 3, 8, 1]
# # print(a)
# # # del a[0]
# # # print(a)
# # # a[3:] = []
# # # print(a)
# # # a.remove(1)
# # # print(a)
# # last = a.pop(-2)
# # print(last)
# # print(a)
#
#
#
#
# # a = [1, 7, 9, 2, 1, 3, 8, 1]
# # print(a)
#
# # num = a.count(9)
# # ch = 7
# # if ch in a:
# #     num = a.index(ch)
# #     print(num)
# # a.clear()
# # print(a)
#
#
# # a = [1, 7, 9, 2, 1, 3, 8, 1]
# # print(a)
#
# # new_list = a.copy()
# # print(new_list)
# # new_list.append(400)
# # print(new_list)
# # print(a)
#
#
#
# # a = [1, 7, 9, 2, 1, 3, 8]
# # print(a)
#
# # # a.reverse()
# # # print(a)
# #
# #
# # lst = list(reversed(a))
# # print(lst)
# # print(a)
# # lst.append(100)
# # print(lst)
# # print(a)
#
#
#
# # a = [1, 7, 9, 2, 1, 3, 8]
# # print(a)
#
# # a.sort(reverse = True)
# # print(a)
#
#
# # lst = ["Виталий", "Сергей", "Александр", "Анна"]
# # print(lst)
# # # lst.sort(key=len, reverse=True)
# # new_lst = sorted(lst)
# # print(new_lst)
# # print(lst)
#
#
# # import random
# #
# # print(random.random())
# # print(random.randint(1,9))
# # print(random.randrange(1,9, 2))
#
#
# # import random as rnd
# #
# # print(rnd.randint(1,9))
# # print(rnd.randrange(1,9, 2))
#
#
# # from random import *
# #
# # print(randint(1,9))
# # print(randrange(1,9, 2))
#
#
# # import random as rnd
# #
# # # city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екб"]
# # # print(rnd.choice(city_list))
# # # print(rnd.choice(city_list, k=2))
# # # # rnd.shuffle(city_list)
# # # print(city_list)
# #
# # lst = [rnd.randint(0, 100) for i in range(10)]
# # print(lst)
#
#
# # lst = [5, 3, 2, 4, 1]
# # print(len(lst))
# # print(min(lst))
# # print(max(lst))
# # print(sum(lst))
#
# # import random
# #
# # lst = [random.randint(0, 100) for i in range(10)]
# # print(lst)
# # maximum = max(lst)
# # print("max =", maximum)
# # lst.remove(maximum)
# # lst.insert(0, maximum)
# # print(lst)
#
#
# # Матрицы
#
# # matrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
# # print(matrix)
# # # print(len(matrix))
# # # print(matrix[1][2])
# #
# # # ==================================================
# #
# # for row in range(len(matrix)):
# #     # print(matrix[row])
# #     for col in range(len(matrix[row])):
# #         print(matrix[row][col], end="\t")
# #     print()
# # print()
# #
# # # ===================================================
# #
# # for row in matrix:
# #     for col in row:
# #         print(col, end="\t")
# #     print()
#
#
# # import math
# #
# # print(math.sqrt(4))  # корень
# # print(math.ceil(3.2))  # округление в большую
# # print(math.floor(3.2))  # округление в меньшую
# # print(math.pi)  # число Пи
#
#
#
#
# # def hello(name, word):  # аргумент
# #     print("Hello ", name, ". Say ", word, sep="")
# #
# #
# # hello("Irina", "hi")  # параметры
# # hello("Ivan", "hello")
#
#
#
#
#
#
#
# # def get_sum(a, b):
# #     print("Сумма:", end=" ")
# #     return a + b
# #
# #
# # x = 2
# # y = 5
# # res = get_sum(x, y)
# # print(res)
#
#
#
#
#
# # def maximum(one, two):
# #     if one > two:
# #         return one
# #     else:
# #         return two
# #
# # print(maximum(9, 16))
#
#
#
#
#
# # def cube(a):
# #     return a * a * a
# #
# # for i in range(1,11):
# #     print(i, "в кубе =", cube(i))
#
#
#
#
#
# # def change(lst):
# # #     last = lst.pop()
# # #     first = lst.pop(0)
# # #     lst.insert(0,last)
# # #     lst.append(first)
# #     lst[0], lst[-1] = lst[-1], lst[0]
# #     return lst
# # #
# # #
# # print(change([1,2,3]))
# # print(change([9,12,33,54,105]))
# # print(change(["с", "л", "о", "н"]))
#
#
#
#
#
# # def is_greater(x,y):
# #     if x > y:
# #         return True
# #     else:
# #         return False
# #
# #
# # print(is_greater(10,5))
# # print(is_greater(5,10))
#
#
#
#
#
#
#
# # def check_password(password):
# #     has_upper = False
# #     has_lower = False
# #     has_num = False
# #
# #     for ch in password:
# #         if "A" <= ch <= "Z":
# #             has_upper = True
# #         if "a" <= ch <= "z":
# #             has_lower = True
# #         if "0" <= ch <= "9":
# #             has_num = True
# #
# #
# #     if len(password) >= 8 and has_upper and has_lower:
# #         return True
# #     return False
# #
# #
# # p = input("Введите пароль: ")
# # if check_password(p):
# #     print("Это надёжный пароль")
# # else:
# #     print("Это ненадёжный пароль")
#
#
#
#
# # def get_sum(a, b, c = 0, d = 1):
# #     return a + b + c + d
# #
# #
# #
# # print(get_sum(1, 5, 2, 7))
# # print(get_sum(1, 5, 2))
# # print(get_sum(1, 5))
# # print(get_sum(1, 5, 2))
#
#
#
#
#
#
# # def display_info(name, age):
# #     print("Name:", name, "\nAge:", age, end = "\n\n")
# #
# #
# # display_info("Ira", 23)
# # display_info(23, "Ira")
# # display_info(age = 23, name = "Ira")
#
#
#
#
#
#
#
#
# # board = [" "] * 9   # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# # game_over = False
# # player = "X"
# #
# #
# # def show():
# #     print(board[0] + " | " + board[1] + " | " + board[2])
# #     print("- + - + -")
# #     print(board[3] + " | " + board[4] + " | " + board[5])
# #     print("- + - + -")
# #     print(board[6] + " | " + board[7] + " | " + board[8])
# #
# #
# # def chek():
# #     return (board[0] == board[1] == board[2] == player or
# #             board[3] == board[4] == board[5] == player or
# #             board[6] == board[7] == board[8] == player or
# #             board[0] == board[3] == board[6] == player or
# #             board[1] == board[4] == board[7] == player or
# #             board[2] == board[5] == board[8] == player or
# #             board[0] == board[4] == board[8] == player or
# #             board[2] == board[4] == board[6] == player)
# #
# # while not game_over:
# #     show()
# #     move = int(input("\nХод " + player + " (1-9): ")) - 1
# #
# #     if board[move] == " ":
# #         board[move] = player
# #     else:
# #         print("Занято")
# #         continue
# #
# #     if chek():
# #         show()
# #         print("\nПользователь " + player + " победил")
# #         game_over = True
# #     elif " " not in board:
# #         show()
# #         print("\nНичья")
# #         game_over = True
# #
# #     player = "O" if player == "X" else "X"
#
#
#
#
# # a = "Hello World"
# # b = "Hello World"
# #
# # print(a == b)  #True
# # print(a is b)  #True
# # print("id(a) = ", id(a))
# # print("id(b) = ", id(b))
# #
# #
# # lt1 = [1,2,3]
# # lt2 = [1,2,3]
# # print(lt1 == lt2)  #True
# # print(lt1 is lt2)  #False
# # print("id(lt1) = ", id(lt1))
# # print("id(lt2) = ", id(lt2))
#
#
#
# # lt1 = [1,2,3]
# # print(lt1, "id(lt1) =", id(lt1))
# # lt1.append(4)
# # print(lt1, "id(lt1) =", id(lt1))
# #
# #
# #
# # s = "Hello"
# # print(s, "id(s) =", id(s))
# # s += " world"
# # print(s, "id(s) =", id(s))
#
#
#
# # lst = [10, 20, 30]  #список
# # tpl = (10, 20, 30)  #кортеж
# #
# # print(lst.__sizeof__())
# # print(tpl.__sizeof__())
# #
# # lst[1] = 5
# # print(lst)
# # tpl[1] = 5
# # print(tpl)
#
#
#
# # a = 1
# # print(a, type(a))
#
# # b = tuple("Hello")
# # print(b, type(b))
# #
# # print(b[3])
# # print(b[1:3])
#
#
#
# # s = tuple(int(input("-> ")) for i in range(5))
# # print(s)
#
#
# # s = input("Введите пятизначное число: ")
# # tpl = tuple(s)
# # print(tpl)
# # res = 0
# # for i in tpl:
# #     res += int(i)
# # print(len(tpl))
# # print(res)
# # print(res / len(tpl))
#
#
# # import random
# #
# # tpl = tuple(random.randint(1,100) for i in range(10))
# # print(tpl)
#
#
# # t1 = tuple("hello")
# # t2 = tuple("world")
# # # print(t1)
# # # print(t2)
# # t3 = t1 + t2
# # print(t3)
# #
# # print(t3.count("l"))
# # print(t3.count("a"))
# # print(t3.index("l", 4))
#
#
# # def slicer(tpl, el):
# #     if el in tpl:
# #         if tpl.count(el) > 1:
# #             # first = tpl.index(el)
# #             # second = tpl.index(el, first + 1)
# #             # return tpl[first:second + 1]
# #             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1] # Второй способ
# #         else:
# #             return tpl[tpl.index(el):]
# #     else:
# #         return ()
# #
# #
# # print(slicer((1, 2, 3),8))
# # print(slicer((1, 8, 3, 4, 8, 8, 9, 2),8))
# # print(slicer((1, 2, 8, 5, 1, 2, 9),8))
#
#
#
# # tpl = (10, 11, [1,2,3], [4,5,6], ["hello", "world"])
# # print(tpl, id(tpl))
# # tpl[4][0] = "new"
# # print(tpl, id(tpl))
# # tpl[4].append("new")
# # print(tpl, id(tpl))
#
#
# # tpl = 1, 2, 3
# # # x = tpl[0]
# # # y = tpl[1]
# # # z = tpl[2]
# # x, y, z = tpl # распаковка кортежа
# # print(x, y, z)
#
#
#
#
# # def get_user():
# #     name = "Tom"
# #     age = 20
# #     is_married = True
# #     return name, age, is_married
# #
# #
# # user, year, married = get_user()
# # print(user, year, married)
#
#
#
# # a = (1, 5, 3, 4, 4, 4, 2, 3, 0, 0)
# # # del a
# # print(a)
# # b = list(a)
# # print(b)
# # b[0] = 100
# # print(b)
# # c = tuple(b)
# # print(c)
#
#
#
# # countries = (
# #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
# #     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# # )
# #
# # print(countries, end="\n\n")
# #
# # for country in countries:
# #     countryName, countryPopulation, cities = country
# #     print("\nСтрана:", countryName, ", Население = ", countryPopulation, sep="")
# #     for city in cities:
# #         cityName, cityPopulation, = city
# #         print(cityName, cityPopulation)
#
#
#
# # tpl = tuple(input("Введите данные: "))
# # print(tpl)
# #
# #
# # lst = []
# # for item in tpl:
# #     if item not in lst:
# #         lst.append(item)
# #
# # # print(lst)
# #
# # for item in lst:
# #     print("Количество:", item, "=", tpl.count(item))
#
#
#
# # s = {"banana", "apple", "mango", "banana", "apple"}
# # print(s, type(s))
# # for x in s:
# #     print(x)
#
#
#
# # a = set("hello")
# # print(a, type(a))
#
#
# # s = {x * x for x in range(10)}
# # print(s)
#
#
# # t = {'red', 'green', 'blue'}
# # print('green' in t)
# # print('yellow' in t)
#
#
# # t = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # # a = [i for i in t]
# # # b = [i for i in t if 'a' not in i]
# # # c = ['A' + i[1:] if i[0] == "a" else "B" + i[1:] for i in t]
# # d = ['A' + i[1:] if i[0] == "a" else "B" + i[1:] for i in t if i[1]=="c"]
# # print(d)
#
#
# # a = {0, 1, 2, 3}
# # print(a)
# # a.add(4)
# # print(a)
#
#
#
# # users = {"Tom", "Bob", "Alice"}
# # print(users)
# # users.remove("Tom")
# # print(users)
# # users.remove("Ann")      #KeyError
# # print(users)
#
# # user = "Alice"
# # if user in users:
# #     users.remove(user)
#
#
# # users.discard("Ann")
#
# # users.pop()
# #
# # users.clear()
# #
# # print(users)
#
#
#
#
# #Папка 10 (операции со множеставами)
# # a = {0,1,2,3}
# # b = {4, 3, 2, 1}
#
# # c = a.union(b)
# # c = a | b
# # print(c)  # {0, 1, 2, 3, 4}
# #
# #
# # a |= b
# # print(a)  # {0, 1, 2, 3, 4}
# #
# #
# # c = a & b
# # print(c)
# #
# #
# # a &= b
# # print(a)
# #
# #
# # c = a - b
# # print(c)
# #
# #
# # a -= b
# # print(a)
#
# #
# # c = a ^ b
# # print(c)
# #
# # #
# # a ^= b
# # print(c)
#
#
#
#
# # s1 = {1,2}
# # s2 = {3}
# # s3 = {4,5}
# # s4 = {3,2,6}
# # s5 = {6}
# # s6 = {7,8}
# # s7 = {9,8}
# #
# # # s = s1.union(s2, s3, s4, s5, s6, s7)
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# #
# # print(s)
# #
# # count = len(s)
# # print("Количество уникальных элементов:", count)
# # print("Min:", min(s))
# # print("Max:", max(s))
#
#
#
# # s1 = "Hello"
# # s2 = "How are you"
# # s = set(s1) & set(s2)
#
# # s1 = set("Hello")
# # s2 = set("How are you")
# # s = s1 & s2
# # for x in s:
# #     print(x, end=" ")
# # print()
# # print(s1)
# # print(s2)
#
#
# # s1 = "Python"
# # s2 = "Programming language"
# #
# # s = list(set(s1) - set(s2))
# # print(s)
# # for i in s:
# #     print(i, end=" ")
#
#
#
#
# # a = {0,1,2,3,4}
# # b = {3,2,1}
# #
# #
# # print(a <= b)
# # print(a < b)
# # print(a >= b)
# # print(a > b)
#
#
# # drawing = {"Marina", "Gena", "Sveta"}
# # music = {"Kostia", "Gena", "Ilia"}
# #
# # one_hobby = drawing ^ music
# # print("Один кружок:", one_hobby)
# #
# # two_hobby = drawing & music
# # print("Оба кружка:", two_hobby)
# #
# # drawing -= two_hobby
# # print(drawing)
#
#
# # s = frozenset([1,2,3,4,5])
# # print(s)
#
#
# # lst = [10, 20, 30]
# # d = {"one": 1, "two": 2, "three": 3}
# # print(lst[0])
# # print(d["one"])
#
#
# # d = {"one": 1, "two": 2, "three": 3}
# # print(d, type(d))
#
# # d1 = dict(one=1, two=2, three=3)
# # print(d, type(d))
#
#
# # d = {0: "text", "one": 45, (5,4): "кортеж", "список": [2,4,5], True: 1, False: 0, 1:45}
# # print(d)
# #
# # for key in d:
# #     print(key, ": ", d[key])
#
#
#
#
# # try:
# #     del d["one"]
# # except KeyError:
# #     print("Элемента с таким ключом не существует")
# # print(d)
#
#
# # print("список" in d)
# # print("списоки" in d)
#
#
#
# # print(d[True])
# # print(d["список"][2])
#
# # lst = [1,2,3]
# # print(tuple(lst))
#
#
# # lst = (
# #     ("one",1),("two",2),("three", 3)
# # )
# # print(dict(lst))
#
#
#
# # d = {a **3: a **2 for a in range(10)}
# # print(d)
#
#
# # d = {"one": 10, "two": 20, "three": 30}
# # print(d)
# # print(d["two"])
# # d["two"] = 2 ** 4
# # print(d)
#
#
#
# # d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# #
# # res = 1
# # for key in d:
# #     res *= d[key]
# #
# # print(res)
#
#
#
# # d = dict()
# # d[1] = input("-> ")
# # d[2] = input("-> ")
# # d[3] = input("-> ")
# # d[4] = input("-> ")
# #
# #
# # d = {i: input("-> ") for i in range(1, 5)}
# # print(d)
# # delite = int(input("Какой эл исключить?: "))
# # del d[delite]
# # print(d)
#
#
#
#
# # goods = {
# #     '1': ['Core-i3-4330', 9, 4500],
# #     '2': ['Core i5-4670k', 3, 8500],
# #     '3': ['AMD FX-6300', 6, 3700],
# #     '4': ['Pentium G3220', 8, 2100],
# #     '5': ['Core i5-3450', 5, 6400],
# # }
# #
# # for i in goods:
# #     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ",
# #           goods[i][2], "руб", sep="")
# #
# # while True:
# #     n = input("№: ")
# #     if n != "0":
# #         if n in goods:
# #             while True:
# #                 try:
# #                     count = int(input("Количество: "))
# #                     goods[n][1] += count
# #                     break
# #                 except ValueError:
# #                     print("Значение не корректное. Введите число")
# #         else:
# #             print("Такого ключа не существует")
# #     else:
# #         break
# #
# #
# # for i in goods:
# #     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ",
# #           goods[i][2], "руб", sep="")
#
#
#
# # d = {"one":1, "two":2, "three":3}
# # print(d)
# # print(d.keys())          # dict_keys(['one', 'two', 'three'])
# # print(d.values())        # dict_values([1, 2, 3])
# # print(d.items())         # dict_items([('one', 1), ('two', 2), ('three', 3)])
# #
# # for key, value in d.items():
# #     print(key, value)
# #
# # value = d["five"]
# # value = d.get("five", 4)
# # print(value)
#
#
# # item = d.popitem()
# # print(item)
# # print(d)
#
#
# # item = d.setdefault("five")
# # print(item)
# # print(d)
#
#
# # d1 = dict.fromkeys(['a','b','c','d'], 100)
# # print(d1)
#
# # d = {"one":1, "two":2, "three":3}
# # print(d)
# #
# #
# # d2 = d.copy()
# # print("d =", d)
# # print("d2 =", d2)
# #
# # d["two"] = 5
# # d2["three"] = 6
# #
# # print("d =", d)
#
#
#
#
# # d = {'a':1, 'b':2, 'c':3}
# # # d2 = {"one":1, "two":2, "three":3}
# # # # d.update({'a':4, 'e':5, 'f':6})
# # # d.update(d2)
# # d.update([('r', 7), ('q', 9)])
# # print(d)
#
#
#
# # d = {'a':1, 'b':2, 'c':3}
# # d2 = {"one":1, "two":2, "three":3}
# #
# # d3 = d | d2
# # print(d3)
#
#
#
#
# # d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# # print(d)
# #
# #
# # # new_d = dict()
# # # new_d["name"] = d.pop("name")
# # # new_d["salary"] = d.pop("salary")
# #
# #
# # new_d = {"name": d.pop("name"), "salary": d.pop("salary")}
# # print(d)
# # print(new_d)
#
#
#
# # d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# # d["location"] = d.pop("city")
# # print(d)
#
# # d = {
# #     "first": {
# #         1: "one",
# #         2: "two",
# #         3: "three",
# #     },
# #     "second": {
# #         4: "four",
# #         5: "five",
# #     }
# # }
# # print(d)
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ": ", d[x][y], sep = "")
# #
# # for x,y in d.items():
# #     print(x)
# #     for k,v in y.items():
# #         print("\t", k, ": ", v, sep="")
#
#
# # d = {"one":1, "two":2, "three":3}
# # print(d)
# #
# # new_d = {v: k for k, v in d.items()}
# # print(new_d)
#
#
# #урок №9 =====================================================================
#
# # lst = [1,2,3,4]
# # d = {k: int(input("-> ")) for k in lst}
# # print(d)
#
#
#
# # d = dict(zip([1,2,3,4],["one","two","three"]))
# # print(d)
# # print(list(zip([1,2,3])))
#
#
#
# # one = {'name': 'Fiona', 'surname': 'Vetrova', 'age': 26}
# # two = {'name': 'Irina', 'surname': 'Petrova', 'age': 28}
# #
# # for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
# #     print(k1, "->", v1)
# #     print(k2, "->", v2)
# #
# # print(list(zip(one.items(), two.items())))
#
#
#
# # one = {'one': 1, 'two': 2, 'three': 'three'}
# # two = {'three': 3, 'four': 4, 'five': 5, 'two':'two'}
# # print({**one, **two})
#
#
#
# # a = [1,2,3]
# # b = [*a, 4, 5, 6]
# # print(b)
#
#
#
# # def func(*args):
# #     return args
# #
# #
# # print(func(1))
# # print(func(1, 2, 3, 'abc'))
# # print(func())
#
#
#
# # def average(*args):
# #     return sum(args) / len(args)
# #
# #
# # print(average(1,2,3,4,5,6))
# # print(average(1,2,3))
#
#
#
#
# # def average(*args):
# #     aver = sum(args)/len(args)
# #     print(aver)
# #     res = []
# #     for num in args:
# #         if num < aver:
# #             res.append(num)
# #     return res
# #
# # print(average(1,2,3,4,5,6,7,8,9))
# # print(average(3,6,1,9,5))
#
#
#
# # def func(a, *args):
# #     return a, args
# #
# #
# # print(func(1))
# # print(func(1,2,3))
#
#
#
# # def print_data(student, *scores):
# #     print("Student Name:",student)
# #     for score in scores:
# #         print(score)
# #     print(*scores, type(*scores))
# #     print(scores, type(scores))
# #
# # print_data("Igor", 100, 95, 88, 92, 99)
# # print_data("Marina", 96, 20, 33, 56)
# # print_data("Irina")
#
#
#
#
# # def func(**kwargs):
# # #     return kwargs
# # #
# # # print(func())
# # # print(func(a=1, b=2, c=3))
# # # print(func(lang = "Python"))
#
#
#
#
# # def func(a, b, *args, e=0, **kwargs):
# #     return a, b, args, kwargs, e
# #
# #
# # print(func(1, 2, 3, 4, 5,  c = 6, d = 7, e = 100))
# # print(func(1))
# # print(func(1, 2, 3))
# # print(func(1, 2, 3, c = 4, d = 5))
#
#
#
#
# # name = "Tom"    #Глобальная переменная (глобальная обл. видимости)
# #
# #
# # def hi():
# #     surname = "Johnson"    #Локальная переменная (локальная обл. видимости)
# #     name = "Sam"
# #     print("Hello", name, surname)
# #
# # def bye():
# #     print("Bye", name)
# #
# #
# # hi()
# # bye()
#
#
# # import builtins
# #
# # names = dir(builtins)
# #
# # for name in names:
# #     print(name)
#
#
#
#
# # one = 10
# #
# #
# # def func(a):
# #         # one = 100
# #         x = 2     # Область объемлющих функций (encloced)
# #
# #         def inner():
# #             # one = 1000
# #             # print("x =", x)
# #             # return a + x
# #             return one
# #
# #
# #         return inner()
# #
# # print(func(5))
#
#
#
#
# # def outer(who):
# #     def inner():
# #         print("Hello,", who)   # 3
# #
# #     inner()   # 2
# #
# # outer("world")   # 1
#
#
#
#
# # who = "World"
# #
# #
# # def outer():
# #     global who
# #     who = "Mari"
# #
# #     def inner():
# #         print("Hello,", who)
# #
# #     inner()
# #
# # outer()
# # print(who)
#
#
#
#
#
# # def fn1():
# #     x = 25
# #
# #     def fn2():
# #         x = 33   #55
# #
# #         def fn3():
# #             nonlocal x
# #             x = 55
# #
# #         fn3()
# #         print("fn2, x =", x)
# #
# #     fn2()
# #     print("fn1, x =", x)
# #
# #
# # fn1()
#
#
#
#
# # x = 25
# #
# #
# # def fn():
# #     global t
# #     a = 30
# #
# #     print("globbal:", x)
# #
# #     def inner():
# #         nonlocal a
# #         a = 35
# #         print("nonlocal:", a)
# #
# #     inner()
# #     print(a)
# #     t = a
# #
# # fn()
# #
# # c = x + t
# # print(c)
#
#
#
#
# # def outer(a1, b1, a2, b2):
# #     a = 0
# #     b = 0
# #
# #     def inner():
# #         nonlocal a, b
# #         a = a1 + a2
# #         b = b1 + b2
# #
# #     inner()
# #     return [a, b]
# #
# #
# # print(outer(2,3,-1,4))
#
#
#
#
# # Замыкание
#
#
# # def outer(n):
# #     def inner(x):
# #         return x + n
# #
# #     return inner
# #
# #
# # add1 = outer(1)
# # print(add1(10))
#
# # add2 = outer(2)
# # print(add2(10))
# #
# # print(outer(3)(10))
#
#
#
# # def outer():
# #     a = 1
# #     b = 'line'
# #     c = [1,2,3]
# #
# #     def inner():
# #         nonlocal a, b
# #         c.append(4)
# #         a = a + 1
# #         b = b + "_new"
# #         return a,b,c
# #
# #     return inner
# #
# #
# # func = outer()
# # print(func())
#
#
#
# #Урок №10 =============================================================================
# #объяснение дз на 00:54:30
#
#
# # def func(city):
# #     many = 0
# #
# #     def inner():
# #         nonlocal many
# #         many += 1
# #         print(city, many)
# #
# #     return inner
# #
# #
# # cont1 = func("Москва")
# # cont1()
# # cont1()
# # cont2 = func("Сочи")
# # cont2()
# # cont2()
# # cont1()
#
#
#
# # Анонимные функции, lambda - выражение
#
# # print((lambda x, y: x + y)(1, 2))
# # print((lambda n,m: n ** 2 + m ** 2)(2, 5))
#
#
# # summ = lambda a = 1, b = 2, c = 3: a+b+c
# # print(summ(10, 20, 30))
#
#
# # print((lambda *args: args)(1,2,3,4))
#
#
# # tpl = (
# #     lambda x: x * 2,
# #     lambda x: x * 3,
# #     lambda x: x * 4
# # )
# #
# # for t in tpl:
# #     print(t("abc"))
#
#
#
# # def outer(n):
# #     def inner(x):
# #         return x + n
# #
# #     return inner
# #
# #
# # f = outer(42)
# # print(f(3))
# #
# #
# # def outer(n):
# #     return lambda x: x + n
# #
# # f = outer(42)
# # print(f(3))
# #
# #
# # outer = lambda n: lambda x: x + n
# #
# # f = outer(42)
# # print(f(3))
# #
# #
# # print((lambda n: lambda x: x + n)(42)(3))
#
#
# # def values(i):
# #     return i[1]
# #
# # d = {'b': 15, 'c': 5, 'a': 10}
# # lst = list(d.items())
# # print(lst)
# # lst.sort(key = values, reverse = True)
# # print(lst)
# # print(dict(lst))
#
#
# # lst = [
# #     lambda x, y: x + y,
# #     lambda x, y: x - y,
# #     lambda x, y: x * y,
# #     lambda x, y: x / y,
# # ]
# #
# # print(lst[0](5,12))
# # print(lst[1](5,12))
#
#
#
# # d = {
# #     1: lambda: print('Понедельник'),
# #     2: lambda: print('Вторник'),
# #     3: lambda: print('Среда'),
# #     4: lambda: print('Четверг'),
# #     5: lambda: print('Пятница'),
# #     6: lambda: print('Суббота'),
# # }
# #
# # d[4]()
#
#
#
# # print((lambda a, b: a if a > b else b)(15,23))
# # print((lambda a, b, c: min(a, b, c))(9,8,5))
#
#
#
# # map(func, *iterables)
#
# # def mult(t):
# #     return t * 2
# #
# #
# # lst = [2, 8, 12, -5, -10]
# #
# # print(list(map(mult, lst)))
# #
# # print(list(map(lambda t: t * 2, lst)))
#
#
# # old = ['5', '4', '7', '8']
# # print(old)
# # print(list(map(int, old)))
#
#
#
# # st = ['a','b','c','d','e']
# # num = [1, 2, 3, 4, 5]
# #
# # print(list(map(lambda x, y: (x, y), st, num)))
# # print(dict(map(lambda x, y: (x, y), st, num)))
#
#
#
# # t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# #
# # print(tuple(filter(lambda s: len(s) == 3, t)))
#
#
# # lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# # print(list(filter(lambda s: s > 75, lst)))
#
#
# # Декораторы
#
# # def hello():
# #     return "Hello, I am func 'hello'"
# #
# #
# # def super_func(func):
# #     print("Hello, I am super_func")
# #     print(func())
# #
# #
# # super_func(hello)
#
#
#
# # def hello():
# #     return "Hello, I am func 'hello'"
# #
# #
# # test = hello
# # print(test())
#
#
#
# # def my_decorator(func):  #декорирующая функция
# #     def wrapper():
# #         print("*" * 30)
# #         func()
# #         print("*" * 30)
# #     return wrapper
# #
# #
# # @my_decorator #декоратор
# # def func_test():  #декорируемая функция
# #     print("Hello, I am func 'func_test'")
# #
# #
# # @my_decorator
# # def hello():
# #     print("Hello, I am func 'hello'")
# #
# #
# # func_test()
# # hello()
#
#
#
# # def circle(fn):
# #     def wrap():
# #         return "(" + fn() + ")"
# #     return wrap
# #
# # def angle(fn):
# #     def wrap():
# #         return "<" + fn() + ">"
# #     return wrap
# #
# #
# #
# #
# # @circle
# # @angle
# # def expression():
# #     return '5 + 2'
# #
# #
# # print(expression())
#
#
#
#
#
# # def cnt(fn):
# #     count = 0
# #
# #     def wrapper():
# #         nonlocal count
# #         count += 1
# #         fn()
# #         print("Вызов функции: ", count)
# #
# #     return wrapper
# #
# #
# #
# # @cnt
# # def hello():
# #     print("Hello")
# #
# #
# # hello()
# # hello()
# # hello()
# # hello()
# # hello()
# # hello()
#
#
#
#
# # def args_decorator(func):
# #     def wrap(*args, **kwargs):
# #         print("args:", args)
# #         print("kwargs:", kwargs)
# #         func(*args, **kwargs)
# #
# #     return wrap
# #
# #
# # @args_decorator
# # def full_name(a,b,c, study = "Python"):
# #     print(a,b,c, "изучают", study, end = "\n\n")
# #
# #
# # full_name("Ирина", "Борис","Светлана", study = "JavaScript")
# # full_name("Владимир", "Екатерина","Виктор")
#
#
#
#
# # def decor(args1, args2):
# #     def args_dec(fn):
# #         def wrap(a,b):
# #             print(args1, a, args2, b, "=", end=' ')
# #             return fn(a,b)
# #
# #         return wrap
# #     return args_dec
# #
# #
# # @decor("Сумма", "+")
# # def summa(x,y):
# #     print(x + y)
# #
# #
# # @decor("Разность", "-")
# # def sub(x,y):
# #     print(x - y)
# #
# #
# # summa(5,2)
# # sub(5,2)
#
#
# # def multiply(arg):  #3
# #     def decor(func):  # return_num
# #         def wrap(*args, **kwargs):   #5
# #             return arg * func(*args, **kwargs)
# #
# #         return wrap
# #     return decor
# #
# #
# #
# # @multiply(3)
# # def return_num(num):
# #     return num
# #
# #
# # print(return_num(5))
#
#
# # def avg(fn):
# #     def wrap(*args):
# #         print("Среднее арифметическое:", args, "=", fn(*args) / len(args))
# #
# #     return wrap
# #
# # @avg
# # def summa(*args):
# #     print("Сумма числел:", args, "=", sum(args))
# #     return sum(args)
# #
# #
# # summa(2,3,3,4)
#
#
#
# # Урок №11============================================================================================
#
# # print(bin(18)) # 0b10010
# # print(oct(18)) # 0o22
# # print(hex(18)) # 0x12
# #
# # print(0b10010)
# # print(0o22)
# # print(0x12)
# #
# # print(0b10010 + 0o22 + 0x12 + 18)
#
#
#
# # q = 'Pyt'
# # w = 'hon'
# # e = q + w
# # print(e)
# # print(e * 3)
# # print('y' in e)
# # print('a' in e)
# # print(e[1])
# # print(e[1:5])
# # print(e[1:5:2])
# # print(e[10])
# # print(e[10:20])
# # print(e[::-1])
#
#
# # print("Привет")
# # print(u"Привет")
#
#
# # print("C:\\folder\\file.py")
# # print(r"C:\folder\file.py")  #r - игнорирует спец символы
#
#
# # name = "Дмитрий"
# # age = 25
# #
# # print("Меня зовут", name, ". Мне", age, "лет.")
# # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# # print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# # print(f"Меня зовут {name}. Мне {age} лет.")
#
#
# # x = 10
# # y = 5
# # print(f"{x} * {y} / 2 = {x * y / 2}")
# # print(f"{x=}, {y=}")
#
#
# # mas = [4,5,7,8]
# # print(f"mas: {mas[1]}")
#
#
# # print(f"13 / 3 = {round(13/3, 2)}")
#
#
# # dir_name = "folder"
# # file_name = "file.py"
# # print(fr"home\{dir_name}\{file_name}")
#
#
# # a = ("Hello"
# #      " World")
# # print(a)
# #
# # b = """Hello
# # World"""
# # print(b)
# #
# # c = '''Hello
# # World'''
# # print(c)
#
#
#
# # def square(x):
# #     """Принимает число n, возвращает квадрат числа n"""
# #     return x ** 2
# #
# #
# # print(square(3))
# # print(square.__doc__)
# # print(max.__doc__)
# # print(len.__doc__)
#
#
#
#
# # import math
# #
# # def cylinder(r, h):
# #     """
# #     Вычисляет площадь цилиндра.
# #
# #     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
# #     :param r: положительное число, радиус основания цилиндра
# #     :param h: положительное число, высота цилиндра
# #     :return: положительное число, площадь цилиндра
# #     """
# #
# #     return 2 * math.pi * r * (r + h)
# #
# # print(cylinder(2, 4))
# # print(cylinder.__doc__)
#
#
#
#
# # print(ord('a')) #97
# # print(ord('ю')) #97
#
#
# # while True:
# #     n = input("-> ")
# #     if n != "-1":
# #         print(ord(n))
# #     else:
# #         break
#
#
#
#
# # my_str = "Test string for me "
# # arr = [ord(x) for x in my_str]
# # print("ASCII коды:", arr)
# # arr = [int(sum(arr) / len(arr))] + arr
# # print("Среднее арифметическое", arr)
# # arr += [ord(x) for x in input("->")[:3] if ord(x) not in arr]
# # print(arr)
# # print("Количество последних символов:",arr.count(arr[-1]) - 1)
# # arr.sort(reverse=True)
# # print(arr)
#
#
#
#
# # print(chr(97))
#
# # from random import randint
# #
# # shortest = 6
# # longest = 12
# # min_ascii = 33
# # max_ascii = 126
# #
# #
# # def random_password():
# #     random_length = randint(shortest, longest)
# #     res = ""
# #     for i in range(random_length):
# #         random_char = chr(randint(min_ascii, max_ascii))
# #         res += random_char
# #     return res
# #
# #
# # print("Ваш случайный пароль:", random_password())
#
#
# # print(dir(str))
#
#
#
# # s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())   # Hello world! i am learning python.
# # print(s.lower())   # hello world! i am learning python.
# # print(s.upper())   # HELLO WORLD! I AM LEARNING PYTHON.
# # print(s.swapcase())   # HELLO world! i AM LEARNING pYTHON.
# # print(s.title())   # Hello World! I Am Learning Python
# #
# # print(s.count("l", 3, 10))
# # print(s.lower().count("l"))
# #
# # print(s.find("l1"))
# # print(s.rfind("l"))
# #
# # print(s.index("l1"))
# # print(s.rindex("l"))
# #
# # print(s.endswith("on"))
# # print(s.startswith("WORLD", 7))
#
#
#
# # print("abc123".isalnum())  # True
# # print("abc123!%%".isalnum())  # False
# #
# # print("ABCaaaa".isalpha())  # Проверка на наличие букв
# #
# # print("123aa".isdigit())  # Проверка на наличие цифр
# #
# # print('abc@!44'.islower()) # True (проверка на буквы в нижнем регистре)
# # print('abcA'.islower())  # False (проверка на буквы в нижнем регистре)
# #
# # print("ABC@%@3214".isupper())  #True (проверка на буквы в верхнем регистре
#
#
#
# # print("py".center(10, "-"))
#
# # print("    py".lstrip())
# # print("py    ".rstrip())
# # print("      py     ".strip())
#
# # print("https://www.python.org/".strip("/:pths").rstrip("/org."))
#
#
#
# # s = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык"
# # print(s.replace("Nython", "Python", 2))
#
#
# # s = "-"
# # seq = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
# # print(s.join(seq))
# #
# # print("..".join(["1","2"]))
# #
# # print(":".join("Hello"))
#
#
# # print("Строка разделённая пробелами".split())
# # print("www.python.org".split("."))
#
# # a = input("-> ").split()
# # print(a)
#
#
#
# # def fio(name):
# #     print(f"{name[0]} {name[1][0]}. {name[2][0]}.")
# #
# # st = input("Введите ФИО: ").split()
# # print(st)
# # fio(st)
#
#
#
# # Урок №12===========================================================================================================
#
#
# # f = open("text.txt","r")
# # f = open(r"C:\ADD\text.txt","r")
# # print(f)
# # print(*f)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # f.close()
# # print(f.closed)
#
#
#
# # f = open(r"C:\для уроков ADD\text.txt")
# # print(f.read(3))
# # print(f.read())
# # f.close()
#
#
#
# # f = open(r"C:\для уроков ADD\text.txt")
# # try:
# #     print(f.read())
# # finally:
# #     f.close()
#
#
#
# # f = open(r"C:\для уроков ADD\text.txt")
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# # f.close()
#
#
#
# # f = open(r"C:\для уроков ADD\text.txt")
# # print(f.readlines())
# # f.close()
#
#
#
# # f = open(r"C:\для уроков ADD\text.txt")
# # for line in f:
# #     print(line)
# # f.close()
#
#
#
# # f = open("C:\для уроков ADD\\xyz.txt", "w")
# # f.write("Hello.\n")
# # f.close()
#
#
#
# # f = open("C:\для уроков ADD\\xyz.txt", "a")
# # f.write("New text.\n")
# # f.close()
#
#
#
# # f = open("C:\для уроков ADD\\xyz.txt", "w")
# #
# # f.close()
#
#
#
# # f = open("C:\для уроков ADD\\xyz1.txt", "a")
# #
# # f.close()
#
#
#
# # ====================================
# # r - чтение (файл должен быть создан)
# # w - запись (файла может не быть)
# # a - дозапись (файла может не быть)
# #=====================================
#
#
#
# # lines = ["This is  line1\n", "This is  line2\n"]
# #
# # f = open("C:\для уроков ADD\\xyz.txt", "w")
# # f.writelines(lines)
# # f.close()
#
#
#
# # lines = [str(i) + "\t" for i in range(1, 20)]
# # print(lines)
# # f = open("C:\для уроков ADD\\xyz.txt", "w")
# # f.writelines(lines)
# # f.close()
#
#
#
#
# # f = open("C:\для уроков ADD\\text2.txt","w")
# # f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# # f.close()
# #
# # f = open("C:\для уроков ADD\\text2.txt","r")
# # read = f.readlines()
# # print(read)
# # read[1] = "Hello World!\n"
# # print(read)
# # f.close()
# #
# # f = open("C:\для уроков ADD\\text2.txt","w")
# # f.writelines(read)
# # f.close()
#
#
#
# # f = open("C:\для уроков ADD\\text.txt","r")
# # print(f.read(3))
# # print(f.tell())
# # print(f.seek(1))
# # print(f.read())
# # print(f.tell())
# # f.close()
#
#
#
#
# # f = open("C:\для уроков ADD\\text.txt","w")
# # print(f.write("I am learning Python"))
# # print(f.seek(3))
# # print(f.write("-new string-"))
# # print(f.tell())
# # f.close()
# #
# #
# # # "I a-new string-m learning Python"
#
#
#
# # f = open("C:\для уроков ADD\\text222.txt","a+")
# # f.write("hello \nWorld\n")
# # print(f.readlines())
# # f.close()
#
#
#
#
# # with open("C:\\для уроков ADD\\text.txt", "w") as f:
# #     print(f.write("0123456789"))
# # print(f.closed)
#
#
#
#
# # with open("C:\для уроков ADD\\text222.txt", "r") as f:
# #     for line in f:
# #         print(line[:3])
#
#
#
#
#
# # file_name = "res.txt"
# # lst = [4.5, 2.8, 1.0, 0.3, 4.3, 7.777]
# #
# # def get_line(lt):
# #     lt = map(str, lt)   # lt = ['4.5', '2.8', '1.0', '0.3', '4.3', '7.777']
# #     return " ".join(lt)  # "4.5 2.8 1.0 0.3 4.3 7.777"
# #
# #
# # with open(file_name,"w") as f:
# #     f.write(get_line(lst))
# #
# # print("Done!")
# #
# #
# # with open(file_name,"r") as f:
# #     nums = f.read()
# #
# # print(nums)
# # num_list = list(map(float, nums.split()))  # [4.5, 2.8, 1.0, 0.3, 4.3, 7.777]
# # print(num_list)
# # print(sum(num_list))
#
#
#
#
#
# # def longest_words(file):
# #     with open(file, encoding="utf-8") as f:
# #         w = f.read().split()
# #         print(w)
# #         max_length = len(max(w, key=len))
# #         res = [word for word in w if len(word) == max_length]
# #         if len == 1:
# #             return res[0]
# #         return res
# #
# #
# # print(longest_words("text.txt"))
#
#
#
#
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
# #
# # with open("one.txt", "w") as f:
# #     f.write(text)
#
#
# # read_file = "one.txt"
# # write_file = "two.txt"
# #
# # with open(read_file, "r") as fr, open(write_file, "w") as fw:
# #     for line in fr:
# #         line = line.replace("Строка", "Линия -")
# #         fw.write(line)
#
#
#
# #picle======================================
#
#
# # import pickle
# #
# # file_name = "basket.txt"
# #
# # shop_list = {"Фрукты": ["яблоки", "манго"],
# #              "Овощи": ("Морковь", "Лук"),
# #              "бюджет": 1000}
# #
# # with open(file_name, "wb") as f:
# #     pickle.dump(shop_list, f)
# #
# # with open(file_name, "rb") as f:
# #     print(pickle.load(f))
# # #
# # #
# # # shop = pickle.dumps(shop_list)
# # # print(shop)
# # #
# # # load_shop = pickle.loads(shop)
# # # print(load_shop)
#
#
#
# # Урок№13=======================================================================================================
# #json==================================
#
# # import json
# #
# # data = {
# #     'name': 'Olga',
# #     'age': 20,
# #     20: None,
# #     True: True,
# #     None: False,
# #     "list": (5,8,9,7),
# # }
# #
# # # with open('data_file.json', 'w') as f:
# # #     json.dump(data, f, indent=4)
# # #
# # #
# # # with open('data_file.json', 'r') as f:
# # #     data = json.load(f)
# # #
# # # print(data)
# #
# #
# # json_string = json.dumps(data)
# # print(json_string, type(json_string))
# #
# # data1 = json.loads(json_string)
# # print(data1, type(data1))
#
#
# # import json
# # from random import choice
# #
# #
# #
# # def gen_person():
# #     name = ''
# #     tel = ''
# #
# #     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# #     nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# #
# #     while len(name) != 7:
# #         name += choice(letters)
# #     # print(name)
# #
# #
# #     while len(tel) != 10:
# #         tel += choice(nums)
# #     # print(tel)
# #
# #
# #     person = {'name': name, 'tel': tel}
# #     return person
# #
# #
# # def write_json(person_dict):
# #     try:
# #         data = json.load(open('persons.json', 'r'))
# #     except FileNotFoundError:
# #         data = []
# #
# #
# #     data.append(person_dict)
# #     with open('persons.json', 'w') as f:
# #         json.dump(data, f, indent=2)
# #
# #
# #
# # for i in range(5):
# #     write_json(gen_person())
#
#
#
# # Из интернета==============================
#
# # import requests
# # import json
# #
# #
# # response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # todos = json.loads(response.text)
# #
# #
# # # print(type(todos))
# # # print(todos[0])
# #
# # filter_todos = []
# #
# # for todo in todos:
# #     if todo['completed']:
# #         filter_todos.append(todo)
# #
# # # print(filter_todos)
# #
# # with open('todos.json', 'w') as f:
# #     json.dump(filter_todos, f, indent=2)
# #
# #
# # with open('todos.json', 'r') as f:
# #     data = json.load(f)
# #     print(data, len(data))
#
#
#
# # import csv
#
# # with open("data.csv") as f:
# #     file_reader = csv.reader(f, delimiter=';')
# #     count = 0
# #     for row in file_reader:
# #         # print(row)
# #         if count == 0:
# #             print(f"файл содержит столцы: {':'.join(row)}")
# #         else:
# #             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
# #         count += 1
# #
# #     print(f"Всего в файле {count} строка.")
#
#
# # with open("data1.") as f:
# #     field_name = ["Имя", "Проффесия", "Год рождения"]
# #     file_reader = csv.DictReader(f, delimiter=';', fieldnames=field_name)
# #     count = 0
# #     for row in file_reader:
# #         if count == 0:
# #             print(f"Файл содержит столбцы: {';'.join(row)}")
# #         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
# #         count += 1
#
#
# # import csv
#
#
# # with open("student.csv", "w") as f:
# #     writer = csv.writer(f, delimiter=";", lineterminator="\r")
# #     writer.writerow(["Имя", "Класс", "Возраст"])
# #     writer.writerow(["Женя", 9, 15])
# #     writer.writerow(["Саша", 5, 12])
# #     writer.writerow(["Маша", 11, 18])
#
#
#
# # data = [['hostname', 'vendor', 'model', 'location'],
# #         ['sw1', 'Cisco', '3750', 'London, Best str'],
# #         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
# #         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
# #         ['sw4', 'Cisco', '3650', 'London, Best str']]
# #
# # with open("data_new.csv", "w") as f:
# #     writer = csv.writer(f, delimiter=';', lineterminator='\r')
# #
# #     # for row in data:
# #     #     writer.writerow(row)
# #
# #     writer.writerows(data)
#
#
#
# # with open("student_1.csv", "w") as f:
# #     names = ["Имя", "Возраст"]
# #     file_writer = csv.DictWriter(f, delimiter=";", fieldnames=names, lineterminator="\r")
# #     file_writer.writeheader()
# #     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
# #     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
# #     file_writer.writerow({"Имя": "Вова", "Возраст": 14})
#
#
#
#
#
# # data = [{
# #     'hostname': 'sw1',
# #     'location': 'London',
# #     'model': '3750',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw2',
# #     'location': 'Liverpool',
# #     'model': '3850',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw3',
# #     'location': 'Liverpool',
# #     'model': '3650',
# #     'vendor': 'Cisco'
# # }, {
# #     'hostname': 'sw4',
# #     'location': 'London',
# #     'model': '3650',
# #     'vendor': 'Cisco'
# # }]
# #
# # with open("file_data.csv", "w", newline='') as f:
# #     writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=';', lineterminator='\r')
# #     writer.writeheader()
# #     for row in data:
# #         writer.writerow(row)
#
#
#
#
# # import sqlite3
#
# #либо так
# # conn = sqlite3.connect('profile.db')
# # cur = conn.cursor()
# #
# # conn.close()
#
# #либо так
# # with sqlite3.connect('profile.db') as connection:
# #     cursor = connection.cursor()
# #     # команда для создания таблицы
# #     # cursor.execute('''CREATE TABLE IF NOT EXISTS users (
# #     #     id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     #     name TEXT NOT NULL,
# #     #     summa REAL,
# #     #     date BLOB
# #     # )''')
# #
# #     cursor.execute('''DROP TABLE IF EXISTS users''')
#
#
# # import sqlite3
# #
# #
# # with sqlite3.connect('users.db') as connection:
# #     cursor = connection.cursor()
#     # cursor.execute('''CREATE TABLE IF NOT EXISTS person (
#     #     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #     name TEXT NOT NULL,
#     #     phone BLOB DEFAULT "+79990000000",
#     #     age INTEGER NOT NULL CHECK (age >=0 AND age <= 100),
#     #     emil TEXT UNIQUE NOT NULL
#     # )''')
#
#
#     # cursor.execute('''
#     # ALTER TABLE person
#     # RENAME TO person_table
#     # ''')
#
#
#     # cursor.execute('''
#     # ALTER TABLE person_table
#     # ADD COLUMN surname TEXT NOT NULL DEFAULT "fio"
#     # ''')
#
#
#
#     # cursor.execute('''
#     # ALTER TABLE person_table
#     # RENAME COLUMN surname TO home_address
#     # ''')
#
#
#     # cursor.execute('''
#     # DROP TABLE person_table
#     # ''')
#
#
#
# # import sqlite3
# #
# #
# # with sqlite3.connect('db_3.db') as connection:
# #     cur = connection.cursor()
# #     cur.execute('''
# #         SELECT *
# #         FROM T1
# #         ORDER BY FNAME
# #         LIMIT 2, 5
# #     ''')
#
#
#     # res1 = cur.fetchone()
#     # print(res1)
#
#
#     # res2 = cur.fetchmany(9)
#     # print(res2)
#
#
#     # res = cur.fetchall()
#     # print(res)
#
#
#     # for res in cur:
#     #     print(res)
#
#
#
#
# # import sqlite3
# #
# ##Просто 2 таблицы
# #
# #
# # with sqlite3.connect('people.db') as connection:
# #     cur = connection.cursor()
# #     cur.execute('''CREATE TABLE IF NOT EXISTS companies (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT NOT NULL
# #     )''')
# #     cur.execute('''CREATE TABLE IF NOT EXISTS users (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT NOT NULL,
# #         age INTEGER,
# #         company_id INTEGER,
# #         FOREIGN KEY (company_id) REFERENCES companies (id) ON DELETE SET NULL
# #     )''')
#
#
#
# # import sqlite3
# #
# # #Многие таблицы ко многим
# #
# # with sqlite3.connect('people.db') as connection:
# #     cur = connection.cursor()
# #     cur.execute('''CREATE TABLE IF NOT EXISTS books (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         title TEXT NOT NULL,
# #         count_page INTEGER NOT NULL CHECK (count_page > 0),
# #         price REAL CHECK (price > 0)
# #     )''')
# #     cur.execute('''CREATE TABLE IF NOT EXISTS author (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT NOT NULL,
# #         age INTEGER CHECK (age > 16)
# #     )''')
# #     cur.execute('''CREATE TABLE IF NOT EXISTS author_books (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         books_id INTEGER NOT NULL,
# #         author_id INTEGER NOT NULL,
# #         FOREIGN KEY (books_id) REFERENCES books (id)
# #         FOREIGN KEY (author_id) REFERENCES author (id)
# #     )''')
#
#
#
# # import sqlite3
# #
# #
# # with sqlite3.connect('people.db') as connection:
# #     cur = connection.cursor()
# #     cur.execute('''CREATE TABLE IF NOT EXISTS student (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         surname TEXT,
# #         name TEXT,
# #         patronymic TEXT,
# #         age INTEGER,
# #         [group] INTEGER NOT NULL,
# #         FOREIGN KEY ([group]) REFERENCES groups (id)
# #     )''')
# #
# #     cur.execute('''CREATE TABLE IF NOT EXISTS groups (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         group_name TEXT
# #     )''')
# #
# #     cur.execute('''CREATE TABLE IF NOT EXISTS association (
# #         lesson_id INTEGER NOT NULL,
# #         group_id INTEGER NOT NULL,
# #         FOREIGN KEY (lesson_id) REFERENCES lessons (id)
# #         FOREIGN KEY (group_id) REFERENCES groups (id)
# #     )''')
# #
# #     cur.execute('''CREATE TABLE IF NOT EXISTS lessons (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         lesson_title TEXT
# #     )''')
#
#
#
# # import sqlite3
#
# # auto = [
# #     ('BMW', 54000),
# #     ('Chevrolet', 46000),
# #     ('Daewoo', 38000),
# #     ('Citroen', 29000),
# #     ('Honda', 33000),
# # ]
# #
# #
#
# # with sqlite3.connect('cars.db') as connection:
# #     cur = connection.cursor()
# #     cur.execute('''CREATE TABLE IF NOT EXISTS cars (
# #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         model TEXT,
# #         price INTEGER
# #     )''')
# #
# #
# #     cur.executescript("""DELETE FROM cars WHERE model  LIKE 'B%';
# #                       UPDATE cars SET price = price + 100;
# #                       """)
#
#
#     # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})
#
#
#
#     # cur.executemany("INSERT INTO cars VALUES (NULL, ?, ?)", auto)
#
#
#
#     # for car in auto:
#     #     cur.execute("INSERT INTO cars VALUES (NULL, ?, ?)", car)
#
#
#     # cur.execute("INSERT INTO cars VALUES (1, 'Renault', 22000)")
#     # cur.execute("INSERT INTO cars VALUES (2, 'Volvo', 29000)")
#     # cur.execute("INSERT INTO cars VALUES (3, 'Mercedes', 57000)")
#     # cur.execute("INSERT INTO cars VALUES (4, 'Bentley', 35000)")
#     # cur.execute("INSERT INTO cars VALUES (5, 'Audi', 52000)")
#
#
# # try:
# #     con = sqlite3.connect('cars.db')
# #     cur = con.cursor()
# #     cur.execute('''CREATE TABLE IF NOT EXISTS cars (
# #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         model TEXT,
# #         price INTEGER
# #         );
# #         BEGIN;
# #         INSERT INTO cars VALUES (NULL, 'Renault', 22000);
# #         UPDATE cars SET price = price + 100;
# #         ''')
# #
# #     con.commit()
# # except sqlite3.Error as e:
# #     if con:
# #         con.rollback()
# #     print("Ошибка выполнения запроса")
# # finally:
# #     if con:
# #         con.close()
#
#
#
# # import sqlite3
# #
# # with sqlite3.connect('cars.db') as connection:
# #     cur = connection.cursor()
# #     cur.executescript('''CREATE TABLE IF NOT EXISTS cars (
# #         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         model TEXT,
# #         price INTEGER
# #     );
# #     CREATE TABLE IF NOT EXISTS cost (
# #         name TEXT, tr_in INTEGER, buy INTEGER,
# #     )''')
# #
# #     cur.executescript('''INSERT INTO cars VALUES (NULL, "Запорожец", 1000)''')
# #     last_id = cur.lastrowid
# #     by_car_id = 2
# #
# #     cur.execute('''INSERT INTO cost VALUES ("Фёдор", ?, ?)''', (last_id, by_car_id))
#
#
#
#
# import sqlite3

# with sqlite3.connect('cars.db') as connection:
#     connection.row_factory = sqlite3.Row
#     cursor = connection.cursor()
#     # cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
#     #     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #     model TEXT,
#     #     price INTEGER,
#     # )''')
#
#
# cursor.execute('''SELECT model, price FROM cars''')
# for row in cursor:
#     print(row[0])



# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#         return True
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sqlite3.connect('cars.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.executescript('''CREATE TABLE IF NOT EXISTS users (
#           name TEXT,
#           ava BLOB,
#           score INTEGER
#          )''')
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Федор', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users LIMIT 1")  # ("бинарный код",)
#     img = cur.fetchone()["ava"]  # "бинарный код"
#     write_ava("out.png", img)




# import sqlite3
#
# with sqlite3.connect('cars_new.db') as conn:
#     cursor = conn.cursor()
#
#     # with open('sql_dump.sql', "w") as f:
#     #     for sql in conn.iterdump():
#     #         f.write(sql)
#
#     with open('sql_dump.sql', "w") as f:
#         sql = f.read()
#         cursor.executescript(sql)



# print("изменения после коммита")

# print("Рабочий процесс")


import numpy as np

lst = [1,2,3,4,5]
# print(lst * 2)

arr = np.array([1,2,3,4,5])
print(arr)

arr2 = np.array([[1,2,3, 11, 12, 13],[4,5,6,14,15,16]])
print(arr2)

# print(arr * 2)
# print(arr ** 2)
# print(arr2 * 2)


# количесвто измерений массива
# print(arr.ndim)
# print(arr2.ndim)



# количество строк и столбцов
# print(arr.shape)
# print(arr2.shape)


# общее количество элементов
# print(arr.size)
# print(arr2.size


# print(arr2[0,2])
# print(arr2[0, :])
# print(arr2[:, 0])

# print(arr2 [0, 1:4:2])
# print(arr2 [1, 0:-1:2])


# arr2[0,0] = 50
# print(arr2)

# arr2 [0, :] = [0,0,0,1,1,1]
# print(arr2)


# zeros = np.zeros((3,4), dtype="int32")
# print(zeros)

# zeros = np.zeros((3,4), dtype="float64")
# print(zeros)

# ones = np.ones((2,3), dtype="int32")
# print(ones)