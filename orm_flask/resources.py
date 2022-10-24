from flask import jsonify, request, Response, Blueprint
from flask_restful import Resource, Api

from orm_flask.services import get_all_users, create_new_user, get_certain_user, delete_user, update_user

users_api_bp = Blueprint('users_api', __name__)
users_api = Api(users_api_bp)


class UsersController(Resource):

    def get(self) -> Response:
        users_list = get_all_users()

        return jsonify(users_list)

    def post(self) -> tuple[str, int]:
        username = request.form.get('username', type=str)
        email = request.form.get('email', type=str)
        create_new_user(username, email)

        return f"Пользователь успешно создан", 201


class UserController(Resource):

    def get(self, pk: int) -> Response:
        user_dict = get_certain_user(pk)

        return jsonify(user_dict)

    def patch(self, pk: int) -> tuple[str, int]:
        username = request.form.get('username')
        email = request.form.get('email')
        update_user(pk, new_username=username, new_email=email)

        return f"Пользователь №{pk} успешно обновлен", 200

    def delete(self, pk: int) -> tuple[str, int]:
        delete_user(pk)

        return f"Пользователь №{pk} успешно удален", 200


users_api.add_resource(UsersController, '/users')
users_api.add_resource(UserController, '/users/<int:pk>')
