from flask import Flask, request
from handlers.UsersHandler import UsersHandler
from handlers.FieldsHandler import FieldsHandler
from flask_cors import CORS
from flask import jsonify

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Welcome to CSGuide!!!'


@app.route('/user', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UsersHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()


@app.route('/user/<int:id>', methods=['GET'])
def getusersbyid(id):
    if request.method == 'GET':
        print("REQUEST: ", request.json)
        response = UsersHandler().getUserById()
        if not response:
            return jsonify(Error="User not found."), 404
        else:
            return True


@app.route('/field', methods=['GET', 'POST'])
def fields():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return FieldsHandler().insertFieldJson(request.json)
    else:
        if not request.args:
            return FieldsHandler().getAllFields()


@app.route('/field/<int:id>', methods=['GET'])
def getfieldsbyid(id):
    if request.method == 'GET':
        print("REQUEST: ", request.json)
        return FieldsHandler().getFieldById()


if __name__ == '__main__':
    app.run()
