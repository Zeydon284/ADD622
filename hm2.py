


a = int(input("pos1 = "))
b = int(input("pos2 = "))

if a >= 3 or b >= 3:
    print("Такой строки не найдено")
else:

    f = open("C:\для уроков ADD\\text2.txt", "w")
    f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
    f.close()


    # f = open("C:\для уроков ADD\\text2.txt","r")
    # read = f.readlines()
    # print(read[a])
    # f.close()
    #
    # f = open("C:\для уроков ADD\\text2.txt","r")
    # read = f.readlines()
    # print(read[b])
    # f.close()

    with open("C:\для уроков ADD\\text2.txt", "r") as f:
        lines = f.readlines()

    lines[a], lines[b] = lines[b], lines[a]

    with open("C:\для уроков ADD\\text2.txt", "w") as f:
        f.writelines(lines)






