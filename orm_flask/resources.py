from flask import jsonify, request, Response
from flask_restful import Resource

from database import db
from orm_flask.models import User


class Products(Resource):

    def get(self) -> Response:
        """Endpoint to get all users from db"""
        users = db.session.query(User).all()
        users_list = [user.to_json() for user in users]
        return jsonify(users_list)

    def post(self) -> tuple[str, int]:
        username = request.form.get('username', type=str)
        email = request.form.get('email', type=str)
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return f"Пользователь успешно создан", 201


class Product(Resource):
    def get(self, pk: int) -> Response:
        """Endpoint to get certain user from db"""
        user = db.session.query(User).get({'id': pk})
        return jsonify(user.to_json())

    def delete(self, pk: int) -> tuple[str, int]:
        """Endpoint to delete certain user"""
        user = db.session.query(User).get({'id': pk})
        db.session.delete(user)
        db.session.commit()
        return f"Пользователь №{pk} успешно удален", 200
