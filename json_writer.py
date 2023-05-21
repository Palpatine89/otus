import json

from csv import DictReader
from files import CSV_FILE_PATH, JSON_FILE_PATH

# Парсим books.csv и users.json
with open(CSV_FILE_PATH, "r") as csv_file, open(JSON_FILE_PATH, "r") as json_file:
    reader = DictReader(csv_file)
    books_list = []

    for row in reader:
        selected_row = {'Title': row['Title'],
                        'Author': row['Author'],
                        'Genre': row['Genre'],
                        'Pages': row['Pages']}
        books_list.append(selected_row)

    users = json.load(json_file)
    users_list = []

    for row in users:
        selected_row = {'name': row['name'],
                        'gender': row['gender'],
                        'address': row['address'],
                        'age': row['age']}
        users_list.append(selected_row)

with open('distributed_books.json', "w") as output_file:
    users_amount = len(users_list)  # Получаем общее количество пользователей
    books_amount = len(books_list)  # Получаем общее количество книг
    books_for_users = books_amount // users_amount  # Вычисляем распределение книг без остатка
    remaining_books = books_amount % users_amount  # Вычисляем остаток книг

    distributed_list = []
    start_index = 0

    for i in range(users_amount):
        end_index = start_index + books_for_users

        if i < remaining_books:
            end_index += 1

        user_books = books_list[start_index:end_index]
        distributed_list.append(user_books)
        start_index = end_index

    for user, books in zip(users_list, distributed_list):
        user['books'] = books

    json.dump(users_list, output_file, indent=4)








