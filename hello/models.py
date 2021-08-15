from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class BooksModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateTimeField("Data publikacji")
    isbn_number = models.IntegerField()
    pages_count = models.IntegerField()
    cover_url = models.CharField(max_length=255)
    publication_language = models.CharField(max_length=255)
