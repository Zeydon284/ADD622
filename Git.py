
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









# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd


# №1

# s = [35, 42, 54, 62, 71, 85, 93, 104, 115, 128]
#
# price = [8.4, 11.3, 14.6, 19.8, 22.1, 28.9, 33.5, 41.6, 49.5, 58.9]
#
# plt.scatter(s, price, color='blue', alpha=0.5)
# plt.grid()
# plt.title('Соотношение площади и стоимоти квартир')
# plt.xlabel("Площадь (метры кв.)")
# plt.ylabel("Стоимость (млн. руб.)")
#
# plt.show()


# №2

# categories = ["Электроника", "Одежда", "Книги", "Дом и сад"]
# price = [450, 320, 180, 290]
# colors = ["red", "green", "blue", "yellow"]
#
# plt.figure(figsize=(8, 5))
#
# plt.bar(categories, price, color=colors, alpha=0.8, width=0.6)
#
# plt.title("Сравнение объемов продаж разных категорий товаров")
# plt.xlabel("Категории")
# plt.ylabel("Стоимость (тыс. руб.)")
# plt.grid(axis="y", alpha=0.5)
# plt.show()















# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd


# №1

# quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# electronics = [40, 55, 48, 70]
# clothing = [30, 45, 40, 65]
# books = [15, 20, 18, 25]
#
#
# colors = ['red', 'green', 'blue']
#
#
# plt.figure(figsize=(8, 5))
#
# plt.title("Продажи отделов магазина")
# plt.xlabel("Кварталы")
# plt.ylabel("Количество продаж")
#
# plt.grid()
#
# plt.plot(quarters, electronics, color=colors[0], label = 'Электроника', marker='o')
# plt.plot(quarters, clothing, color=colors[1], label = 'Одежда', marker='s')
# plt.plot(quarters, books, color=colors[2], label = 'Книги', marker='^')
#
# plt.legend()
#
# plt.show()



#№2

# brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
# market_share = [30, 25, 20, 25]
#
# plt.figure(figsize=(6, 6))
# plt.pie(market_share, labels=brands, autopct='%1.1f%%', startangle=140)
# plt.title("Доли рынка смартфонов")
#
#
# plt.show()











# ======================================================================================================================
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd



#№1

# tips = sns.load_dataset("tips")
#
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
#
# plt.title("взаимосвязь между общим счетом и оставленными чаевыми")
# plt.xlabel("Общий счет")
# plt.ylabel("Чаевые")
#
# plt.tight_layout()
#
# plt.show()



#№2

# tips = sns.load_dataset("tips")
#
# sns.boxplot(data=tips, x="smoker", y="total_bill")
#
# plt.title("распределение общего счета между курящими и некурящими клиентами")
# plt.xlabel("курящий клиент")
# plt.ylabel("Общий счёт")
# plt.tight_layout()
#
# plt.show()



#№3

# iris = sns.load_dataset("iris")
#
# corr_matrix = iris.corr(numeric_only=True)
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Тепловая карта корреляции признаков датасета Iris")
# plt.tight_layout()
#
#
# plt.show()







# plotly 1 hm===========================================================================================================

# import plotly.express as px


# №1 =======================
#
# df = px.data.gapminder()
# df_canada = df[df['country'] == 'Canada']
#
# fig = px.bar(df_canada, x="year", y="pop", title="Изменение численности населения Канады",
#              labels={'year': 'Год', 'pop': 'Численность населения'})
#
# fig.show()



# №2 =========================
#
# df = px.data.tips()
#
# fig = px.sunburst(df, path=["day", "time", "smoker"], values="total_bill", title="Иерархическая структура чаевых")
#
# fig.show()







# plotly 2 hm ==========================================================================================================


# import plotly.express as px
# import pandas as pd


#№1
#
# import plotly.express as px
# import pandas as pd
#
#
# df = {
#     "month": ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб', 'Дек'],
#     "temp": [-20, -12, 8, 9, 20, 35, 38, 40, 15, 9, -16, -30]
# }
#
# df = pd.DataFrame(df)
#
# fig = px.bar(df, x="month", y="temp", animation_frame="month", color="temp", title="Температура по месяцам",
#              labels={"temp": "Температура (°C)", "month": "Месяц года"})
#
#
# fig.show()



#№2
#
# from dash import Dash, html, dcc
# import pandas as pd
# import plotly.express as px
#
#
# x_values = [1, 2, 3, 4, 5]
# y_values = [x**2 for x in x_values]
#
# df = {
#     'x': x_values,
#     'y': y_values
# }
#
# df = pd.DataFrame(df)
#
# fig = px.line(
#     df,
#     x='x',
#     y='y',
#     title='График функции y = x**2',
#     labels={'x': 'Значение X', 'y': 'Значение Y (x**2)'}
# )
#
# app = Dash()
#
# app.layout = html.Div([html.H1(
#         children="Мой первый дашборд"),
#     dcc.Graph(
#         id='controls-and-graph',
#         figure=fig)
# ])
#
# if __name__ == '__main__':
#     app.run(debug=True)







