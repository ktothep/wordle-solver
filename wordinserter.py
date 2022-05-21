from dbconnection.MongoConnection import Connection
from orm.fiveletter import fiveletter


def parseandinsertfiveletter(document):
    f=open(document,'r')
    mongoConnection=Connection(host='0.0.0.0', port=27017, database='words')
    mongoConnection.connect()
    for words in f:
        fivo=fiveletter()
        fivo.word=words.replace("\n","")
        fivo.save()


parseandinsertfiveletter('wordfiles/5letter.csv')
