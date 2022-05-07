from flask import jsonify
from dao import UsersDao


class UsersHandler:
    def build_users_dict(self, row):
        result = {}
        result['UAID'] = row[0]
        result['FirstName'] = row[1]
        result['LastName'] = row[2]
        result['Email'] = row[3]
        result['Password'] = row[4]
        result['Status'] = row[5]
        return result

    def build_users_attributes(self, UAID,  FirstName, LastName, Email, Password, Status):
        result = {}
        result['UAID'] = UAID
        result['FirstName'] = FirstName
        result['LastName'] = LastName
        result['Email'] = Email
        result['Password'] = Password
        result['Status'] = Status
        return result

    def getAllUsers(self):
        dao = UsersDao.UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, UAID):
        dao = UsersDao.UserDAO()
        row = dao.getUserById(UAID)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users=users)

    def insertUserJson(self, json):
        firstname = json['FirstName']
        lastname = json['LastName']
        email = json['Email']
        password = json['Password']
        status = json['Status']
        if firstname and lastname and email and password and status:
            dao = UsersDao.UserDAO()
            UAID = dao.insert(firstname, lastname, email, password, status)
            result = self.build_users_attributes(
                UAID, firstname, lastname, email, password, status)
            return jsonify(Users=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteUser(self, UAID):
        dao = UsersDao.UserDAO()
        if not dao.getUserById(UAID):
            return jsonify(Error="User not found."), 404
        else:
            dao.delete(UAID)
            return jsonify(DeleteStatus="OK"), 200

    def updateUserJson(self, UAID, json):
        dao = UsersDao.UserDAO()
        if not dao.getUserById(UAID):
            return jsonify(Error="Admin not found."), 404
        else:
            firstname = json['FirstName']
            lastname = json['LastName']
            email = json['Email']
            password = json['Password']
            status = json['Status']
            if firstname and lastname and email and password and status:
                dao.update(firstname, lastname, email, password, status)
                result = self.build_users_attributes(
                    UAID, firstname, lastname, email, password, status)
                return jsonify(Users=result), 200
