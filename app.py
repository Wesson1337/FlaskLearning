from flask import Flask

app = Flask(__name__)


@app.route('/hello/<username>')
def hello_world(username) -> str:  # put application's code here
    return f'Hello {username}!'


if __name__ == '__main__':
    app.run(debug=True)
