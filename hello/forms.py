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
