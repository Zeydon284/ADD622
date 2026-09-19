
# import pandas as pd


# №1 =====================
# s = pd.Series([12, 15, 8, 20, 25, 30, 10], index=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])
# print(s)
# print("*" * 50)
# filtered_data = s[s > 15]
# print(filtered_data)


# №2 ======================
# s = pd.Series([85, 90, 78, 92, 88, 76, 95, 92], index=['Аня', 'Боря', 'Влад', 'Глаша', 'Дима', 'Ева', 'Жора', 'Зина'])
# print(s)
#
# print("*" * 50)
#
# print(s.nlargest(3))


# №3 ======================
# s = pd.Series([16, 25, 38, 17, 42, 15])
# s_new = s>=18
# print(s_new)