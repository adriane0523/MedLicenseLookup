from parse import startWebparse
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from functools import wraps
from parse import startWebparse
import threading
  
# creates Flask object
app = Flask(__name__)
# configuration
# NEVER HARDCODE YOUR CONFIGURATION IN YOUR CODE
# INSTEAD CREATE A .env FILE AND STORE IN IT
app.config['SECRET_KEY'] = 'Hello my name is Jeff'
# database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# creates SQLALCHEMY object
db = SQLAlchemy(app)
x = None

# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = User.query\
                .filter_by(username = data['username'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated
  
# User Database Route
# this route sends back list of users
@app.route('/get_all_users', methods =['GET'])
@token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    users = User.query.all()
    # converting the query objects
    # to list of jsons
    output = []
    for user in users:
        # appending the user data json
        # to the response list
        output.append({
            'username': user.username,
            'name' : user.name,
            'email' : user.email
        })
  
    return jsonify({'users': output})
  
# route for logging user in
@app.route('/login', methods =['POST'])
def login():
    # creates dictionary of form data
    auth = request.json
    print(auth)
  
    if not auth or not auth['password'] or not auth['username']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(username = auth['username'])\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, auth['password']):
        # generates the JWT Token
        token = jwt.encode({
            'username': user.username,
            'exp' : datetime.utcnow() + timedelta(minutes = 3000000)
        }, app.config['SECRET_KEY'],algorithm="HS256")
  
        return make_response(jsonify({'token_data' : jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"]), 'token': token  }), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )
  
# signup route
@app.route('/signup', methods =['POST'])
def signup():
    # creates a dictionary of the form data
    data = request.json
  
    # gets name, email and password
    name, email = data['name'], data['email']
    password = data['password']
    username = data['username']
    print(data)
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            username = username,
            name = name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)

def background_task(lastNames, firstNames, username):
    startWebparse(lastNames, firstNames, username)
    x = None
    

    
# route for logging user in
@app.route('/parse', methods =['POST'])
@token_required
def parse(current_user):
    global thread
    global x
 
    # creates dictionary of form data
    data = request.json
    token = None
    # jwt is passed in the request header
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
    # return 401 if token is not passed
    if not token:
        return jsonify({'message' : 'Token is missing !!'}), 401
    
    print(data)

    # decoding the payload to fetch the stored details
    jwtData = jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
    current_user = User.query\
        .filter_by(username = jwtData['username'])\
        .first()
    print(jwtData)

    if (not(jwtData == None) and  (x == None)):
        x = threading.Thread(target=background_task, args=(data["lastNames"], data["firstNames"], jwtData["username"]))
        x.start()
        return jsonify({'status': 'Succes, Parsing current names'})
    else: 
        return jsonify({'status': 'Failed, Already Parsing current names'})




if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    app.run(debug = True)

    #sio.run(app)