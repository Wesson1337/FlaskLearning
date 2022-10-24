from flask import jsonify, request
from flask_restful import Resource

from orm_flask.models import User
from database import db


class Products(Resource):

    def get(self):
        users = db.session.query(User).all()
        users_list = [user.to_json() for user in users]
        return jsonify(users_list)

    def post(self):
        username = request.form.get('username', type=str)
        email = request.form.get('email', type=str)
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return f"Пользователь успешно создан", 201




