from flask import Flask, request
import os.path


app = Flask(__name__)
books_dir_root = "D:/PycharmProjects/ReadingGroup/books/"


@app.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    username = credentials['username']
    password = credentials['password']

    if username == 'admin' and password == 'secret':
        return 'Login successful', 200
    else:
        return 'Invalid login credentials', 401


@app.route('/book', methods=['GET'])
def get_book():
    book_name = request.args.get("book_name")
    if not book_name:
        return "Invalid book name"
    full_path = books_dir_root + book_name
    if os.path.isfile(full_path):
        return read_file_into_string(full_path)
    return f'Can\'t find the book with name ${book_name}'

def read_file_into_string(file_path):
    with open(file_path, "rb") as file:
        return file.read()

if __name__ == '__main__':
    app.run(None, 8080, True)