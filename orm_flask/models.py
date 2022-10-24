from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
