from flask import Flask

from database import db
from orm_flask.resources import users_api_bp
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration


def traces_sampler(sampling_context):
    return 1


sentry_sdk.init(
    dsn="https://f599762fadf94cb8a0515396ac3f05b9@o4504058251706368.ingest.sentry.io/4504058252623872",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # Alternatively, to control sampling dynamically
    traces_sampler=traces_sampler
)

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_ECHO'] = True

# Api resources
app.register_blueprint(users_api_bp)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
