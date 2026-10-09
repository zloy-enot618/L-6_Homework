from fastapi import FastAPI

my_app = FastAPI()



books_list = [
    {
        "name": "Во круг света за 80 дней",
        "author": "Жуль Верн",
        "genre": "Приключения"
    },
    {
        "name": "Гарри Поттер",
        "author": "Джоанн Роулинг",
        "genre": "Фантастика"
    },
    {
        "name": "Шерлок Холмс",
        "author": "Артур Конан Дойл",
        "genre": "Детектив"
    },
    {
        "name": "Властелин Колец",
        "author": "Джон Рональд Руэл Толкин",
        "genre": "Фантастика"
    }
]

@my_app.get("/")
def say_hello():
    return {
        "api-name": "Books API!",
        "books-directory": "/books"
    }

@my_app.get("/books")
def show_books_function():
    return books_list