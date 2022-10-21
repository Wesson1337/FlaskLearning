from dataclasses import asdict

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from rest_with_flask.models import get_all_books, init_db, BOOKS, Book, add_book
from rest_with_flask.schema import BookSchema

app = Flask(__name__)
api = Api(app)


class BookList(Resource):

    def get(self):
        return {'data': [asdict(book) for book in get_all_books()]}, 200

    def post(self):

        data = request.json

        schema = BookSchema()

        try:
            schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(Book(**data))
        return schema.dump(book), 201


api.add_resource(BookList, '/api/books')


if __name__ == '__main__':
    init_db(initial_records=BOOKS)
    app.run(debug=True)
