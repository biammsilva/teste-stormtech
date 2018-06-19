from django.test import TestCase
from microservice.models import Book
from microservice.sorting_service import sort

class BooksTestCase(TestCase):
    def setUp(self):
        for book in Book.objects().all():
            book.delete()
        Book(title="A menina que roubava livros",
            author="Markus Zusak",
            edition_year=2005,
            created_at=datetime.now()).save()
        Book(title="O Senhor dos Anéis - As duas torres",
            author="J. R. R. Tolkien",
            edition_year=1949,
            created_at=datetime.now()).save()
        Book(title="O Senhor dos Anéis - A sociedade do anel",
            author="J. R. R. Tolkien",
            edition_year=1949,
            created_at=datetime.now()).save()
        Book(title="O Senhor dos Anéis - O retorno do Rei",
            author="J. R. R. Tolkien",
            edition_year=1949,
            created_at=datetime.now()).save()

    def test_sorting_by_title(self):
        sorted = sort("title")
        self.assertEqual(sorted[0].title, 'A menina que roubava livros')
        self.assertEqual(sorted[-1].title, 'O Senhor dos Anéis - O retorno do Rei')

    def test_sorting_by_title(self):
        sorted = sort("author")
        self.assertEqual(sorted[0].author, 'J. R. R. Tolkien')
        self.assertEqual(sorted[-1].title, 'Markus Zusak')

    def test_sorting_by_title(self):
        sorted = sort("tiedition_yeartle")
        self.assertEqual(sorted[0].title, 1949)
        self.assertEqual(sorted[-1].title, 2005)
