from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    def __repr__(self):
        return f"User №{self.id}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


association_table = db.Table(
    'association_table',
    db.Column('parent_id', db.ForeignKey('parent.id'), primary_key=True),
    db.Column('child_id', db.ForeignKey('child.id'), primary_key=True)
)


class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship('Child', secondary=association_table, backref='parents')


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
