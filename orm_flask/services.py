from database import db
from orm_flask.models import User


def get_all_users() -> list[dict]:
    # Get all users from db

    users = db.session.query(User).all()
    users_list = [user.to_dict() for user in users]
    return users_list


def create_new_user(username: str, email: str) -> None:
    # Create new user in db

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()


def get_certain_user(pk: int) -> dict:
    # Get certain user from db

    user = db.session.get(User, {User.id: pk})
    return user.to_dict()


def delete_user(pk: int) -> None:
    # Delete certain user

    user = db.session.get(User, {User.id: pk})
    db.session.delete(user)
    db.session.commit()


def update_user(pk: int, new_username: str, new_email: str) -> None:
    # Update certain user

    user = db.session.query(User).filter(User.id == pk)
    user.update({User.username: new_username, User.email: new_email})
    db.session.commit()
