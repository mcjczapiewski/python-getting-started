from django.test import TestCase, RequestFactory

from .views import all_books
from .views import delete_book
from .models import BooksModel
from .forms import BooksForm


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        book = BooksModel()
        book.title = "Additional"
        book.author = "Anonymous"
        book.save()
        self.book = book

        form = BooksForm()
        form.title = "new book"
        form.author = "author"
        self.form = form

    def test_calling_main_page_with_success(self):
        request = self.factory.get("/")
        response = all_books(request)
        self.assertTrue(response.status_code == 200)

    def test_book_is_properly_created(self):
        record = BooksModel.objects.get(pk=1)
        self.assertEqual(record, self.book)

    def test_books_count_equal_one(self):
        books_count = BooksModel.objects.all().count()
        self.assertEqual(books_count, 1)

    def test_books_form(self):
        self.assertEqual(self.form.title, "new book")

    def test_form_redirect_to_all_books_page(self):
        single_book = {"title": "new book", "author": "author"}
        response = self.client.post("/create-edit/", single_book, follow=True)
        response_path = response.request.get("PATH_INFO")
        self.assertEqual(response_path, "/")

    def test_book_is_deleted_redirect_after(self):
        response = delete_book(self, 1)
        books_count = BooksModel.objects.all().count()
        response_path = response.url
        self.assertEqual(books_count, 0)
        self.assertEqual(response_path, "/")
