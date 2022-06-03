import pymssql
import deal


class FieldDAO:
    def __init__(self):
        connection_url = pymssql.connect(
            'no clue', 'nope', 'nope', 'nopee')
        self.conn = connection_url

    def getAllFields(self):
        cursor = self.conn.cursor()
        query = "select * from Fields;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    @deal.pre(lambda _: _.result > 0)
    def getFieldById(self, FID):
        cursor = self.conn.cursor()
        query = "select * from Fields Where FID = %s;"
        cursor.execute(query, (FID,))
        result = cursor.fetchone()
        return result

    def insert(self, fieldname):
        cursor = self.conn.cursor()
        query = "insert into Fields(FieldName) values (%s) ;"
        cursor.execute(query, (fieldname))
        query = "SELECT LAST_INSERT_ID();"
        cursor.execute(query)
        FID = cursor.fetchall()[0]
        self.conn.commit()
        return FID

    def delete(self, FID):
        cursor = self.conn.cursor()
        query = "delete from Fields where FID = %s;"
        cursor.execute(query, (FID,))
        self.conn.commit()
        return FID

    def update(self, FID, fieldname):
        cursor = self.conn.cursor()
        query = "update Fields set FieldName = %s where FID = %s;"
        cursor.execute(query, (fieldname, FID,))
        self.conn.commit()
        return FID
