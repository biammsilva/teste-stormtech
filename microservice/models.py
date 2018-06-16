from mongoengine import Document, fields

class Book(Document):
    title = fields.StringField(required=True)
    author = fields.StringField(required=True)
    edition_year = fields.IntField(required=True)
    created_at = fields.DateTimeField()
