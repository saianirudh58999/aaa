from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1',
        'publication_year': 2021
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2',
        'publication_year': 2022
    }
]

# GET /books - Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET /books/<int:book_id> - Get a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404



if __name__ == '__main__':
    app.run(debug=True)