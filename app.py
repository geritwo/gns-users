import os
from flask import Flask, request, abort, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime as dt

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

    def get_user_details(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'last_login': self.last_login if self.last_login else "Never"
        }


@app.route("/", methods=['GET'])
def hello():
    # Just to make sure server is running
    return "<p>Hello World!</p>"


@app.route("/api/users", methods=['GET', 'POST'])
# List users or add user
def list_add_users():
    if request.method == 'GET':
        users = User.query.all()
        return [user.get_user_details() for user in users]
    if request.method == 'POST':
        username = request.args['username']
        email = request.args['email']
        password = request.args['password']

        # Validate parameters
        if username is None or password is None or email is None:
            abort(400)
        if User.query.filter_by(username=username).first() is not None:
            return "Error: Username already exists"  # NOTE: Forgot password?

        if User.query.filter_by(email=email).first() is not None:
            return "Error: Email address already exists"  # NOTE: Forgot username?

        # Store user in db
        user = User(
            username=username,
            email=email,
            last_login=None
        )
        user.hash_password(request.args['password'])
        db.session.add(user)
        db.session.commit()
        return f"User {user.username} added"


@app.route("/api/users/<int:id>", methods=['PUT', 'DELETE'])
# Update or delete user
def update_delete_user():
    pass


@app.route("/api/login")
@auth.login_required
def get_profile():
    return f"Hello, {auth.current_user()}! Login successful"


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        with app.app_context():
            db.drop_all()
            db.create_all()
    app.run(port=9001, debug=True)