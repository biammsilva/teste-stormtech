from microservice.models import Book

def sort(type):
    types = ("title", "author", "edition_year")
    if type in types:
        books = list(Book.objects().all())
        books.sort(key=lambda x: getattr(x, type), reverse=False)
        return books
    raise IndexError("Filter must be one of those types: " + str(types))
