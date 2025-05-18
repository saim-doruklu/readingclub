from flask import Flask, request
import os.path

from server.book import Book
import json

app = Flask(__name__)

books_dir_root = "resources/books/"

@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    username = credentials['username']
    password = credentials['password']

    if username == 'admin' and password == 'secret':
        return 'Login successful', 200
    else:
        return 'Invalid login credentials', 401


@app.route('/book/<book_id>', methods=['GET'])
def get_book(book_id):
    if not book_id:
        return "Invalid book name"
    full_path = f'{books_dir_root}{book_id}/raw'
    if os.path.isfile(full_path):
        return read_file_into_string(full_path)
    return f'Can\'t find the book with name ${book_id}'


def read_file_into_string(file_path):
    with open(file_path, "rb") as file:
        return file.read()


@app.route('/books', methods=['GET'])
def get_book_list():
    files = os.listdir(books_dir_root)
    books: list[Book] = []
    for f in files:
        this_book = Book()
        this_book.id = f
        book_metadata = json.loads(read_file_into_string(f'{books_dir_root}{f}/metadata.json'))
        this_book.author = book_metadata['author']
        this_book.language = book_metadata['language']
        this_book.name = book_metadata['name']
        books.append(this_book)
    return json.dumps(books, default=vars)


def read_file_into_string(file_path):
    with open(file_path, "rb") as file:
        return file.read()


if __name__ == '__main__':
    app.run(None, 8080, True)
