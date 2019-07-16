from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from models import Base, User
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://robert:moss@localhost/blog_api_db'
app.config['SECRET_KEY'] = 'thisissecret'
DATABASE_URI = 'postgresql://robert:moss@localhost/blog_api_db'
db = SQLAlchemy(app)

# read docs for this approach...
# is it a better way to structure config?
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return "<h1> Velkommen til dette apiet</h1>"

# making the decorator..
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message" : "Token is missing"}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = session.query(User).filter_by(id=data['user_id']).first()
            # print(current_user.name)
        except:
            return jsonify({"message" : "Token is invalid"}), 401

        return f(current_user, *args, **kwargs)
    return decorated

# This function is not necessary at this point
@app.route('/user/<user_id>', methods=['GET'])
@token_required
def get_one_user(user_id):

    user = session.query(User).get(user_id)

    if not user:
        return jsonify({"message:" : "The user does not exist" })

    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({"user" : user_data})

@app.route('/user', methods=['GET'])
@token_required
def get_users(current_user):

    # returns a list of User-objects
    users = session.query(User).all()

    user_output = []

    for user in users:
        data = {}
        data['id'] = user.id
        data['name'] = user.name
        data['email'] = user.email
        data['password'] = user.password
        data['admin'] = user.admin
        user_output.append(data)

    return jsonify({"users" : data})

# Why does the trailing / need to be ther?
# This function is not necessary, since amdmin is the only active user..
@app.route('/user/', methods=['POST'])
@token_required
def create_user():
    # gets the json object anc converts it.
    # Should not be force=True

    data = request.get_json(force=True)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(name = data['name'], email = data['email'], password = hashed_password, admin = False)
    session.add(new_user)
    session.commit()
    return jsonify({"message" : "user created"})

# Update user to admin
@app.route('/user/<user_id>', methods=['PUT'])
@token_required
def make_admin(user_id):
    user = session.query(User).get(user_id)

    if not user:
        return jsonify({"message:" : "The user does not exist" })

    user.admin = True
    session.commit()
    return jsonify({"message" : "User has been made admin"})

@app.route('/user/<user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({"message:" : "The user does not exist" })

    session.delete(user)
    session.commit()

    return jsonify({'message' : 'the user has been deleted!'})

@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    user = session.query(User).filter_by(name=auth.username).first()
    #print(user.name)
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'user_id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({"token" : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
