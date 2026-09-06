
figure = int(input("1-прямоугольник, 2-треугольник, 3-круг: "))

if figure == 1:
    a = int(input("Ширина: "))
    b = int(input("Высота: "))


    def rectangle (a, b):
        return a * b


    print("Площадь:", rectangle(a,b))


if figure == 2:
    a = int(input("Основание: "))
    b = int(input("Высота: "))


    def triangle (a, b):
        return (a * b) / 2


    print("Площадь:", triangle(a,b))


if figure == 3:
    a = int(input("Радиус окружности: "))

    import math


    def cercle (a):
        return math.pi * (a ** 2)


    print("Площадь:", cercle(a))

