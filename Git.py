
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









# import pandas as pd
# import numpy as np

# №1 =======================

# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга'],
#     'Возраст': [25, 34, 41, 28],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# print("*" * 50)
#
# print(df[df['Возраст'] > 30])



# №2 =======================

# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга', 'Марина', 'Роман', 'Екатерина', 'Виктор', 'Ирина'],
#     'Возраст': [25, 34, 41, 28, 19, 20, 36, 41, 38],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Санкт-Петербург', 'Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# print("*" * 50)
#
# print(df.groupby("Город")["Возраст"].mean())



# №3 =======================

# data = {
#     'Имя': ['Анна', 'Борис', 'Влад', 'Ольга', 'Марина', 'Роман', 'Екатерина', 'Виктор', 'Ирина'],
#     'Возраст': [25, 34, 41, 28, 19, 20, 36, 41, 38],
#     'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Сочи', 'Санкт-Петербург', 'Москва', 'Санкт-Петербург', 'Казань', 'Сочи']
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# print("*" * 50)
#
# df['Статус'] = np.where(df['Возраст'] >= 30, 'Взрослый', 'Молодой')
#
# print(df)



# №4 =======================

# data = {
#     'Имя товара': ['Монитор', np.nan, 'Мышка', 'Клавиатура'],
#     'Продажи': [15000, 23000, np.nan, 8000]
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# print("*" * 50)
#
# df = df.dropna(subset=['Имя товара'])
#
# ms = df['Продажи'].mean()
#
# df['Продажи'] = df['Продажи'].fillna(ms)
#
# print(df)








# import numpy as np
# import matplotlib.pyplot as plt

# №1

# Ay = np.array([20, 22, 19, 23, 25])
# By = np.array([15, 17, 18, 16, 21])
#
# x = np.array([1, 2, 3, 4, 5])
#
# fig, ax = plt.subplots()
#
# ax.set_xticks(x)
# ax.set_xticklabels(["Пн", "Вт", "Ср", "Чт", "Пт"])
#
# ax.plot(x, Ay,  label = "Температура A", color = "red", marker = "o" )
# ax.plot(x, By,  label = "Температура Б", color = "green",marker = "s", linestyle = "-." )
#
# ax.set_title("Изменение температуры")
# ax.set_xlabel("День")
# ax.set_ylabel("Температура")
#
# ax.legend(loc="upper left", fontsize = 12, framealpha = 0.8)
#
# plt.grid()
# plt.show()



# №2

# x = np.array([1, 2, 3, 4, 5, 6])
# y = np.array([120, 150, 90, 210, 180, 250])
#
# fig, ax = plt.subplots()
#
# ax.set_title("Изменение дохода")
# ax.set_xlabel("Месяц")
# ax.set_ylabel("Доход (тыс. руб.)")
#
# ax.set_xticks(x)
# ax.set_xticklabels(["Янв", "Фев", "Март", "Апрель", "Май", "Июнь"])
#
# ax.plot(x, y, color = 'purple',  linewidth=3)
# ax.plot(6, 250, marker = 'o', markerfacecolor = 'red', markersize = 10)
# ax.grid()
# plt.show()
