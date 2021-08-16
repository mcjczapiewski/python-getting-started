from django.db import models


class BooksModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Tytuł", max_length=255)
    author = models.CharField("Autor", max_length=255)
    publication_date = models.CharField(
        "Data publikacji", max_length=50, null=True, blank=True
    )
    isbn_number = models.CharField(
        "Numer ISBN", max_length=100, null=True, blank=True
    )
    pages_count = models.IntegerField("Liczba stron", null=True, blank=True)
    cover_url = models.URLField(
        "Link do okładki", max_length=255, null=True, blank=True
    )
    publication_language = models.CharField(
        "Język publikacji", max_length=255, null=True, blank=True
    )

    def __str__(self):
        return self.title
