from flask import Flask, request, jsonify

app = Flask(__name__)


def validate_login(username, password):
    pass


@app.route("/", methods=['GET'])
def hello():
    return "<p>Hello World!</p>"


@app.route("/users/list", methods=['GET'])
def list_users():
    pass


@app.route("/users/create", methods=['POST'])
def add_user():
    pass


@app.route("/users/update", methods=['PUT'])
def update_user():
    pass


@app.route("/users/delete", methods=['POST'])
def delete_user():
    pass


@app.route("/login/<username>:<password>", methods=['POST'])
def login(username, password):
    return {
        'user': username,
        'pass': password
    }
