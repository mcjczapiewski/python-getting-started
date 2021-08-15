from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class BooksModel(models.Model):
    title = models.CharField("Tytuł", max_length=255)
    author = models.CharField("Autor", max_length=255)
    publication_date = models.DateTimeField("Data publikacji")
    isbn_number = models.IntegerField("Numer ISBN")
    pages_count = models.IntegerField("Liczba stron")
    cover_url = models.CharField("Link do okładki", max_length=255)
    publication_language = models.CharField("Język publikacji", max_length=255)

    def __str__(self):
        return self.title
