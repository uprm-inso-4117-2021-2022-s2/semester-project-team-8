from flask import jsonify
from dao import FieldsDao


class FieldsHandler:
    def build_fields_dict(self, row):
        result = {}
        result['FID'] = row[0]
        result['FieldName'] = row[1]
        return result

    def build_fields_attributes(self, FID, FieldName):
        result = {}
        result['FID'] = FID
        result['FieldName'] = FieldName

        return result

    def getAllFields(self):
        dao = FieldsDao.FieldDAO()
        fields_list = dao.getAllFields()
        result_list = []
        for row in fields_list:
            result = self.build_fields_dict(row)
            result_list.append(result)
        return jsonify(fields=result_list)

    def getFieldById(self, FID):
        dao = FieldsDao.FieldDAO()
        row = dao.getFieldById(FID)
        if not row:
            return jsonify(Error="Field Not Found"), 404
        else:
            fields = self.build_fields_dict(row)
            return jsonify(fields=fields)

    def insertFieldJson(self, json):
        fieldname = json['FieldName']
        if fieldname:
            dao = FieldsDao.FieldDAO()
            FID = dao.insert(fieldname)
            result = self.build_fields_attributes(
                FID, fieldname)
            return jsonify(fields=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteField(self, FID):
        dao = FieldsDao.FieldDAO()
        if not dao.getFieldById(FID):
            return jsonify(Error="Field not found."), 404
        else:
            dao.delete(FID)
            return jsonify(DeleteStatus="OK"), 200

    def updateFieldJson(self, FID, json):
        dao = FieldsDao.FieldDAO()
        if not dao.getFieldById(FID):
            return jsonify(Error="Field not found."), 404
        else:
            fieldname = json['FieldName']
            if fieldname:
                dao.update(fieldname)
                result = self.build_fields_attributes(
                    FID, fieldname)
                return jsonify(fields=result), 200
