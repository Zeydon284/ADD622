
def func(city):
    many = 0

    def inner():
        nonlocal many
        many += 1
        print(city, many)

    return inner


cont1 = func("Москва")
cont1()
cont1()
cont2 = func("Сочи")
cont2()
cont2()
cont1()

