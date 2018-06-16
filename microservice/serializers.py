from rest_framework_mongoengine.serializers import serializers, DocumentSerializer
from microservice import models
from datetime import datetime

class BookInput(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    edition_year = serializers.IntegerField()

    def save(self):
        data = self.validated_data
        book = models.Book(title=data['title'],
                           author=data['author'],
                           edition_year=data['edition_year'],
                           created_at=datetime.now())
        book.save()
        return BookOutput(book).data


class BookOutput(DocumentSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'
