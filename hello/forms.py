from django import forms
from django.forms.widgets import DateInput
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

        widgets = {
            "publication_date": DateInput(attrs={"type": "date"}),
        }
