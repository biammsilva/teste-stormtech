from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from microservice.models import Book
from microservice import serializers

# Create your views here.
class BookView(viewsets.GenericViewSet):

    queryset = Book.objects
    input_serializer = serializers.BookInput
    output_serializer = serializers.BookOutput

    # This class says to django docs what is the returned data
    def get_serializer_class(self):
        return self.input_serializer

    # this function is the POST method
    def create(self, request):
        data = request.data
        serializer = self.input_serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.save(), 200)
        return Response(serializer.errors, 500)

    # this function is the GET method without parameter
    def list(self, request):
        data = request.data
        return Response(self.output_serializer(self.queryset().all(), many=True).data, 200)

    # this function is the GET method with parameter
    def retrieve(self, request, id=None):
        data = request.data
        return Response(self.output_serializer(self.queryset(id=id).first()).data, 200)
