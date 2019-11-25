from flask import Flask, request, jsonify
from database.model import Mongodb

app = Flask(__name__)
db = Mongodb()
session = {"username":None}

@app.route('/', methods=['POST'])
def home():
    # if "username" in session:
    # print(session["username"])
    if request.method == 'POST':
        a = request.get_json(force=True)
        print(a)
        return jsonify(a)
    # return "Be register"

@app.route('/register', methods=['POST',"GET"])
def register():
    if request.method == 'POST':
        user = request.get_json().get("user")
        passw = request.get_json().get("passw")
        if db.createUser(username=user,password=passw) == True:
            return "success"
        return "That username is exists"
    return "Request error"

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.get_json().get("user")
        passw = request.get_json().get("passw")
        if db.authUser(username=user,password=passw) == True:
            session["username"] = user
            return user
        return "Username or password is Incorrect"
    return "Request error"

@app.route('/properties', methods=['GET'])
def properties():
    if request.method == 'GET':
        return jsonify(db.allKeys())
    return False


@app.route('/property', methods=['POST'])
def property():
    if request.method == "POST":
        name = request.get_json().get("name")
        return jsonify(db.getProperty(name=name))

@app.route('/property/create', methods=['POST'])
def property_create():
    if ("username" in session):
        if request.method == "POST":
            name = request.get_json().get("name")
            numberOfBedrooms = request.get_json().get("numberOfBedrooms")
            numberOfRooms = request.get_json().get("numberOfRooms")
            property = db.createProperty(username=session["username"],
                              name=name,
                              numberOfBedrooms=numberOfBedrooms,
                              numberOfRooms=numberOfRooms)
            print(property)
            return "succes"
        return "post olmadi"


@app.route('/property/delete', methods=['POST'])
def property_delete():
    if ("username" in session):
        print(session["username"])
        if request.method == "POST":
            id = request.get_json().get("property_id")
            print(id)
            return jsonify(db.deleteProperty(username=session["username"],property_id=id))
    return "You need log in"

if __name__ == '__main__':
    app.secret_key = "merhaba123456sfdasf"
    app.run(debug=True)
