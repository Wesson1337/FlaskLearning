from flask import Flask

from database import db
from orm_flask.resources import users_api_bp

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'


# Api resources
app.register_blueprint(users_api_bp)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
