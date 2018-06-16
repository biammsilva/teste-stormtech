from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from microservice.models import Book

# Create your views here.
class BookView(viewsets.GenericViewSet):

    queryset = Book.objects

    def create(self, request):
        try:
            return Response("", 200)
        except Exception as e:
            return Response(str(e), 500)

    def list(self, request):
        try:
            return Response("", 200)
        except Exception as e:
            return Response(str(e), 500)

    def retrieve(self, request, id=None):
        try:
            return Response("", 200)
        except Exception as e:
            return Response(str(e), 500)