# Dash 1 hm ==========================================================================================================


#№1
#
# from dash import Dash, html, dcc, callback, Input, Output
# import plotly.express as px
# import pandas as pd
#
#
# data = {
#     "Товар": ["Яблоки", "Бананы", "Манго", "Груши", "Апельсины"],
#     "Продажи (шт.)": [40, 80, 20, 45, 60]
# }
#
# df = pd.DataFrame(data)
#
# app = Dash()
#
#
# app.layout = html.Div([
#     html.H2("Переключатель графиков"),
#
#     html.Div([
#         html.Label("Выберите тип визуализации:"),
#         dcc.RadioItems(
#             id="chart-type-radio",
#             options=[
#                 {"label": "Столбчатая диаграмма", "value": "bar"},
#                 {"label": "Линейный график", "value": "line"}
#             ],
#             value="bar"
#         )
#     ]),
#
#     dcc.Graph(id="sales-chart")
#
# ])
#
#
# @app.callback(
#     Output("sales-chart", "figure"),
#     Input("chart-type-radio", "value")
# )
#
# def update_graph(chart_type):
#     if chart_type == "bar":
#
#
#         fig = px.bar(
#             df,
#             x="Товар",
#             y="Продажи (шт.)",
#             title="Продажи товаров (Столбчатая диаграмма)",
#             color="Товар"
#         )
#
#     else:
#
#
#         fig = px.line(
#             df,
#             x="Товар",
#             y="Продажи (шт.)",
#             title="Продажи товаров (Линейный график)",
#             markers=True
#         )
#
#
#     return fig
#
#
# if __name__ == "__main__":
#     app.run(debug=True)






# Dash/SQL 2 hm ========================================================================================================
#
# import sqlite3
# import pandas as pd
# import plotly.express as px
# from dash import Dash, html, dcc, Input, Output
#
#
# def create_sample_db():
#     conn = sqlite3.connect('sales.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             city TEXT,
#             month TEXT,
#             amount REAL
#     )
#     ''')
#
#     sample_data = [
#         ('Москва', 'Январь', 120000),
#         ('Москва', 'Февраль', 150000),
#         ('Москва', 'Март', 170000),
#         ('Санкт-Питербург', 'Январь', 90000),
#         ('Санкт-Питербург', 'Февраль', 95000),
#         ('Санкт-Питербург', 'Март', 110000),
#         ('Казань', 'Январь', 50000),
#         ('Казань', 'Февраль', 60000),
#         ('Казань', 'Март', 75000),
#     ]
#
#     cursor.executemany('''INSERT INTO sales (city, month, amount) VALUES (?, ?, ?)''', sample_data)
#     conn.commit()
#     conn.close()
#
# # create_sample_db()
#
#
#
# def get_data_from_db():
#     conn = sqlite3.connect('sales.db')
#     df = pd.read_sql_query('SELECT city, month, amount FROM sales', conn)
#     conn.close()
#     return df
#
#
# df_sales = get_data_from_db()
# cities = df_sales['city'].unique()
# # print(cities)
#
#
# app = Dash()
#
# app.layout = html.Div([
#     html.H1("Динамика продаж по городам", style={'textAlign': 'center'}),
#     html.Div([
#         html.Label("Выберите город:"),
#         dcc.Dropdown(
#             id='city-dropdown',
#             options=[{'label': city, 'value': city} for city in cities],
#             value=cities[0],
#             clearable=False
#         )
#     ], style={'width': '50%', 'margin': '0 auto'}),
#
#     dcc.Graph(id='sales-graph')
# ])
#
# @app.callback(
#     Output('sales-graph', 'figure'),
#     Input('city-dropdown', 'value')
# )
#
# def update_graph(selected_city):
#     filtered_df = df_sales[df_sales['city'] == selected_city]
#     fig = px.bar(filtered_df, x='month', y='amount', color='month' ,title=f"Продажи в городе: {selected_city}",
#     labels={'month': 'Месяц', 'amount': 'Сумма продаж (руб.)'})
#
#     return fig
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# Бернулли (1) hm ======================================================================================================

import math

n = 10
k = 5
p = 0.4
q = 1 - p

combinations = math.comb(n, k)
probability = combinations * (p ** k) * (q ** (n-k))

print(f"Число сочетаний: {combinations}")
print(f"Вероятность в процентах: {probability * 100:.2f}%")


