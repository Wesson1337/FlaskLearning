from flask import Flask
from flask_restful import Api

from database import db
from orm_flask.resources import Products, Product

app = Flask(__name__)
api = Api(app)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'


# Api resources
api.add_resource(Products, '/products')
api.add_resource(Product, '/products/<int:pk>')

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
