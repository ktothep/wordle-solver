from mongoengine import StringField, Document


class fiveletter(Document):
   word=StringField(required=True)
