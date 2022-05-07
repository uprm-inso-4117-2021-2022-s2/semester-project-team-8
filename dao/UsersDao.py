import pymssql
import deal


class UserDAO:
    def __init__(self):
        connection_url = pymssql.connect(
            't8csguide.cftycj6fuueb.us-east-1.rds.amazonaws.com', 'csgadmin', 'csg123456', 'csguide')
        self.conn = connection_url

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    @deal.pre(lambda _: _.result > 0)
    def getUserById(self, UAID):
        cursor = self.conn.cursor()
        query = "select * from Users Where UAID = %s;"
        cursor.execute(query, (UAID,))
        result = cursor.fetchone()
        return result

    def insert(self, firstname, lastname, email, password, status):
        cursor = self.conn.cursor()
        query = "insert into Users(firstname, lastname, email, password, status) values (%s, %s, %s, %s, %s) ;"
        cursor.execute(query, (firstname, lastname, email, password, status))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        UAID = cursor.fetchall()[0]
        self.conn.commit()
        return UAID

    def delete(self, UAID):
        cursor = self.conn.cursor()
        query = "delete from Users where UAID = %s;"
        cursor.execute(query, (UAID,))
        self.conn.commit()
        return UAID

    def update(self, UAID, firstname, lastname, email, password, status):
        cursor = self.conn.cursor()
        query = "update Users set firstname = %s, lastname = %s, email = %s, password = %s, status = %s where UAID = %s;"
        cursor.execute(query, (firstname, lastname,
                       email, password, status, UAID,))
        self.conn.commit()
        return UAID
