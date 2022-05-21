from flask import Flask, request
from flask_restful import Resource, Api

from dbconnection.MongoConnection import Connection
from orm.fiveletter import fiveletter
from utilities.utils import regexmatch

app = Flask(__name__)
api = Api(app)


class WordStartsWith(Resource):
    def get(self, letters):
        mongoConnection = Connection(host='0.0.0.0', port=27017, database='words')
        mongoConnection.connect()
        query_output = [startwithword.word for startwithword in fiveletter.objects(word__istartswith=letters)]
        if query_output:
            return query_output, 200
        return "No such Word Found !!!!", 200


class WordEndsWith(Resource):
    def get(self, letters):
        mongo_connection = Connection(host='0.0.0.0', port=27017, database='words')
        mongo_connection.connect()
        query_output = [endwithword.word for endwithword in fiveletter.objects(word__iendswith=letters)]
        if query_output:
            return query_output, 200
        return "No such Word Found !!!!", 200


class WordsContainingLetters(Resource):
    def get(self, letters):
        mongo_connection = Connection(host='0.0.0.0', port=27017, database='words')
        mongo_connection.connect()
        query_output = [letterscontain.word for letterscontain in fiveletter.objects(word__icontains=letters)]
        if query_output:
            return query_output, 200
        return "No such Word Found !!!!", 200


class WordsSubsequence(Resource):
    def get(self, letters):
        mongo_connection = Connection(host='0.0.0.0', port=27017, database='words')
        mongo_connection.connect()
        query_output = [letterscontain.word for letterscontain in fiveletter.objects(word__contains=letters)]
        if query_output:
            return query_output, 200
        return "No such Word Found !!!!", 200


class WordWithAndWithoutLetter(Resource):
    def get(self):
        param = request.args
        with_letters = param.get('with')
        without_letters = param.get('without')
        mongo_connection = Connection(host='0.0.0.0', port=27017, database='words')
        mongo_connection.connect()
        query_output = [letterscontain.word for letterscontain in fiveletter.objects(word__contains=with_letters)]
        if without_letters == "":
            return query_output, 200
        new_list = regexmatch(query_output, without_letters)
        if new_list:
            return new_list, 200
        return "No Such Word !!!!!", 200


api.add_resource(WordStartsWith, "/startswith/<string:letters>")
api.add_resource(WordEndsWith, "/endswith/<string:letters>")
api.add_resource(WordsContainingLetters, "/contains/<string:letters>")
api.add_resource(WordWithAndWithoutLetter, "/noletter")

app.run()
