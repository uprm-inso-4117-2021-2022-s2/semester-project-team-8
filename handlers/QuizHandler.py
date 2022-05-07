'''
#This has been commented for the sake of completing Phase 2 and its user login function without hastle. 
#Focusing on other aspects.

from flask import jsonify
from dao import QuizDao

class QuizHandler:
    def build_quiz_dict(self, row):
        result = {}
        result['SQID'] = row[0]
        result['UAID'] = row[1]
        result['SF1'] = row[2]
        result['SF2'] = row[3]
        result['SF3'] = row[4]
        result['SF4'] = row[5]
        result['SF5'] = row[6]
        result['SF6'] = row[7]
        result['SF7'] = row[8]
        result['SF8'] = row[9]
        result['SF9'] = row[10]
        result['SF10'] = row[11]
        result['SF11'] = row[12]
        return result

    def build_quiz_attributes(self, SQID, UAID, SF1, SF2, SF3, SF4, SF5, SF6, SF7, SF8, SF9, SF10, SF11):
        result = {}
        result['SQID'] = SQID
        result['UAID'] = UAID
        result['SF1'] = SF1
        result['SF2'] = SF2
        result['SF3'] = SF3
        result['SF4'] = SF4
        result['SF5'] = SF5
        result['SF6'] = SF6
        result['SF7'] = SF7
        result['SF8'] = SF8
        result['SF9'] = SF9
        result['SF10'] = SF10
        result['SF11'] = SF11
        return result

    def getAllQuizes(self):
        dao = QuizDao.QuizDAO()
        Quizs_list = dao.getAllQuizes()
        result_list = []
        for row in Quizs_list:
            result = self.build_quiz_dict(row)
            result_list.append(result)
        return jsonify(Quizs=result_list)

    def getQuizById(self, SQID):
        dao = QuizDao.QuizDAO()
        row = dao.getQuizById(SQID)
        if not row:
            return jsonify(Error="Quiz Not Found"), 404
        else:
            Quizs = self.build_quiz_dict(row)
            return jsonify(Quizs=Quizs)

    def insertQuizJson(self, json):
        UAID = json('UAID')
        SF1 = json('SF1')
        SF2 = json('SF2')
        SF3 = json('SF3')
        SF4 = json('SF4')
        SF5 = json('SF5')
        SF6 = json('SF6')
        SF7 = json('SF7')
        SF8 = json('SF8')
        SF9 = json('SF9')
        SF10 = json('SF10')
        SF11 = json('SF11')
        if UAID and SF1 and SF2 and SF3 and SF4 and SF5 and SF6 and SF7 and SF8 and SF9 and SF10 and SF11:
            dao = QuizDao.QuizDAO()
            SQID = dao.insert(UAID, SF1, SF2, SF3, SF4, SF5,
                              SF6, SF7, SF8, SF9, SF10, SF11)
            result = self.build_Quizs_attributes(
                SQID, UAID, SF1, SF2, SF3, SF4, SF5, SF6, SF7, SF8, SF9, SF10, SF11)
            return jsonify(Quizs=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteQuiz(self, SQID):
        dao = QuizDao.QuizDAO()
        if not dao.getQuizById(SQID):
            return jsonify(Error="Quiz not found."), 404
        else:
            dao.delete(SQID)
            return jsonify(DeleteStatus="OK"), 200

# From here on is the algorithm for the Survey Quiz score (Which is to say, organizing its output)
# Algorithm information is as follows
# This will collect the information, and with the help of a join table with more knowledge regarding what each question entails
# It will catalogue information, and show a pie chart/or other chart, with a TLDR; of the users' preferences for one of the CSFields
# This algorithm is to hold the information, catalogue what they preffer, and fit this information into
# A Array of X segments (X being the number of CS Fields) with the number being higher depending on the question
# This will then be taken by the frontend and used to create a piechart or other chart to visually show the user their preferences.
# Confer with Omar Yusuf for knowledge and confirmation of this before beginning full deployment.
    def sqtemp(self, SQID):

        return

'''
