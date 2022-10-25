import os
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'


# Extensions
db = SQLAlchemy(app)
db.init_app(app)
auth = HTTPBasicAuth


class User(db.Model):
    __tablename__ = 'users'  # Override default
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    last_login = db.Column(db.DateTime)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route("/", methods=['GET'])
def hello():
    # Just to make sure server is running
    return "<p>Hello World!</p>"


@app.route("/api/users", methods=['GET', 'POST'])
# List users or add user
def list_add_users():
    if request.method == 'GET':
        users = User.query.all()
        return users
    if request.method == 'POST':
        pass


@app.route("/api/users/<int:id>", methods=['PUT', 'DELETE'])
# Update or delete user
def update_user():
    pass


@app.route("/api/login")
@auth.login_required
def get_profile():
    return f"Hello, {auth.current_user()}! Login successful"


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)