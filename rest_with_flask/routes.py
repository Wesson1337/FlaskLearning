from dataclasses import asdict
from typing import Tuple, Dict

from apispec.ext.marshmallow import MarshmallowPlugin
from flasgger import APISpec, Swagger
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError
from apispec_webframeworks.flask import FlaskPlugin

from rest_with_flask.models import get_all_books, init_db, BOOKS, Book, add_book
from rest_with_flask.schema import BookSchema

app = Flask(__name__)
api = Api(app)

spec = APISpec(
    title='Booklist',
    version='1.0.0',
    openapi_version='2.0',
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin()
    ]
)

class BookList(Resource):

    def get(self):
        """
        This is an endpoint for obtaining the books list.
        ---
        tags:
          - books
        responses:
          200:
            description: Books data
            schema:
              type: array
              items:
                $ref: '#/definitions/Book'
        """
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> Tuple[Dict, int]:
        """
        This is an endpoint for book creation.
        ---
        tags:
          - books
        parameters:
          - in: body
            name: new book params
            schema:
              $ref: '#/definitions/Book'
        responses:
          201:
            description: The book has been created
            schema:
              $ref: '#/definitions/Book'
        """

        data = request.json

        schema = BookSchema()

        try:
            schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(Book(**data))
        return schema.dump(book), 201


template = spec.to_flasgger(
    app,
    definitions=[BookSchema],
)

swagger = Swagger(app, template=template)

api.add_resource(BookList, '/api/books')

if __name__ == '__main__':
    init_db(initial_records=BOOKS)
    app.run(debug=True)
