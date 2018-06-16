from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from microservice.models import Book
from microservice import serializers

# Create your views here.
class BookView(viewsets.GenericViewSet):

    queryset = Book.objects
    input_serializer = serializers.BookInput
    output_serializer = serializers.BookOutput

    def create(self, request):
        data = request.data
        serializer = self.input_serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.save(), 200)
        return Response(serializer.errors, 500)

    def list(self, request):
        data = request.data
        return Response(self.output_serializer(self.queryset().all(), many=True).data, 200)

    def retrieve(self, request, id=None):
        data = request.data
        print()
        return Response(self.output_serializer(self.queryset(id=id).first()).data, 200)
