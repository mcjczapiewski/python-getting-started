from django import forms
from .models import BooksModel


class BooksForm(forms.ModelForm):
    class Meta:
        model = BooksModel

        fields = [
            "title",
            "author",
            "publication_date",
            "isbn_number",
            "pages_count",
            "cover_url",
            "publication_language",
        ]


class GBooksForm(forms.Form):
    q = forms.CharField(label="Słowa klucze", max_length=100)
    intitle = forms.CharField(
        label="Tytuł zawiera", max_length=100, required=False
    )
    inauthor = forms.CharField(
        label="Autor zawiera", max_length=100, required=False
    )
    isbn = forms.CharField(label="Numer ISBN", max_length=20, required=False)
