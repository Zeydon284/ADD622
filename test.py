

import csv
import requests

url = "https://jsonplaceholder.typicode.com/todos"

columns = ['userId', 'id', 'title', 'completed']


response = requests.get(url)
data = response.json()

with open('todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')

    writer.writeheader()
    writer.writerows(data)












