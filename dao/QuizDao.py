'''
#This has been commented for the sake of completing Phase 2 and its user login function without hastle. 
#Focusing on other aspects.

import mysql.connector
import deal


class QuizDAO:
    def __init__(self):

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    @deal.pre(lambda _: _.result > 0)
    def getUserById(self, UserID):
        cursor = self.conn.cursor()
        query = "select * from Users Where userid = %s;"
        cursor.execute(query, (UserID,))
        result = cursor.fetchone()
        return result

    def insert(self, firstname, lastname, email, status):
        cursor = self.conn.cursor()
        query = "insert into Users(firstname, lastname, email, status) values (%s, %s, %s, %s) ;"
        cursor.execute(query, (firstname, lastname, email, status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        userid = cursor.fetchall()[0]
        self.conn.commit()
        return userid

    def delete(self, UserID):
        cursor = self.conn.cursor()
        query = "delete from Users where userid = %s;"
        cursor.execute(query, (UserID,))
        self.conn.commit()
        return UserID

    def update(self, UserID, firstname, lastname, email, status):
        cursor = self.conn.cursor()
        query = "update Users set firstname = %s, lastname = %s, email = %s, status = %s where userid = %s;"
        cursor.execute(query, (firstname, lastname, email, status, UserID,))
        self.conn.commit()
        return UserID

'''
